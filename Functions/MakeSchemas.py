def make_schemas(model,is_list=True):
    name = model.__tablename__
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
    type {name.title()} {{
    {d}
    }}
    """
    if is_list:
        y += f"""
            extend type Query{{
            {name.lower()}s(input: ListInput): [{name.title()}]
            }}
            """
    return y
