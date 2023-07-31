import logging
import traceback

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from jsonschema import validate

from services import QuestionService, QuizService
from validation import UPLOAD_QUIZ_SCHEMA


quiz = Blueprint("quiz", __name__)
logger = logging.getLogger("auth")


question_service_obj = QuestionService()
quiz_service_obj = QuizService()


@quiz.route("/list", methods=["GET"])
def get_all_quizzes():
    try:
        quizzes = quiz_service_obj.get_all_quizzes()
        return jsonify(quizzes), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@quiz.route("/<int:user_id>/list", methods=["GET"])
def get_all_quizzes(user_id):
    try:
        quizzes = quiz_service_obj.get_all_quizzes(user_id)
        return jsonify(quizzes), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@quiz.route("/upload_quiz", methods=["POST"])
# @jwt_required()
def upload_quiz():
    try:
        data = request.get_json()
        validate(data, UPLOAD_QUIZ_SCHEMA)
        # identity = get_jwt_identity()
        # user_id = identity["user_id"]
        user_id = data["user_id"]
        quiz_name = data["quiz_name"]
        questions = data["questions"]
        pass_marks = data["pass_marks"]
        next_quiz_to_unlock = data["next_quiz_to_unlock"]
        response = quiz_service_obj.upload_quiz(
            user_id, quiz_name, questions, pass_marks, next_quiz_to_unlock
        )
        return jsonify(response)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@quiz.route("/<int:quiz_id>/questions", methods=["GET"])
def get_quiz(quiz_id):
    try:
        response = quiz_service_obj.get_quiz(quiz_id)
        return jsonify(response)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
