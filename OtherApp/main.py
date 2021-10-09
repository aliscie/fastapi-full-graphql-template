from collections import AsyncGenerator

from ariadne import SubscriptionType, MutationType
from broadcaster import Broadcast

from core import models
# from core.main import app
from db_conf import db_session

db = db_session.session_factory()

sub2 = SubscriptionType()

send_mutation = MutationType()
subscription = SubscriptionType()

broadcast = Broadcast("redis://localhost:6379")


#

# @app.on_event("startup")
# async def startup_event():
#     x = broadcast.connect
#
#
# @app.on_event("shutdown")
# async def startup_event():
#     x = broadcast.disconnect


@send_mutation.field("send")
def resolve_send(*args, **kwargs):
    # broadcast.publish(channel="chatroom", message="Hello world!")

    # for i in Post.query.all():
    # sql1 = delete(Post).where(Post.id == i.id)
    # db.execute(sql1)
    # db.commit()

    number = kwargs.get('number')
    db_post = models.Post(title=number)
    db.add(db_post)
    db.commit()
    return db_post.id


@sub2.source("counter2")
async def counter_generator() -> AsyncGenerator[str, None]:
    async with broadcast.subscribe(channel="chatroom") as subscriber:
        async for message in subscriber:
            yield message


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
