<template>
  <div>
    <Header/>
    <main class="main">
        <div class="form_wrapper">
              <h2>Регистрация</h2>
              <div class="columns">
                  <div class="firstColumn">
                      <label for="userName"></label>
                      <input type="text" id="userName" name="userName"
                        placeholder="Имя пользователя" size="28" required><br>
                      <label for="firstName"></label>
                      <input type="text" id="firstName" name="firstName"
                        placeholder="Ваше имя" size="28" required v-model="firstName"><br>
                  </div>
                  <div class="secondColumn">
                      <label for="mailAddress"></label>
                      <input type="text" id="mailAddress" name="mailAddress"
                        placeholder="Почта" size="28" required v-model="email"><br>
                      <label for="secondName"></label>
                      <input type="text" id="secondName" name="secondName"
                        placeholder="Ваша фамилия" size="28" required v-model="secondName"><br>
                  </div>
              </div>

              <label for="password"></label>
              <input type="password" id="password" name="password"
                placeholder="Пароль" size="28" required v-model="password"><br>
              <p>Уже зарегистрированы?</p>
              <p>Чего вы ждете? Заходите в ваш <a href="#">личный кабинет</a></p>
              <input type="submit" value="Присоединиться" @click="register">
        </div>
    </main>
  </div>
</template>

<script>
import { EventBus } from '@/utils';
import Header from './Header.vue';

import '@/assets/styles/dialogBoxes.css';
import '@/assets/styles/registration.css';

export default {
  name: 'Registration',
  components: {
    Header,
  },
  data() {
    return {
      firstName: '',
      secondName: '',
      email: '',
      password: '',
      errorMsg: '',
    };
  },
  methods: {
    register() {
      console.log('Registration');
      this.$store.dispatch('register', {
        first_name: this.firstName,
        last_name: this.secondName,
        email: this.email,
        password: this.password,
      })
        .then(() => this.$router.push('/'));
    },
  },
  mounted() {
    EventBus.$on('failedRegistering', (msg) => {
      this.errorMsg = msg;
    });
  },
  beforeDestroy() {
    EventBus.$off('failedRegistering');
  },
};
</script>
