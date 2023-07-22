import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import axios from "axios";
import Navbar from "./components/Navbar";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";
import ResetPassword from "./components/auth/ResetPassword";
import Homepage from "./components/Homepage";
import Dashboard from "./components/Dashboard";
import Quiz from "./components/Quiz";
import QuizList from "./components/QuizList"; // <- import your new component
import Result from "./components/Result";

// Set up axios
const api = axios.create({
  baseURL: "http://localhost:5000",
});

const App = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");

  const handleLogin = async () => {
    const data = {
      username: username,
      password: password,
    };

    await api.post("/api/login", data);
  };

  const handleRegister = async () => {
    const data = {
      username: username,
      password: password,
      email: email,
    };

    await api.post("/api/register", data);
  };

  return (
    <Router>
      <Navbar />
      <div className="content">
        <Routes>
          <Route path="/" element={<Homepage />} />
          <Route
            path="/login"
            element={
              <Login
                username={username}
                setUsername={setUsername}
                password={password}
                handleLogin={handleLogin}
              />
            }
          />
          <Route
            path="/register"
            element={
              <Register
                username={username}
                setUsername={setUsername}
                password={password}
                email={email}
                setEmail={setEmail}
                handleRegister={handleRegister}
              />
            }
          />
          <Route path="/reset-password" element={<ResetPassword />} />
          <Route path="/dashboard" element={<Dashboard />} />
          <Route path="/quiz/:id" element={<Quiz />} />
          <Route path="/quiz" element={<QuizList />} />{" "}
          {/* <- your new route */}
          <Route path="/result" element={<Result />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
