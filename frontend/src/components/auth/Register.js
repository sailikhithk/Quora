// frontend/src/components/auth/Register.js

import React, { useState } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";
import styled from "styled-components";
import quizImage from "../../assets/quiz-time.webp";

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
  max-width: 200%; // Increase this to enlarge the image size
  height: auto;
  margin-right: 10%;
`;

const Form = styled.form`
  padding: 40px; // Increased this from 30px to 40px
  width: 400px; // Increased this from 360px to 400px
  background-color: transparent;
`;

const InputText = styled.input.attrs((props) => ({
  type: "text",
}))`
  display: block;
  width: 100%;
  padding: 15px; // Increased padding from 10px to 15px
  margin-bottom: 20px; // Increased margin from 10px to 20px
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

function Register({ handleRegister }) {
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("");
  const [institution, setInstitution] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await handleRegister(username, password, email, role, institution);
      navigate("/login");
    } catch (err) {
      console.error(err);
      alert("Registration failed");
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
        <InputText
          placeholder="Email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <InputPassword
          placeholder="Password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <InputText
          placeholder="Institution"
          onChange={(e) => setInstitution(e.target.value)}
        />
        <select
          value={role}
          onChange={(e) => setRole(e.target.value)}
          style={{
            width: "100%",
            boxSizing: "border-box",
            marginBottom: "10px",
          }}
        >
          <option value="">Select Role...</option>
          <option value="Student">Student</option>
          <option value="Teacher">Teacher</option>
          <option value="Admin">Admin</option>
        </select>
        <InputSubmit value="Register" />
        <p>
          Already a user? <StyledButton to="/login">Login</StyledButton>
        </p>
      </Form>
      <ButtonsContainer>
        <StyledButton to="/">To Go Home</StyledButton>
      </ButtonsContainer>
    </Container>
  );
}

export default Register;
