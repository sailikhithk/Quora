from database import Base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text
from sqlalchemy.orm import relationship, backref


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    password_hash = Column(String(128))
    email = Column(String(120), index=True, unique=True)
    institution = Column(String(128))
    role_id = Column(Integer, ForeignKey("roles.id"))  # Add this line

    # Relationships
    quizzes = relationship(
        "Quiz", backref="quiz_author", lazy="dynamic"
    )  # Notice "Quiz" is a string and 'author' is changed to 'quiz_author'
    results = relationship(
        "Result", backref="user", lazy="dynamic"
    )  # Notice "Result" is a string
    
    def __repr__(self):
        return "<User %r>" % self.username
