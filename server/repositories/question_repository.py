from models.question_model import Question


class QuestionRepository:
    def __init__(self, db):
        self.db = db

    def get_all_questions(self):
        return self.db.session.query(Question).all()

    def get_question_by_id(self, question_id):
        return self.db.session.query(Question).filter_by(id=question_id).first()

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
