<script setup>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

const router = useRouter();
const baseUrl = 'http://localhost:8080';

const form = ref({
  last_name: '',
  first_name: '',
  middle_name: '',
  email: '', 
  password: ''
});

const loading = ref(false);
const error = ref(null);

const handleRegister = async () => {
  loading.value = true;
  error.value = null;

  try {
    const response = await axios.post(`${baseUrl}/auth/register`, form.value);
    
    alert('Регистрация прошла успешно!');
    router.push('/');
  } catch (err) {
    error.value = err.response?.data?.error || 'Ошибка при регистрации';
  } finally {
    loading.value = false;
  }
};
</script>

<template>
  <div class="auth-container">
    <form @submit.prevent="handleRegister" class="auth-card">
      <h2>Регистрация</h2>
      
      <div class="grid-fields">
        <input v-model="form.last_name" placeholder="Фамилия" required />
        <input v-model="form.first_name" placeholder="Имя" required />
        <input v-model="form.middle_name" placeholder="Отчество (если есть)" />
        
        <hr class="divider" /> <input v-model="form.email" type="email" placeholder="Email (для входа)" required />
        <input v-model="form.password" type="password" placeholder="Пароль" required />
      </div>

      <p v-if="error" class="error-msg">{{ error }}</p>

      <button type="submit" :disabled="loading" class="login-btn">
        {{ loading ? 'Создание аккаунта...' : 'Зарегистрироваться' }}
      </button>

      <div class="auth-footer">
        <router-link to="/">Уже есть аккаунт? Войти</router-link>
      </div>
    </form>
  </div>
</template>

<style scoped>
.auth-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f4f7f6;
}

.auth-card {
  background: white;
  padding: 30px;
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0,0,0,0.08);
  width: 100%;
  max-width: 400px;
}

h2 {
  text-align: center;
  margin-bottom: 25px;
  color: #333;
}

.grid-fields {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
}

input {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 15px;
  transition: border-color 0.2s;
}

input:focus {
  outline: none;
  border-color: #f39200;
}

.divider {
  border: 0;
  border-top: 1px solid #eee;
  margin: 5px 0;
}

.login-btn {
  width: 100%;
  padding: 14px;
  background-color: #f39200;
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: bold;
  cursor: pointer;
}

.login-btn:disabled {
  opacity: 0.7;
}

.error-msg {
  color: #e74c3c;
  font-size: 14px;
  text-align: center;
  margin-bottom: 15px;
}

.auth-footer {
  margin-top: 20px;
  text-align: center;
}

.auth-footer a {
  color: #f39200;
  text-decoration: none;
  font-size: 14px;
}
</style>