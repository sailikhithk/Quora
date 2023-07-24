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
        session.add(new_answer)
        session.commit()
        return {"message": "Answer Updated"}
    
    def update_answer(self, answer_id, content, is_correct, question_id, user_id):
        answer = session.query(Answer).filter_by(id=answer_id).first()
        if answer:
            answer.content = content
            answer.is_correct = is_correct
            session.commit()
        return answer

    def delete_answer(self, answer_id):
        answer = session.query(Answer).filter_by(id=answer_id).first()
        if answer:
            session.delete(answer)
            session.commit()
