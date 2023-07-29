from database import session
from models.result_model import Result
from utils import obj_to_dict
from services import QuestionService, QuizService, UserQuizMappingService

import json

question_services_obj = QuestionService()
quiz_service_obj = QuizService()
user_quiz_mapping_obj = UserQuizMappingService()

class ResultService:
    def __init__(self):
        pass

    def get_result_by_id(self, result_id):
        result = session.query(Result).filter_by(id=result_id).first()
        if not result:
            return {"error": "Result not found"}
        return obj_to_dict(result)

    def create_result(self, score, quiz_id, user_id, answers, is_qualified):
        new_result = Result(
            score=score, quiz_id=quiz_id, user_id=user_id, answers=answers, is_qualified=is_qualified
        )
        session.add(new_result)
        session.commit()
        return {"message": "results updated"}
    
    def submit_answer(self, content, user_id, quiz_id):
        total_score = 0
        answers = []
        quiz = quiz_service_obj.get_quiz(quiz_id)
        quiz_pass_mark = quiz.get("pass_marks", 100)
            
        # evaluating answers
        for i in content:
            question_id = i["question_id"]
            answer = i["selected_options"]
            question = question_services_obj.get_question_by_id(question_id)    
            question_info = question["content"]
            if isinstance(question_info, str):
                question_info = json.loads(
                    question_info
                )
            print(question_info)
            act_answer = question_info["correct_option"]
            marks = question_info.get(
                "marks", 1
            )
            if set(answer) == set(
                act_answer
            ):
                total_score += marks
                i["is_correct"] = True
                i["score_allocated"] = marks
                i["correct_options"] = act_answer
            else:
                i["is_correct"] = False
                i["score_allocated"] = 0
                i["correct_options"] = act_answer
            answers.append(i)
        print("-------------")
        print(answers)
        is_qualified = False
        if total_score >= quiz_pass_mark:
            is_qualified = True
        
        self.create_result(total_score, quiz_id, user_id, answers, is_qualified)
        user_quiz_info = user_quiz_mapping_obj.get_record(user_id, quiz_id)
        if user_quiz_info:
            update_dic = {}
            update_dic["no_of_attempts"] = 1 + user_quiz_info["no_of_attempts"]
            if total_score > user_quiz_info["max_scored_marks"]:
                update_dic["max_scored_marks"] = total_score

            if is_qualified:
                update_dic["is_qualified"] = is_qualified
            
            user_quiz_mapping_obj.update_record(update_dic, user_id, quiz_id)    
        else:
            user_quiz_mapping_obj.create_record(user_id, quiz_id, is_qualified, total_score)
                
        return {"score": total_score}
