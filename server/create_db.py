from models.role_model import Role
from database import session
from sqlalchemy import func

def create_dummy_roles():
    roles_data = ['Admin', 'Teacher', 'Student']
    query_result = session.query(func.count(Role.id)).filter(Role.name.in_(roles_data)).scalar()
    if query_result != 3:
        for role_name in roles_data:
            role = Role(name=role_name)
            session.add(role)
        session.commit()