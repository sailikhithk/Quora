import React, { useEffect, useState } from "react";
import apiService from "../services/apiService";
import styled from "styled-components";

const DashboardContainer = styled.div`
  padding-left: 15%; // Padding to offset the Navbar
  padding-top: 20px;
  width: 90%;
  background: #fdfaf5;
  height: 100%;
`;

const QuizSummary = styled.div`
  display: flex;
  overflow-x: scroll; // Enables horizontal scrolling
  white-space: nowrap; // Prevents wrapping to the next line
`;

const QuizCard = styled.div`
  border-radius: 10px;
  padding: 15px;
  margin: 10px;
  width: 300px; // Fixed width for uniform size
  height: 270px;
  display: inline-block; // Inline display to place cards beside each other
  transition: 0.3s;
  &:hover {
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  }
  background: #fff;
`;

const QuizTitle = styled.h3`
  font-size: 24px;
  margin: 10px 0;
  color: #071437;
  margin-left: 5px;
`;

const QuizDetails = styled.div`
  font-size: 14px;
  margin: 5px 0;
  padding: 5px;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const DashboardButton = styled.button`
  color: #fff;
  background-color: #00B2FF;
  border: none;
  border-radius: 20px;
  padding: 0.5rem 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
  &:hover {
    color: unset;
    text-decoration: none;
  }
`;

const Dashboard = () => {
  const [quizzes, setQuizzes] = useState([]);
  const user_id = localStorage.getItem("user_id");

  useEffect(() => {
    const user_id = "1";
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
      <h2 style={{ color: "#071437" }}>Your Quiz Performance Summary</h2>
      <QuizSummary>
        {quizzes.map((quiz) => (
          <QuizCard key={quiz.quiz_id}>
            <QuizTitle>{quiz.title}</QuizTitle>
            <div style={{ marginTop: "20px" }}>
              <QuizDetails>
                <span style={{ color: "#B5B5C3", fontSize: "1rem" }}>
                  Recent Score:{" "}
                </span>
                <span
                  style={{
                    color: "#4B5675",
                    fontSize: "1rem",
                    fontWeight: "bold",
                  }}
                >
                  {quiz.max_scored_marks}
                </span>
              </QuizDetails>
              <QuizDetails>
                <span style={{ color: "#B5B5C3", fontSize: "1rem" }}>
                  Number of Attempts:{" "}
                </span>
                <span
                  style={{
                    color: "#4B5675",
                    fontSize: "1rem",
                    fontWeight: "bold",
                  }}
                >
                  {quiz.no_of_attempts}
                </span>
              </QuizDetails>
              <QuizDetails>
                <span style={{ color: "#B5B5C3", fontSize: "1rem" }}>
                  Highest Score:{" "}
                </span>
                <span
                  style={{
                    color: "#4B5675",
                    fontSize: "1rem",
                    fontWeight: "bold",
                  }}
                >
                  {quiz.max_scored_marks}
                </span>
              </QuizDetails>
              <QuizDetails>
                <span style={{ color: "#B5B5C3", fontSize: "1rem" }}>
                  Is Qualified:{" "}
                </span>
                <span
                  style={{
                    color: "#4B5675",
                    fontSize: "1rem",
                    fontWeight: "bold",
                  }}
                >
                  {quiz.is_qualified ? "Yes" : "No"}
                </span>
              </QuizDetails>
            </div>
            <div
              style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                marginTop: "30px",
              }}
            >
              <DashboardButton as="a" href={`/quiz/${quiz.quiz_id}/questions`}>
                Attempt Quiz
              </DashboardButton>
            </div>
          </QuizCard>
        ))}
      </QuizSummary>
    </DashboardContainer>
  );
};

export default Dashboard;
