import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
// import Api from './views/Api.vue'
import Game from './views/Game.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    // {
    //   path: '/api',
    //   name: 'api',
    //   component: Api
    // },
    {
      path: '/game',
      name: 'game',
      component: Game
    }
  ]
})
