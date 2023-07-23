from repositories.quiz_repository import QuizRepository
from sqlalchemy.exc import SQLAlchemyError
from flask import current_app as app
from models import Quiz
from models import QuizAttempt, Answer


class QuizService:
    def __init__(self, quiz_repository):
        self.quiz_repository = quiz_repository

    def get_all_quizzes(self):
        try:
            app.logger.info("QuizService: Fetching all quizzes")
            return self.quiz_repository.get_all_quizzes()
        except SQLAlchemyError as e:
            app.logger.error("QuizService: Error fetching quizzes")
            app.logger.error(str(e))
            return None

    def save_answers_and_score(self, quiz_id, user_id, user_answers):
        try:
            # Fetch the correct answers from the database
            correct_answers = self.quiz_repository.get_correct_answers(
                quiz_id, list(user_answers.keys())
            )

            correct_answers_dict = {
                answer.question_id: answer.content for answer in correct_answers
            }

            # Compare user's answers to the correct ones and calculate the score
            score = sum(
                [
                    1
                    for question_id, answer in user_answers.items()
                    if correct_answers_dict.get(question_id) == answer
                ]
            )

            # Save the user's score in the database
            quiz_attempt = QuizAttempt(user_id=user_id, quiz_id=quiz_id, score=score)
            self.quiz_repository.db.session.add(quiz_attempt)
            self.quiz_repository.db.session.commit()

        except SQLAlchemyError as e:
            app.logger.error("QuizService: Error saving user's score")
            app.logger.error(str(e))
            return None

    def get_quiz_by_id(self, quiz_id):
        return self.quiz_repository.get_quiz_by_id(quiz_id)

    def create_quiz(self, title, user_id):
        return self.quiz_repository.create_quiz(title, user_id)

    def update_quiz(self, quiz_id, title):
        return self.quiz_repository.update_quiz(quiz_id, title)

    def delete_quiz(self, quiz_id):
        return self.quiz_repository.delete_quiz(quiz_id)

    def get_quizzes_by_user(self, user_id):
        return self.quiz_repository.get_quizzes_by_user(user_id)
