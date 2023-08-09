import axios from "axios";

// Create axios instance
const apiService = axios.create({
  baseURL: "http://localhost:5000/", // replace this with your server's base URL
});

// Add a request interceptor
apiService.interceptors.request.use(
  (config) => {
    // Do something before request is sent
    const token = localStorage.getItem("token");
    if (token) {
      console.log(`Token: ${token}`);
      config.headers["Authorization"] = "Bearer " + token;
    }
    return config;
  },
  (error) => {
    // Do something with request error
    return Promise.reject(error);
  }
);

export default apiService;
