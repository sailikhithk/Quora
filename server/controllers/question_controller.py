# question_controller.py
from flask import Blueprint, request, jsonify
from services.question_service import QuestionService
from flask_cors import CORS


class QuestionController:
    def __init__(self, app):
        self.app = app
        self.question = Blueprint("question", __name__)
        CORS(self.question)
        self.question_service = QuestionService()
        self.setup_routes()

    def setup_routes(self):
        @self.question.route("/<int:id>", methods=["GET"])
        def get_question(id):
            question = self.question_service.get_question_by_id(id)
            if not question:
                return jsonify({"error": "Question not found"}), 404

            return jsonify(question)

        @self.question.route("/", methods=["POST"])
        def create_question():
            data = request.get_json()
            content = data["content"]
            quiz_id = data["quiz_id"]
            question = self.question_service.create_question(content, quiz_id)
            return jsonify(question)
