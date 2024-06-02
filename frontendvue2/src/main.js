import axios from 'axios';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import Vuetify from 'vuetify';
import 'vuetify/dist/vuetify.min.css';
axios.defaults.baseURL = 'http://127.0.0.1:8000';

Vue.config.productionTip = false;

Vue.use(Vuetify);

const vuetify = new Vuetify({});
new Vue({
  vuetify,

  router,
  store,
  render: (h) => h(App),
}).$mount('#app');
