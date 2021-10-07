from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from fastapi import FastAPI
from icecream import ic

from core import models
from MyApp.main import query, subscription
from OtherApp.main import sub2
from db_conf import db_session
from core.TypeDef import type_defs

db = db_session.session_factory()
app = FastAPI()
#
# db_user = models.User(username='alisci3', password='password_hash')
# db.add(db_user)
# db.commit()
for i in db.query(models.User).all():
    ic(i.username)

#
# db.query(models.User).filter(models.User.username == 'alisci').first()
# db_user_info = db.query(models.User).filter(models.User.username == 'alisci').first()
# ic(db.query(models.Post).filter(models.Post.id == 1).first())

types = [subscription, query, sub2]
schema = make_executable_schema(type_defs, *types)
ariadneApp = GraphQL(schema, debug=True)
app.mount("/", ariadneApp)
