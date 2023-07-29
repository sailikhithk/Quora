from models import Quiz, Question, UserQuizMapping
from services import QuestionService 
from database import session
from sqlalchemy.orm import aliased
from sqlalchemy import desc, and_
from utils import obj_to_list, obj_to_dict

question_service_obj = QuestionService()
class QuizService:
    def __init__(self):
        pass

    def get_all_quizzes(self, user_id):
        try:
            QuizAlias = aliased(Quiz)
            UserQuizMappingAlias = aliased(UserQuizMapping)
            result = session.query(
                Quiz.id, Quiz.title, Quiz.author_id, Quiz.pass_marks,
                Quiz.next_quiz_to_unlock, Quiz.created_date, Quiz.updated_date,
                UserQuizMapping.id, UserQuizMapping.user_id, UserQuizMapping.quiz_id,
                UserQuizMapping.no_of_attempts, UserQuizMapping.is_qualified,
                UserQuizMapping.max_scored_marks, UserQuizMapping.created_date,
                UserQuizMapping.updated_date
            )\
            .outerjoin(UserQuizMappingAlias, and_(Quiz.id == UserQuizMappingAlias.quiz_id, UserQuizMappingAlias.user_id == user_id))\
            .order_by(desc(UserQuizMappingAlias.updated_date))\
            .all()
            
            
            quiz_results = []
            for row in result:
                quiz_data = {
                    "quiz_id": row[0],
                    "title": row[1],
                    "author_id": row[2],
                    "pass_marks": row[3],
                    "next_quiz_to_unlock": row[4],
                    "created_date_quiz": str(row[5]),  # Convert DateTime to string
                    "updated_date_quiz": str(row[6]),  # Convert DateTime to string
                    "user_quiz_mapping_id": row[7],
                    "user_id": row[8],
                    "user_quiz_id": row[9],
                    "no_of_attempts": row[10],
                    "is_qualified": row[11],
                    "max_scored_marks": row[12],
                    "created_date_mapping": str(row[13]),  # Convert DateTime to string
                    "updated_date_mapping": str(row[14])  # Convert DateTime to string
                }
                quiz_results.append(quiz_data)

            return quiz_results                
        except Exception as e:
            return []

    def get_quiz_by_id(self, quiz_id):
        quiz = session.query(Quiz).filter_by(id=quiz_id).first()
        if not quiz:
            return {"error": "Quiz not found"}
        return quiz

    def create_quiz(self, title, user_id, pass_marks, next_quiz_to_unlock):
        new_quiz = Quiz(
            title=title,
            author_id=user_id,
            pass_marks=pass_marks,
            next_quiz_to_unlock=",".join([str(x) for x in next_quiz_to_unlock]),
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

    def upload_quiz(
        self, user_id, quiz_name, questions, pass_marks, next_quiz_to_unlock
    ):
        result = self.create_quiz(quiz_name, user_id, pass_marks, next_quiz_to_unlock)
        quiz_id = result.get("id", None)
        for question in questions:
            question_service_obj.create_question(question, quiz_id)
        return {"message": "Quiz uploaded"}

    def get_questions_by_quiz_id(self, id):
        questions = session.query(Question).filter_by(quiz_id=id).all()
        return obj_to_list(questions)

    def get_quiz(self, id):
        quiz = self.get_quiz_by_id(id)
        quiz = obj_to_dict(quiz)
        quiz["questions"] = self.get_questions_by_quiz_id(id)
        return quiz