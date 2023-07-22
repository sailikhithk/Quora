from routes.routes import create_app, db

# from models.role_model import Role
# from models.user_model import User
# from models.quiz_model import Quiz
# from models.quiz_attempt_model import QuizAttempt
# from models.question_model import Question
# from models.answer_model import Answer
# from models.result_model import Result  # Import the Result model
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from models import Role, User, Quiz, QuizAttempt, Question, Answer, Result

app, db = create_app()
bcrypt = Bcrypt(app)
CORS(app)

with app.app_context():
    print("Database created")
    # Create the database tables
    # from models.role_model import Role
    # from models.user_model import User
    # from models.quiz_model import Quiz
    # from models.quiz_attempt_model import QuizAttempt
    # from models.question_model import Question
    # from models.answer_model import Answer
    # from models.result_model import Result  # Import the Result model
    # create_db.py

    from models import Role, User, Quiz, QuizAttempt, Question, Answer, Result

    # rest of your code
    db.create_all()
    hashed_password = bcrypt.generate_password_hash("password")
    print("hashed password", hashed_password)

    # Create roles
    role_names = ["student", "teacher", "admin"]
    roles = {}
    for role_name in role_names:
        role = Role.query.filter_by(name=role_name).first()
        if role is None:
            role = Role(name=role_name)
            db.session.add(role)
            db.session.commit()  # Commit the new role to the database before using its id
        roles[role_name] = role

    # Then, create a User with the Role
    dummy_user = User(
        username="test2",
        email="test2@example.com",
        password_hash=hashed_password,  # Use 'password_hash' here
        institution="NYU",
        role_id=roles["student"].id,  # Use 'role_id' here
    )
    print("dummy user look")
    db.session.add(dummy_user)
    db.session.commit()

    # Create a Quiz
    dummy_quiz = Quiz(title="Test Quiz", author_id=dummy_user.id)
    db.session.add(dummy_quiz)
    db.session.commit()

    # Create some Questions and Answers
    dummy_questions = [
        Question(content="What's the capital of France?", quiz_id=dummy_quiz.id),
        Question(content="Who painted the Mona Lisa?", quiz_id=dummy_quiz.id),
    ]

    for question in dummy_questions:
        db.session.add(question)
    db.session.commit()

    # We use index-based access here because we know the exact order of the questions
    dummy_answers = [
        Answer(content="Paris", is_correct=True, question_id=dummy_questions[0].id),
        Answer(content="London", is_correct=False, question_id=dummy_questions[0].id),
        Answer(
            content="Leonardo da Vinci",
            is_correct=True,
            question_id=dummy_questions[1].id,
        ),
        Answer(
            content="Vincent van Gogh",
            is_correct=False,
            question_id=dummy_questions[1].id,
        ),
    ]

    for answer in dummy_answers:
        db.session.add(answer)
    db.session.commit()

    # Create a Result
    dummy_result = Result(
        user_id=dummy_user.id, quiz_id=dummy_quiz.id, score=100
    )  # Score is 100% as the user answered all questions correctly
    db.session.add(dummy_result)
    db.session.commit()

    # Create a Quiz Attempt
    dummy_attempt = QuizAttempt(quiz_id=dummy_quiz.id, user_id=dummy_user.id, score=100)
    db.session.add(dummy_attempt)
    db.session.commit()
