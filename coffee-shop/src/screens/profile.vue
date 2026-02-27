<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const userId = localStorage.getItem('userId');
const baseUrl = 'http://localhost:8080';

const profile = ref({
  first_name: '',
  last_name: '',
  middle_name: '',
  email: '',
  password: ''
});

const loading = ref(true);
const message = ref({ text: '', type: '' });

const fetchProfile = async () => {
  if (!userId) {
    message.value = { text: 'Пользователь не авторизован', type: 'error' };
    loading.value = false;
    return;
  }

  try {
    const response = await axios.get(`${baseUrl}/users/${userId}`);
    
    profile.value = { 
      ...response.data, 
      password: '' 
    };
  } catch (err) {
    message.value = { text: 'Ошибка при загрузке профиля', type: 'error' };
    console.error('Детали:', err.response?.status, err.response?.data);
  } finally {
    loading.value = false;
  }
};

const handleUpdate = async () => {
  try {
    message.value = { text: '', type: '' };
    const updateData = { ...profile.value };
    
    if (!updateData.password) delete updateData.password;

    await axios.put(`${baseUrl}/users/${userId}`, updateData);
    message.value = { text: 'Данные успешно обновлены!', type: 'success' };
  } catch (err) {
    message.value = { text: 'Ошибка при сохранении (проверь, есть ли PUT метод на бэкенде)', type: 'error' };
  }
};

onMounted(fetchProfile);
</script>

<template>
  <div class="profile-container">
    <div class="profile-card">
      <h2>Мой профиль</h2>
      
      <div v-if="loading" class="status">Загрузка данных...</div>
      
      <form v-else @submit.prevent="handleUpdate">
        <div class="input-group">
          <label>Имя</label>
          <input v-model="profile.first_name" type="text" placeholder="Введите имя" />
        </div>

        <div class="input-group">
          <label>Фамилия</label>
          <input v-model="profile.last_name" type="text" placeholder="Введите фамилию" />
        </div>

        <div class="input-group">
          <label>Отчество</label>
          <input v-model="profile.middle_name" type="text" placeholder="Введите отчество" />
        </div>

        <div class="input-group">
          <label>Email (Логин)</label>
          <input v-model="profile.email" type="email" placeholder="example@mail.com" />
        </div>

        <div class="input-group">
          <label>Новый пароль</label>
          <input v-model="profile.password" type="password" placeholder="Оставьте пустым, чтобы не менять" />
        </div>

        <p v-if="message.text" :class="['msg', message.type]">{{ message.text }}</p>

        <div class="actions">
          <button type="submit" class="save-btn">Сохранить изменения</button>
          <router-link to="/catalog" class="back-link">Вернуться в меню</router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
.profile-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 80vh;
  padding: 20px;
}

.profile-card {
  background: white;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 450px;
}

h2 {
  text-align: center;
  color: #333;
  margin-bottom: 25px;
}

.input-group {
  margin-bottom: 15px;
  display: flex;
  flex-direction: column;
}

.input-group label {
  margin-bottom: 5px;
  font-size: 13px;
  font-weight: bold;
  color: #777;
}

.input-group input {
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 15px;
}

.input-group input:focus {
  outline: none;
  border-color: #f39200;
}

.actions {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 20px;
}

.save-btn {
  width: 100%;
  padding: 14px;
  background-color: #178529;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
  font-size: 16px;
}

.back-link {
  text-align: center;
  color: #f39200;
  text-decoration: none;
  font-size: 14px;
}

.msg {
  text-align: center;
  margin: 10px 0;
  font-size: 14px;
  padding: 8px;
  border-radius: 6px;
}

.msg.success { background: #eafaf1; color: #27ae60; }
.msg.error { background: #fdf2f0; color: #e74c3c; }
.status { text-align: center; color: #777; }
</style>