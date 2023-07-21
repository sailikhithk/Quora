from app import app, db, bcrypt, User, Role  # Add Role
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS



with app.app_context():
    print("Database created")
    db.create_all()
    hashed_password = bcrypt.generate_password_hash('password').decode('utf-8')
    print('hashed password', hashed_password)
    # Check if the role already exists in the database
    student_role = Role.query.filter_by(name='student').first()
    
    # If the role doesn't exist, create it
    if student_role is None:
        student_role = Role(name='student')
        db.session.add(student_role)
    
    # Then, create a User with the Role
    dummy_user = User(username='test2', email='test2@example.com',
                      password=hashed_password, role=student_role)  # Use the Role object
    print('dummy user look')
    db.session.add(dummy_user)
    db.session.commit()
