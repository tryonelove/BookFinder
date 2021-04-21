import history from "../history";
import jwt_decode from "jwt-decode";

import RequestService from "../services/requestService";
import { SIGN_IN } from "../constants/constants";

export function handleInput(event, setCallback) {
  setCallback(event.target.value);
}

export function signIn(formData, signType) {
  RequestService.post("/api/auth/login", formData).then((data) => {
    if (data.authenticated === false) {
      alert(data.message);
    } else {
      localStorage.setItem("token", JSON.stringify(data));
      console.log(jwt_decode(JSON.stringify(data)));
      signType == SIGN_IN ? history.push("/main") : history.push("/genres");
    }
  });
}
