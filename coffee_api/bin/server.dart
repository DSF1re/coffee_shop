import 'dart:convert';
import 'package:postgres/postgres.dart';
import 'package:shelf/shelf.dart';
import 'package:shelf_router/shelf_router.dart';
import 'package:shelf/shelf_io.dart';

void main() async {
  final conn = await Connection.open(
    Endpoint(
      host: 'localhost',
      database: 'coffee_shop',
      username: 'postgres',
      password: '1234',
    ),
    settings: ConnectionSettings(sslMode: SslMode.disable),
  );

  final coffeeApi = CoffeeApi(conn);

  // В функции main
  final handler = Pipeline()
      .addMiddleware(logRequests())
      .addMiddleware(
        (innerHandler) => (request) async {
          if (request.method == 'OPTIONS') {
            return Response.ok(
              '',
              headers: {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods':
                    'GET, POST, PUT, DELETE, OPTIONS',
                'Access-Control-Allow-Headers': 'Origin, Content-Type',
              },
            );
          }

          final response = await innerHandler(request);

          return response.change(
            headers: {
              'content-type': 'application/json',
              'Access-Control-Allow-Origin': '*',
              'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
              'Access-Control-Allow-Headers': 'Origin, Content-Type',
            },
          );
        },
      )
      .addHandler(coffeeApi.router.call);
  final server = await serve(handler, '0.0.0.0', 8080);
  print('Сервер кофейни (учебный) запущен: http://localhost:${server.port}');
}

class CoffeeApi {
  final Connection conn;
  CoffeeApi(this.conn);

  Router get router {
    final router = Router();

    router.post('/auth/register', (Request request) async {
      try {
        final data = jsonDecode(await request.readAsString());
        final email = data['email']?.toString().trim() ?? '';

        if (email.isEmpty) {
          return Response.badRequest(
            body: jsonEncode({'error': 'Email обязателен'}),
          );
        }

        final checkEmail = await conn.execute(
          r'SELECT user_id FROM users WHERE email = $1',
          parameters: [email],
        );

        if (checkEmail.isNotEmpty) {
          return Response(
            409,
            body: jsonEncode({'error': 'Этот email уже занят'}),
          );
        }

        await conn.execute(
          r'''INSERT INTO users (last_name, first_name, middle_name, email, password_hash) 
              VALUES ($1, $2, $3, $4, $5)''',
          parameters: [
            data['last_name'],
            data['first_name'],
            data['middle_name'],
            email,
            data['password'],
          ],
        );

        return Response.ok(
          jsonEncode({
            'status': 'success',
            'message': 'Пользователь успешно зарегистрирован',
          }),
        );
      } catch (e) {
        return Response.internalServerError(
          body: jsonEncode({'error': 'Ошибка сервера: $e'}),
        );
      }
    });

    router.post('/auth/login', (Request request) async {
      final data = jsonDecode(await request.readAsString());

      final result = await conn.execute(
        r'SELECT user_id, first_name, last_name, email, password_hash FROM users WHERE email = $1',
        parameters: [data['email']],
      );

      if (result.isEmpty) {
        return Response.forbidden(
          jsonEncode({'error': 'Пользователь не найден'}),
        );
      }

      final user = result.first;
      final storedPassword = user[4] as String;

      if (storedPassword == data['password']) {
        return Response.ok(
          jsonEncode({
            'status': 'success',
            'user': {
              'id': user[0],
              'first_name': user[1],
              'last_name': user[2],
              'email': user[3],
            },
          }),
        );
      }
      return Response.forbidden(jsonEncode({'error': 'Неверный пароль'}));
    });

    router.put('/users/<id>', (Request request, String id) async {
      final data = jsonDecode(await request.readAsString());
      final userId = int.parse(id);

      if (data['password'] != null && data['password'].toString().isNotEmpty) {
        await conn.execute(
          r'UPDATE users SET first_name=$1, last_name=$2, middle_name=$3, email=$4, password_hash=$5 WHERE user_id=$6',
          parameters: [
            data['first_name'],
            data['last_name'],
            data['middle_name'],
            data['email'],
            data['password'],
            userId,
          ],
        );
      } else {
        await conn.execute(
          r'UPDATE users SET first_name=$1, last_name=$2, middle_name=$3, email=$4 WHERE user_id=$5',
          parameters: [
            data['first_name'],
            data['last_name'],
            data['middle_name'],
            data['email'],
            userId,
          ],
        );
      }
      return Response.ok(jsonEncode({'status': 'success'}));
    });

    router.get('/users/<id>', (Request request, String id) async {
      try {
        final userId = int.parse(id);
        final result = await conn.execute(
          r'SELECT first_name, last_name, middle_name, email FROM users WHERE user_id = $1',
          parameters: [userId],
        );

        if (result.isEmpty) {
          return Response.notFound(
            jsonEncode({'error': 'Пользователь не найден'}),
          );
        }

        final user = result.first;
        return Response.ok(
          jsonEncode({
            'first_name': user[0],
            'last_name': user[1],
            'middle_name': user[2],
            'email': user[3],
          }),
        );
      } catch (e) {
        return Response.internalServerError(
          body: jsonEncode({'error': e.toString()}),
        );
      }
    });

    router.get('/products', (Request request) async {
      final res = await conn.execute(
        'SELECT product_id, name, description, price, image_url FROM products',
      );
      final products = res
          .map(
            (r) => {
              'id': r[0],
              'name': r[1],
              'description': r[2],
              'price': r[3],
              'image': r[4],
            },
          )
          .toList();
      return Response.ok(jsonEncode(products));
    });

    router.post('/orders', (Request request) async {
      try {
        final data = jsonDecode(await request.readAsString());

        final orderRes = await conn.execute(
          r'INSERT INTO orders (user_id, total_price, status) VALUES ($1, $2, $3) RETURNING order_id',
          parameters: [data['user_id'], data['total_price'], 'new'],
        );

        final orderId = orderRes.first[0];

        for (var item in data['items']) {
          await conn.execute(
            r'INSERT INTO order_items (order_id, product_id, quantity, price_at_purchase) VALUES ($1, $2, $3, $4)',
            parameters: [
              orderId,
              item['product_id'],
              item['quantity'],
              item['price'],
            ],
          );
        }

        return Response.ok(
          jsonEncode({'order_id': orderId, 'message': 'Заказ создан'}),
        );
      } catch (e) {
        return Response.internalServerError(
          body: jsonEncode({'error': e.toString()}),
        );
      }
    });

    router.get('/orders/<userId>', (Request request, String userId) async {
      try {
        final id = int.parse(userId);
        // Этот запрос объединяет таблицы и склеивает названия кофе
        final result = await conn.execute(
          r'''
      SELECT o.order_id, o.total_price, STRING_AGG(p.name, ', ') as items_names
      FROM orders o
      JOIN order_items oi ON o.order_id = oi.order_id
      JOIN products p ON oi.product_id = p.product_id
      WHERE o.user_id = $1
      GROUP BY o.order_id, o.total_price
      ORDER BY o.order_id DESC
      ''',
          parameters: [id],
        );

        final orders = result
            .map(
              (row) => {
                'id': row[0],
                'total_price': row[1],
                'names': row[2], // Вот тут будут наши названия
              },
            )
            .toList();

        return Response.ok(jsonEncode(orders));
      } catch (e) {
        return Response.internalServerError(
          body: jsonEncode({'error': e.toString()}),
        );
      }
    });
    return router;
  }
}
