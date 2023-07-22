import React, { useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import "../../css/main.css";

function Register() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("");
  const [institution, setInstitution] = useState(""); // Add this line

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://localhost:5000/api/user/register", {
        username,
        password,
        email,
        role,
        institution, // Add this line
      });
      alert("Registration successful!");
    } catch (err) {
      alert("Registration failed");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
        style={{ width: "100%", boxSizing: "border-box" }}
      />
      <input
        type="text"
        placeholder="Email"
        onChange={(e) => setEmail(e.target.value)}
        style={{ width: "100%", boxSizing: "border-box" }}
      />
      <input
        type="password"
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
        style={{ width: "100%", boxSizing: "border-box" }}
      />
      <input
        type="text"
        placeholder="Institution"
        onChange={(e) => setInstitution(e.target.value)}
        style={{ width: "100%", boxSizing: "border-box" }}
      />
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
