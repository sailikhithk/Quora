# Quora

### Table of Contents

1. [Introduction](#introduction)
2. [Backend Implementation](#backend-implementation)
   1. [Authentication and User Management](#authentication-and-user-management)
   2. [Quiz Management](#quiz-management)
   3. [Database Models](#database-models)
3. [Frontend Implementation](#frontend-implementation)
   1. [Dashboard](#dashboard)
   2. [User Authentication](#user-authentication)
4. [Local Environment Setup](#local-environment-setup)
5. [Deployment and Hosting](#deployment-and-hosting)
6. [Conclusion](#conclusion)

### Introduction

The Quiz Platform is a web application that allows students to take quizzes, teachers to manage quizzes, and admins to oversee the entire system. It consists of a React frontend and a Flask backend.

### Backend Implementation

#### Authentication and User Management

The backend server provides endpoints for user registration, login, password reset, and admin user creation.

1. **Login**:

   - **Endpoint**: `/login`
   - **Method**: `POST`
   - **Parameters**: `username`, `password`
   - **Description**: Authenticates the user and returns an access token.

2. **Register**:

   - **Endpoint**: `/register`
   - **Method**: `POST`
   - **Parameters**: `username`, `password`, `email`, etc.
   - **Description**: Registers a new user.

3. **Create User (Admin)**:

   - **Endpoint**: `/create_user`
   - **Method**: `POST`
   - **Parameters**: `username`, `password`, `role`, etc.
   - **Description**: Admin endpoint to create a new user (e.g., teacher).

4. **Reset Password**:

   - **Endpoint**: `/reset_password`
   - **Method**: `POST`
   - **Parameters**: `email`
   - **Description**: Initiates a password reset process for a user.

#### Quiz Management

The backend server provides various endpoints related to quizzes, including listing quizzes, uploading quizzes, downloading quizzes, getting specific quiz details, and deleting quizzes.

1. **List All Quizzes**:

   - **Endpoint**: `/<int:user_id>/list`
   - **Method**: `GET`
   - **Description**: Returns a list of all quizzes for a specific user.

2. **Upload Quiz**:

   - **Endpoint**: `/upsert_quiz`
   - **Method**: `POST`
   - **Parameters**: `file` (optional), `user_id`, `quiz_id` (optional)
   - **Description**: Allows uploading a quiz via a file or JSON data.

3. **Download Quiz**:

   - **Endpoint**: `/<int:quiz_id>/download_quiz`
   - **Method**: `GET`
   - **Description**: Downloads the quiz as an Excel file.

4. **Get Quiz**:

   - **Endpoint**: `/<int:quiz_id>/questions`
   - **Method**: `GET`
   - **Description**: Retrieves details of a specific quiz.

5. **Delete Quiz**:

   - **Endpoint**: `/<int:quiz_id>/delete_quiz`
   - **Method**: `GET`
   - **Description**: Deletes a specific quiz.

#### Database Models

The backend includes several database models such as `Question`, `Quiz`, `Result`, `Role`, `User`, and `UserQuizMapping`. Could you please provide the code for these models to help us document them in detail?

### Frontend Implementation

#### Dashboard

The Dashboard component in React serves as the main view for students to see available quizzes. It fetches quizzes from the backend and displays them in styled cards.

Key Features:

- **Logout Button**: Allows users to log out of their accounts.
- **Quiz Cards**: Display quizzes with title, category, and progress bar.
- **Error Handling**: Shows an error message if an error occurs while fetching quizzes.

#### User Authentication

The frontend includes components for user authentication, including `Login.js`, `Register.js`, and `ResetPassword.js`.

### Local Environment Setup

To set up the application locally, please follow these steps:

1. **Backend Setup**:

   - Clone the repository.
   - Navigate to the server directory.
   - Install dependencies with `pip install -r requirements.txt`.
   - Start the server with `python app.py`.

2. **Frontend Setup**:

   - Navigate to the frontend directory.
   - Install dependencies with `npm install`.
   - Start the server with `npm start`.

The application should now be accessible at `http://localhost:3000`.

### Deployment and Hosting

The application can be hosted on public hosting platforms like Digital Ocean. Detailed deployment scripts and configurations would be needed to document this section further.

### Conclusion

The Quiz Platform offers a comprehensive solution for online quiz management, catering to students, teachers, and administrators. The technical architecture encompasses a robust backend API built with Flask and a dynamic frontend built with React.

Please provide additional code snippets or files related to database models, deployment configurations, or any other specific areas you'd like us to cover in the technical documentation.
