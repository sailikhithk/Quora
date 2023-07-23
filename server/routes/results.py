import logging
from flask import Blueprint, request, jsonify
from services.result_service import ResultService
from models.result_model import Result
from app import db


result = Blueprint("result", __name__)
logger = logging.getLogger('auth')


result_service_obj = ResultService()

result.route("/<int:id>", methods=["GET"])
def get_result(id):
    result = db.session.query(Result).filter_by(id=id).first()
    if not result:
        return jsonify({"error": "Result not found"}), 404

    return jsonify(result)

result.route("/", methods=["POST"])
def create_result():
    data = request.get_json()
    score = data["score"]
    quiz_id = data["quiz_id"]

    new_result = Result(score=score, quiz_id=quiz_id, user_id=user_id)
    db.session.add(new_result)
    db.session.commit()
    return new_result
        
    
    return jsonify(result)
