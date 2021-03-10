import Vue from 'vue';
import VueRouter from 'vue-router';
import HelloWorld from '@/components/HelloWorld.vue';
import Registration from '@/components/Registration.vue';
import Login from '@/components/Login.vue';
import store from '@/store';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    component: HelloWorld,
    props: { msg: 'Hello, username' },
    meta: { title: 'Home' },
    beforeEnter(to, from, next) {
      if (!store.getters.isAuthenticated) {
        next({
          path: 'login',
        });
      } else {
        next();
      }
    },
  },
  {
    path: '/register',
    component: Registration,
    meta: { title: 'Registration' },
    beforeEnter(to, from, next) {
      if (store.getters.isAuthenticated) {
        next({
          path: '/',
        });
      } else {
        next();
      }
    },
  },
  {
    path: '/login',
    component: Login,
    meta: { title: 'Login' },
    beforeEnter(to, from, next) {
      if (store.getters.isAuthenticated) {
        next({
          path: '/',
        });
      } else {
        next();
      }
    },
  },
];

export default new VueRouter({
  mode: 'history',
  routes,
});
