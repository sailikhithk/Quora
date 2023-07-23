from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship, backref



class Quiz(Base):
    __tablename__ = "quizzes"

    id = Column(Integer, primary_key=True)
    title = Column(String(128))
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    # Relationships
    questions = relationship("Question", backref="quiz", lazy="dynamic")
    results = relationship("Result", backref="quiz", lazy="dynamic")
    author = relationship("User", back_populates="quizzes", overlaps="quiz_author")

    def __repr__(self):
        return "<Quiz %r>" % self.title