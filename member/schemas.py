from graphene_django.types import DjangoObjectType

from member.models.user import User
from member.models.user_profile import UserProfile


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('uuid', 'username', )


class UserProfileType(DjangoObjectType):
    class Meta:
        model = UserProfile
        fields = ('uid', 'user', 'last_name', 'first_name', 'birth', 'sex', 'followers_num', 'inoculation_at', )
