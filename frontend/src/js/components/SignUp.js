import React, { useState } from "react";
import history from "../history";

import "../../styles/dialogBoxes.css";
import "../../styles/registration.css";
import AuthorizationHeader from "./AuthorizationHeader";

import { handleInput, signIn } from "../services/authService";
import requestService from "../services/requestService";

function SignUp() {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  function sendFormData(event) {
    event.preventDefault();
    if (
      email !== "" &&
      password !== "" &&
      firstName !== "" &&
      lastName !== ""
    ) {
      const formData = {
        email,
        password,
        first_name: firstName,
        last_name: lastName,
      };
      requestService
        .post("/api/auth/register", formData)
        .then(() => signIn({ email, password }));
    } else alert("Заполните все поля");
  }

  return (
    <div className="authorization">
      <AuthorizationHeader />
      <main className="main">
        <div className="form_wrapper">
          <form action="">
            <h2>Регистрация</h2>
            <div className="columns">
              <div className="firstColumn">
                <label htmlFor="firstName"></label>
                <input
                  type="text"
                  id="firstName"
                  name="firstName"
                  placeholder="Ваше имя"
                  size="28"
                  onChange={(event) => handleInput(event, setFirstName)}
                />
                <br />
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
              </div>
              <div className="secondColumn">
                <label htmlFor="secondName"></label>
                <input
                  type="text"
                  id="secondName"
                  name="secondName"
                  placeholder="Ваша фамилия"
                  size="28"
                  onChange={(event) => handleInput(event, setLastName)}
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
              </div>
            </div>
            <p>Уже зарегистрированы?</p>
            <p>
              Чего вы ждете? Заходите в ваш{" "}
              <span onClick={() => history.push("/signIn")}>
                личный кабинет
              </span>
            </p>
            <input
              type="submit"
              value="Присоединиться"
              onClick={(event) => sendFormData(event)}
            />
          </form>
        </div>
      </main>
    </div>
  );
}

export default SignUp;
