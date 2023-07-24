import logging
from flask import Blueprint, request, jsonify
from services.answer_service import AnswerService
from flask_jwt_extended import (jwt_required, get_jwt_identity)


answer = Blueprint("answer", __name__)
logger = logging.getLogger('answer')


answer_service_obj = AnswerService()


@answer.route("/<int:id>/get_answer>", methods=["GET"])
@jwt_required()
def get_answer(id):
    answer = answer_service_obj.get_answer_by_id(id)
    if not answer:
        return jsonify({"error": "Answer not found"}), 404

    return jsonify(answer)

@answer.route("/create_answer", methods=["POST"])
@jwt_required()
def create_answer():
    data = request.get_json()
    content = data["content"]
    is_correct = data["is_correct"]
    question_id = data["question_id"]
    identity = get_jwt_identity()
    user_id = identity['user_id']    
    answer = answer_service_obj.create_answer(
        content, is_correct, question_id, user_id
    )
    return jsonify(answer)
