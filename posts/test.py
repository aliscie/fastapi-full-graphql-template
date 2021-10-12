from Functions.printJson import printJ


def test_query(querying):
    result = querying("""
    query{
    posts(filter:"{'title':'title lkdsjf'}"){
    title
    content
    }
    }
    """)
    printJ(result.data['hello'])
