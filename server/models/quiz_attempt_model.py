from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Float
from sqlalchemy.orm import relationship, backref

class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"), nullable=False)
    score = Column(Float, nullable=False)

    # relationships
    quiz = relationship("Quiz", backref=backref("quiz_attempts", lazy="dynamic"))
    user = relationship(
        "User", back_populates="quiz_attempts", overlaps="attempted_quizzes"
    )

    def __repr__(self):
        return "<QuizAttempt %r>" % self.id
