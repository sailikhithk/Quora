from app import db
from models.answer_model import Answer
from database import session

class AnswerService:
    def __init__(self):
        pass

    def get_all_answers(self):
        return session.query(Answer).all()

    def get_answer_by_id(self, answer_id):
        return session.query(Answer).filter_by(id=answer_id).first()

    def create_answer(self, content, is_correct, question_id, user_id):
        new_answer = Answer(
            content=content,
            is_correct=is_correct,
            question_id=question_id,
            user_id=user_id,
        )

        self.session.add(new_answer)
        self.session.commit()
        return new_answer
    
    def update_answer(self, answer_id, content, is_correct, question_id, user_id):
        answer = self.session.query(Answer).filter_by(id=answer_id).first()
        if answer:
            answer.content = content
            answer.is_correct = is_correct
            self.session.commit()
        return answer

    def delete_answer(self, answer_id):
        answer = self.session.query(Answer).filter_by(id=answer_id).first()
        if answer:
            self.session.delete(answer)
            self.session.commit()
