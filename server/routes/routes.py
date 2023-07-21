# routes.py
from flask import Flask
from flask_cors import CORS
import os

from controllers.user_controller import user
from controllers.quiz_controller import QuizController
from controllers.question_controller import QuestionController
from controllers.result_controller import ResultController
from controllers.answer_controller import AnswerController  # Add this line
from flask_bcrypt import Bcrypt
from services.result_service import ResultService
from repositories.result_repository import ResultRepository
from db import db


def create_app():
    app = Flask(__name__)

    # Apply CORS to app
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Configuring the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app.db"
    )
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    #     os.path.abspath(os.path.dirname(__file__)), "app.db"
    # )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config[
        "SECRET_KEY"
    ] = "sailikhithk"  # Replace this with a real secret in production!

    db.init_app(app)

    # Initialize the Controllers
    quiz_controller = QuizController(app)
    question_controller = QuestionController(app)
    answer_controller = AnswerController(app)

    # Initialize the Services
    result_repository = ResultRepository(db)
    result_service = ResultService(result_repository)

    # Initialize the ResultController
    result_controller = ResultController(app, result_service)

    # Registering the blueprints
    app.register_blueprint(user, url_prefix="/api/user")
    app.register_blueprint(quiz_controller.quiz, url_prefix="/api/quiz")
    app.register_blueprint(question_controller.question, url_prefix="/api/question")
    app.register_blueprint(answer_controller.answer, url_prefix="/api/answer")
    app.register_blueprint(result_controller.result, url_prefix="/api/result")

    return app, db