import { createRouter, createWebHistory } from 'vue-router'
import GameView from '../views/GameView.vue'
import MainMenuView from '../views/MainMenuView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
