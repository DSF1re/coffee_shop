<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();

const email = ref('');
const password = ref('');
const loading = ref(false);
const error = ref(null);

const baseUrl = 'http://localhost:8080';

const handleLogin = async () => {
  if (!email.value || !password.value) {
    error.value = 'Заполните почту и пароль';
    return;
  }

  loading.value = true;
  error.value = null;
  
  try {
    const response = await axios.post(`${baseUrl}/auth/login`, {
      email: email.value,
      password: password.value
    });
    
    if (response.data.status === 'success') {
      const userData = response.data.user;
      
      localStorage.setItem('userId', userData.id);
      localStorage.setItem('userName', userData.name);
      
      console.log('Вход выполнен для:', userData.name);
      router.push('/catalog'); 
    }
    
  } catch (err) {
    error.value = err.response?.data?.error || 'Ошибка подключения к серверу';
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="auth-container">
    <form @submit.prevent="handleLogin" class="auth-card">
      <h2>Кофейня: Вход</h2>
      
      <div class="input-group">
        <label>Email</label>
        <input 
          v-model="email" 
          type="email" 
          placeholder="example@mail.com"
          :disabled="loading"
        />
      </div>

      <div class="input-group">
        <label>Пароль</label>
        <input 
          v-model="password" 
          type="password" 
          placeholder="Ваш пароль"
          :disabled="loading"
        />
      </div>

      <p v-if="error" class="error-msg">{{ error }}</p>

      <button type="submit" :disabled="loading" class="login-btn">
        {{ loading ? 'Проверка...' : 'Войти' }}
      </button>

      <div class="auth-footer">
        <span>Нет аккаунта? <router-link to="/register">Создать профиль</router-link></span>
      </div>
    </form>
  </div>
</template>

<style scoped>

.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 40px 20px;
  background-color: #f4f7f6;
  min-height: 100vh;
}
.auth-card {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.05);
  width: 100%;
  max-width: 350px;
}
.input-group {
  margin-bottom: 15px;
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.input-group input {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 6px;
}
.login-btn {
  width: 100%;
  padding: 12px;
  background-color: #f39200;
  color: white;
  border: none;
  border-radius: 6px;
  font-weight: bold;
  cursor: pointer;
}
.error-msg {
  color: #e74c3c;
  margin-bottom: 10px;
  font-size: 14px;
}
.auth-footer {
  margin-top: 15px;
  text-align: center;
  font-size: 13px;
}
</style>