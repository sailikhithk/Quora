# main.py
import os
import logging

from flask import Flask, request
from flask_cors import CORS
from datetime import timedelta


# Registering the blueprints after initializing the app
from routes.user import user as user_router
from routes.quiz import quiz as quiz_router
from routes.question import question as question_router
from routes.result import result as result_router

from flask_jwt_extended import JWTManager

from database import Base, engine

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "your-secret-key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)

# Apply CORS to app
# CORS(app, resources={r"*": {"origins": "*"}})


# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Registering the blueprints
app.register_blueprint(user_router, url_prefix="/auth")
app.register_blueprint(quiz_router, url_prefix="/quiz")
app.register_blueprint(question_router, url_prefix="/question")
app.register_blueprint(result_router, url_prefix="/result")

@app.before_request
def before_request():
    print()
    print("Request Received:")
    print("URL:", request.url)
    print("Method:", request.method)
    # print("Headers:", request.headers)
    print("Query Params:", request.args)
    
    if request.method == "POST":
        if request.content_type.startswith('application/json'):
            print("Body (JSON):", request.get_json())
        elif request.content_type.startswith('multipart/form-data'):
            print("Form Data:")
            for key, value in request.form.items():
                print(f"{key}: {value}")    
    else:
        print("Body: No request body")
@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,POST")
    
    print()
    print("Response Sent:")
    print("Status Code:", response.status_code)
    print("Content Type:", response.content_type)
    
    if response.content_type == "application/json":
        print("Data:", response.get_json())
    elif response.content_type.startswith("image/") or response.content_type.startswith("application/"):
        print("File Response: Not Printing Binary Data")
    else:
        print("Data:", response.get_data(as_text=True))    
    return response

if __name__ == "__main__":
    from models.question_model import Question
    from models.quiz_model import Quiz
    from models.result_model import Result
    from models.role_model import Role
    from models.user_model import User

    Base.metadata.create_all(engine)

    from create_db import (
        create_dummy_roles,
        create_dummy_questions,
        create_dummy_quizzes,
        create_dummy_results,
        create_dummy_users,
    )

    create_dummy_roles()
    # create_dummy_users()
    
    # create_dummy_quizzes()
    # create_dummy_questions()
    # create_dummy_results()

    app.run(debug=True)
