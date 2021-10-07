import asyncio

from ariadne import SubscriptionType

from core.TypeDef import AddTypeDef

sub2 = SubscriptionType()


counter2_type_def = '''

extend type Subscription {
"""
- This returns 0 value test, 1 value test, 3 value test
"""
counter2: String!
}
'''

AddTypeDef(counter2_type_def)
@sub2.source("counter2")
async def counter_generator(obj, info):
    for i in range(3):
        await asyncio.sleep(0.3)
        yield i


@sub2.field("counter2")
def counter_resolver(count, info):
    return f'{count } value test'