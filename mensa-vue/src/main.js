import Vue from 'vue'
import axios from 'axios'
import App from './App.vue'
import VueHead from 'vue-head'
import VueRouter from 'vue-router'
import routes from './routes'
import { store } from './store/store'

Vue.use(VueHead)
Vue.use(VueRouter)

const router = new VueRouter({mode:'history',routes});

new Vue({
  store :store,
  el: '#app',
  beforeCreate(){
    Vue.prototype.$http = axios
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    axios.defaults.xsrfCookieName = 'csrftoken'
  },
  render: h => h(App),
  router
}).$mount('#app');
