import Vue from 'vue';
import App from './App';

import VueSidebarMenu from 'vue-sidebar-menu' //sidebar
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css' //sidebar
Vue.use(VueSidebarMenu)



new Vue({
  render: h => h(App)
}).$mount('#app');
