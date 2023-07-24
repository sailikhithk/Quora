import logging
from flask import Blueprint, request, jsonify
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from services.result_service import ResultService
result = Blueprint("result", __name__)
logger = logging.getLogger('auth')


result_service_obj = ResultService()

@result.route("/<int:id>/get_result", methods=["GET"])
def get_result(id):
    response = result_service_obj.get_result_by_id(id)
    if not response:
        return jsonify({"error": "Result not found"}), 404
    return jsonify(response)

@result.route("/submit_answer", methods=["POST"])
@jwt_required()
def submit_answer():
    data = request.get_json()
    content = data["content"]
    identity = get_jwt_identity()
    user_id = identity['user_id']    
    quiz_id = data['quiz_id']
    answer = result_service_obj.submit_answer(
        content, user_id, quiz_id
    )
    return jsonify(answer)
