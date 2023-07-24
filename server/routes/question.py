import logging


from flask import Blueprint, request, jsonify
from services.question_service import QuestionService
from flask_jwt_extended import (jwt_required, get_jwt_identity)

question = Blueprint("question", __name__)
logger = logging.getLogger('question')

question_service_obj = QuestionService()

@question.route("/<int:id>/get_question", methods=["GET"])
def get_question(id):
    question = question_service_obj.get_question_by_id(id)
    if not question:
        return jsonify({"error": "Question not found"}), 404

    return jsonify(question)
