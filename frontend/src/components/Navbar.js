// frontend/src/components/Navbar.js

import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";

const StyledNavbar = styled.nav`
  display: flex;
  justify-content: space-around;
  background-color: #000;
  padding: 1rem;
  color: white;
`;

const StyledLink = styled(Link)`
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

function Navbar({ authenticated, handleLogout }) {
  return (
    <StyledNavbar>
      <StyledLink to="/">Home</StyledLink>
      {authenticated ? (
        <>
          <StyledLink to="/dashboard">Dashboard</StyledLink>
          <StyledLink to="/quiz">Quiz</StyledLink>
          <StyledLink to="/result">Result</StyledLink>
          <StyledLink to="/logout" onClick={handleLogout}>
            Logout
          </StyledLink>
        </>
      ) : (
        <>
          <StyledLink to="/login">Login</StyledLink>
          <StyledLink to="/register">Register</StyledLink>
        </>
      )}
    </StyledNavbar>
  );
}

export default Navbar;
