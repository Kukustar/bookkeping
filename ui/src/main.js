import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import jwtGuard from './jwt-guard'
import vuetify from '@/plugins/vuetify'

router.beforeEach((to, from, next) => jwtGuard(to, from, next))

createApp(App)
  .use(router)
  .use(vuetify)
  .mount('#app')
