from database import session
from models.result_model import Result
from utils import obj_to_dict
class ResultService:
    def __init__(self):
        pass

    # def get_all_results(self):
    #     return self.result_repository.get_all_results()

    def get_result_by_id(self, result_id):
        result = session.query(Result).filter_by(id=result_id).first()
        return obj_to_dict(result)        

    def create_result(self, score, quiz_id, user_id):
        new_result = Result(score=score, quiz_id=quiz_id, user_id=user_id)
        session.add(new_result)
        session.commit()
        return {"message": "results updated"}

    # def update_result(self, result_id, score):
    #     return self.result_repository.update_result(result_id, score)

    # def delete_result(self, result_id):
    #     return self.result_repository.delete_result(result_id)

    # def get_results_by_user(self, user_id):
    #     return self.result_repository.get_results_by_user(user_id)
