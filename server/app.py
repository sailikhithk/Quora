# main.py
import os
import logging

from flask import Flask
from flask_cors import CORS
from datetime import timedelta


# Registering the blueprints after initializing the app
from routes.user import user as user_router
from routes.quiz import quiz as quiz_router
from routes.question import question as question_router
from routes.answer import answer as answer_router
from routes.result import result as result_router

from flask_jwt_extended import JWTManager

from database import Base, engine

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'your-secret-key'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=30)
jwt = JWTManager(app)

# Apply CORS to app
CORS(app)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Registering the blueprints
app.register_blueprint(user_router, url_prefix='/auth')
app.register_blueprint(quiz_router, url_prefix='/quiz')
app.register_blueprint(question_router, url_prefix='/question')
app.register_blueprint(answer_router, url_prefix='/answer')
app.register_blueprint(result_router, url_prefix='/result')


if __name__ == "__main__":
    from models.answer_model import Answer
    from models.question_model import Question
    from models.quiz_attempt_model import QuizAttempt
    from models.quiz_model import Quiz
    from models.result_model import Result
    from models.role_model import Role
    from models.user_model import User

    Base.metadata.create_all(engine)

    from create_db import create_dummy_roles
    create_dummy_roles()
    
    app.run(debug=True)
