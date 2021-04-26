import React from "react";
import jwt_decode from "jwt-decode";

import Logo from "../../assets/images/logo.svg";
import history from "../history";

function GeneralHeader() {
  function logOut() {
    localStorage.clear();
    history.push("/signIn");
  }

  return (
    <header className="general_header">
      <div className="header_content_wrapper">
        <nav className="navigation">
          <ul className="page_actions">
            <li onClick={() => history.push("/main")}>Главная</li>
            <li onClick={() => history.push("/catalog")}>Каталог</li>
          </ul>
        </nav>
        <div className="logo_wrapper">
          <img src={Logo} alt="logo" />
        </div>
        <nav className="navigation">
          <ul className="user_account_actions">
            <li onClick={() => history.push("/myLibrary")}>
              <span>
                {localStorage.getItem("token")
                  ? `${jwt_decode(localStorage.getItem("token")).name}`
                  : ""}
              </span>
            </li>
            <li onClick={logOut}>Выйти</li>
          </ul>
        </nav>
      </div>
    </header>
  );
}

export default GeneralHeader;
