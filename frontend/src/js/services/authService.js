import history from "../history";

import RequestService from "../services/requestService";

export function handleInput(event, setCallback) {
  setCallback(event.target.value);
}

export function signIn(formData) {
  RequestService.post("/api/auth/login", formData).then((data) => {
    if (data.authenticated === false) {
      alert(data.message);
      return;
    }
    localStorage.setItem("token", JSON.stringify(data));
    history.push("/genres");
  });
}
