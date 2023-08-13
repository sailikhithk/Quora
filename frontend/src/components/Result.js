import React, { useEffect, useState, useCallback } from "react";
import apiService from "../services/apiService";
import { useParams } from "react-router-dom"; // Import useParams

const Result = () => {
  const [result, setResult] = useState(null);
  const { id } = useParams(); // Use useParams to get the id

  // Added useCallback
  const fetchResult = useCallback(async () => {
    try {
      // Update the URL to match the correct endpoint
      const response = await apiService.get(`/result/${id}/get_result`);
      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
  }, [id]); // Dependency array for useCallback

  useEffect(() => {
    fetchResult();
  }, [fetchResult]); // Updated dependency array

  return (
    <div>
      <h2>Result</h2>
      {result ? (
        <div>
          <h3>Your score: {result.score}</h3>
          {/* Display additional result details here */}
          {result.answers.map((answer, index) => (
            <div key={index}>
              <p>Question ID: {answer.question_id}</p>
              <p>Correct Options: {answer.correct_options.join(", ")}</p>
              <p>Your Selection: {answer.selected_options.join(", ")}</p>
              <p>Is Correct: {answer.is_correct ? "Yes" : "No"}</p>
              <p>Score Allocated: {answer.score_allocated}</p>
            </div>
          ))}
        </div>
      ) : (
        "Loading..."
      )}
    </div>
  );
};

export default Result;
