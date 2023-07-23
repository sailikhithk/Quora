# question_model.py
from db import db


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(128))
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizzes.id"), nullable=False)

    # Relationships
    quiz = db.relationship("Quiz", back_populates="questions", overlaps="quiz_question")

    def __repr__(self):
        return "<Question %r>" % self.content

    def serialize(self):
        return {"id": self.id, "content": self.content, "quiz_id": self.quiz_id}
