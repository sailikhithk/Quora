// Dashboard.js
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import apiService from "../services/apiService";

const Dashboard = () => {
  const [quizzes, setQuizzes] = useState([]);

  useEffect(() => {
    fetchQuizzes();
  }, []);

  const fetchQuizzes = async () => {
    try {
      const response = await apiService.get("/quiz");
      setQuizzes(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Dashboard</h2>
      {quizzes.map((quiz) => (
        <div key={quiz.id}>
          <Link to={`/quiz/${quiz.id}`}>{quiz.title}</Link>
        </div>
      ))}
    </div>
  );
};

export default Dashboard;
