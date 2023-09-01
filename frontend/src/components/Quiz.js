import React, { useEffect, useState, useCallback } from "react";
import { useParams, useNavigate } from "react-router-dom";
import apiService from "../services/apiService";
import styled from "styled-components";

const QuizContainer = styled.form`
  color: #fff;
  background-color: transparent;
  padding-left: 11%; #quiz padding
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

const ButtonContainer = styled.div`
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  margin-top: 1rem;
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

const GoToDashboardButton = styled.button`
  color: #fff;
  background-color: #0a0;
  border: none;
  border-radius: 5px;
  padding: 0.5rem 1rem;
  transition: background-color 0.3s ease;
  &:hover {
    background-color: #0c0;
  }
`;

const Quiz = () => {
  const [quiz, setQuiz] = useState(null);
  const [questions, setQuestions] = useState([]);
  const { id } = useParams();
  const navigate = useNavigate();
  const [answers, setAnswers] = useState({});
  const user_id = localStorage.getItem("user_id"); // Retrieve the user_id from localStorage

  const fetchQuiz = useCallback(async () => {
    try {
      const response = await apiService.get(`/quiz/${id}/questions`);
      setQuiz(response.data);
      setQuestions(response.data.questions);
    } catch (error) {
      console.error(error);
    }
  }, [id]);

  useEffect(() => {
    fetchQuiz();
  }, [fetchQuiz]);

  const handleChange = (e, questionId) => {
    const selectedIndex = e.target.value;
    setAnswers({ ...answers, [questionId]: parseInt(selectedIndex, 10) });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const formattedAnswers = Object.keys(answers).map((question_id) => ({
        question_id: parseInt(question_id, 10),
        selected_options: [answers[question_id]],
      }));
      const payload = {
        user_id: parseInt(user_id, 10),
        quiz_id: parseInt(id, 10),
        content: formattedAnswers,
      };
      const response = await apiService.post(`/result/submit_answer`, payload);
      alert(`Your score is: ${response.data.score}`);
      navigate(`/result/${user_id}`);
    } catch (error) {
      console.error(error);
    }
  };

  const goToDashboard = () => {
    navigate("/dashboard");
  };

  return (
    <QuizContainer onSubmit={handleSubmit}>
      <h2 style={{ color: "white" }}>{quiz ? quiz.title : "Loading..."}</h2>
      {questions.map((question) => (
        <QuestionContainer key={question.id}>
          <p>{question.content.question}</p>
          {question.content.options.map((answer, index) => (
            <OptionLabel key={index}>
              <OptionInput
                type="radio"
                id={`question-${question.id}-option-${index}`}
                name={`question-${question.id}`}
                value={index}
                onChange={(e) => handleChange(e, question.id)}
              />
              {answer}
            </OptionLabel>
          ))}
        </QuestionContainer>
      ))}
      <ButtonContainer>
        <SubmitButton type="submit">Submit Quiz</SubmitButton>
        <GoToDashboardButton onClick={goToDashboard}>
          Go to Dashboard
        </GoToDashboardButton>
      </ButtonContainer>
    </QuizContainer>
  );
};

export default Quiz;
