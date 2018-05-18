import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import Api from './views/Api.vue'
import Test from './views/Test.vue'

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
            name: 'test',
            component: Test
        }
    ]
})