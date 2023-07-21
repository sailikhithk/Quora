import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { BrowserRouter as Router } from "react-router-dom";
import App from "./App";

test("renders Login and Register", () => {
  render(
    <Router>
      <App />
    </Router>
  );

  // Navigate to Login and Register components
  userEvent.click(screen.getByText(/Login/i));
  expect(screen.getByText("Login")).toBeInTheDocument();

  userEvent.click(screen.getByText(/Register/i));
  expect(screen.getByText("Register")).toBeInTheDocument();
});
