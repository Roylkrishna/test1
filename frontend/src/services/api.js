import axios from "axios";

// Base URL of your Flask backend
const API_URL = "https://<your-username>.pythonanywhere.com";

export const api = axios.create({
  baseURL: API_URL,
});
