import asyncio

from ariadne import SubscriptionType, QueryType
from icecream import ic


query = QueryType()
subscription = SubscriptionType()

# class AuthenticationError(Exception):
#     extensions = {"code": "UNAUTHENTICATED"}
#
#
# type_def = """
#     type Query {
#         field: Boolean
#     }
# """
#
# query_type = QueryType()


@query.field("hello")
def resolve_hello(*args, **kwargs):
    # raise AuthenticationError("PLEASE LOGIN")
    ic('resolve_helloresolve_helloresolve_helloresolve_helloresolve_hello')
    return "xxxxxxx"


@subscription.source("counter")
async def counter_generator(obj, info):
    for i in range(5):
        await asyncio.sleep(1)
        yield i


@subscription.field("counter")
def counter_resolver(count, info):
    return count


types = [query, subscription]