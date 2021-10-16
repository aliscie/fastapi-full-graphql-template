from ariadne.asgi import GQL_START
from ariadne.wsgi import GraphQL
from icecream import ic
from starlette.testclient import TestClient

from Functions.ListFilter import list_filter
from Functions.printJson import printJ
from core.main import app, schema
from werkzeug.test import Client

from db_conf import db_session
from posts.models import Post


def test_sql_querying(test_db, querying):
    def mainQ(x):
        return f"""
        query{{
        posts{x}{{
        id
        title
        }}
        }}
        """
    for i in range(3):
        res = querying("""
                mutation{
                post(title:"title",content:"onee")
                }
                """)
    res = querying("""
        mutation{
        post(title:"xx",content:"onee")
        }
        """)
    res = querying(mainQ("""(input:{search:"xx"})"""))
    assert res.data['posts'][0]['title'] == 'xx'
    res = querying(mainQ("""(input:{search:"title"})"""))
    assert res.data['posts'][0]['title'] == 'title'
    res = querying(mainQ("""(input:{filter:"{'title':'xx'}"})"""))
    assert res.data['posts'][0]['title'] == 'xx'

def test_pagination(test_db, querying):
    for i in range(10):
        res = querying("""
                            mutation{
                            post(title:"title",content:"onee")
                            }
                            """)
    res = querying("""
           query{
           posts{
           id
           title
           }
           }
           """)
    assert len(res.data['posts']) == 10
    assert res.data['posts'][-1]['id'] == 10
    # assert len(res.data)
    res = querying("""
        query{
        posts(input:{to:2}){
        id
        title
        }
        }
        """)
    assert len(res.data['posts']) == 2
    assert res.data['posts'][-1]['id'] == 2


def test_subscription(client, get_messages):
    subscription = """
            subscription { counter }
            """

    with client.websocket_connect("/", "graphql-ws") as ws:
        ws.send_json(
            {
                "type": GQL_START,
                "payload": {"query": subscription},
            }
        )
        x = get_messages(ws.receive_json, 22)
        printJ(x)


def test_posts_filtering(test_db, querying):
    res = querying("""
                    mutation{
                    post(title:"title",content:"onee")
                    }
                    """)
    res = querying("""
                    mutation{
                    post(title:"1",content:"onee")
                    }
                    """)

    assert res.data['post'] == True

    res = querying("""
    query{
    posts{
    title
    content
    }
    }
    """)
    printJ(res.data)
    assert len(res.data['posts']) == 2
    assert res.data['posts'][0]['title'] == 'title'

    res = querying("""
        query{
        posts(input:{search:"1"}){
        title
        content
        }
        }
        """)
    assert len(res.data['posts']) == 1
    assert res.data['posts'][0]['title'] == '1'


def test_subscription(test_db, client, get_messages):
    with client.websocket_connect("/", "graphql-ws") as ws:
        ws.send_json(
            {
                "type": GQL_START,
                "payload": {"query": "subscription { counter }"},
            }
        )
        x = get_messages(ws.receive_json, 22)
        printJ(x)
