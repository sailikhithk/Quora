# result_service.py
from repositories.result_repository import ResultRepository


class ResultService:
    def __init__(self, result_repository):
        self.result_repository = result_repository

    def get_all_results(self):
        return self.result_repository.get_all_results()

    def get_result_by_id(self, result_id):
        return self.result_repository.get_result_by_id(result_id)

    def create_result(self, score, quiz_id, user_id):
        return self.result_repository.create_result(score, quiz_id, user_id)

    def update_result(self, result_id, score):
        return self.result_repository.update_result(result_id, score)

    def delete_result(self, result_id):
        return self.result_repository.delete_result(result_id)

    def get_results_by_user(self, user_id):
        return self.result_repository.get_results_by_user(user_id)
