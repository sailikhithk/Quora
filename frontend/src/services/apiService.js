import axios from "axios";

const apiService = axios.create({
  baseURL: "http://localhost:5000/api", // replace this with your server's base URL
});

export default apiService;
