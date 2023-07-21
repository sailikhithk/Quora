import React, { useState } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import "../css/main.css";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [failedAttempts, setFailedAttempts] = useState(0); // state for failed attempts
  const navigate = useNavigate(); // hook for programmatic navigation

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://localhost:5000/login", {
        username,
        password,
      });
      localStorage.setItem("token", res.data.token);
      alert("Login successful!");
      setFailedAttempts(0); // reset the failed attempts counter
    } catch (err) {
      if (err.response.data.error === "Username not found") {
        alert("Username not found. Please try again or register.");
      } else if (err.response.data.error === "Incorrect password") {
        setFailedAttempts(failedAttempts + 1); // increment the failed attempts counter
        if (failedAttempts >= 2) {
          alert("3 incorrect attempts. Redirecting to reset password page...");
          navigate("/reset-password");
        } else {
          alert("Incorrect password. Please try again.");
        }
      } else {
        alert("Login failed");
      }
    }
  };

  return (
    <form onSubmit={handleSubmit} className="auth-form">
      <input
        type="text"
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
        style={{ width: "100%", boxSizing: "border-box" }}
      />
      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
        style={{ width: "100%", boxSizing: "border-box" }}
      />
      <input type="submit" value="Login" className="auth-button" />
      <p>
        New user? <Link to="/register">Register</Link>
      </p>
      <p>
        <Link to="/reset-password">Forgot Password?</Link>
      </p>
    </form>
  );
}

export default Login;
