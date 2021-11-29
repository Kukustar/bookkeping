import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home'
import Login from '../views/Login'
import Deposits from '../views/Deposits'

const routes = [
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/deposits',
    name: 'Deposits',
    component: Deposits
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes // short for `routes: routes`
})

export default router
