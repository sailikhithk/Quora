import logging

from flask import Blueprint, request, jsonify
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from services.question_service import QuestionService
from services.quiz_service import QuizService


quiz = Blueprint("quiz", __name__)
logger = logging.getLogger('auth')


question_service_obj = QuestionService()
quiz_service_obj = QuizService()

@quiz.route("/list", methods=["GET"])
def get_all_quizzes():
    quizzes = quiz_service_obj.get_all_quizzes()
    return jsonify(quizzes), 200

@quiz.route("/create_quiz", methods=["POST"])
@jwt_required()
def create_quiz():
    data = request.get_json()
    identity = get_jwt_identity()
    user_id = identity['user_id']    
    title = data["title"]
    response = quiz_service_obj.create_quiz(title, user_id)
    return jsonify(response)

@quiz.route("/<int:quiz_id>/create_questions", methods=["POST"])
def add_question_to_quiz(quiz_id):
    data = request.get_json()
    content = data["content"]
    response = question_service_obj.create_question(content, quiz_id)
    return jsonify(response)
