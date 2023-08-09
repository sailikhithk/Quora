import React from "react";

const Question = ({ question }) => {
  return (
    <div>
      <p>{question.content}</p>
      {question.answers.map((answer) => (
        <div key={answer.id}>
          <input
            type="radio"
            id={answer.id}
            name={question.id}
            value={answer.id}
          />
          <label for={answer.id}>{answer.content}</label>
        </div>
      ))}
    </div>
  );
};

export default Question;
