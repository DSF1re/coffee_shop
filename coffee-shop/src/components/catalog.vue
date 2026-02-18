<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const products = ref([]);
const cart = ref([]);
const loading = ref(true);
const error = ref(null);

const baseUrl = 'http://127.0.0.1:8000';

const fetchProducts = async () => {
  try {
    const response = await axios.get(`${baseUrl}/api/product`);
    products.value = response.data;
  } catch (err) {
    error.value = 'Не удалось загрузить меню';
    console.error(err);
  } finally {
    loading.value = false;
  }
};

const toggleCart = (id) => {
  const index = cart.value.indexOf(id);
  if (index > -1) {
    cart.value.splice(index, 1);
  } else {
    cart.value.push(id);
  }
};

const isSelected = (id) => cart.value.includes(id);

onMounted(() => {
  fetchProducts();
});
</script>

<template>
  <div class="catalog">
    <div v-if="cart.length > 0" class="cart-counter">
      Выбрано товаров: {{ cart.length }}
    </div>

    <div v-if="loading" class="status">Загрузка вкусного кофе...</div>
    <div v-else-if="error" class="status error">{{ error }}</div>
    
    <div v-else class="coffee-grid">
      <div 
        v-for="product in products" 
        :key="product.product_id" 
        class="coffee-card"
        :class="{ 'coffee-card--selected': isSelected(product.product_id) }"
      >
        <div class="card-image">
          <img src="/assets/images/coffee.jpg" :alt="product.product_name"/>
          <div class="badge">Must have</div>
        </div>
        
        <div class="card-content">
          <h3 class="product-name">{{ product.product_name }}</h3>
          <p class="product-desc">Бодрящий напиток из свежеобжаренных зерен</p>
          
          <div class="card-footer">
            <span class="price">{{ product.price }} ₽</span>
            
            <button 
              @click="toggleCart(product.product_id)"
              class="add-btn"
              :class="{ 'add-btn--selected': isSelected(product.product_id) }"
            >
              <span v-if="!isSelected(product.product_id)">+</span>
              <span v-else>✓</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
/* Твои базовые стили остаются такими же, добавляем только новые состояния */

.catalog {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.cart-counter {
  background: #f39200;
  color: white;
  padding: 10px 20px;
  border-radius: 10px;
  display: inline-block;
  margin-bottom: 20px;
  font-weight: bold;
}

.coffee-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 30px;
}

.coffee-card {
  background: #fff;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 10px 20px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
  border: 2px solid transparent; /* Заготовка под обводку */
}

/* Стиль отмеченной карточки */
.coffee-card--selected {
  border-color: #f39200;
  transform: scale(1.02);
}

.card-image {
  position: relative;
  height: 250px;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.badge {
  position: absolute;
  top: 15px;
  left: 15px;
  background: #f39200;
  color: #fff;
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 700;
}

.card-content {
  padding: 20px;
}

.product-name {
  font-size: 1.2rem;
  margin: 0 0 10px 0;
  color: #333;
}

.product-desc {
  font-size: 0.9rem;
  color: #777;
  line-height: 1.4;
  margin-bottom: 20px;
}

.card-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.price {
  font-size: 1.3rem;
  font-weight: 800;
  color: #333;
}

/* Кнопка добавления */
.add-btn {
  background: #178529;
  color: white;
  border: none;
  width: 45px;
  height: 45px;
  border-radius: 14px;
  font-size: 22px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

/* Состояние "В корзине" для кнопки */
.add-btn--selected {
  background: #f39200;
  transform: rotate(360deg);
}

.add-btn:hover {
  transform: scale(1.1);
}

.status {
  text-align: center;
  padding: 50px;
}

.error {
  color: #e74c3c;
}
</style>