from graphene_sqlalchemy import SQLAlchemyObjectType
from Users.models import User


class UserSchema(SQLAlchemyObjectType):
    class Meta:
        model = User


class PostSchema(SQLAlchemyObjectType):
    class Meta:
        model = Post

