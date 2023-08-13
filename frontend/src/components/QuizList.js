import React, { useEffect, useState } from "react";
import apiService from "../services/apiService";
import { Link } from "react-router-dom"; // Import Link from react-router-dom

const QuizList = () => {
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
      <h2>Quizzes</h2>
      {quizzes.map((quiz) => (
        <div key={quiz.id}>
          <h3>{quiz.title}</h3>
          <Link to={`/quiz/${quiz.id}`}>Start Quiz</Link>{" "}
          {/* Link to start the quiz */}
        </div>
      ))}
    </div>
  );
};

export default QuizList;
