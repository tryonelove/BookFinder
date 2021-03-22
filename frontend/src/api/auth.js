import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000/api/auth';

export function authorize(userData) {
  return axios.post(`${API_URL}/login`, userData);
}

export function register(userData) {
  return axios.post(`${API_URL}/register`, userData);
}
