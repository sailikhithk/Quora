import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './css/index.css'; // or './index.css' if you move it to the 'src' directory

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
