import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/Main.vue'),
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue'),
    },
    {
      path: '/sign-up',
      name: 'sign-up',
      component: () => import('../views/SignUp.vue'),
    },
    {
      path: '/task/create',
      name: 'task-create',
      component: () => import('../views/TaskCreate.vue'),
    },
    {
      path: '/task/:id',
      name: 'task-detail',
      component: () => import('../views/TaskDetail.vue'),
      props: true,
    },
    {
      path: '/task/edit',
      name: 'task-edit',
      component: () => import('../views/TaskEdit.vue'),
    }
  ],
})

export default router
