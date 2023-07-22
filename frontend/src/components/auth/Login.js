import React, { useState } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import styled from "styled-components";

const Form = styled.form`
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
`;

const InputText = styled.input.attrs((props) => ({
  type: "text",
}))`
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #007aff;
  border-radius: 5px;
`;

const InputPassword = styled.input.attrs((props) => ({
  type: "password",
}))`
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #007aff;
  border-radius: 5px;
`;

const InputSubmit = styled.input.attrs((props) => ({
  type: "submit",
}))`
  background-color: red;
  color: #fff;
  padding: 10px;
  border: none;
  border-radius: 50px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: darkred;
  }
`;

function Login({ handleLogin }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://localhost:5000/api/user/login", {
        username,
        password,
      });
      localStorage.setItem("token", res.data.token);
      alert("Login successful!");
      handleLogin();
      navigate("/dashboard");
    } catch (err) {
      alert("Login failed");
    }
  };

  return (
    <Form onSubmit={handleSubmit}>
      <InputText
        placeholder="Username"
        onChange={(e) => setUsername(e.target.value)}
      />
      <InputPassword
        placeholder="Password"
        onChange={(e) => setPassword(e.target.value)}
      />
      <InputSubmit value="Login" />
      <p>
        New user? <Link to="/register">Register</Link>
      </p>
      <p>
        <Link to="/reset-password">Forgot Password?</Link>
      </p>
    </Form>
  );
}

export default Login;
