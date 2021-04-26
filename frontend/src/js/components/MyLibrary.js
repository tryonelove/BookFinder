import React from "react";
import jwt_decode from "jwt-decode";
import { Image } from "antd";

import GeneralHeader from "./GeneralHeader";
import Footer from "./Footer";
import BookWormImage from "../../assets/images/bookworm.svg";

import "../../styles/main.css";
import "../../styles/myLibrary.css";

function MyLibrary() {
  return (
    <>
      <GeneralHeader />
      <main className='libraryMain'>
        <section className="general_user_info_wrapper">
          <div className="image_wrapper">
            <Image width={200} src={BookWormImage} />
          </div>
          <div className="user_info_wrapper">
            <p>{jwt_decode(localStorage.getItem("token")).name}, Фамилия</p>
            <div className="books_info_wrapper">
              <span>
                Прочитано: <strong>34</strong>
              </span>
              <span>
                Читаю сейчас: <strong>3</strong>
              </span>
              <span>
                Хочу прочитать: <strong>123</strong>
              </span>
            </div>
          </div>
        </section>
        <section className="week_selection_wrapper">
          <h1>Подборка недели</h1>
        </section>
        <section className="already_read_wrapper">
          <h1>Прочитано - 34</h1>
        </section>
        <section className="reading_now_wrapper">
          <h1>Читаю сейчас - 3</h1>
        </section>
        <section className="want_to_read_wrapper">
          <h1>Хочу прочитать - 123</h1>
        </section>
      </main>
      <Footer />
    </>
  );
}

export default MyLibrary;
