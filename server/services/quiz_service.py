from repositories.quiz_repository import QuizRepository
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app
from models import Quiz


class QuizService:
    def __init__(self, quiz_repository):
        self.quiz_repository = quiz_repository

    def get_all_quizzes(self):
        try:
            app.logger.info("QuizService: Fetching all quizzes")  # Logging here
            return self.quiz_repository.get_all_quizzes()
        except SQLAlchemyError as e:
            app.logger.error("QuizService: Error fetching quizzes")  # Logging here
            app.logger.error(str(e))
            return None

    def get_quiz_by_id(self, quiz_id):
        return self.quiz_repository.get_quiz_by_id(quiz_id)

    def create_quiz(self, title, user_id):
        return self.quiz_repository.create_quiz(title, user_id)

    def update_quiz(self, quiz_id, title):
        return self.quiz_repository.update_quiz(quiz_id, title)

    def delete_quiz(self, quiz_id):
        return self.quiz_repository.delete_quiz(quiz_id)

    def get_quizzes_by_user(self, user_id):
        return self.quiz_repository.get_quizzes_by_user(user_id)
