# answer_controller.py
from flask import Blueprint, request, jsonify
from services.answer_service import AnswerService
from repositories.answer_repository import AnswerRepository
from flask_cors import CORS


class AnswerController:
    def __init__(self, app):
        self.app = app
        self.answer = Blueprint("answer", __name__)
        CORS(self.answer)
        self.setup_routes()

    def setup_routes(self):
        @self.answer.route("/<int:id>", methods=["GET"])
        def get_answer(id):
            answer_repository = AnswerRepository(self.app.db)
            answer_service = AnswerService(answer_repository)
            answer = answer_service.get_answer_by_id(id)
            if not answer:
                return jsonify({"error": "Answer not found"}), 404

            return jsonify(answer)

        @self.answer.route("/", methods=["POST"])
        def create_answer():
            data = request.get_json()
            content = data["content"]
            is_correct = data["is_correct"]
            question_id = data["question_id"]
            user_id = data["user_id"]
            answer_repository = AnswerRepository(self.app.db)
            answer_service = AnswerService(answer_repository)
            answer = answer_service.create_answer(
                content, is_correct, question_id, user_id
            )
            return jsonify(answer)
