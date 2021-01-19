import graphene
from graphene_django.types import DjangoObjectType
from member.models.user import User
from utils.decorators import auth_token

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(object):
    my_info = graphene.Field(UserType, token=graphene.String())

    @auth_token
    def resolve_my_info(self, info, user, **kwargs):
        return user