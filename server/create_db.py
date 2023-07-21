from routes.routes import create_app, db
from models.role_model import Role
from models.user_model import User
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app, db = create_app()
bcrypt = Bcrypt(app)
CORS(app)

with app.app_context():
    print("Database created")
    db.create_all()
    hashed_password = bcrypt.generate_password_hash("password")
    print("hashed password", hashed_password)

    # Check if the role already exists in the database
    student_role = Role.query.filter_by(name="student").first()

    # If the role doesn't exist, create it
    if student_role is None:
        student_role = Role(name="student")
        db.session.add(student_role)
        db.session.commit()  # Commit the new role to the database before using its id

    # Then, create a User with the Role
    dummy_user = User(
        username="test2",
        email="test2@example.com",
        password_hash=hashed_password,  # Use 'password_hash' here
        institution="NYU",
        role_id=student_role.id,  # Use 'role_id' here
    )
    print("dummy user look")
    db.session.add(dummy_user)
    db.session.commit()
