import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Overview.vue'
import Electricity from "./views/Electricity";
import Settings from "./views/Settings";
import Temperature from "./views/Temperature";
import Sauna from "./views/Sauna";

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/electricity',
      name: 'electricity',
      component: Electricity
    },
    {
      path: '/sauna',
      name: 'sauna',
      component: Sauna
    },
    {
      path: '/temperature',
      name: 'temperature',
      component: Temperature
    },
    {
      path: '/settings',
      name: 'settings',
      component: Settings
    }
  ]
})
