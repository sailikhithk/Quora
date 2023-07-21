# role_model.py
from db import db
from models.user_model import User  # add this line


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(
        db.String(64), unique=True
    )  # The role name e.g. "admin", "student"

    # Relationships
    users = db.relationship("User", backref="role", lazy="dynamic")

    def __repr__(self):
        return "<Role %r>" % self.name
