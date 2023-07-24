from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True)
    content = Column(String)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return "<Answer %r>" % self.content
