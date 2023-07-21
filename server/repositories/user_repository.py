from models.user_model import User, db


class UserRepository:
    @staticmethod
    def get_all_users():
        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)

    @staticmethod
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    @staticmethod
    def create_user(username, hashed_password, email, institution, role):
        user = User(
            username=username,
            password_hash=hashed_password,
            email=email,
            institution=institution,
            role=role,
        )
        db.session.add(user)
        db.session.commit()
        return user

    @staticmethod
    def update_user(user_id, username, email, hashed_password, role, institution):
        user = User.query.get(user_id)
        if not user:
            return None

        user.username = username
        user.email = email
        user.password_hash = hashed_password
        user.role = role
        user.institution = institution

        db.session.commit()
        return user

    @staticmethod
    def delete_user(user_id):
        user = User.query.get(user_id)
        if not user:
            return None

        db.session.delete(user)
        db.session.commit()
        return user
