import Auth from '@/screens/auth.vue'
import Catalog from '@/screens/catalog.vue'
import Profile from '@/screens/profile.vue'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'auth',
      component: Auth
    },
    {
      path: '/catalog',
      name: 'catalog',
      component: Catalog
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile
    }
  ],
})

export default router