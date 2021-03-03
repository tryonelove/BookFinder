<template>
  <div>
    <Header/>
    <main class="main">
      <div class="form_wrapper">
        <form action="">
            <h2>Вход в библиотеку</h2>
            <label for="userName"></label>
            <input type="text" id="userName" name="userName"
                    placeholder="Имя пользователя" size="28" required><br>
            <label for="password"></label>
            <input type="password" id="password" name="password"
                    placeholder="Пароль" size="28" required><br>
            <p>Ещё не зарегистрированы?</p>
            <p>Начните погружение в мир книг <a href="#">прямо сейчас</a></p>
            <input type="submit" value="Войти">
        </form>
      </div>
    </main>
  </div>
</template>

<script>
import '@/assets/styles/dialogBoxes.css';
import '@/assets/styles/login.css';

import Header from './Header.vue';

export default {
  name: 'Login',
  components: {
    Header,
  },
};
</script>
