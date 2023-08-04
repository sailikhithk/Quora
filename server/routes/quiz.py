import logging
import traceback
import pandas

from flask import Blueprint, request, jsonify, send_file
from flask_jwt_extended import jwt_required, get_jwt_identity
from jsonschema import validate

from services import QuestionService, QuizService
from validation import UPLOAD_QUIZ_SCHEMA


quiz = Blueprint("quiz", __name__)
logger = logging.getLogger("auth")


question_service_obj = QuestionService()
quiz_service_obj = QuizService()


# @quiz.route("/<int:user_id>/list", methods=["GET"])
# def get_all_quizzes(user_id):
#     try:
#         quizzes = quiz_service_obj.get_all_quizzes(user_id)
#         return jsonify(quizzes), 200
#     except Exception as e:
#         traceback.print_exc()
#         return jsonify({"error": str(e)}), 500


@quiz.route("/<int:user_id>/list", methods=["GET"])
def get_all_quizzes(user_id):
    try:
        quizzes = quiz_service_obj.get_all_quizzes(user_id)
        return jsonify(quizzes), 200
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@quiz.route("/upsert_quiz", methods=["POST"])
# @jwt_required()
def upload_quiz():
    try:
        if "file" in request.files:
            # uploading quiz via file
            file = request.files["file"]
            if file.filename == "":
                return jsonify({"error": "No selected file"}), 500        
            user_id = request.form.get('user_id')
            quiz_id = request.form.get("quiz_id", None)            
            response = quiz_service_obj.upsert_quiz_file(file, user_id, quiz_id)    
        else:
            data = request.get_json()
            validate(data, UPLOAD_QUIZ_SCHEMA)
            # identity = get_jwt_identity()
            # user_id = identity["user_id"]
            response = quiz_service_obj.upload_quiz_json(data)
        return jsonify(response)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@quiz.route("/<int:quiz_id>/download_quiz", methods=["GET"])
def download_quiz(quiz_id):
    try:
        quiz_service_obj.download_quiz(quiz_id)
        return send_file("output.xlsx", as_attachment=True)
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

@quiz.route("/<int:quiz_id>/delete_quiz", methods=["GET"])
def delete_quiz(quiz_id):
    try:
        response = quiz_service_obj.delete_quiz(quiz_id)
        return jsonify(response)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
