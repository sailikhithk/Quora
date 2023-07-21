import React, { useState } from "react";
import axios from "axios";
import "../css/main.css";

function ResetPassword() {
  const [email, setEmail] = useState("");
  const [emailError, setEmailError] = useState("");

  const validateEmail = () => {
    var re = /\S+@\S+\.\S+/;
    if (!re.test(email)) {
      setEmailError(
        "Invalid email format. Correct format: example@example.com"
      );
    } else {
      setEmailError("");
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    validateEmail();

    if (emailError) return;

    try {
      await axios.post("http://localhost:5000/reset-password", { email });
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
        onBlur={validateEmail}
        style={{ width: "100%", boxSizing: "border-box" }}
      />
      {emailError && (
        <p style={{ color: "red" }}>
          <i className="fa fa-exclamation-circle" aria-hidden="true"></i>{" "}
          {emailError}
        </p>
      )}
      <input type="submit" value="Reset Password" className="auth-button" />
    </form>
  );
}

export default ResetPassword;
