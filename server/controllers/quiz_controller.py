# quiz_controller.py
from flask import Blueprint, request, jsonify
from services.quiz_service import QuizService
from repositories.quiz_repository import QuizRepository
from flask_cors import CORS
from db import db  # <- Add this line


class QuizController:
    def __init__(self, app):
        self.quiz_service = QuizService(QuizRepository(db))
        self.quiz = Blueprint("quiz", __name__)
        CORS(self.quiz)

        @self.quiz.route("/<int:id>", methods=["GET"])
        def get_quiz(id):
            quiz = self.quiz_service.get_quiz_by_id(id)
            if not quiz:
                return jsonify({"error": "Quiz not found"}), 404

            return jsonify(quiz)

        @self.quiz.route("/", methods=["POST"])
        def create_quiz():
            data = request.get_json()
            title = data["title"]

            quiz = self.quiz_service.create_quiz(title)
            return jsonify(quiz)
