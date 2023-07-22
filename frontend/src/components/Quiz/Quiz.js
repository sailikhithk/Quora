import React, { useEffect, useState } from "react";
import apiService from "../services/apiService";

const Quiz = ({ match }) => {
  const [quiz, setQuiz] = useState(null);
  const [questions, setQuestions] = useState([]);

  useEffect(() => {
    fetchQuiz();
  }, []);

  const fetchQuiz = async () => {
    try {
      const response = await apiService.get(`/quiz/${match.params.id}`);
      // For now, we're assuming that the "response.data.questions" array has the same format as our hardcoded data.
      const apiQuestions = response.data.questions.map((question) => ({
        ...question,
        answers: ["Option 1", "Option 2", "Option 3", "Option 4"], // Hardcoded options
      }));
      setQuiz(response.data);
      setQuestions(apiQuestions);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>{quiz ? quiz.title : "Loading..."}</h2>
      {questions.map((question) => (
        <div key={question.id}>
          <p>{question.content}</p>
          {question.answers.map((answer, index) => (
            <div key={index}>
              <input
                type="radio"
                id={`question-${question.id}-option-${index}`}
                name={`question-${question.id}`}
                value={answer}
              />
              <label htmlFor={`question-${question.id}-option-${index}`}>
                {answer}
              </label>
            </div>
          ))}
        </div>
      ))}
    </div>
  );
};

export default Quiz;
