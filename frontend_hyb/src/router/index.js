import Vue from 'vue'
import VueRouter from 'vue-router'
import Antd from 'ant-design-vue';
import Menu from 'ant-design-vue/lib/menu';
import 'ant-design-vue/dist/antd.css';
import Home from '../views/home/Home.vue'
import Login from '../views/login/Login.vue'
import Register from '../views/register/Register.vue'
/*import Help from '../views/help/Help.vue'
import Word from '../views/tools/Word.vue'
import Pdf from '../views/tools/Pdf.vue'*/

Vue.use(VueRouter)
Vue.use(Antd)
Vue.use(Menu);


const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: Login
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  /*{
    path: '/help',
    name: 'Help',
    component: Help
  },
  {
    path: '/word',
    name: 'Word',
    component: Word
  },
  {
    path: '/pdf',
    name: 'Pdf',
    component: Pdf
  }*/
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
