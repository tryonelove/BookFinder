const ADD_BOOKS = "ADD_BOOKS";

const defaultState = {
  books: null,
};

export const booksReducer = (state = defaultState, action) => {
  switch (action.type) {
    case ADD_BOOKS:
      return { ...state, books: action.payload };
    default:
      return state;
  }
};

export const addBooksAction = (payload) => ({
  type: ADD_BOOKS,
  payload: payload,
});
