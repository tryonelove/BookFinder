import React from "react";
import { Route } from "react-router-dom";
import { Router } from "react-router";
import history from "../history";

import SignIn from "./SignIn";
import SignUp from "./SignUp";
import Main from "./Main";

function App() {
  return (
    <Router history={history}>
      <Route path="/signIn">
        <SignIn />
      </Route>
      <Route path="/signUp">
        <SignUp />
      </Route>
      <Route path="/main">
        <Main />
      </Route>
      <Route exact path="/">
        <SignIn />
      </Route>
    </Router>
  );
}

export default App;
