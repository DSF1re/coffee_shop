<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

// Простой массив ссылок
const menuItems = [
  { name: 'О нас', url: '/about' },
  { name: 'Меню', url: '/menu' },
  { name: 'Контакты', url: '/contacts' },
]

const goToProfile = () => {
  router.push('/profile')
}
</script>

<template>
  <header class="header">
    <div class="container">
      <div class="header__wrapper">
        
        <router-link to="/" class="logo">COFFEE LIKE</router-link>

        <nav>
          <ul class="menu">
            <li v-for="item in menuItems" :key="item.name">
              <router-link :to="item.url" class="menu__link">{{ item.name }}</router-link>
            </li>
          </ul>
        </nav>

        <button @click="goToProfile" class="profile-btn">
          Профиль
        </button>

      </div>
    </div>
  </header>
</template>

<style scoped>
.header {
  background: #fff;
  border-bottom: 1px solid #eee;
  height: 70px;
  display: flex;
  align-items: center;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  width: 100%;
}

.header__wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  font-weight: 900;
  font-size: 20px;
  color: #178529;
  text-decoration: none;
}

.menu {
  display: flex;
  gap: 20px;
  list-style: none;
}

.menu__link {
  text-decoration: none;
  color: #333;
  font-weight: 600;
  font-size: 14px;
}

.menu__link:hover {
  color: #178529;
}

.profile-btn {
  background: #178529;
  color: #fff;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-weight: 600;
}

.profile-btn:hover {
  background: #136b21;
}
</style>