import { createRouter, createWebHistory } from 'vue-router'

import DisclaimerView from '@/views/DisclaimerView.vue'
import { verifyJWT } from '@/services/apiService/user/user';

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'disclaimer',
      component: DisclaimerView
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/AuthenticationView.vue')
    },
    {
      path: '/game',
      name: 'game',
      component: () => import('../views/GameView.vue')
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
});

router.beforeEach(async (to) => {
  const publicPages = ['/', '/login', '/notfound'];
  const loginRequired = !publicPages.includes(to.path);

  if (loginRequired) {
    try {
      await verifyJWT()
    } catch(error) {
      return '/login';
  }
}});

export default router
