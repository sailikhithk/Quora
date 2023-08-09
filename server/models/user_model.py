import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float, JSON
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship, backref


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(64), index=True, unique=True)
    password_hash = Column(String(128))
    email = Column(String(120), index=True, unique=True)
    institution = Column(String(128))
    role_id = Column(Integer, ForeignKey("roles.id"))  # Add this line
    created_date = Column(DateTime, default=func.now(), nullable=False)
    updated_date = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    quizzes = relationship(
        "Quiz", backref="quiz_author", lazy="dynamic"
    )  # Notice "Quiz" is a string and 'author' is changed to 'quiz_author'
    results = relationship(
        "Result", backref="user", lazy="dynamic"
    )  # Notice "Result" is a string