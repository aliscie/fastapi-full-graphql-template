from sqlalchemy import Column, Integer, String

from db_conf import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    birth_date = Column(String)
    email = Column(String)
    password = Column(String(255))
