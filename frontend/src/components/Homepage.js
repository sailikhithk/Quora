// frontend/src/components/Homepage.js

import React from "react";
import { Link } from "react-router-dom";

function Homepage() {
  return (
    <div>
      <h1>Welcome to Quora Clone!</h1>
      <Link to="/login">Login</Link>
      <Link to="/register">Register</Link>
    </div>
  );
}

export default Homepage;
