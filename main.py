import asyncio
import uvicorn
from fastapi import FastAPI
from ariadne import make_executable_schema, SubscriptionType, QueryType, ObjectType
from ariadne.asgi import GraphQL
from icecream import ic

app = FastAPI()

# ariadne copied from https://ariadnegraphql.org/docs/subscriptions

type_def = """
    type Query {
        _unused: Boolean
        hello: String!
    }

    type Subscription {
        counter: Int!
    }
"""

subscription = SubscriptionType()
# query = QueryType()

query = ObjectType("Query")


@query.field("hello")
def resolve_hello( *args, **kwargs):
    ic(args, kwargs)
    ic('yyyyyyyyyyyyyyyyyyyyyy')
    return 'xxxxxxx'


@subscription.source("counter")
async def counter_generator(obj, info):
    for i in range(5):
        await asyncio.sleep(1)
        yield i


@subscription.field("counter")
def counter_resolver(count, info):
    return count + 1


schema1 = make_executable_schema(type_def, subscription)
schema = make_executable_schema(type_def, query)
app.mount("/", GraphQL(schema1, debug=True))
# app.mount("/", GraphQL(schema, debug=True))
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
