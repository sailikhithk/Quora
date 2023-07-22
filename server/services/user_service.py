from werkzeug.security import generate_password_hash, check_password_hash
from repositories.user_repository import UserRepository
from models.user_model import User
from db import db
import jwt
import datetime


class UserService:
    def __init__(self, app, bcrypt):
        self.app = app
        self.bcrypt = bcrypt
        self.user_repository = UserRepository()

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_user_by_username(self, username):
        return self.user_repository.get_by_username(username)

    def check_password(self, user, password):
        return self.bcrypt.check_password_hash(user.password_hash, password)

    def create_user(self, username, password, email, institution, role_id):
        hashed_password = self.bcrypt.generate_password_hash(password).decode(
            "utf-8"
        )  # decode to string before saving
        new_user = User(
            username=username,
            password_hash=hashed_password,
            email=email,
            institution=institution,
            role_id=role_id,
        )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def update_user(self, user_id, username, email, password, role, institution):
        hashed_password = self.bcrypt.generate_password_hash(password).decode("utf-8")
        return self.user_repository.update_user(
            user_id, username, email, hashed_password, role, institution
        )

    def delete_user(self, user_id):
        return self.user_repository.delete_user(user_id)

    def generate_auth_token(self, user):
        payload = {
            "sub": user.username,
            "iat": datetime.datetime.utcnow(),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
        }
        token = jwt.encode(payload, self.app.config["SECRET_KEY"], algorithm="HS256")
        return token
