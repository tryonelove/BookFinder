<template>
  <div>
    <Header/>
    <main class="main">
        <div class="form_wrapper">
            <form action="">
              <h2>Регистрация</h2>
              <div class="columns">
                  <div class="firstColumn">
                      <label for="userName"></label>
                      <input type="text" id="userName" name="userName"
                        placeholder="Имя пользователя" size="28" required><br>
                      <label for="firstName"></label>
                      <input type="text" id="firstName" name="firstName"
                        placeholder="Ваше имя" size="28" required><br>
                  </div>
                  <div class="secondColumn">
                      <label for="mailAddress"></label>
                      <input type="text" id="mailAddress" name="mailAddress"
                        placeholder="Почта" size="28" required><br>
                      <label for="secondName"></label>
                      <input type="text" id="secondName" name="secondName"
                        placeholder="Ваша фамилия" size="28" required><br>
                  </div>
              </div>

              <label for="password"></label>
              <input type="password" id="password" name="password"
                placeholder="Пароль" size="28" required><br>
              <p>Уже зарегистрированы?</p>
              <p>Чего вы ждете? Заходите в ваш <a href="#">личный кабинет</a></p>
              <input type="submit" value="Присоединиться">
            </form>
        </div>
    </main>
  </div>
</template>

<script>
import '@/assets/styles/dialogBoxes.css';
import '@/assets/styles/registration.css';

import Header from './Header.vue';

export default {
  name: 'Registration',
  components: {
    Header,
  },
};
</script>
