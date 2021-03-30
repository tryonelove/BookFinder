import React from "react";

import BlackLogo from "../../assets/images/black-logo.svg";

function AuthorizationHeader() {
  return (
    <header className="header">
      <img src={BlackLogo} alt="polygon" />
    </header>
  );
}

export default AuthorizationHeader;
