from sqlalchemy import and_
from models import Quiz, Question, Answer


class QuizRepository:
    def __init__(self, db):
        self.db = db

    def get_all_quizzes(self):
        return self.db.session.query(Quiz).all()

    def get_quiz_by_id(self, quiz_id):
        return self.db.session.query(Quiz).filter_by(id=quiz_id).first()

    def create_quiz(self, title, user_id):
        new_quiz = Quiz(title=title, author_id=user_id)
        self.db.session.add(new_quiz)
        self.db.session.commit()
        return new_quiz

    def update_quiz(self, quiz_id, title):
        quiz = self.db.session.query(Quiz).filter_by(id=quiz_id).first()
        if quiz:
            quiz.title = title
            self.db.session.commit()
        return quiz

    def delete_quiz(self, quiz_id):
        quiz = self.db.session.query(Quiz).filter_by(id=quiz_id).first()
        if quiz:
            self.db.session.delete(quiz)
            self.db.session.commit()

    # New method to fetch correct answers for a quiz from the database
    def get_correct_answers(self, quiz_id):
        return (
            self.db.session.query(Answer)
            .join(Question)
            .filter(and_(Question.quiz_id == quiz_id, Answer.is_correct == True))
            .all()
        )
