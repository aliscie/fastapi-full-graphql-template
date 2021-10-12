import bcrypt
from ariadne import MutationType
from icecream import ic

from Users import models
from db_conf import db_session

db = db_session.session_factory()

mutation = MutationType()


class AuthenticationError(Exception):
    extensions = {"code": "UNAUTHENTICATED"}


@mutation.field("signin")
def __init__(*args, **kwargs):
    username = kwargs.get('username')
    password = kwargs.get('password')
    db_user_info = db.users_query(models.User).filter(models.User.username == username).first()
    if bcrypt.checkpw(password.encode("utf-8"), db_user_info.password.encode("utf-8")):
        return True
    else:
        return AuthenticationError("invalid credentials.")


@mutation.field("signup")
def __init__(*args, **kwargs):
    password = kwargs.get('password')
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    data = {}
    for i in models.User.__table__.columns.keys():
        if i != 'id':
            data[i] = kwargs.get(i)
    data['password'] = hashed_password.decode("utf8")

    db_user = models.User(**data)
    db.add(db_user)

    try:
        db.commit()
        db.refresh(db_user)
        ok = True
    except Exception as e:
        ic(e)
        db.rollback()
        ok = False
    return ok
