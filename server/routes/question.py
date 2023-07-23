import logging


from flask import Blueprint, request, jsonify
from services.question_service import QuestionService

question = Blueprint("question", __name__)
logger = logging.getLogger('question')

question_service_obj = QuestionService()

question.route("/<int:id>", methods=["GET"])
def get_question(id):
    question = question_service_obj.get_question_by_id(id)
    if not question:
        return jsonify({"error": "Question not found"}), 404

    return jsonify(question)

question.route("/", methods=["POST"])
def create_question():
    data = request.get_json()
    content = data["content"]
    quiz_id = data["quiz_id"]
    question = question_service_obj.create_question(content, quiz_id)
    return jsonify(question)
