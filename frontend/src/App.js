import React, { useState } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import axios from "axios";
import Login from "./components/Login";
import Register from "./components/Register";
import ResetPassword from "./components/ResetPassword"; // import the ResetPassword component

const App = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");

  const handleLogin = async () => {
    const data = {
      username: username,
      password: password,
    };

    await axios.post("/api/login", data, {
      headers: {
        "Access-Control-Allow-Origin": "*",
      },
    });
  };

  const handleRegister = async () => {
    const data = {
      username: username,
      password: password,
      email: email,
    };

    await axios.post("/api/register", data, {
      headers: {
        "Access-Control-Allow-Origin": "*",
      },
    });
  };

  return (
    <BrowserRouter>
      <Routes>
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
        <Route
          path="/reset-password"
          element={<ResetPassword />} // add a route for the ResetPassword component
        />
      </Routes>
    </BrowserRouter>
  );
};

export default App;