from icecream import ic


def make_schemas(model):
    d = """
        """
    for i, key in model.__table__.columns.items():

        x = str(key.type.python_type)
        x = x.replace("<class '", '')
        x = x.replace("'>", '')
        x = x.title()
        if x in ['Str', 'Datetime.Datetime']:
            x = 'String'
        if x == 'Bool':
            x = 'Boolean'
        d += f"""
                {i}: {x}
                """
    y = f"""
    type {model.__tablename__.title()} {{
    {d}
    }}
    """
    return y
