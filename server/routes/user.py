import logging
import traceback

from flask import Blueprint, request, jsonify
from services.user_service import UserService

user = Blueprint("user", __name__)
logger = logging.getLogger('auth')
# logger.info('Login page accessed')

user_service_obj = UserService()

@user.route("/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        response = user_service_obj.login_user(data)
        return jsonify(response)
    
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

@user.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
        response = user_service_obj.register_user(data)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500