<script setup>
import { ref } from 'vue'

const isMobileMenuOpen = ref(false)

const menuItems = [
  {
    title: 'Компания',
    links: [
      { name: 'О нас', url: 'https://coffee-like.com/about' },
      { name: 'СМИ', url: 'https://coffee-like.com/news' },
      { name: 'Блог', url: 'https://coffee-like.com/blog' },
      { name: 'Адреса', url: 'https://coffee-like.com/coffee-like-v-tvoem-gorode' },
    ]
  },
  {
    title: 'Кофе',
    links: [
      { name: 'Напитки', url: 'https://coffee-like.com/menu' },
      { name: 'Домой', url: 'https://coffee-like.com/coffee-home' },
    ]
  },
  {
    title: 'Франшиза',
    links: [
      { name: 'Стать партнёром', url: 'https://coffee-like.com/franshiza' },
    ]
  },
  {
    title: 'Партнерство',
    links: [
      { name: 'Поглощение', url: 'https://coffee-like.com/absorption' },
      { name: 'Поставщики', url: 'https://coffee-like.com/supplier' },
    ]
  },
  {
    title: 'Работа',
    links: [
      { name: 'Бариста', url: 'https://coffee-like.com/barista' },
      { name: 'Тайный гость', url: 'https://coffee-like.com/agent' },
    ]
  }
]

const toggleMenu = () => {
  isMobileMenuOpen.value = !isMobileMenuOpen.value
}
</script>
<template>
  <header class="header-upgrade js-header header-upgrade_fixed">
    <div class="container-upgrade">
      <div class="header-upgrade__wrapper">
        <a class="logo logo_new" href="https://coffee-like.com">
          <p>Coffee Like</p>
        </a>

        <nav class="header-upgrade__menu">
          <ul class="menu-upgrade">
            <li v-for="item in menuItems" :key="item.title">
              <a href="#" rel="nofollow">{{ item.title }}</a>
              <ul class="sub-menu-upgrade">
                <li v-for="link in item.links" :key="link.url">
                  <a :href="link.url">{{ link.name }}</a>
                  <div class="_icon-arrow"></div>
                </li>
              </ul>
            </li>
          </ul>
        </nav>

        <div class="header-upgrade__navigation">
          <a class="phone" href="tel:78003334130" rel="nofollow">
            <span>+7 800 333-41-30</span>
            <div class="_icon-phone-transparent"></div>
          </a>
          <div 
            class="icon-menu-mobile" 
            :class="{ '_active': isMobileMenuOpen }" 
            @click="toggleMenu"
          >
            <span></span><span></span><span></span>
          </div>
        </div>

        <div class="main-menu" :class="{ '_open': isMobileMenuOpen }">
          <div class="main-menu__wrap">
            <div class="main-menu__menu">
              <div v-for="item in menuItems" :key="'mob-' + item.title" class="main-menu__menu-item">
                <div class="main-menu__title">{{ item.title }}</div>
                <ul class="block-menu">
                  <li v-for="link in item.links" :key="link.url" class="block-menu__item">
                    <a :href="link.url">{{ link.name }}</a>
                  </li>
                </ul>
              </div>
            </div>
            
            <div class="main-menu__contacts">
              <ul class="social-icon social-icon_upgrade">
                <li class="social-icon__item"><a class="_icon-vk" href="https://vk.com/coffeelike_com"></a></li>
                <li class="social-icon__item"><a class="_icon-youtube" href="https://www.youtube.com/c/coffeelikeru"></a></li>
                <li class="social-icon__item"><a class="_icon-telegram" href="https://t.me/CLHT_bot"></a></li>
              </ul>
              <div class="main-menu__link">
                <a href="tel:+78003334130">+7 (800) 333-41-30</a>
                <span>для звонков из России и <br>других стран</span>
              </div>
              <div class="main-menu__link">
                <a href="mailto:hotline@coffee-like.com">hotline@coffee-like.com</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<style scoped>
/* Сброс стилей и базовые настройки */
:component {
  font-family: 'Inter', sans-serif; /* По умолчанию подставится системный шрифт */
}

ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

a {
  text-decoration: none;
  color: #333;
  transition: color 0.3s ease;
}

a:hover {
  color: #178529;
}

.container-upgrade {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* --- HEADER --- */
.header-upgrade {
  background: #0000002A;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  position: sticky;
  top: 0;
  z-index: 1000;
}

.header-upgrade__wrapper {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 80px;
}

.logo p {
  font-weight: 800;
  font-size: 24px;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin: 0;
}

/* --- DESKTOP MENU --- */
.menu-upgrade {
  display: flex;
  gap: 30px;
}

.menu-upgrade > li {
  position: relative;
  padding: 30px 0;
}

.menu-upgrade > li > a {
  font-weight: 600;
  font-size: 15px;
}

/* Выпадающее меню */
.sub-menu-upgrade {
  position: absolute;
  top: 100%;
  left: 0;
  background: #fff;
  min-width: 200px;
  border-radius: 8px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  padding: 15px 0;
  opacity: 0;
  visibility: hidden;
  transform: translateY(10px);
  transition: all 0.3s ease;
}

.menu-upgrade li:hover .sub-menu-upgrade {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.sub-menu-upgrade li a {
  display: block;
  padding: 10px 20px;
  font-size: 14px;
}

.sub-menu-upgrade li a:hover {
  background: #fdf5e6;
}

/* --- NAVIGATION --- */
.header-upgrade__navigation {
  display: flex;
  align-items: center;
  gap: 20px;
}

.phone {
  font-weight: 700;
  color: #178529;
}

/* --- MOBILE BURGER --- */
.icon-menu-mobile {
  display: none; /* Прячем на десктопе */
  flex-direction: column;
  gap: 5px;
  cursor: pointer;
}

.icon-menu-mobile span {
  width: 25px;
  height: 2px;
  background: #333;
  transition: 0.3s;
}

/* --- MOBILE MENU OVERLAY --- */
.main-menu {
  display: none; /* Включается через JS/классы на мобилках */
}

/* --- АДАПТИВНОСТЬ --- */
@media (max-width: 992px) {
  .header-upgrade__menu {
    display: none; /* Прячем основное меню */
  }

  .icon-menu-mobile {
    display: flex;
  }

  /* Стили для открытого мобильного меню */
  .main-menu._open {
    display: block;
    position: fixed;
    top: 80px;
    left: 0;
    width: 100%;
    height: calc(100vh - 80px);
    background: #fff;
    overflow-y: auto;
    padding: 40px 20px;
    z-index: 999;
  }

  .main-menu__menu-item {
    margin-bottom: 25px;
  }

  .main-menu__title {
    font-weight: 800;
    font-size: 18px;
    margin-bottom: 10px;
    color: #f39200;
  }

  .block-menu__item {
    margin-bottom: 8px;
    font-size: 16px;
  }
}
</style>