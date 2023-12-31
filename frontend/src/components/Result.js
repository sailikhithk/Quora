import React, { useEffect, useState, useCallback } from "react";
import apiService from "../services/apiService";
import { useParams, useNavigate } from "react-router-dom"; // Import useNavigate
import styled from "styled-components";

const ResultContainer = styled.div`
  padding: 20px;
  margin-left: 100px; // Added to offset the navbar
`;

const QuestionContainer = styled.div`
  background-color: #444;
  border-radius: 5px;
  padding: 1rem;
  margin-bottom: 1rem;
`;

const Option = styled.div`
  display: flex;
  align-items: center;
  padding: 0.5rem;
  border-radius: 5px;
  color: ${(props) =>
    props.isCorrect ? "#0a0" : props.isSelected ? "#f00" : "#fff"};
`;

const DashboardButton = styled.button`
  padding: 0.5rem;
  margin-top: 1rem;
  background-color: #0a0;
  border: none;
  border-radius: 5px;
  color: #fff;
  cursor: pointer;
  transition: background-color 0.3s ease;
  &:hover {
    background-color: #0c0;
  }
`;

const Result = () => {
  const [result, setResult] = useState(null);
  const { id } = useParams();
  const navigate = useNavigate(); // Define navigate function

  const fetchResult = useCallback(async () => {
    try {
      const response = await apiService.get(`/result/${id}/get_result`);
      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
  }, [id]);

  useEffect(() => {
    fetchResult();
  }, [fetchResult]);

  return (
    <ResultContainer>
      <h2>Result</h2>
      {result ? (
        <div>
          <h3>Your score: {result.score}</h3>
          {result.answers.map((answer, index) => (
            <QuestionContainer key={index}>
              <p>Question ID: {answer.question_id}</p>
              {answer.correct_options.map((option, idx) => (
                <Option
                  key={idx}
                  isCorrect={answer.correct_options.includes(idx)}
                  isSelected={answer.selected_options.includes(idx)}
                >
                  Option {option}: {answer.is_correct ? "✓" : "✗"}
                </Option>
              ))}
              <p>Is Correct: {answer.is_correct ? "Yes" : "No"}</p>
              <p>Score Allocated: {answer.score_allocated}</p>
            </QuestionContainer>
          ))}
          <DashboardButton onClick={() => navigate("/dashboard")}>
            Go back to Dashboard
          </DashboardButton>{" "}
          {/* Added Dashboard Button */}
        </div>
      ) : (
        "Loading..."
      )}
    </ResultContainer>
  );
};

export default Result;
