import importlib
from ariadne import make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL
from broadcaster import Broadcast
from core.MiddleWare.Pagination import pagination
from core.MiddleWare.SearchAndFiltering import serach
from core.settings import APPS, origins
from db_conf import engine
from fastapi_admin.app import app as admin_app
from fastapi import FastAPI
import contextlib
from sqlalchemy import MetaData
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


broadcast = Broadcast("redis://redis:6379")
# broadcast = Broadcast("redis://localhost:6379")



meta = MetaData()

with contextlib.closing(engine.connect()) as con:
    trans = con.begin()
    for table in reversed(meta.sorted_tables):
        con.execute(table.delete())
    trans.commit()


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

middleware = [pagination, serach]
schema = make_executable_schema(type_defs, *types)

ariadneApp = GraphQL(schema, debug=True, middleware=middleware)
app.mount("/", ariadneApp)
app.mount("/admin", admin_app)
