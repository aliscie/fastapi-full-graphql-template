from Functions.printJson import printJ


def test_query(querying):
    result = querying("{ hello }")
    assert result.data['hello'] == 'xxxxxxx'
    printJ(result.data['hello'])
