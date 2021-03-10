import Vue from 'vue';
import Vuex from 'vuex';
import { authorize, register } from '@/api/auth';
import { fetchBooks } from '@/api/books';
import { isValidJwt, EventBus } from '@/utils';

Vue.use(Vuex);

const data = {
  books: [],
  currentBook: {},
  user: {},
  jwt: { token: localStorage.getItem('token') },
};

const actions = {
  // Books management
  loadBooks(context) {
    return fetchBooks()
      .then((response) => context.commit('setBooks', { books: response }));
  },
  loadBook(context, { id }) {
    return fetchBooks()
      .then((response) => context.commit('setBook', { book: response }));
  },
  // Authentication
  login(context, userData) {
    context.commit('setUserData', { userData });
    return authorize(userData)
      .then((response) => context.commit('setJwtToken', { jwt: response.data }))
      .catch((error) => {
        // eslint-disable-next-line
        console.log('Error while Authenticating: ', error);
        EventBus.$emit('failedAuthentication', error);
      });
  },
  register(context, userData) {
    context.commit('setUserData', { userData });
    return register(userData)
      .then(context.dispatch('login', userData))
      .catch((error) => {
        // eslint-disable-next-line
        console.log('Error Registering: ', error);
        EventBus.$emit('failedRegistering: ', error);
      });
  },
};

const mutations = {
  // Books setters
  setBooks(state, payload) {
    state.surveys = payload.books;
  },

  setBook(state, payload) {
    state.currentSurvey = payload.book;
  },
  // User data setters
  setUserData(state, payload) {
    // eslint-disable-next-line
    console.log('setUserData payload = ', payload);
    state.userData = payload.userData;
  },
  setJwtToken(state, payload) {
    // eslint-disable-next-line
    console.log('setJwtToken payload = ', payload);
    localStorage.token = payload.jwt.token;
    state.jwt = payload.jwt;
  },
};

const getters = {
  isAuthenticated(state) {
    return isValidJwt(state.jwt.token);
  },
};

export default new Vuex.Store({
  state: data,
  actions,
  getters,
  mutations,
});
