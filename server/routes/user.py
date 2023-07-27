import logging
import traceback

from flask import Blueprint, request, jsonify, make_response
from services.user_service import UserService

user = Blueprint("user", __name__)
logger = logging.getLogger("user")
# logger.info('Login page accessed')

user_service_obj = UserService()


@user.route("/login", methods=["POST"])
def login():
    # if request.method == "OPTIONS":  # Respond to the preflight request
    #     return _build_cors_preflight_response()
    # else:
    try:
        print("request========", request)
        print("request========", type(request))
        data = request.get_json()
        print("data========", data)
        response = user_service_obj.login_user(data)
        print("response=========", response)
        return jsonify(response)

    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500


@user.route("/register", methods=["POST"])
def register():
    try:
        data = request.get_json()
        response = user_service_obj.register_user(data)
        print("request========", request)
        print("request========", type(request))
        print("register response========", response)
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
