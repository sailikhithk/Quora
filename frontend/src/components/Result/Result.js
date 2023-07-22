import React, { useEffect, useState } from "react";
import apiService from "../services/apiService";

const Result = ({ match }) => {
  const [result, setResult] = useState({});

  useEffect(() => {
    fetchResult();
  }, []);

  const fetchResult = async () => {
    try {
      const response = await apiService.get(`/result/${match.params.id}`);
      setResult(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Result</h2>
      <p>Score: {result.score}</p>
    </div>
  );
};

export default Result;
