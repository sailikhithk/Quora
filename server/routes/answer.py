import logging
from flask import Blueprint, request, jsonify
from services.answer_service import AnswerService

answer = Blueprint("answer", __name__)
logger = logging.getLogger('answer')


answer_service_obj = AnswerService()


@answer.route("/<int:id>", methods=["GET"])
def get_answer(id):
    answer = answer_service_obj.get_answer_by_id(id)
    if not answer:
        return jsonify({"error": "Answer not found"}), 404

    return jsonify(answer)

@answer.route("/", methods=["POST"])
def create_answer():
    data = request.get_json()
    content = data["content"]
    is_correct = data["is_correct"]
    question_id = data["question_id"]
    user_id = data["user_id"]
    answer = answer_service_obj.create_answer(
        content, is_correct, question_id, user_id
    )
    return jsonify(answer)
