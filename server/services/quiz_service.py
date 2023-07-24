from models import Quiz
from models import Question
from database import session
from utils import obj_to_list, obj_to_dict
from .question_service import QuestionService

question_service_obj = QuestionService()
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

    def create_quiz(self, title, user_id, pass_marks, next_quiz_to_unlock):
        new_quiz = Quiz(
            title=title, 
            author_id=user_id,
            pass_marks=pass_marks, 
            next_quiz_to_unlock= ','.join([str(x) for x in next_quiz_to_unlock])
            )
        session.add(new_quiz)
        session.commit()
        return {"message": "Quiz created", "id": new_quiz.id}        

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

    def upload_quiz(self, user_id, quiz_name, questions, pass_marks, next_quiz_to_unlock):
        result = self.create_quiz(quiz_name, user_id, pass_marks, next_quiz_to_unlock)
        quiz_id = result.get("id", None)
        for question in questions:
            question_service_obj.create_question(question, quiz_id)
        return {"message": "Quiz uploaded"}

    def get_questions_by_quiz_id(self, id):
        questions = session.query(Question).filter_by(quiz_id = id).all()
        return obj_to_list(questions)
    
    def get_quiz(self, id):
        quiz = self.get_quiz_by_id(id)
        quiz = obj_to_dict(quiz)
        quiz['questions'] = self.get_questions_by_quiz_id(id)
        return quiz 