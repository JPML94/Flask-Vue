import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import './filters'

import vModal from 'vue-js-modal';

Vue.config.productionTip = false
Vue.use(vModal, { dynamics: true })

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app')