from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, JSON, Float
from sqlalchemy.orm import relationship

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    content = Column(JSON)    
    quiz_id = Column(Integer, ForeignKey("quizzes.id"))
    # Relationships

    def __repr__(self):
        return "<Question %r>" % self.content
