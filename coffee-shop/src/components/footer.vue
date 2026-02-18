<script setup>
import { ref } from 'vue'

const currentYear = new Date().getFullYear()

const footerMenu = [
  {
    title: 'Компания',
    links: [
      { name: 'О нас', url: '/about' },
      { name: 'СМИ', url: '/news' },
      { name: 'Блог', url: '/blog' },
      { name: 'Адреса', url: '/coffee-like-v-tvoem-gorode' },
    ]
  },
  {
    title: 'Кофе',
    links: [
      { name: 'Напитки', url: '/menu' },
      { name: 'Домой', url: '/coffee-home' },
    ]
  },
  {
    title: 'Франшиза',
    links: [
      { name: 'Стать партнёром', url: '/franshiza' },
    ]
  },
  {
    title: 'Партнерство',
    links: [
      { name: 'Поглощение', url: '/absorption' },
      { name: 'Поставщики', url: '/supplier' },
    ]
  },
  {
    title: 'Работа',
    links: [
      { name: 'Бариста', url: '/barista' },
      { name: 'Тайный гость', url: '/agent' },
    ]
  }
]

const socialLinks = [
  { class: '_icon-vk', url: 'https://vk.com/coffeelike_com' },
  { class: '_icon-youtube', url: 'https://www.youtube.com/c/coffeelikeru' },
  { class: '_icon-telegram', url: 'https://t.me/CLHT_bot' }
]
</script>

<template>
  <footer class="footer-upgrade">
    <div class="container-upgrade">
      <div class="footer-upgrade__wrap">
        
        <div class="footer-upgrade__item footer-upgrade__item_logo">
          <a class="logo" href="https://coffee-like.com"></a>
        </div>

        <div class="footer-upgrade__item footer-upgrade__item_menu footer-menu">
          <div v-for="section in footerMenu" :key="section.title" class="footer-menu__item">
            <div class="footer-menu__title">{{ section.title }}</div>
            <ul class="footer-menu__menu">
              <li v-for="link in section.links" :key="link.url">
                <a :href="link.url">{{ link.name }}</a>
              </li>
            </ul>
          </div>
        </div>

        <div class="footer-upgrade__item footer-upgrade__item_contacts">
          <div class="footer-upgrade__link" data-da=".footer-upgrade__item_logo,991,1">
            <a href="tel:+78003334130">+7 (800) 333-41-30</a>
            <span>для звонков из России и других стран</span>
          </div>
          
          <div class="footer-upgrade__link">
            <a href="mailto:hotline@coffee-like.com">hotline@coffee-like.com</a>
          </div>
          
          <div class="footer-upgrade__data">
            <a href="/loyalty-program-rules" target="_blank">ПРАВИЛА ПРОГРАММЫ ЛОЯЛЬНОСТИ</a>
          </div>

          <ul class="social-icon social-icon_upgrade" data-da=".footer-upgrade__bottom,991,0">
            <li v-for="social in socialLinks" :key="social.url" class="social-icon__item">
              <a :class="social.class" :href="social.url" target="_blank"></a>
            </li>
          </ul>

          <div class="footer-upgrade__data" data-da=".footer-upgrade__item_contacts,991,3">
            <p>
              Общество с ограниченной ответственностью "Кофе Лайк" (ООО "Кофе Лайк")<br>
              426004, Россия, Удмуртская респ., город Ижевск, Ленина ул., д. 21, офис 401
            </p>
            <div class="footer-upgrade__info">
              <p>ИНН - 1832114280</p>
              <p>ОГРН – 1131832006778</p>
            </div>
            <a href="/politika-konfidencialnosti">Политика конфиденциальности</a>
          </div>
        </div>
      </div>

      <div class="footer-upgrade__bottom">
        <p class="footer-upgrade__copyright">© {{ currentYear }} COFFEE LIKE</p>
      </div>
    </div>
  </footer>
</template>

<style scoped>
/* Основной фон футера */
.footer-upgrade {
  background-color: #1a1a1a; /* Темный стильный фон */
  color: #ffffff;
  padding: 60px 0 30px 0;
  font-family: 'Inter', sans-serif;
}

.container-upgrade {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

/* Flex-контейнер для основных блоков */
.footer-upgrade__wrap {
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap; /* Чтобы блоки переносились, если не влезают */
  gap: 40px;
  margin-bottom: 50px;
}

/* Логотип */
.logo {
  display: block;
  width: 150px;
  height: 50px;
  background: url('/img/svg/logo-new.webp') no-repeat center/contain;
  filter: brightness(0) invert(1); /* Делаем лого белым, если исходник темный */
}

/* Сетка меню */
.footer-menu {
  display: flex;
  flex-wrap: wrap;
  gap: 50px;
  flex: 1; /* Занимает всё свободное место */
}

.footer-menu__title {
  font-weight: 700;
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 1px;
  margin-bottom: 20px;
  color: #f39200; /* Фирменный оранжевый */
}

.footer-menu__menu {
  list-style: none;
  padding: 0;
}

.footer-menu__menu li {
  margin-bottom: 12px;
}

.footer-menu__menu a {
  color: #aaaaaa;
  text-decoration: none;
  font-size: 14px;
  transition: color 0.3s ease;
}

.footer-menu__menu a:hover {
  color: #ffffff;
}

/* Блок контактов */
.footer-upgrade__item_contacts {
  max-width: 350px;
}

.footer-upgrade__link a {
  display: block;
  font-size: 20px;
  font-weight: 700;
  color: #ffffff;
  text-decoration: none;
  margin-bottom: 5px;
}

.footer-upgrade__link span {
  font-size: 12px;
  color: #777;
  display: block;
  margin-bottom: 15px;
}

.footer-upgrade__data {
  margin-top: 20px;
  font-size: 12px;
  line-height: 1.6;
  color: #666;
}

.footer-upgrade__data a {
  color: #f39200;
  text-decoration: underline;
}

/* Соцсети */
.social-icon {
  display: flex;
  gap: 15px;
  margin: 20px 0;
  padding: 0;
  list-style: none;
}

.social-icon__item a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: #333;
  border-radius: 50%;
  color: #fff;
  transition: background 0.3s;
}

.social-icon__item a:hover {
  background: #f39200;
}

/* Нижняя панель с копирайтом */
.footer-upgrade__bottom {
  border-top: 1px solid #333;
  padding-top: 30px;
  text-align: center;
}

.footer-upgrade__copyright {
  font-size: 13px;
  color: #555;
}

/* Адаптивность для мобильных устройств */
@media (max-width: 768px) {
  .footer-upgrade__wrap {
    flex-direction: column;
    align-items: flex-start;
  }

  .footer-menu {
    display: grid;
    grid-template-columns: 1fr 1fr; /* Меню в две колонки на мобилках */
    gap: 30px;
    width: 100%;
  }

  .footer-upgrade__item_contacts {
    max-width: 100%;
    border-top: 1px solid #333;
    padding-top: 30px;
  }
}
</style>