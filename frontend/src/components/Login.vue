<template>
  <div>
    <Header/>
    <main class="main">
      <div class="form_wrapper">
          <h2>Вход в библиотеку</h2>
          <label for="userName"></label>
          <input type="text" id="userName" name="userName"
                  placeholder="Имя пользователя" required v-model="email"><br>
          <label for="password"></label>
          <input type="password" id="password" name="password"
                  placeholder="Пароль" required v-model="password"><br>
          <p>Ещё не зарегистрированы?</p>
          <p>Начните погружение в мир книг <a href="#">прямо сейчас</a></p>
          <input type="submit" value="Войти" @click="authenticate">
      </div>
    </main>
  </div>
</template>

<script>
import { EventBus } from '@/utils';
import '@/assets/styles/dialogBoxes.css';
import '@/assets/styles/login.css';

import Header from './Header.vue';

export default {
  components: {
    Header,
  },
  data() {
    return {
      email: '',
      password: '',
      errorMsg: '',
    };
  },
  methods: {
    authenticate() {
      console.log('Authentication');
      this.$store.dispatch('login', { email: this.email, password: this.password })
        .then(() => this.$router.push('/'));
    },
  },
  mounted() {
    EventBus.$on('failedAuthentication', (msg) => {
      this.errorMsg = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off('failedAuthentication');
  },
};
</script>
