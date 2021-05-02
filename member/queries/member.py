import graphene

from member.schemas import UserType, UserProfileType

from utils.decorators import login_required
from utils.libs.member import get_user_profile_by_user_obj


class Query(graphene.ObjectType):
    get_user_info = graphene.Field(UserType, token=graphene.String(required=True))
    get_user_profile_info = graphene.Field(UserProfileType, token=graphene.String(required=True))

    @classmethod
    @login_required
    def resolve_get_user_info(cls, root, info, token):
        user_obj = info.context.user
        return user_obj

    @classmethod
    @login_required
    def resolve_get_user_profile_info(cls, root, info, token):
        user_obj = info.context.user
        user_profile_obj = get_user_profile_by_user_obj(user_obj)
        return user_profile_obj
