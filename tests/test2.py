from Functions.printJson import printJ
from db_conf import db_session
from posts.models import Post
db = db_session.session_factory()


def test_posts_filtering(test_db, querying):
    for i in range(7):
        db.add(Post(title=f'title{i}', content=f'i'))
    db.commit()

    result = querying("""
    query{
    posts{
    title
    content
    }
    }
    """)
    printJ(result.data)

