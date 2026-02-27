<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const baseUrl = 'http://localhost:8080';
const userId = localStorage.getItem('userId');

const products = ref([]); 
const orders = ref([]);
const cart = ref([]);     

const fetchProducts = async () => {
  const res = await axios.get(`${baseUrl}/products`);
  products.value = res.data;
};

const fetchOrders = async () => {
  const res = await axios.get(`${baseUrl}/orders/${userId}`);
  orders.value = res.data;
};

const toggleCart = (item) => {
  if (cart.value.includes(item)) {
    cart.value = cart.value.filter(i => i !== item);
  } else {
    cart.value.push(item);
  }
};

const createOrder = async () => {
  const totalPrice = cart.value.reduce((sum, i) => sum + parseFloat(i.price), 0);
  const orderData = {
    user_id: userId,
    total_price: totalPrice,
    items: cart.value.map(i => ({ product_id: i.id, quantity: 1, price: i.price }))
  };

  await axios.post(`${baseUrl}/orders`, orderData);
  alert('Готово!');
  cart.value = [];
  fetchOrders();
};

onMounted(() => {
  fetchProducts();
  fetchOrders();
});
</script>

<template>
  <div class="app">
    <div v-if="cart.length > 0" class="cart-bar">
      Товаров: {{ cart.length }}
      <button @click="createOrder">Заказать</button>
    </div>

    <h2>Меню</h2>
    <div class="grid">
      <div v-for="p in products" :key="p.id" class="card">
        <h4>{{ p.name }}</h4>
        <p>{{ p.price }} ₽</p>
        <button @click="toggleCart(p)">
          {{ cart.includes(p) ? 'Удалить' : 'Добавить' }}
        </button>
      </div>
    </div>

    <hr>

    <h2>Мои заказы</h2>
    <div v-for="o in orders" :key="o.id" class="order-row">
      <div>
        <b>Заказ №{{ o.id }}</b> — {{ o.total_price }} ₽
      </div>
      <small style="color: #666;">Состав: {{ o.names }}</small>
    </div>
  </div>
</template>

<style scoped>
.app { font-family: sans-serif; padding: 20px; }
.grid { display: flex; gap: 10px; flex-wrap: wrap; }
.card { border: 1px solid #ccc; padding: 10px; border-radius: 8px; width: 150px; }
.cart-bar { background: orange; padding: 15px; margin-bottom: 20px; border-radius: 8px; }
.order-row { background: #f0f0f0; padding: 10px; margin-bottom: 5px; }
</style>