import logging
from flask import Blueprint, request, jsonify
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from services.result_service import ResultService
from models.result_model import Result


result = Blueprint("result", __name__)
logger = logging.getLogger('auth')


result_service_obj = ResultService()

@result.route("/<int:id>/get_result", methods=["GET"])
def get_result(id):
    response = result_service_obj.get_result_by_id(id)
    if not response:
        return jsonify({"error": "Result not found"}), 404
    return jsonify(response)

@result.route("/create_result", methods=["POST"])
@jwt_required()
def create_result():
    data = request.get_json()
    score = data["score"]
    quiz_id = data["quiz_id"]
    identity = get_jwt_identity()
    user_id = identity['user_id']
    response = result_service_obj.create_result(score, quiz_id, user_id)
    return jsonify(response)