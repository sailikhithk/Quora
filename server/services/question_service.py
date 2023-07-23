# question_service.py

from repositories.question_repository import QuestionRepository
from app import db
from models.question_model import Question
class QuestionService:
    def __init__(self):
        pass
    
    def get_all_questions(self):
        return self.question_repository.get_all_questions()

    def get_question_by_id(self, question_id):
        return db.session.query(Question).filter_by(id=question_id).first()

    def create_question(self, content, quiz_id):
        new_question = Question(content=content, quiz_id=quiz_id)
        self.db.session.add(new_question)
        self.db.session.commit()
        return new_question
    
    def update_question(self, question_id, content):
        question = self.db.session.query(Question).filter_by(id=question_id).first()
        if question:
            question.content = content
            self.db.session.commit()
        return question


    def delete_question(self, question_id):
        question = self.db.session.query(Question).filter_by(id=question_id).first()
        if question:
            self.db.session.delete(question)
            self.db.session.commit()

    # def get_questions_by_quiz(self, quiz_id):
    #     return self.question_repository.get_questions_by_quiz(quiz_id)
