import asyncio

from ariadne import QueryType
from icecream import ic

from Users import models
from Users.auth import mutation
from db_conf import db_session

db = db_session.session_factory()

users_query = QueryType()


def send_auth_email(user):
    asyncio.sleep(1)
    print(f'verification email is sent to {user}')


@users_query.field("users")
def resolve_users(*args, **kwargs):
    # record_query = db.query.paginate(1, 2, False)
    # total = record_query.total
    # record_items = record_query.items
    return {"items": db.query(models.User).all()}


types = [mutation, users_query]
