from Functions.MakeSchemas import make_schemas
from Users.models import User
x = []

type_defs = [make_schemas(User)]
