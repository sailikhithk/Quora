from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'sailikhithk'  # Replace this with a real secret in production!

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(80))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    role = db.relationship('Role')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')

    # Check if all fields are provided and if the username isn't already taken
    if not username or not password or not role:
        return jsonify({"error": "Missing field(s)"}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username taken"}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email taken"}), 400

    # Create a new user
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    user = User(
        username=username,
        email=email,
        password=hashed_password, 
        role=Role.query.filter_by(name=role).first()
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({"error": "Missing field(s)"}), 400

    # Check if the user exists and the password is correct
    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Bad username or password"}), 401

    return jsonify({"message": "Logged in"}), 200


if __name__ == "__main__":
    app.run(debug=True)