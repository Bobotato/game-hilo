import { createRouter, createWebHistory } from 'vue-router'
import DisclaimerView from '@/views/DisclaimerView.vue'

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'disclaimer',
      component: DisclaimerView
    },
    {
      path: '/game',
      name: 'game',
      component: () => import('../views/GameView.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/AuthenticationView.vue')
    },
    {
      path: '/mainmenu',
      name: 'mainmenu',
      component: () => import('../views/MainMenuView.vue')
    },
    {
      path: '/:notfound',
      name: 'notfound',
      component: () => import('../views/NotFoundView.vue')
    }
  ]
})

export default router
