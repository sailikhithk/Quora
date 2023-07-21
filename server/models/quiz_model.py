# quiz_model.py
from db import db


class Quiz(db.Model):
    __tablename__ = "quizzes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # Relationships
    questions = db.relationship("Question", backref="quiz", lazy="dynamic")
    results = db.relationship("Result", backref="quiz", lazy="dynamic")

    def __repr__(self):
        return "<Quiz %r>" % self.title