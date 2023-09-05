import { useEffect } from "react";

const GLOBAL_CONSTANTS = {
  backend_url: "http://127.0.0.1:5000/",
  loggedIn:JSON.parse(sessionStorage?.getItem("user_data")) ? true : false,
  user_cred:JSON.parse(sessionStorage?.getItem("user_data"))?.data 
};

export default GLOBAL_CONSTANTS;