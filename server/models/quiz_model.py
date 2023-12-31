import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float, JSON
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship, backref


class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    pass_marks = Column(Float)
    next_quiz_to_unlock = Column(String)
    created_date = Column(DateTime, default=func.now(), nullable=False)
    updated_date = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    questions = relationship("Question", backref="quiz", lazy="dynamic")
    results = relationship("Result", backref="quiz", lazy="dynamic")
    author = relationship("User", back_populates="quizzes", overlaps="quiz_author")

