from Functions.MakeSchemas import make_schemas
from Users.models import User, Post
x = []

type_defs = [make_schemas(User), make_schemas(Post)]
