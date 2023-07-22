# quiz_attempt_model.py
from db import db


class QuizAttempt(db.Model):
    __tablename__ = "quiz_attempts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey("quizzes.id"), nullable=False)
    score = db.Column(db.Float, nullable=False)

    # relationships
    quiz = db.relationship("Quiz", backref=db.backref("quiz_attempts", lazy="dynamic"))
    user = db.relationship(
        "User", back_populates="quiz_attempts", overlaps="attempted_quizzes"
    )

    def __repr__(self):
        return "<QuizAttempt %r>" % self.id
