from models.question_model import Question
from database import session
from utils import obj_to_list


class QuestionService:
    def __init__(self):
        pass
    
    def get_all_questions(self):
        return self.question_repository.get_all_questions()

    def get_question_by_id(self, question_id):
        return session.query(Question).filter_by(id=question_id).first()

    def create_question(self, content, quiz_id):
        new_question = Question(content=content, quiz_id=quiz_id)
        session.add(new_question)
        session.commit()
        return {"message": "Question created"}
    
    def update_question(self, question_id, content):
        question = self.session.query(Question).filter_by(id=question_id).first()
        if question:
            question.content = content
            self.session.commit()
        return question


    def delete_question(self, question_id):
        question = self.session.query(Question).filter_by(id=question_id).first()
        if question:
            self.session.delete(question)
            self.session.commit()

    # def get_questions_by_quiz(self, quiz_id):
    #     return self.question_repository.get_questions_by_quiz(quiz_id)
