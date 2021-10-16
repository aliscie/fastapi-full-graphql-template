import json
from typing import Any, AsyncGenerator

from ariadne import MutationType
from ariadne import SubscriptionType, QueryType
from graphql import GraphQLResolveInfo

from Functions.CRUD import Create
from Functions.Filtering import filtering
from core.main import broadcast
from db_conf import db_session
from posts.models import Post

db = db_session.session_factory()

sub2 = SubscriptionType()
mutation = MutationType()
query = QueryType()


@mutation.field("send")
async def __init__(*args, **kwargs):
    number = kwargs.get('number')
    await broadcast.publish(channel="chatroom", message=json.dumps({'message': number, "sender": 1}))

    # for i in Post.query.all():
    # sql1 = delete(Post).where(Post.id == i.id)
    # db.execute(sql1)
    # db.commit()

    # db_post = models.Post(title=number)
    # db.add(db_post)
    # db.commit()
    return number


@sub2.source("chat")
async def counter_generator(_: Any, info: GraphQLResolveInfo) -> AsyncGenerator[str, None]:
    async with broadcast.subscribe(channel="chatroom") as subscriber:
        async for event in subscriber:
            yield json.loads(event.message)


@sub2.field("chat")
def counter_resolver(count, info):
    return count


@mutation.field('post')
def __init__(*args, **kwargs):
    return Create(Post,kwargs)


@query.field('posts')
def resolve_posts(*args, **kwargs):
    return db.query(Post).all()

# @event.listens_for(models.Post, 'after_insert')
# def do_stuff(mapper, connection, target, *args, **kwargs):
#     ic('do_stuffdo_stuffdo_stuffdo_stuff')
#     # ic(mapper, connection, target, args, kwargs)


types = [sub2, mutation, query]
