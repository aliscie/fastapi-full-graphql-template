import asyncio

from ariadne import SubscriptionType

sub2 = SubscriptionType()

@sub2.source("counter2")
async def counter_generator(obj, info):
    for i in range(3):
        await asyncio.sleep(0.3)
        yield i


@sub2.field("counter2")
def counter_resolver(count, info):
    return f'{count } value test'