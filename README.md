# Quora

Quiz App

# Quora Quiz Project

This project is a simple quiz application. The backend is built with Flask, and the frontend is built with React.

## Project Structure

Here is a brief explanation of the project structure:

<pre grepper_trigger_added="1"><div class="bg-black rounded-md mb-4"><div class="flex items-center relative text-gray-200 bg-gray-800 px-4 py-2 text-xs font-sans justify-between rounded-t-md"><span>yaml</span><button class="flex ml-auto gap-2"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="h-4 w-4" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"></path><rect x="8" y="2" width="8" height="4" rx="1" ry="1"></rect></svg>Copy code</button></div><div class="p-4 overflow-y-auto"><code class="!whitespace-pre hljs language-yaml">.
├── LICENSE: The license for this project.
├── README.md: This file, containing information about this project.
├── build: Contains files related to building the application.
├── dist: Contains distribution files.
├── features.txt: A file listing the features of this application.
├── frontend: Contains all frontend-related files, written in React.
│   ├── public: Static files for the frontend.
│   ├── src: Source files for the frontend.
│   │   ├── components: React components for the application.
│   │   ├── services: Services to interact with the backend.
│   │   └── assets: Static assets like images.
├── quora.egg-info: Metadata about this Python package.
├── server: Contains all backend-related files, written in Flask.
│   ├── models: Database models for SQLAlchemy.
│   ├── routes: Routes for the Flask application.
│   ├── services: Services to interact with the database and perform business logic.
│   ├── database.py: Configuration for the SQLAlchemy database.
│   ├── app.py: The main entry point for the Flask application.
│   ├── create_db.py: Script to create and seed the database.
│   ├── utils.py: Utility functions for the backend.
│   └── requirements.txt: Python dependencies for the backend.
└── setup.py: Python package setup file.
</code></div></div><div class="open_grepper_editor gpt_grepper_add_answer_trigger" title="Edit & Save To Grepper">Save to grepper</div></pre>

## Frontend

The frontend of this application is built with React. It contains several pages and components, including pages for taking a quiz, viewing results, and a user dashboard. The frontend communicates with the backend through an API.

## Backend

The backend of this application is built with Flask, a Python web framework. It uses SQLAlchemy to interact with a SQLite database. The backend provides a RESTful API for the frontend to interact with.

## Database

The database consists of several tables, including `User`, `Role`, `Quiz`, `Question`, and `Result`. These tables store information about users, their roles, quizzes, questions in quizzes, and users' results, respectively.

## Running the Project

To run this project locally, you'll need to have Python and Node.js installed. Then, you can install the necessary dependencies with `pip` and `npm`, respectively.

For the backend, you can start the server by running `python app.py` from the `server` directory.

For the frontend, you can start the React development server by running `npm start` from the `frontend` directory.

## License

This project is licensed under the MIT License.
