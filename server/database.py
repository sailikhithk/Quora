import os

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

DATABASE_URL = "sqlite:///" + os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app.db"
)


engine = create_engine(DATABASE_URL)

Base = declarative_base()
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
session = Session()