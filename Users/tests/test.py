from Functions.printJson import printJ


def test_query(querying):
    result = querying("{ hello }")
    printJ(result.data)
