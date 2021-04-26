import React from "react";
import { Route } from "react-router-dom";
import { Router } from "react-router";
import history from "../history";
import { Provider } from "react-redux";
import store from "../redux/store";

import SignIn from "./SignIn";
import SignUp from "./SignUp";
import Main from "./Main";
import Genres from "./Genres";
import Catalog from "./Catalog";
import MyLibrary from "./MyLibrary";

function App() {
  return (
    <Provider store={store}>
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
        <Route path="/catalog">
          <Catalog />
        </Route>
        <Route path="/genres">
          <Genres />
        </Route>
        <Route path="/myLibrary">
          <MyLibrary />
        </Route>
        <Route exact path="/">
          {localStorage.getItem("token") ? <Main /> : <SignIn />}
        </Route>
      </Router>
    </Provider>
  );
}

export default App;
