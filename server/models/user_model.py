# user_model.py
from db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    institution = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))  # Add this line

    # Relationships
    quizzes = db.relationship(
        "Quiz", backref="author", lazy="dynamic"
    )  # Notice "Quiz" is a string
    answers = db.relationship(
        "Answer", backref="user", lazy="dynamic"
    )  # Notice "Answer" is a string
    results = db.relationship(
        "Result", backref="user", lazy="dynamic"
    )  # Notice "Result" is a string

    def __repr__(self):
        return "<User %r>" % self.username