from ariadne.asgi import GQL_START

from Functions.printJson import printJ


def test_query(querying):
    result = querying("{ hello }")
    printJ(result.data)


def test_posts_filtering(querying):
    result = querying("""
    query{
    posts(input:{search:"title"}){
    title
    content
    }
    }
    """)
    printJ(result.data)


def test_subscription(client, get_messages):
    with client.websocket_connect("/", "graphql-ws") as ws:
        ws.send_json(
            {
                "type": GQL_START,
                "payload": {"query": "subscription { counter }"},
            }
        )
        x = get_messages(ws.receive_json, 22)
        printJ(x)
