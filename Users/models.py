from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from db_conf import Base




class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    birth_date = Column(String)
    email = Column(String)
    password = Column(String(255))
