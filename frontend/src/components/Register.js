import React, { useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import "../css/main.css";

function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("");
  const [emailError, setEmailError] = useState("");
  const [usernameError, setUsernameError] = useState("");
  const [passwordError, setPasswordError] = useState("");

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

  const validateUsername = () => {
    if (username.trim() === "") {
      setUsernameError("Username is required");
    } else {
      setUsernameError("");
    }
  };

  const validatePassword = () => {
    var re = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$/;
    if (!re.test(password)) {
      setPasswordError(
        "Password must contain minimum eight characters, at least one letter, one number and one special character"
      );
    } else {
      setPasswordError("");
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    validateEmail();
    validateUsername();
    validatePassword();

    if (emailError || usernameError || passwordError) return;

    try {
      await axios.post("http://localhost:5000/register", {
        username,
        password,
        email,
        role,
      });
      alert("Registration successful!");
    } catch (err) {
      if (err.response.data.error === "Username taken") {
        alert(
          "Username is already taken. If you are an existing user, please login"
        );
      }
      if (err.response.data.error === "Email taken") {
        alert(
          "Email is already registered. If you are an existing user, please login"
        );
      } else {
        alert("Registration failed");
      }
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
        onBlur={validateUsername}
        style={{ width: "100%", boxSizing: "border-box" }}
      />
      {usernameError && (
        <p style={{ color: "red" }}>
          <i className="fa fa-exclamation-circle" aria-hidden="true"></i>{" "}
          {usernameError}
        </p>
      )}
      <input
        type="text"
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
        onBlur={validateEmail}
        style={{ width: "100%", boxSizing: "border-box" }}
        title="The email should contain '@' and a domain extension like '.com'"
      />
      {emailError && (
        <p style={{ color: "red" }}>
          <i className="fa fa-exclamation-circle" aria-hidden="true"></i>{" "}
          {emailError}
        </p>
      )}
      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
        onBlur={validatePassword}
        style={{ width: "100%", boxSizing: "border-box" }}
        title="The password should contain alphanumeric characters with a minimum length of 8 and at least one special character"
      />
      {passwordError && (
        <p style={{ color: "red" }}>
          <i className="fa fa-exclamation-circle" aria-hidden="true"></i>{" "}
          {passwordError}
        </p>
      )}
      <select
        value={role}
        onChange={(e) => setRole(e.target.value)}
        style={{ width: "100%", boxSizing: "border-box" }}
      >
        <option value="">Select Role...</option>
        <option value="student">Student</option>
        <option value="teacher">Teacher</option>
        <option value="admin">Admin</option>
      </select>
      <input type="submit" value="Register" />
      <p>
        Already a user? <Link to="/login">Login</Link>
      </p>
    </form>
  );
}

export default Register;
