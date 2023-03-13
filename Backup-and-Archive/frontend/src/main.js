import Vue from 'vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import router from "./router/routes.js";
import Toasted from 'vue-toasted'

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.config.productionTip = false
Vue.use(Toasted,{duration:2000,position:'bottom-center'});
new Vue({
  router,
  render: h => h(App),
}).$mount('#app')