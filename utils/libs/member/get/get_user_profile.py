from member.models.user import User
from member.models.user_profile import UserProfile

from utils.libs import GraphQLError


def get_user_profile_by_user_obj(user_obj: User):
    try:
        user_profile_obj = UserProfile.objects.get(user=user_obj)
    except UserProfile.DoesNotExist:
        raise GraphQLError('UserProfile not found')
    except Exception as e:
        raise GraphQLError(e)

    return user_profile_obj