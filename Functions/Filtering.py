import json

import sqlalchemy
from icecream import ic
from sqlalchemy import or_

from db_conf import db_session


def filtering(Model, data):
    db = db_session.session_factory()
    objects = db.query(Model)
    data = data.get('input')
    if data:
        search = data.get('search')
        filter_operator = data.get('filter_operator')

        filter_operator = filter_operator if filter_operator else 'and'
        filter_operator = filter_operator.lower()
        filter_operator = filter_operator + '_'
        filter_operator = getattr(sqlalchemy, filter_operator)
        filter = data.get('filter')

        filters = []
    #
        if search:
            for key in Model.__table__.columns.keys():
                if key in ['title', 'content']:
                    filters.append(getattr(Model, key).contains(search))
            return objects.filter(or_(*filters))

        if filter:
            filter = filter.replace("'", '"') if filter else None
            filter = filter.replace("'", '"')
            filter = json.loads(filter)
            for key, value in filter.items():
                filters.append(getattr(Model, key).__eq__(value))
            return objects.filter(filter_operator(*filters))
    return objects.all()