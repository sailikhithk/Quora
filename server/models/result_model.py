# result_model.py
from db import db


class Result(db.Model):
    __tablename__ = "results"

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Float)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizzes.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __repr__(self):
        return "<Result %r>" % self.id
