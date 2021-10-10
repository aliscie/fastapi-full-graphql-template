import json
from collections import AsyncGenerator
from typing import Any

from ariadne import SubscriptionType, MutationType
from graphql import GraphQLResolveInfo

from core.main import broadcast
from db_conf import db_session

db = db_session.session_factory()

sub2 = SubscriptionType()
send_mutation = MutationType()




@send_mutation.field("send")
async def resolve_send(*args, **kwargs):
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

    #     yield str(subscriber)


@sub2.field("chat")
def counter_resolver(count, info):
    return count


# @event.listens_for(models.Post, 'after_insert')
# def do_stuff(mapper, connection, target, *args, **kwargs):
#     ic('do_stuffdo_stuffdo_stuffdo_stuff')
#     # ic(mapper, connection, target, args, kwargs)


types = [sub2, send_mutation]
# AddTypeDef(chat_type_def)
# AddType([sub2, send_mutation])
