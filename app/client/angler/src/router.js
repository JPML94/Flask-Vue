import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Api from './views/Api.vue'
import Ping from './views/Ping.vue'
import Modal from './views/Modal.vue'

Vue.use(Router)

export default new Router({
    routes: [{
            path: '/',
            name: 'home',
            component: Home
        },
        {
            path: '/api',
            name: 'api',
            component: Api
        },
        {
            path: '/ping',
            name: 'ping',
            component: Ping
        },
        {
            path: '/modal',
            name: 'modal',
            component: Modal
        }
    ]
})