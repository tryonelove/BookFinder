import React from "react";

import Logo from "../../assets/images/logo.svg";

function GeneralHeader() {
  return (
    <header className="general_header">
      <div className="header_content_wrapper">
        <nav className="navigation">
          <ul className="page_actions">
            <li>Главная</li>
            <li>Лента</li>
          </ul>
        </nav>
        <div className="logo_wrapper">
          <img src={Logo} alt="logo" />
        </div>
        <nav className="navigation">
          <ul className="user_account_actions">
            <li>
              <span>{"$user1"}</span>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
}

export default GeneralHeader;
