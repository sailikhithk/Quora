import traceback
from flask_jwt_extended import create_access_token

from models.user_model import User
from models.role_model import Role
from utils import encrypt, decrypt
from database import session


class UserService:
    def __init__(self):
        pass

    def get_all_users(self):
        return self.user_repository.get_all_users()

    def get_user_by_id(self, user_id):
        return self.user_repository.get_user_by_id(user_id)

    def get_user_by_username(self, username):
        return session.query(User).filter(User.username == username).first()

    def create_user(self, username, password, email, institution, role_id):
        hashed_password = encrypt(password)
        new_user = User(
            username=username,
            password_hash=hashed_password,
            email=email,
            institution=institution,
            role_id=role_id,
        )
        session.add(new_user)
        session.commit()
        return new_user

    # def update_user(self, user_id, username, email, password, role, institution):
    #     hashed_password = self.bcrypt.generate_password_hash(password).decode("utf-8")
    #     return self.user_repository.update_user(
    #         user_id, username, email, hashed_password, role, institution
    #     )

    # def delete_user(self, user_id):
    #     return self.user_repository.delete_user(user_id)

    def login_user(self, data):
        user_name = data["username"]
        password = data["password"]
        user = self.get_user_by_username(user_name)
        if not user:
            return {"error": "Invalid username or password"}

        hashpwd = user.password_hash
        db_password = decrypt(hashpwd)

        if db_password == password:
            user_data = {
                "user_name": user.username,
                "email": user.email,
                "institution": user.institution,
                "role_id": user.role_id,
                "user_id": user.id,
            }
            access_token = create_access_token(identity=user_data)
            return {"access_token": access_token}
        else:
            print("db_password", db_password)
            print("password", password)
            return {"error": "Invalid username or password"}

    def register_user(self, data):
        try:
            username = data["username"]
            password = data["password"]
            email = data["email"]
            institution = data["institution"]
            role_name = data["role"]

            role = session.query(Role).filter_by(name=role_name).first()
            if role is None:
                return {"error": f"Role '{role_name}' not found."}

            role_id = role.id
            user = self.create_user(username, password, email, institution, role_id)
            if user:
                return {"message": f"User created plese login from login page"}
            else:
                return {"message": f"User not created"}
        except Exception as e:
            traceback.print_exc()
