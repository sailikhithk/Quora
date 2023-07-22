from models.answer_model import Answer


class AnswerRepository:
    def __init__(self, db):
        self.db = db

    def get_all_answers(self):
        return self.db.session.query(Answer).all()

    def get_answer_by_id(self, answer_id):
        return self.db.session.query(Answer).filter_by(id=answer_id).first()

    def create_answer(self, content, is_correct, question_id, user_id):
        new_answer = Answer(
            content=content,
            is_correct=is_correct,
            question_id=question_id,
            user_id=user_id,
        )

        self.db.session.add(new_answer)
        self.db.session.commit()
        return new_answer

    def update_answer(self, answer_id, content, is_correct):
        answer = self.db.session.query(Answer).filter_by(id=answer_id).first()
        if answer:
            answer.content = content
            answer.is_correct = is_correct
            self.db.session.commit()
        return answer

    def delete_answer(self, answer_id):
        answer = self.db.session.query(Answer).filter_by(id=answer_id).first()
        if answer:
            self.db.session.delete(answer)
            self.db.session.commit()
