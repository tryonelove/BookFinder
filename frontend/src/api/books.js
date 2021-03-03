import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/books/';

export function fetchBooks() {
  return axios.get(`${API_URL}`);
}

export function fetchBook(bookId) {
  return axios.get(`${API_URL}/${bookId}/`);
}

export function postNewBook(book) {
  return axios.post(`${API_URL}/`, book);
}
