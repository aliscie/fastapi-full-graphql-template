import asyncio

from ariadne import make_executable_schema, SubscriptionType, ObjectType, load_schema_from_path
from ariadne.asgi import GraphQL
from fastapi import FastAPI

app = FastAPI()
query_type_def = '''
type Query {
    """
    ### A brief summary of the search result.
    - value two
    ```
    code test here.
    ```
    """
_unused: Boolean 
hello: String!
}

type Post{
title: String!
id: ID!
content: String!
time_created: String!
}

'''
subscription_type_def = '''

type Subscription {
counter: Int!
}
'''

type_defs = '''    
schema {
query: Query
subscription: Subscription
}
''' + query_type_def + subscription_type_def


subscription = SubscriptionType()

# query = QueryType()
query = ObjectType("Query")


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


schema = make_executable_schema(type_defs, [subscription, query])
app.mount("/", GraphQL(schema, debug=True))
