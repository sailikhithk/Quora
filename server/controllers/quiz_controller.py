# quiz_controller.py
from flask import Blueprint, request, jsonify
from services.quiz_service import QuizService
from services.question_service import QuestionService, QuestionRepository
from repositories.quiz_repository import QuizRepository
from flask_cors import CORS
from models import Quiz

from db import db  # <- Add this line


class QuizController:
    def __init__(self, app):
        self.quiz_service = QuizService(QuizRepository(db))
        self.question_service = QuestionService()  # Updated this QuestionService
        self.quiz = Blueprint("quiz", __name__)

        @self.quiz.route("/", methods=["GET"])
        def get_all_quizzes():
            app.logger.info("Getting all quizzes")  # Logging here
            quizzes = self.quiz_service.get_all_quizzes()
            app.logger.info("Received quizzes from service")  # Logging here
            return jsonify([quiz.serialize() for quiz in quizzes]), 200

        @self.quiz.route("/", methods=["POST"])
        def create_quiz():
            data = request.get_json()
            title = data["title"]
            user_id = data["user_id"]  # Assume this is passed from the frontend

            quiz = self.quiz_service.create_quiz(title, user_id)
            return jsonify(quiz)

        @self.quiz.route("/<int:quiz_id>/questions", methods=["POST"])
        def add_question_to_quiz(quiz_id):
            data = request.get_json()
            content = data["content"]

            question = self.question_service.create_question(content, quiz_id)
            return jsonify(question)
