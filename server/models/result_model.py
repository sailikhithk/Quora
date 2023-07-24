from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Float, JSON
from sqlalchemy.orm import relationship, backref


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True)
    score = Column(Float)
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    answers = Column(JSON)

    def __repr__(self):
        return "<Result %r>" % self.id
