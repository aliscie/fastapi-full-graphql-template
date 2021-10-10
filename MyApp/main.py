import asyncio

from ariadne import SubscriptionType, QueryType, ObjectType

from core.TypeDef import AddTypeDef

query = QueryType()
query.bind_resolvers_to_graphql_type('hello', "String!")
subscription = SubscriptionType()

query = ObjectType("Query")

@query.field("hello")
def resolve_hello(*args, **kwargs):
    return 'xxxxxxx'

hello_type_def = '''
extend type Query{
hello: String!}

'''
subscription_type_def = '''

extend type Subscription {
"""
- This returns `1, 2, 3, 4,`
"""
counter: Int!
}
'''

AddTypeDef([subscription_type_def,hello_type_def])

@subscription.source("counter")
async def counter_generator(obj, info):
    for i in range(5):
        await asyncio.sleep(1)
        yield i


@subscription.field("counter")
def counter_resolver(count, info):
    return count