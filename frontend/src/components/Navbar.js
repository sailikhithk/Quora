import React from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import {
  BiHomeAlt,
  BiBookOpen,
  BiUserCircle,
  BiCog,
  BiLogOut,
} from "react-icons/bi";

const StyledNavbar = styled.nav`
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  background-color: #000;
  color: white;
  padding: 1rem;
  width: 80px;
  height: 100vh;
  position: fixed;
`;

const StyledLink = styled(Link)`
  color: white;
  text-decoration: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0.5rem 0;
  transition: color 0.3s ease;

  &:hover {
    color: darkred;
  }
`;

function Navbar({ handleLogout }) {
  return (
    <StyledNavbar>
      <StyledLink to="/">
        <BiHomeAlt size={30} />
        Home
      </StyledLink>
      <StyledLink to="/dashboard">
        <BiHomeAlt size={30} />
        Dashboard
      </StyledLink>
      <StyledLink to="/quiz">
        <BiBookOpen size={30} />
        Quiz
      </StyledLink>
      <StyledLink to="/profile">
        <BiUserCircle size={30} />
        Profile
      </StyledLink>
      <StyledLink to="/settings">
        <BiCog size={30} />
        Settings
      </StyledLink>
      <StyledLink to="/" onClick={handleLogout}>
        <BiLogOut size={30} />
        Logout
      </StyledLink>
    </StyledNavbar>
  );
}

export default Navbar;
