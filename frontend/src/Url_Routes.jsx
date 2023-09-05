import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { BrowserRouter, Navigate, Route, Routes } from "react-router-dom";
import Login from "./screens/Login";
import HeaderFooterLayout from "./HeaderFooterLayout";
import Dashboard from "./screens/Dashboard";
import Profile from "./screens/Profile";
import Users from "./screens/Users";
import Home from "./screens/Home";
import LessonIndex from "./screens/Quiz/LessonIndex";
import GLOBAL_CONSTANTS from "../GlobalConstants";
import LessonView from "./screens/Quiz/LessonView";
import QuizListing from "./screens/QuizListing";

function Url_Routes() {
   
  

  return (
    <BrowserRouter>
      <Routes>
      {
        GLOBAL_CONSTANTS?.loggedIn &&
          <>
          {
            GLOBAL_CONSTANTS?.user_cred?.role_id == 1 ? <>
          <Route excat path="/" element={<HeaderFooterLayout render={Dashboard} /> } />
          <Route excat path="/dashboard" element={<HeaderFooterLayout render={Dashboard} /> } />
          <Route excat path="/quiz" element={<HeaderFooterLayout render={QuizListing} /> } />
          <Route excat path="/users" element={<HeaderFooterLayout render={Users} /> } />
          <Route excat path="/profile" element={<HeaderFooterLayout render={Profile} /> } />
              
            </>:<>
            <Route excat path="/" element={<HeaderFooterLayout render={Dashboard} /> } />
          <Route excat path="/dashboard" element={<HeaderFooterLayout render={Dashboard} /> } />
          <Route excat path="/lessons" element={<HeaderFooterLayout render={LessonIndex} /> } />
          <Route excat path="/lesson/:id" element={<HeaderFooterLayout render={LessonView} /> } />
          <Route excat path="/profile" element={<HeaderFooterLayout render={Profile} /> } />
            </>
          }
          </>
      }
          <Route excat path="/" element={<Login />} />
          <Route path="*" element={<Navigate to="/" />} />

      </Routes>
    </BrowserRouter>
  );
}

export default Url_Routes;
