import React, { useState } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import styled from "styled-components";
import quizImage from "../../assets/quiz-time.webp"; // <-- Add this

const StyledButton = styled(Link)`
  display: inline-block;
  background-color: red;
  color: white;
  padding: 0.5rem 1rem;
  margin: 0.5rem;
  border-radius: 5px;
  text-decoration: none;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #b30000;
  }
`;

const ButtonsContainer = styled.div`
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  width: 200px;
  position: absolute;
  right: 2rem;
  top: 2rem;
`;

const Container = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 50px);
  position: relative;
  background-color: #000;
`;

const QuizImage = styled.img`
  max-width: 200%;
  height: auto;
  margin-right: 10%;
`;

const Form = styled.form`
  padding: 40px;
  width: 400px;
  background-color: transparent;
`;

const InputText = styled.input.attrs((props) => ({
  type: "text",
}))`
  display: block;
  width: 100%;
  padding: 15px;
  margin-bottom: 20px;
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
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #b30000;
  }
`;

function Login({ handleLogin }) {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://localhost:5000/auth/login", {
        username,
        password,
      });
      localStorage.setItem("token", res.data.access_token); // changed "token" to "access_token"
      alert("Login successful!");
      handleLogin();
      navigate("/dashboard");
    } catch (err) {
      alert("Login failed");
    }
  };

  return (
    <Container>
      <QuizImage src={quizImage} alt="Quiz" />
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
          New user? <StyledButton to="/register">Register</StyledButton>
        </p>
        <p>
          <Link to="/reset-password">Forgot Password?</Link>
        </p>
      </Form>
      <ButtonsContainer>
        <StyledButton to="/">Go to Home</StyledButton>
      </ButtonsContainer>
    </Container>
  );
}

export default Login;
