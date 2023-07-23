from flask import Blueprint, request, jsonify, current_app, make_response
from flask_bcrypt import Bcrypt
from models.role_model import Role
from services.user_service import UserService

user = Blueprint("user", __name__)


@user.route("/login", methods=["POST"])
def login():
    bcrypt = Bcrypt(current_app)
    user_service = UserService(current_app, bcrypt)
    try:
        data = request.get_json()
        user = user_service.get_user_by_username(data["username"])

        if not user or not user_service.check_password(user, data["password"]):
            return jsonify({"error": "Invalid username or password"}), 400

        response = make_response(
            jsonify({"token": user_service.generate_auth_token(user)})
        )
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@user.route("/register", methods=["POST", "OPTIONS"])
def register():
    if request.method == "OPTIONS":  # Responding to 'preflight' CORS calls.
        return make_response()
    bcrypt = Bcrypt(current_app)
    user_service = UserService(current_app, bcrypt)
    try:
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        email = data["email"]
        institution = data["institution"]
        role_name = data["role"]

        role = Role.query.filter_by(name=role_name).first()

        if role is None:
            return jsonify({"error": f"Role '{role_name}' not found."}), 400

        user = user_service.create_user(username, password, email, institution, role.id)
        response = make_response(
            jsonify({"token": user_service.generate_auth_token(user)})
        )
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500
