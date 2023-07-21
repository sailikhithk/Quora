from models.result_model import Result


class ResultRepository:
    def __init__(self, db):
        self.db = db

    def get_all_results(self):
        return self.db.session.query(Result).all()

    def get_result_by_id(self, result_id):
        return self.db.session.query(Result).filter_by(id=result_id).first()

    def create_result(self, score, quiz_id, user_id):
        new_result = Result(score=score, quiz_id=quiz_id, user_id=user_id)
        self.db.session.add(new_result)
        self.db.session.commit()
        return new_result

    def update_result(self, result_id, score):
        result = self.db.session.query(Result).filter_by(id=result_id).first()
        if result:
            result.score = score
            self.db.session.commit()
        return result

    def delete_result(self, result_id):
        result = self.db.session.query(Result).filter_by(id=result_id).first()
        if result:
            self.db.session.delete(result)
            self.db.session.commit()
