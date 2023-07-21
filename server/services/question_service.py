# question_service.py

from repositories.question_repository import QuestionRepository
from db import db


class QuestionService:
    def __init__(self):
        self.question_repository = QuestionRepository(db)

    def get_all_questions(self):
        return self.question_repository.get_all_questions()

    def get_question_by_id(self, question_id):
        return self.question_repository.get_question_by_id(question_id)

    def create_question(self, content, quiz_id):
        return self.question_repository.create_question(content, quiz_id)

    def update_question(self, question_id, content):
        return self.question_repository.update_question(question_id, content)

    def delete_question(self, question_id):
        return self.question_repository.delete_question(question_id)

    def get_questions_by_quiz(self, quiz_id):
        return self.question_repository.get_questions_by_quiz(quiz_id)
