import React, { useEffect, useState } from "react";
import apiService from "../services/apiService";

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
          {/* Here you can add a button/link to start the quiz */}
        </div>
      ))}
    </div>
  );
};

export default QuizList;
