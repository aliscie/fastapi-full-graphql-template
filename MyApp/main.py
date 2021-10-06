import asyncio

from ariadne import ObjectType, SubscriptionType

query = ObjectType("Query")
subscription = SubscriptionType()

@query.field("hello")
def resolve_hello(*args, **kwargs):
    return 'xxxxxxx'



@subscription.source("counter")
async def counter_generator(obj, info):
    for i in range(5):
        await asyncio.sleep(1)
        yield i


@subscription.field("counter")
def counter_resolver(count, info):
    return count + 1


