import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import apiService from "../services/apiService";
import styled from "styled-components";

const UserDetails = styled.div`
  background-color: #f0f0f0;
  padding: 10px;
  border-radius: 5px;
  margin: 10px;
`;

const LogoutButton = styled.button`
  color: white;
  background-color: red;
  border: none;
  border-radius: 5px;
  padding: 0.5rem 1rem;
  position: absolute;
  top: 10px;
  right: 10px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  &:hover {
    background-color: darkred;
  }
`;

const QuizCard = styled.div`
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 5%;
  margin: 10%;
  width: 20%;
  transition: 0.3s;
  &:hover {
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  }
`;

const QuizImage = styled.img`
  width: 100%;
  height: 200px;
`;

const QuizTitle = styled.h2`
  font-size: 48px;
`;

const QuizCategory = styled.p`
  font-size: 14px;
  color: grey;
`;

const Progress = styled.div`
  background-color: #fff;
  height: 20px;
  position: relative;
  border-radius: 5px;
  &::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: ${(props) => props.progress}%;
    height: 100%;
    background-color: green;
    border-radius: 5px;
  }
`;

const DashboardTitle = styled.h2`
  padding-left: 10%;
`;

const Dashboard = () => {
  const [quizzes, setQuizzes] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const user_id = localStorage.getItem("user_id"); // Retrieve the user_id from localStorage
  const user_name = localStorage.getItem("user_name"); // Retrieve the username from localStorage
  const email = localStorage.getItem("email"); // Retrieve the email from localStorage

  useEffect(() => {
    const fetchQuizzes = async () => {
      try {
        const response = await apiService.get(`quiz/${user_id}/list`); // Include the user_id in the route
        console.log(response.data); // Log the response data to inspect
        setQuizzes(response.data);
        setLoading(false);
      } catch (error) {
        console.error(error);
        setError(error.message || "An error occurred");
        setLoading(false);
      }
    };

    fetchQuizzes();
  }, [user_id]);

  const handleLogout = () => {
    localStorage.removeItem("user_id"); // Add this line
    localStorage.removeItem("user_name");
    localStorage.removeItem("email");
    window.location.reload();
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div>
      <LogoutButton onClick={handleLogout}>Logout</LogoutButton>
      <UserDetails>
        <p>Username: {user_name}</p>
        <p>Email: {email}</p>
      </UserDetails>
      <DashboardTitle>Dashboard</DashboardTitle>
      <div style={{ display: "flex", flexWrap: "wrap" }}>
        {quizzes.map((quiz) => (
          <QuizCard key={quiz.id}>
            <Link to={`/quiz/${quiz.quiz_id}/questions`}>
              <QuizImage src={quiz.image} alt="Quiz" />
              <QuizTitle>{quiz.title}</QuizTitle>
              <QuizCategory>Category: {quiz.category}</QuizCategory>
              <Progress progress={quiz.progress} />
            </Link>
          </QuizCard>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
