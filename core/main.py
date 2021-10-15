import importlib

from ariadne import make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
from broadcaster import Broadcast
from fastapi import FastAPI
from icecream import ic

from Users.models import User
from core.settings import APPS

app = FastAPI()

broadcast = Broadcast("redis://redis:6379")

# broadcast = Broadcast("redis://localhost:6379")


@app.on_event("startup")
async def startup_event():
    await broadcast.connect()


@app.on_event("shutdown")
async def startup_event():
    await broadcast.disconnect()


types = []
type_defs = [load_schema_from_path('../../')]

for i in APPS:
    x = importlib.import_module(f'{i}.main')
    try:
        y = importlib.import_module(f'{i}.TypeDefs')
        type_defs.extend(y.type_defs)
    except:
        pass
    types.extend(x.types)

cost_map = {
    "Query": {
        "users": {"complexity": 1, "multipliers": ['pages']},
    },
}


def pagination(resolver, obj, info, **args):
    i = args.get('from')
    f = args.get('to')
    value = resolver(obj, info, **args)
    if 'list' in str(type(value)):
        if not i:
            return value[:f]
        return value[i:f]
    return value


# def serach(resolver, obj, info, **args):
#     value = resolver(obj, info, **args)
#     #TODO
#     # if obj and args:
#     #     return filtering(obj,args)
#     # try:
#     #     ic(value.filter(Post.title == 'title lkdsjf'))
#     #     ic('passs')
#     # except:
#     #     pass
#     return value

ic('xxx')
# schema_dict = UserSchema.introspect()
# my_types = schema_dict["__schema"]["types"]
# list(filter(lambda my_types: types['name'] == 'PostSchema', my_types))

schema = make_executable_schema(type_defs, *types)
ariadneApp = GraphQL(schema, debug=True, middleware=[pagination])
app.mount("/", ariadneApp)
