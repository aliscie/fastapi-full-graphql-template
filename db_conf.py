import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

load_dotenv(".env")
try:
    SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]
    print('========================== DEPLOYED MODE =======================================')
except:
    print('========================== LOCAL MODE =======================================')
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.users_query = db_session.query_property()
