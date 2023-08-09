// frontend/src/components/Homepage.js

import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import quizImage from "../assets/quiz.png"; // Update this with your image path
import quizLogo from "../assets/logo.png";

const StyledButton = styled(Link)`
  display: inline-block;
  background-color: red;
  color: white;
  padding: 0.5rem 1rem;
  margin: 0.5rem;
  border-radius: 5px;
  text-decoration: none;
  transition: background-color 0.3s ease;
  font-family: "Roboto", sans-serif;

  &:hover {
    background-color: #b30000;
    color: white; // This line ensures that the color stays white even on hover
  }
`;

const Heading = styled.h1`
  color: white;
  font-family: "Roboto", sans-serif;
  font-weight: bold;
  font-size: 2rem;
`;

const SubCaption = styled.h2`
  color: white;
  font-family: "Roboto", sans-serif;
  font-size: 1rem;
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

const QuizImage = styled.img`
  max-width: 50%;
  height: auto;
  border-radius: 20px; // Add this to make the image corners rounded
`;

const Logo = styled.img`
  max-width: 100px;
  height: auto;
  margin-bottom: 1rem;
`;

const ContentContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-left: 2rem; // Add this to create space between the image and text
`;

const HomepageContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 50px); // Subtract the height of the Navbar
  position: relative; // This is needed to position the ButtonsContainer absolutely
`;

function Homepage() {
  return (
    <HomepageContainer>
      <QuizImage src={quizImage} alt="Quiz" />
      <ContentContainer>
        <Logo src={quizLogo} alt="QuizLogo" />
        <Heading>QuizMate Student</Heading>
        <SubCaption>Pocket Quiz</SubCaption>
      </ContentContainer>
      <ButtonsContainer>
        <StyledButton to="/login">Login</StyledButton>
        <StyledButton to="/register">Register</StyledButton>
      </ButtonsContainer>
    </HomepageContainer>
  );
}

export default Homepage;
