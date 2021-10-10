import bcrypt
from ariadne import MutationType

from Users import models
from Users.schemas import UserSchema
from db_conf import db_session

mutation = MutationType()
db = db_session.session_factory()


class AuthenticationError(Exception):
    extensions = {"code": "UNAUTHENTICATED"}


@mutation.field("signup")
def resolve_signup(*args, **kwargs):
    username = kwargs.get('username')
    password = kwargs.get('password')
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    password_hash = hashed_password.decode("utf8")

    user = UserSchema(username=username, password=password_hash)
    db_user = models.User(username=user.username, password=password_hash)
    db.add(db_user)

    try:
        db.commit()
        db.refresh(db_user)
        ok = True

    except:
        db.rollback()
        ok = False
    return ok


@mutation.field("signin")
def resolve_signin(*args, **kwargs):
    username = kwargs.get('username')
    password = kwargs.get('password')
    user = UserSchema(username=username, password=password)
    db_user_info = db.query(models.User).filter(models.User.username == username).first()
    if bcrypt.checkpw(user.password.encode("utf-8"), db_user_info.password.encode("utf-8")):
        return True
    else:
        return AuthenticationError("dummy auth error")


types = [mutation]
