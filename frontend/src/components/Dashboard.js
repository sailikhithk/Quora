// Dashboard.js
import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import apiService from "../services/apiService";

const Dashboard = () => {
  const [quizzes, setQuizzes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchQuizzes();
  }, []);

  const fetchQuizzes = async () => {
    try {
      const response = await apiService.get("/quiz");
      setQuizzes(response.data);
      console.log(response.data);
      setLoading(false);
    } catch (error) {
      console.error(error);
      setError(error.message || "An error occurred");
      setLoading(false);
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <h2>Dashboard</h2>
      {quizzes.map((quiz) => {
        console.log(quiz);
        return (
          <div key={quiz.id}>
            <Link to={`/quiz/${quiz.id}`}>{quiz.title}</Link>
          </div>
        );
      })}
    </div>
  );
};

export default Dashboard;
