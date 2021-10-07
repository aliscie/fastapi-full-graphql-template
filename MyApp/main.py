import asyncio

from ariadne import SubscriptionType, QueryType, ObjectType

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
## def counter1 
"""
counter: Int!

"""
## def counter2
"""
counter2: String!
}
'''

@subscription.source("counter")
async def counter_generator(obj, info):
    for i in range(5):
        await asyncio.sleep(1)
        yield i


@subscription.field("counter")
def counter_resolver(count, info):
    return count
