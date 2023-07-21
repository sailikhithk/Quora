from repositories.answer_repository import AnswerRepository


class AnswerService:
    def __init__(self, db):
        self.answer_repo = AnswerRepository(db)

    def get_all_answers(self):
        return self.answer_repo.get_all_answers()

    def get_answer_by_id(self, answer_id):
        return self.answer_repo.get_answer_by_id(answer_id)

    def create_answer(self, content, is_correct, question_id, user_id):
        return self.answer_repo.create_answer(content, is_correct, question_id, user_id)

    def update_answer(self, answer_id, content, is_correct, question_id, user_id):
        return self.answer_repo.update_answer(
            answer_id, content, is_correct, question_id, user_id
        )

    def delete_answer(self, answer_id):
        return self.answer_repo.delete_answer(answer_id)
