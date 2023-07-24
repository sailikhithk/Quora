from database import session
from models.result_model import Result
from utils import obj_to_dict
from .question_service import QuestionService

question_services_obj = QuestionService()
class ResultService:
    def __init__(self):
        pass

    def get_result_by_id(self, result_id):
        result = session.query(Result).filter_by(id=result_id).first()
        return obj_to_dict(result)        

    def create_result(self, score, quiz_id, user_id, answers):
        new_result = Result(score=score, quiz_id=quiz_id, user_id=user_id, answers=answers)
        session.add(new_result)
        session.commit()
        return {"message": "results updated"}

    def submit_answer(self, content, user_id, quiz_id):        
        total_score = 0
        answers = []
        for i in content:
            question_id = i["question_id"]
            answer = i["selected_options"]
            question = question_services_obj.get_question_by_id(question_id)
            question_info = question["content"]
            act_answer = question_info["correct_option"]
            marks = question_info["marks"]
            if answer == act_answer:
                total_score = total_score + marks
                i["is_correct"] = True
                i["score_allocated"] = marks
            else:
                i["is_correct"] = False
                i["score_allocated"] = 0
            answers.append(i)
        print("-------------")
        print(answers)
        self.create_result(
            total_score,
            quiz_id,
            user_id,
            answers
        )
        return{"score": total_score}
