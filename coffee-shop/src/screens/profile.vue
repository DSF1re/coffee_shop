<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const userId = localStorage.getItem('userId');
const baseUrl = 'http://127.0.0.1:8000';

const profile = ref({
  first_name: '',
  last_name: '',
  login: '',
  password: ''
});

const loading = ref(true);
const message = ref({ text: '', type: '' });

const fetchProfile = async () => {
  try {
    const response = await axios.get(`${baseUrl}/api/user/${userId}`);
    profile.value = { ...response.data, password: '' };
  } catch (err) {
    message.value = { text: 'Ошибка при загрузке профиля', type: 'error' };
  } finally {
    loading.value = false;
  }
};

// Сохранение изменений
const handleUpdate = async () => {
  try {
    const updateData = { ...profile.value };
    if (!updateData.password) delete updateData.password;

    await axios.put(`${baseUrl}/api/user/${userId}`, updateData);
    message.value = { text: 'Данные успешно обновлены!', type: 'success' };
  } catch (err) {
    message.value = { text: 'Ошибка при сохранении данных', type: 'error' };
  }
};

onMounted(fetchProfile);
</script>

<template>
  <div class="profile-container">
    <div class="profile-card">
      <h2>Редактирование профиля</h2>
      
      <div v-if="loading">Загрузка...</div>
      
      <form v-else @submit.prevent="handleUpdate">
        <div class="input-group">
          <label>Имя</label>
          <input v-model="profile.first_name" type="text" />
        </div>

        <div class="input-group">
          <label>Фамилия</label>
          <input v-model="profile.last_name" type="text" />
        </div>

        <div class="input-group">
          <label>Логин</label>
          <input v-model="profile.login" type="text" />
        </div>

        <div class="input-group">
          <label>Новый пароль (оставьте пустым, если не меняете)</label>
          <input v-model="profile.password" type="password" />
        </div>

        <p v-if="message.text" :class="['msg', message.type]">{{ message.text }}</p>

        <button type="submit" class="save-btn">Сохранить изменения</button>
      </form>
    </div>
  </div>
</template>

<style scoped>
.profile-container {
  display: flex;
  justify-content: center;
  padding: 40px;
}

.profile-card {
  background: white;
  padding: 30px;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 500px;
}

.input-group {
  margin-bottom: 15px;
  display: flex;
  flex-direction: column;
}

.input-group label {
  margin-bottom: 5px;
  font-size: 14px;
  color: #666;
}

.input-group input {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.save-btn {
  width: 100%;
  padding: 12px;
  background-color: #178529;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-weight: bold;
}

.msg {
  text-align: center;
  margin-bottom: 10px;
  font-size: 14px;
}

.msg.success { color: #27ae60; }
.msg.error { color: #e74c3c; }
</style>