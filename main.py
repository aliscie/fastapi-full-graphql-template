import asyncio

from ariadne import make_executable_schema, SubscriptionType, ObjectType, load_schema_from_path, ScalarType
from ariadne.asgi import GraphQL
from fastapi import FastAPI
from icecream import ic

from MyApp.main import query, subscription, hello_type_def, subscription_type_def
from OtherApp.main import sub2
from db_conf import db_session
import models
from schemas import UserSchema

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

main_type_defs = ''' 
schema {
query: Query
subscription: Subscription
}

type Query {
_unused: Boolean 
}

type Subscription {
_unused: Boolean
}
'''

types = [subscription, query, sub2]
type_defs = [main_type_defs, subscription_type_def, hello_type_def]
schema = make_executable_schema(type_defs, *types)
ariadneApp = GraphQL(schema, debug=True)
app.mount("/", ariadneApp)
