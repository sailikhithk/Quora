from models.role_model import Role
from models.user_model import User
from models.quiz_model import Quiz
from models.question_model import Question
from models.result_model import Result
from database import session
from sqlalchemy import func
import json, random


def create_dummy_roles():
    """
    Function to create and insert dummy roles in the database.
    The roles include "Admin", "Teacher", and "Student".
    """
    roles_data = ["Admin", "Teacher", "Student"]
    query_result = (
        session.query(func.count(Role.id)).filter(Role.name.in_(roles_data)).scalar()
    )
    if query_result != 3:
        for role_name in roles_data:
            role = Role(name=role_name)
            session.add(role)
        session.commit()


def create_dummy_users():
    """
    Function to create and insert dummy users in the database.
    Three users are created, each with a corresponding role and institution.
    """
    roles = session.query(Role).all()
    institutions = ["Institution 1", "Institution 2", "Institution 3"]
    for i, role in enumerate(roles):
        existing_user = session.query(User).filter_by(username=f"user{i+1}").first()
        if not existing_user:
            user = User(
                username=f"user{i+1}",
                password_hash=f"password{i+1}",
                email=f"user{i+1}@example.com",
                institution=institutions[i % len(institutions)],
                role_id=role.id,
            )
            session.add(user)
    session.commit()


def create_dummy_quizzes():
    """
    Function to create and insert dummy quizzes in the database.
    Quizzes are created for each user and include pass marks and next quiz to unlock.
    """
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
    """
    Function to create and insert dummy questions in the database.
    Questions are created for each quiz and include content, options, correct answers, and marks.
    """
    quizzes = session.query(Quiz).all()
    options_list = ["a", "b", "c", "d"]  # predefined list of options

    for i, quiz in enumerate(quizzes):
        question_content = {
            "question": f"Q{i+1}",  # generate question text
            "is_multichoice": False
            if i % 2 == 0
            else True,  # alternate between True and False
            "options": options_list,
            "correct_option": [0]
            if i % 2 == 0
            else [0, 1],  # alternate between single and multiple correct options
            "is_mandatory": True,
            "marks": 5,  # or any value that suits your scoring system
        }
        question = Question(
            content=question_content,  # No need to convert to string or replace ' with "
            quiz_id=quiz.id,
        )
        session.add(question)
    session.commit()


def create_dummy_results():
    """
    Function to create and insert dummy results in the database.
    Results are created for each user and include scores, answers, and correctness.
    """
    users = session.query(User).all()
    quizzes = session.query(Quiz).all()
    for i, user in enumerate(users):
        if i < len(quizzes):
            answers = [
                {
                    "question_id": question.id,
                    "selected_options": [3, 4],
                    "is_correct": False,
                    "score_allocated": 0,
                }
                if question.content["is_multichoice"]
                else {
                    "question_id": question.id,
                    "selected_options": [1],
                    "is_correct": True,
                    "score_allocated": question.content["marks"],
                }
                for question in quizzes[i].questions
            ]
            result = Result(
                score=80.0,
                quiz_id=quizzes[i].id,
                user_id=user.id,
                answers=answers,
            )
            session.add(result)
    session.commit()
    print("Dummy data created successfully!")
