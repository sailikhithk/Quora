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
        return session.query(User).filter_by(id=user_id).first()

    def get_user_by_username(self, username):
        return session.query(User).filter_by(username = username).first()

    def get_user_by_email(self, email):
        return session.query(User).filter_by(email = email).first()

    def create_user(self, username, password, email, institution, role_id):
        try:
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
        except Exception as e:
            session.rollback()
            traceback.print_exc()
            return {"message": str(e), "status": False}
    
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
            
            existing_user = self.get_user_by_email(email)
            if existing_user:
                return {"message": "User with same email exist", "status": False}
            
            
            user = self.create_user(username, password, email, institution, role_id)
            if user:
                return {"message": "User created plese re-login from login page", "status": True}
            else:
                return {"message": "User not created", "status": False}
        except Exception as e:
            session.rollback()
            traceback.print_exc()
            return {"message": str(e), "status": False}

    def login_user(self, data):
        try:
            user_name = data["username"]
            password = data["password"]
            user = self.get_user_by_username(user_name)
            if not user:
                return {"message": "Invalid username or password", "status": False}

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
                return {"data": user_data, "message": "Login success", "access_token": access_token , "status": True}
            else:
                return {"message": "Invalid username or password", "status": False}
        except Exception as e:
            session.rollback()
            traceback.print_exc()
            return {"message": str(e), "status": False}

    def reset_password(self, data):
        try:
            password = data["password"]
            user_id = data["user_id"]

            hashed_password = encrypt(password)
            user = self.get_user_by_id(user_id)
            user.password_hash = hashed_password
            session.commit()
            return {"message": "Password updated, relogin again", "status": False}
        except Exception as e:
            session.rollback()
            traceback.print_exc()
            return {"message": str(e), "status": False}

    def is_valid_admin(self, user_id):
        try:
            admin_role = session.query(Role).filter_by(name="Admin").first()
            if admin_role:
                admin_id = admin_role.id
            else:
                return False
            user = session.query(User).filter_by(id=user_id).filter_by(role_id=admin_id)
            if user:
                return True
            else:
                return False
        except Exception as e:
            session.rollback()
            traceback.print_exc()
            return False
    