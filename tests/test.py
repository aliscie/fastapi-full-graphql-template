from ariadne.asgi import GQL_START
from icecream import ic

from Functions.printJson import printJ


def test_query(querying):
    result = querying("{ hello }")
    printJ(result.data)


def test_selfs(self):
    ic(self.querying)

def test_posts_filtering(self):
    from db_conf import db_session
    db = db_session.session_factory()

    db_user = models.User(username='mm', password='password')
    db.add(db_user)
    try:
        db.commit()
        db.refresh(db_user)
        ok = True
    except Exception as e:
        ic(e)
        db.rollback()
        ok = False
    ic(db.query(models.User).all())
    result = self.querying("""
            mutation {
            post(title: "String", content: "String")
            }
            """)
    ic(db.query(models.User).all())
    printJ(result.data)

    result = self.querying("""
    query{
    posts(input:{search:"title"}){
    title
    content
    }
    }
    """)
    printJ(result.data)


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
