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

@quiz.route("/upload_quiz", methods=["POST"])
@jwt_required()
def upload_quiz():
    data = request.get_json()
    identity = get_jwt_identity()
    user_id = identity['user_id']    
    quiz_name = data["quiz_name"]
    questions = data['questions']
    pass_marks = data['pass_marks']
    next_quiz_to_unlock = data['next_quiz_to_unlock']
    response = quiz_service_obj.upload_quiz(user_id, quiz_name, questions, pass_marks, next_quiz_to_unlock)
    return jsonify(response)


@quiz.route("/<int:quiz_id>/questions", methods=["GET"])
def get_quiz(quiz_id):
    response = quiz_service_obj.get_quiz(quiz_id)
    return jsonify(response)
