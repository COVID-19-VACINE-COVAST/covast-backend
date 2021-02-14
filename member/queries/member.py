import graphene

from member.models.user_profile import UserProfile
from member.schemas import UserType, UserProfileType

from utils.decorators import login_required


class Query(graphene.ObjectType):
    get_user_info = graphene.Field(UserType, token=graphene.String(required=True))
    get_user_profile_info = graphene.Field(UserProfileType, token=graphene.String(required=True))

    @classmethod
    @login_required
    def resolve_get_user_info(cls, root, info, token):
        return info.context.user

    @classmethod
    @login_required
    def resolve_get_user_profile_info(cls, root, info, token):
        user_obj = info.context.user
        return UserProfile.objects.get(user=user_obj)
