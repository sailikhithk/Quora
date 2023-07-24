from models import Quiz
from database import session
from utils import obj_to_list
class QuizService:
    def __init__(self):
        pass

    def get_all_quizzes(self):
        try:
            records =  session.query(Quiz).all()
            return obj_to_list(records)
        except Exception as e:
            return []

    def get_quiz_by_id(self, quiz_id):
        return session.query(Quiz).filter_by(id=quiz_id).first()

    def create_quiz(self, title, user_id):
        new_quiz = Quiz(title=title, author_id=user_id)
        session.add(new_quiz)
        session.commit()
        return {"message": "Quiz created"}        

    def update_quiz(self, quiz_id, title):
        quiz = session.query(Quiz).filter_by(id=quiz_id).first()
        if quiz:
            quiz.title = title
            session.commit()
        return quiz
    
    def delete_quiz(self, quiz_id):
        quiz = session.query(Quiz).filter_by(id=quiz_id).first()
        if quiz:
            session.delete(quiz)
            session.commit()