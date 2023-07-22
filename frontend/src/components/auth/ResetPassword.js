import React, { useState } from "react";
import axios from "axios";
import "../../css/main.css";

function ResetPassword() {
  const [email, setEmail] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Your backend currently doesn't support password reset.
      // When you implement it, make sure to replace the endpoint below.
      await axios.post("http://localhost:5000/api/user/reset-password", {
        email,
      });
      alert("A reset password link has been sent to your email.");
    } catch (err) {
      alert("An error occurred. Please try again later.");
    }
  };

  return (
    <form onSubmit={handleSubmit} className="auth-form">
      <input
        type="email"
        placeholder="Enter your email"
        onChange={(e) => setEmail(e.target.value)}
        style={{ width: "100%", boxSizing: "border-box" }}
      />
      <input type="submit" value="Reset Password" className="auth-button" />
    </form>
  );
}

export default ResetPassword;
