import importlib
from ariadne import make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
from ariadne.validation import cost_validator
from broadcaster import Broadcast
from fastapi import FastAPI
from icecream import ic

from core.settings import APPS

app = FastAPI()

broadcast = Broadcast("redis://redis:6379")


@app.on_event("startup")
async def startup_event():
    await broadcast.connect()


@app.on_event("shutdown")
async def startup_event():
    await broadcast.disconnect()


types = []
type_defs = [load_schema_from_path(f'../../')]

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


schema = make_executable_schema(type_defs, *types)
ariadneApp = GraphQL(schema, debug=True, middleware=[pagination])
app.mount("/", ariadneApp)
