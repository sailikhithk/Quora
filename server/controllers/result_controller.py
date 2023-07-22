# result_controller.py
from flask import Blueprint, request, jsonify
from services.result_service import ResultService
from repositories.result_repository import ResultRepository
from flask_cors import CORS
from db import db  # <- Add this line


class ResultController:
    def __init__(self, app):
        self.result_service = ResultService(ResultRepository(db))
        self.result = Blueprint("result", __name__)
        CORS(self.result)

        @self.result.route("/<int:id>", methods=["GET"])
        def get_result(id):
            result = self.result_service.get_result_by_id(id)
            if not result:
                return jsonify({"error": "Result not found"}), 404

            return jsonify(result)

        @self.result.route("/", methods=["POST"])
        def create_result():
            data = request.get_json()
            score = data["score"]
            quiz_id = data["quiz_id"]

            result = self.result_service.create_result(score, quiz_id)
            return jsonify(result)
