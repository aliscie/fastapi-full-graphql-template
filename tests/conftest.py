import pytest
from ariadne import make_executable_schema
from ariadne.asgi import GraphQL
from graphql import graphql_sync
from icecream import ic
from starlette.testclient import TestClient

from main import query, type_def, schema1


@pytest.fixture
def client():
    app = GraphQL(schema1)
    return TestClient(app)


def parsequery(x):
    schema = make_executable_schema(type_def, query)
    return graphql_sync(schema, x)


@pytest.fixture
def querying(*args, **kwargs):
    return parsequery


def getMessages(x, range_value):
    messages = []

    for i in range(range_value):
        response = x()
        messages.append(response)
        if response.get('type') == 'complete':
            break
    return messages


@pytest.fixture
def get_messages(*args, **kwargs):
    return getMessages
