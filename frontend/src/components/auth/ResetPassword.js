import React, { useState } from "react";
import axios from "axios";
import { Link } from "react-router-dom";
import styled from "styled-components";
import quizImage from "../../assets/quiz-time.webp";

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

const StyledButton = styled(Link)`
  color: white;
  text-decoration: none;
  padding: 0.5rem 1rem;
  background-color: red;
  border: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: darkred;
  }
`;

const InputEmail = styled.input.attrs((props) => ({
  type: "email",
}))`
  display: block;
  width: 100%;
  padding: 15px;
  margin-bottom: 20px;
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

function ResetPassword() {
  const [email, setEmail] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://localhost:5001/auth/reset-password", {
        email,
      });
      alert("A reset password link has been sent to your email.");
    } catch (err) {
      alert("An error occurred. Please try again later.");
    }
  };

  return (
    <Container>
      <QuizImage src={quizImage} alt="Quiz" />
      <Form onSubmit={handleSubmit}>
        <InputEmail
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <InputSubmit value="Reset Password" />
        <p style={{ marginTop: "1rem" }}>
          Already a user? <StyledButton to="/login">Login</StyledButton>
        </p>
        <p style={{ marginTop: "1rem" }}>
          New user? <StyledButton to="/register">Register</StyledButton>
        </p>
      </Form>
    </Container>
  );
}

export default ResetPassword;
