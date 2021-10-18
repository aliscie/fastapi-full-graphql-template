import os

from dotenv import load_dotenv
from icecream import ic
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker


load_dotenv(".env")
# beat_dburi = 'sqlite:///schedule.db'

try:
    SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]
    beat_dburi = os.environ["DATABASE_URL"]
    print('========================== DEPLOYED MODE =======================================')
except:
    SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
    # beat_dburi = 'postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/celery-schedule'
    beat_dburi = "sqlite:///./sql_app.db"
    print('========================== LOCAL MODE =======================================')


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.users_query = db_session.query_property()
