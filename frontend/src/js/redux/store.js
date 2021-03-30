import { createStore } from "redux";
import { composeWithDevTools } from "redux-devtools-extension";
import { booksReducer } from "./booksReducer";

const store = createStore(booksReducer, composeWithDevTools());

export default store;
