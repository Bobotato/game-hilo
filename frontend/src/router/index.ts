import { createRouter, createWebHistory } from 'vue-router'
import PreGameView from '@/views/PreGameView.vue'

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'pregame',
      component: PreGameView
    },
    {
      path: '/game',
      name: 'game',
      component: () => import('../views/GameView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/mainmenu',
      name: 'mainmenu',
      component: () => import('../views/MainMenuView.vue')
    },
    {
      path: '/:notfound',
      name: 'notfound',
      component: () => import('../views/NotFound.vue')
    }
  ]
})

export default router
