import asyncio

from ariadne import make_executable_schema, SubscriptionType, ObjectType, load_schema_from_path, ScalarType
from ariadne.asgi import GraphQL
from fastapi import FastAPI

from MyApp.main import query, subscription
from OtherApp.main import sub2

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
counter2: String!
}
'''
type_defs = '''    
schema {
query: Query
subscription: Subscription
}
''' + query_type_def + subscription_type_def

types = [subscription, query, sub2]
schema = make_executable_schema(type_defs, *types)
ariadneApp = GraphQL(schema, debug=True)
app.mount("/", ariadneApp)
