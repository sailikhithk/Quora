import logging
import traceback

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from jsonschema import validate

from services import ResultService
from validation import SUBMIT_ANSWER_SCHEMA
result = Blueprint("result", __name__)
logger = logging.getLogger("auth")


result_service_obj = ResultService()


@result.route("/<int:id>/get_result", methods=["GET"])
def get_result(id):
    try:
        response = result_service_obj.get_result_by_id(id)
        if not response:
            return jsonify({"error": "Result not found"}), 404
        return jsonify(response)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@result.route("/submit_answer", methods=["POST"])
def submit_answer():
    try:
        data = request.get_json()
        validate(data, SUBMIT_ANSWER_SCHEMA)
        content = data["content"]
        # identity = get_jwt_identity()
        # user_id = identity["user_id"]
        user_id = data["user_id"]
        quiz_id = data["quiz_id"]
        answer = result_service_obj.submit_answer(content, user_id, quiz_id)
        return jsonify(answer)
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500
