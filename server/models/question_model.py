# question_model.py
from db import db


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizzes.id"))

    # Relationships
    answers = db.relationship("Answer", backref="question", lazy="dynamic")

    def __repr__(self):
        return "<Question %r>" % self.content
