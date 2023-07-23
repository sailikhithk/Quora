# routes.py
from flask import Flask
from flask_cors import CORS
import os
import logging

from db import db

# import routers
from user import user as user_router
from quiz import quiz as quiz_router
from question import question as question_router
from answer import answer as answer_router
from results import result as result_router
def create_app():
    app = Flask(__name__)

    # Configuring the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app.db"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "sailikhithk"

    db.init_app(app)

    # Apply CORS to app
    CORS(app)


    # Configure logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    # Registering the blueprints
    app.register_blueprint(user_router)
    app.register_blueprint(quiz_router)
    app.register_blueprint(question_router)
    app.register_blueprint(answer_router)
    app.register_blueprint(result_router)

    return app, db
