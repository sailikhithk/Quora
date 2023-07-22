import React from "react";

const Answer = ({ answer }) => {
  return (
    <div>
      <input type="radio" id={answer.id} name="answer" value={answer.id} />
      <label htmlFor={answer.id}>{answer.content}</label>
    </div>
  );
};

export default Answer;
