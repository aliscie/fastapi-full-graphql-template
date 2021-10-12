from Functions.MakeSchemas import make_schemas
from posts.models import Post

x = []

type_defs = [make_schemas(Post)]
