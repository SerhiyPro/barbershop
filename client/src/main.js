import Vue from 'vue'
import App from './App.vue'
import './assets/css/style.css'
import './assets/css/fonts.css'
import './assets/css/media.css'
import './assets/css/vanilla-calendar.css'
import './assets/css/main.css'
//import './assets/js/ vanilla-calendar-min'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import VueCarousel from 'vue-carousel';
Vue.use(VueCarousel);
import router from "@/routes";

import {default as Vuedals} from 'vuedals';


Vue.use(Vuedals);
import BootstrapVue from 'bootstrap-vue'

Vue.use(BootstrapVue)


Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
