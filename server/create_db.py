from models.role_model import Role
from models.user_model import User
from models.quiz_model import Quiz
from models.question_model import Question
from models.result_model import Result
from models.profile_model import Profile

from database import session
from sqlalchemy import func
import json, random


def create_dummy_roles():
    roles_data = ["Admin", "Teacher", "Student", "SAI"]
    query_result = (
        session.query(func.count(Role.id)).filter(Role.name.in_(roles_data)).scalar()
    )
    if query_result != len(roles_data):
        for role_name in roles_data:
            role = Role(name=role_name)
            session.add(role)
        session.commit()


def create_dummy_users():
    roles = session.query(Role).all()
    institutions = ["Institution 1", "Institution 2", "Institution 3", "SAI"]
    users_data = [
        {
            "username": "Harnath-1",
            "password": "harnath",
            "email": "harnath@gmail.com",
            "institution": "SAI",
            "role": "Admin",
        },
        # Add other users as needed
    ]
    for user_data in users_data:
        existing_user = (
            session.query(User).filter_by(username=user_data["username"]).first()
        )
        if not existing_user:
            role_id = next(
                (role.id for role in roles if role.name == user_data["role"]), None
            )
            user = User(
                username=user_data["username"],
                password_hash=user_data["password"],
                email=user_data["email"],
                institution=user_data["institution"],
                role_id=role_id,
            )
            session.add(user)
    session.commit()


def create_dummy_quizzes():
    users = session.query(User).all()
    next_quizzes_to_unlock = [2, 3, 4, 5, 6, 1]
    for i, user in enumerate(users):
        quiz = Quiz(
            title=f"Quiz {i+1}",
            author_id=user.id,
            pass_marks=80.0,
            next_quiz_to_unlock=next_quizzes_to_unlock[i % len(next_quizzes_to_unlock)],
        )
        session.add(quiz)
    session.commit()


def create_dummy_questions():
    quizzes = session.query(Quiz).all()
    options_list = ["a", "b", "c", "d"]
    for i, quiz in enumerate(quizzes):
        for j in range(2):  # Creating 2 questions for each quiz
            is_multichoice = random.choice([True, False])
            question = Question(
                content=f"Q{j+1}",
                is_multichoice=is_multichoice,
                options=json.dumps(options_list),
                correct_option=json.dumps([1, 2] if is_multichoice else [1]),
                is_mandatory=True,
                marks=5 if is_multichoice else 1,
                quiz_id=quiz.id,
            )
            session.add(question)
    session.commit()


def create_dummy_results():
    users = session.query(User).all()
    quizzes = session.query(Quiz).all()
    for user in users:
        for quiz in quizzes:
            result = Result(
                user_id=user.id,
                quiz_id=quiz.id,
                content=json.dumps(
                    [
                        {"question_id": 1, "selected_options": [0]},
                        {"question_id": 2, "selected_options": [2]},
                    ]
                ),
                # Other attributes as needed
            )
            session.add(result)
    session.commit()
