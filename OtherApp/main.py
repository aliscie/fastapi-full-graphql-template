import asyncio
from collections import AsyncGenerator
from typing import Any

from ariadne import SubscriptionType, MutationType
from broadcaster import Broadcast

# from core.main import app
from graphql import GraphQLResolveInfo
from icecream import ic

from core.main import app
from db_conf import db_session

db = db_session.session_factory()

sub2 = SubscriptionType()
send_mutation = MutationType()
broadcast = Broadcast("redis://redis:6379")


@app.on_event("startup")
async def startup_event():
    ic('start')
    await broadcast.connect()
    ic('pass')


@app.on_event("shutdown")
async def startup_event():
    ic('shutdown')
    await broadcast.disconnect()


@send_mutation.field("send")
async def resolve_send(*args, **kwargs):
    number = kwargs.get('number')
    await broadcast.publish(channel="chatroom", message=number)

    # for i in Post.query.all():
    # sql1 = delete(Post).where(Post.id == i.id)
    # db.execute(sql1)
    # db.commit()


    # db_post = models.Post(title=number)
    # db.add(db_post)
    # db.commit()
    return number


@sub2.source("counter2")
async def counter_generator(_: Any, info: GraphQLResolveInfo) -> AsyncGenerator[str, None]:
    async with broadcast.subscribe(channel="chatroom") as subscriber:
        async for event in subscriber:
            yield event



    #     yield str(subscriber)


@sub2.field("counter2")
def counter_resolver(count, info):
    return count


# @event.listens_for(models.Post, 'after_insert')
# def do_stuff(mapper, connection, target, *args, **kwargs):
#     ic('do_stuffdo_stuffdo_stuffdo_stuff')
#     # ic(mapper, connection, target, args, kwargs)


types = [sub2, send_mutation]
# AddTypeDef(counter2_type_def)
# AddType([sub2, send_mutation])
