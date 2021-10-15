
import pytest
from ariadne.asgi import GraphQL
from graphql import graphql_sync
from starlette.testclient import TestClient

from core.main import schema
from db_conf import engine, Base, db_session


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def client():
    app = GraphQL(schema)
    return TestClient(app)

def parsequery(x):
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
