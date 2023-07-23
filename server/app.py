import os
import logging

from flask import Flask
from flask_cors import CORS

# Registering the blueprints after initializing the db and app
from routes.user import user as user_router
from routes.quiz import quiz as quiz_router
from routes.question import question as question_router
# from routes.answer import answer as answer_router
# from routes.results import result as result_router

from database import Session
from models.answer_model import Answer
from models.question_model import Question
from models.quiz_attempt_model import QuizAttempt
from models.quiz_model import Quiz
from models.result_model import Result
from models.role_model import Role
from models.user_model import User

app = Flask(__name__)


# Apply CORS to app
CORS(app)


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Registering the blueprints
app.register_blueprint(user_router)
app.register_blueprint(quiz_router)
app.register_blueprint(question_router)
# app.register_blueprint(answer_router)
# app.register_blueprint(result_router)


# Create the database tables
from database import Base, engine
Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(debug=True)