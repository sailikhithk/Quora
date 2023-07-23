import React, { useEffect, useState, useCallback } from "react";
import { useParams } from "react-router-dom";
import apiService from "../services/apiService";
import styled from "styled-components";

const QuizContainer = styled.form`
  color: #fff;
  background-color: transparent;
`;

const QuestionContainer = styled.div`
  background-color: #444;
  border-radius: 5px;
  padding: 1rem;
  margin-bottom: 1rem;
`;

const OptionInput = styled.input`
  margin-right: 0.5rem;
`;

const OptionLabel = styled.label`
  display: flex;
  align-items: center;
  padding: 0.5rem;
  border-radius: 5px;
  cursor: pointer;
  &:hover {
    background-color: #555;
  }
`;

const SubmitButton = styled.button`
  color: #fff;
  background-color: red;
  border: none;
  border-radius: 5px;
  padding: 0.5rem 1rem;
  transition: background-color 0.3s ease;
  &:hover {
    background-color: darkred;
  }
`;

const Quiz = () => {
  const [quiz, setQuiz] = useState(null);
  const [questions, setQuestions] = useState([]);
  const { id } = useParams();

  const [answers, setAnswers] = useState({});

  const fetchQuiz = useCallback(async () => {
    try {
      const response = await apiService.get(`/quiz/${id}`);
      const apiQuestions = response.data.questions.map((question) => ({
        ...question,
        answers: ["Option 1", "Option 2", "Option 3", "Option 4"],
      }));
      setQuiz(response.data);
      setQuestions(apiQuestions);
    } catch (error) {
      console.error(error);
    }
  }, [id]);

  useEffect(() => {
    fetchQuiz();
  }, [fetchQuiz]);

  const handleChange = (e, questionId) => {
    setAnswers({ ...answers, [questionId]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await apiService.post(`/quiz/${id}/submit`, answers);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <QuizContainer onSubmit={handleSubmit}>
      <h2 style={{ color: "white" }}>{quiz ? quiz.title : "Loading..."}</h2>{" "}
      {/* Color of quiz title changed to white */}
      {questions.map((question) => (
        <QuestionContainer key={question.id}>
          <p>{question.content}</p>
          {question.answers.map((answer, index) => (
            <OptionLabel key={index}>
              <OptionInput
                type="radio"
                id={`question-${question.id}-option-${index}`}
                name={`question-${question.id}`}
                value={answer}
                onChange={(e) => handleChange(e, question.id)}
              />
              {answer}
            </OptionLabel>
          ))}
        </QuestionContainer>
      ))}
      <SubmitButton type="submit">Submit Quiz</SubmitButton>
    </QuizContainer>
  );
};

export default Quiz;
