
def pagination(resolver, obj, info, **args):
    input = args.get('input', {})
    i = input.get('from')
    f = input.get('to')
    value = resolver(obj, info, **args)
    if 'list' in str(type(value)):
        if not i:
            return value[:f]
        return value[i:f]
    return value

