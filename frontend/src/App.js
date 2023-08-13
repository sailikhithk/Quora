// frontend/src/components/App.js

import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { createGlobalStyle } from "styled-components";
import axios from "axios";
import Navbar from "./components/Navbar";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";
import ResetPassword from "./components/auth/ResetPassword";
import Homepage from "./components/Homepage";
import Dashboard from "./components/Dashboard";
import Quiz from "./components/Quiz";
import QuizList from "./components/QuizList";
import Result from "./components/Result";
import styled from "styled-components";

const api = axios.create({
  baseURL: "http://localhost:5000",
});

const GlobalStyle = createGlobalStyle`
  body, html, #root {
    height: 100%;
    width: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden;
  }

  body {
    background-color: #000; 
    color: #fff; 
    font-family: 'Poppins', sans-serif;
    overflow: auto; // Add this to allow scrolling
  }

  a {
    color: #fff; 
  }
`;

const MainContent = styled.div`
  margin-left: 80px; // Adjust this to match the navbar width
  padding: 1rem;
`;

const App = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [authenticated, setAuthenticated] = useState(false);

  const handleLogin = async () => {
    const data = {
      username: username,
      password: password,
    };

    await api.post("/auth/login", data);
    setAuthenticated(true);
  };

  const handleRegister = async (
    username,
    password,
    email,
    role,
    institution
  ) => {
    const data = {
      username: username,
      password: password,
      email: email,
      role: role,
      institution: institution,
    };

    await api.post("/auth/register", data);
    setAuthenticated(true);
  };

  const handleLogout = () => {
    setAuthenticated(false);
  };

  return (
    <Router>
      <GlobalStyle />
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route
          path="/login"
          element={
            <>
              <Navbar
                authenticated={authenticated}
                handleLogout={handleLogout}
              />
              <Login
                username={username}
                setUsername={setUsername}
                password={password}
                setPassword={setPassword}
                handleLogin={handleLogin}
              />
            </>
          }
        />
        <Route
          path="/register"
          element={
            <>
              <Register
                username={username}
                setUsername={setUsername}
                password={password}
                setPassword={setPassword}
                email={email}
                setEmail={setEmail}
                handleRegister={handleRegister}
              />
            </>
          }
        />
        <Route
          path="/reset-password"
          element={
            <>
              <Navbar
                authenticated={authenticated}
                handleLogout={handleLogout}
              />
              <ResetPassword />
            </>
          }
        />
        <Route
          path="/dashboard"
          element={
            <>
              <Navbar
                authenticated={authenticated}
                handleLogout={handleLogout}
              />
              <Dashboard />
            </>
          }
        />
        <Route
          path="/quiz"
          element={
            <>
              <Navbar
                authenticated={authenticated}
                handleLogout={handleLogout}
              />
              <QuizList />
            </>
          }
        />
        <Route
          path="/quiz/:id/questions"
          element={
            <>
              <Navbar
                authenticated={authenticated}
                handleLogout={handleLogout}
              />
              <Quiz />
            </>
          }
        />
        <Route
          path="/quiz/:id"
          element={
            <>
              <Navbar
                authenticated={authenticated}
                handleLogout={handleLogout}
              />
              <Quiz />
            </>
          }
        />
        <Route
          path="/result/:id"
          element={
            <>
              <Navbar
                authenticated={authenticated}
                handleLogout={handleLogout}
              />
              <MainContent>
                <Result />
              </MainContent>
            </>
          }
        />
      </Routes>
    </Router>
  );
};

export default App;
