from models import Question
from database import session
from utils import obj_to_list, obj_to_dict
from urllib.parse import urlparse


class QuestionService:
    def __init__(self):
        pass

    def get_all_questions(self):
        return obj_to_list(session.query(Question).all())

    def get_question_by_id(self, question_id):
        question = session.query(Question).filter_by(id=question_id).first()
        if not question:
            return {"error": "Question not found"}
        return obj_to_dict(question)

    def create_question(self, content, quiz_id, image_url=None):
        # Validate input
        if not content and not image_url:
            return {"error": "Either content or image_url must be provided"}
        if image_url and not self.is_valid_url(image_url):
            return {"error": "Invalid image_url"}
        if content and not isinstance(content, str):
            return {"error": "Content must be a string"}

        new_question = Question(content=content, quiz_id=quiz_id, image_url=image_url)
        session.add(new_question)
        session.commit()
        return {"message": "Question created", "question_id": new_question.id}

    def is_valid_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def update_question(self, content):
        question_id = content["id"]
        content.pop("id", None)
        question = session.query(Question).filter_by(id=question_id).first()
        if question:
            question.content = content.get("content", question.content)
            question.image_url = content.get("image_url", question.image_url)
            if not question.content and not question.image_url:
                return {"error": "Either content or image_url must be provided"}
            session.commit()
            return {"message": "Question updated"}
        return {"error": "Question not found"}

    def delete_question(self, question_id):
        question = session.query(Question).filter_by(id=question_id).first()
        if question:
            session.delete(question)
            session.commit()
            return {"message": "Question Deleted"}
        return {"error": "Question not found"}
