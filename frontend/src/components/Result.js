import React, { useEffect, useState, useCallback } from "react"; // Add useCallback
import apiService from "../services/apiService";

const Result = ({ match }) => {
  const [result, setResult] = useState(null);

  // Added useCallback
  const fetchResult = useCallback(async () => {
    try {
      const response = await apiService.get(`/result/${match.params.id}`);
      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
  }, [match.params.id]); // Dependency array for useCallback

  useEffect(() => {
    fetchResult();
  }, [fetchResult]); // Updated dependency array

  return (
    <div>
      <h2>Result</h2>
      {result ? (
        <div>
          <h3>Your score: {result.score}</h3>
          <p>Total questions: {result.totalQuestions}</p>
        </div>
      ) : (
        "Loading..."
      )}
    </div>
  );
};

export default Result;
