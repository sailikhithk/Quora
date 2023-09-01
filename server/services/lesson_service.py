import traceback
from flask_jwt_extended import create_access_token
from models import Lesson
from models import User
from utils import encrypt, decrypt, obj_to_dict, obj_to_list
from database import session
import os


class LessonService:
    def __init__(self):
        pass

    def get_lesson_by_title(self, title):
        return session.query(Lesson).filter_by(title=title).first()
    
    def get_lesson_by_id(self, id):
        return session.query(Lesson).filter_by(id=id).first()
    
    def create_lesson(self, data):
        try:
            lesson_name = data['title']
            existing_lesson = self.get_lesson_by_title(lesson_name)
            if existing_lesson:
                return {"message": "lesson with same title exist", "status": False}
                
            new_lesson = Lesson(**data)
            session.add(new_lesson)
            session.commit()
            return {"message": "lesson created", "status": True, "data": obj_to_dict(new_lesson)}
        except Exception as e:
            session.rollback()
            traceback.print_exc()
            return {"message": str(e), "status": False}

    def update_lesson(self, data):
        try:
            lesson_id = data['lesson_id']
            lesson = self.get_lesson_by_id(lesson_id)
            if not lesson:
                return {"message": "lesson not exist", "status": False}
            for key, value in data.items():
                setattr(lesson, key, value)  
                session.commit()
            return {"message": "lesson Updated", "status": True, "data": obj_to_dict(lesson)}
        except Exception as e:
            session.rollback()
            traceback.print_exc()
            return {"message": str(e), "status": False}
    
    def get_lesson(self, lesson_id):
        try:
            lesson = self.get_lesson_by_id(lesson_id)
            lesson_dic = obj_to_dict(lesson)
            full_file_path =  os.path.abspath(os.path.join(os.pardir, "server/data/lessons", "python_intro.html"))
            if os.path.exists(full_file_path):
                with open(full_file_path, "r") as file:
                    content = file.read()
                    lesson_dic["lesson"] = content
            else:
                lesson_dic["lesson"] = ""
            return  {"data": lesson_dic, "status": True}
           
        except Exception as e:
            session.rollback()
            traceback.print_exc()
            return {"message": str(e), "status": False}
    
    def list_lesson(self, user_id):
        try:
            lessons = session.query(Lesson).all()
            lessons_list = obj_to_list(lessons)
            user = session.query(User).filter_by(id=user_id).first()
            lessons_unlocked = user.lessons_unlocked
            lessons_unlocked = lessons_unlocked.replace(", ", ",").split(",")
            for i in range(len(lessons_list)):
                if str(lessons_list[i]["id"]) in lessons_unlocked:
                    lessons_list[i]["locked"] = False
                else:
                    lessons_list[i]["locked"] = True
            return  {"data": lessons_list, "status": True}
        
        except Exception as e:
            session.rollback()
            traceback.print_exc()
            return {"message": str(e), "status": False}
       
    def delete_lesson(self, lesson_id):
        try:
            lesson = session.query(Lesson).get(lesson_id)
            if lesson:
                session.delete(lesson)
                session.commit()
                return {"message": "Lesson Deleted", "status": True}
            else:
                return {"message": "Lesson not Deleted", "status": False}
        except Exception as e:
            session.rollback()
            traceback.print_exc()
            return {"message": str(e), "status": False}