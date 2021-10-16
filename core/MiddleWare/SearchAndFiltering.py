import json

from Functions.ListFilter import list_filter


def serach(resolver, obj, info, **args):
    value = resolver(obj, info, **args)
    if 'list' in str(type(value)):
        input = args.get('input', {})
        serach = input.get('search')
        filter_operator = input.get('filter_operator', 'and')
        filter = input.get('filter','{}')
        if filter or serach:
            filter = filter.replace("'",'"')
            filter = json.loads(filter)
            value = list_filter(value, data=filter, operator=filter_operator, search=serach)
            return value
    return value