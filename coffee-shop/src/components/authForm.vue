<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();

const login = ref('');
const password = ref('');

const loading = ref(false);
const error = ref(null);

const baseUrl = 'http://localhost:8000';

const handleLogin = async () => {
  if (!login.value || !password.value) {
    error.value = 'Заполните все поля';
    return;
  }

  loading.value = true;
  error.value = null;
  
  try {
    const response = await axios.post(`${baseUrl}/api/user/login`, {
      login: login.value,
      password: password.value
    });
    
    console.log('Успех:', response.data);
    if (response.data) {
      localStorage.setItem('userId', response.data.userId);
    }
    
    if (response.data.token) {
      localStorage.setItem('user_token', response.data.token);
    }

    router.push('/catalog'); 
    
  } catch (err) {
    error.value = err.response?.data?.detail || `${err} Неверный логин или пароль`;
    console.error(err);
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="auth-container">
    <form @submit.prevent="handleLogin" class="auth-card">
      <h2>Авторизация</h2>
      
      <div class="input-group">
        <label for="login">Логин</label>
        <input 
          id="login"
          v-model="login" 
          type="text" 
          placeholder="Введите логин"
          :disabled="loading"
        />
      </div>

      <div class="input-group">
        <label for="password">Пароль</label>
        <input 
          id="password"
          v-model="password" 
          type="password" 
          placeholder="Введите пароль"
          :disabled="loading"
        />
      </div>

      <p v-if="error" class="error-msg">{{ error }}</p>

      <button type="submit" :disabled="loading" class="login-btn">
        <span v-if="loading">Вход...</span>
        <span v-else>Войти</span>
      </button>

      <div class="auth-footer">
        <a href="#">Забыли пароль?</a>
        <span>Нет аккаунта? <a href="#">Зарегистрироваться</a></span>
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
  min-height: 60vh; /* Чтобы форма была по центру экрана */
}

.auth-card {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 10px 25px rgba(0,0,0,0.05);
  width: 100%;
  max-width: 400px;
}

h2 {
  margin-bottom: 25px;
  text-align: center;
  color: #333;
}

.input-group {
  margin-bottom: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.input-group label {
  font-size: 14px;
  font-weight: 600;
  color: #666;
}

.input-group input {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 16px;
  transition: border-color 0.3s;
}

.input-group input:focus {
  outline: none;
  border-color: #f39200; /* Оранжевый Coffee Like */
}

.login-btn {
  width: 100%;
  padding: 14px;
  background-color: #f39200;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 16px;
  font-weight: 700;
  cursor: pointer;
  transition: background 0.3s;
}

.login-btn:hover:not(:disabled) {
  background-color: #d68100;
}

.login-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error-msg {
  color: #e74c3c;
  font-size: 14px;
  margin-bottom: 15px;
  text-align: center;
}

.auth-footer {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  font-size: 13px;
}

.auth-footer a {
  color: #f39200;
  text-decoration: none;
}
</style>