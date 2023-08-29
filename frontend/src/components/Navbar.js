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
  background-color: #fff;
  padding: 1rem;
  width: 150px;
  height: 100vh;
  position: fixed;
`;

const StyledLink = styled(Link)`
  color: white;
  text-decoration: none;
  display: flex;
  flex-direction: row;
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
      <div style={{ padding: "20px" }}>
        <StyledLink to="/">
          <BiHomeAlt size={25} color={"#78829D"} />
          <span style={{ marginLeft: "10px", color: "#78829D" }}>Home</span>
        </StyledLink>
      </div>
      <div style={{ padding: "20px" }}>
        <StyledLink to="/dashboard">
          <BiHomeAlt size={25} color={"#78829D"} />
          <span style={{ marginLeft: "10px", color: "#78829D" }}>
            Dashboard
          </span>
        </StyledLink>
      </div>
      <div style={{ padding: "20px" }}>
        <StyledLink to="/quiz">
          <BiBookOpen size={25} color={"#78829D"} />
          <span style={{ marginLeft: "10px", color: "#78829D" }}>Quiz</span>
        </StyledLink>
      </div>
      <div style={{ padding: "20px" }}>
        <StyledLink to="/profile">
          <BiUserCircle size={25} color={"#78829D"} />
          <span style={{ marginLeft: "10px", color: "#78829D" }}>Profile</span>
        </StyledLink>
      </div>
      <div style={{ padding: "20px" }}>
        <StyledLink to="/settings">
          <BiCog size={25} color={"#78829D"} />
          <span style={{ marginLeft: "10px", color: "#78829D" }}>Settings</span>
        </StyledLink>
      </div>
      <div style={{ padding: "20px" }}>
        <StyledLink to="/" onClick={handleLogout}>
          <BiLogOut size={25} color={"#78829D"} />
          <span style={{ marginLeft: "10px", color: "#78829D" }}>Logout</span>
        </StyledLink>
      </div>
    </StyledNavbar>
  );
}

export default Navbar;
