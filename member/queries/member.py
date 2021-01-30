import graphene

from member.schemas import UserType

from utils.decorators import login_required


class Query(graphene.ObjectType):
    get_user_info = graphene.Field(UserType, token=graphene.String(required=True))

    @classmethod
    @login_required
    def resolve_get_user_info(cls, root, info, token):
        return info.context.user
