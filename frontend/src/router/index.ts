import { createRouter, createWebHistory } from 'vue-router'
import PreGameView from '@/views/PreGameView.vue'
import GameView from '@/views/GameView.vue'
import MainMenuView from '@/views/MainMenuView.vue'

const router = createRouter({
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
      component: GameView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    },
    {
      path: '/mainmenu',
      name: 'mainmenu',
      component: MainMenuView
    },
  ]
})

export default router
