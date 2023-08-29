import React, { useEffect, useState } from "react";
import apiService from "../services/apiService";
import styled from "styled-components";

const DashboardContainer = styled.div`
  padding-left: 10%; // Padding to offset the Navbar
  padding-top: 20px;
  width: 90%;
`;

const QuizSummary = styled.div`
  display: flex;
  overflow-x: scroll; // Enables horizontal scrolling
  white-space: nowrap; // Prevents wrapping to the next line
`;

const QuizCard = styled.div`
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 15px;
  margin: 10px;
  width: 300px; // Fixed width for uniform size
  display: inline-block; // Inline display to place cards beside each other
  transition: 0.3s;
  &:hover {
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  }
`;

const QuizTitle = styled.h3`
  font-size: 24px;
  margin: 10px 0;
`;

const QuizDetails = styled.p`
  font-size: 14px;
  margin: 5px 0;
`;

const DashboardButton = styled.button`
  color: white;
  background-color: #0a0;
  border: none;
  border-radius: 5px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  &:hover {
    background-color: #0c0;
  }
`;

const Dashboard = () => {
  const [quizzes, setQuizzes] = useState([]);
  const user_id = localStorage.getItem("user_id");
  console.log(user_id);

  useEffect(() => {
    const fetchQuizzes = async () => {
      try {
        const response = await apiService.get(`quiz/${user_id}/list`);
        setQuizzes(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    fetchQuizzes();
  }, [user_id]);

  return (
    <DashboardContainer>
      <h2>Your Quiz Performance Summary</h2>
      <QuizSummary>
        {quizzes.map((quiz) => (
          <QuizCard key={quiz.quiz_id}>
            <QuizTitle>{quiz.title}</QuizTitle>
            <QuizDetails>Recent Score: {quiz.max_scored_marks}</QuizDetails>
            <QuizDetails>Number of Attempts: {quiz.no_of_attempts}</QuizDetails>
            <QuizDetails>Highest Score: {quiz.max_scored_marks}</QuizDetails>
            <QuizDetails>
              Is Qualified: {quiz.is_qualified ? "Yes" : "No"}
            </QuizDetails>
            <DashboardButton as="a" href={`/quiz/${quiz.quiz_id}/questions`}>
              Attempt Quiz
            </DashboardButton>
          </QuizCard>
        ))}
      </QuizSummary>
    </DashboardContainer>
  );
};

export default Dashboard;
