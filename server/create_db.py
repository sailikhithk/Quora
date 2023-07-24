from models.role_model import Role
from database import session

def create_dummy_roles():
    roles_data = ['Admin', 'Teacher', 'Student']
    for role_name in roles_data:
        role = Role(name=role_name)
        session.add(role)
    session.commit()