import React, { useState } from "react";
import history from "../history";

import "../../styles/dialogBoxes.css";
import "../../styles/login.css";
import AuthorizationHeader from "./AuthorizationHeader";

import { handleInput, signIn } from "../services/authService";

function SignIn() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  function sendFormData(event) {
    event.preventDefault();
    if (email !== "" && password !== "") {
      const formData = { email, password };
      signIn(formData);
    } else alert("Заполните все поля");
  }

  return (
    <div className="authorization">
      <AuthorizationHeader />
      <main className="main">
        <div className="form_wrapper">
          <form action="">
            <h2>Вход в библиотеку</h2>
            <label htmlFor="mailAddress"></label>
            <input
              type="text"
              id="mailAddress"
              name="mailAddress"
              placeholder="Почта"
              size="28"
              onChange={(event) => handleInput(event, setEmail)}
            />
            <br />
            <label htmlFor="password"></label>
            <input
              type="password"
              id="password"
              name="password"
              placeholder="Пароль"
              size="28"
              onChange={(event) => handleInput(event, setPassword)}
            />
            <br />
            <p>Ещё не зарегистрированы?</p>
            <p>
              Начните погружение в мир книг{" "}
              <span onClick={() => history.push("/signUp")}>прямо сейчас</span>
            </p>
            <input
              type="submit"
              value="Войти"
              onClick={(event) => sendFormData(event)}
            />
          </form>
        </div>
      </main>
    </div>
  );
}

export default SignIn;
