from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from member.models.user import User
from member.models.user_profile import UserProfile

from utils.libs import GraphQLError


def create_user(user_data: dict):
    password = user_data.pop('password')

    try:
        user_obj = User(**user_data)
        validate_password(password, user_obj)
        user_obj.set_password(password)
        user_obj.save()
    except Exception as e:
        raise GraphQLError(e)

    return user_obj

def create_user_profile(user_obj: User, user_profile_data: dict):
    try:
        user_profile_data['user'] =  user_obj
        user_profile_obj = UserProfile.objects.create(**user_profile_data)
    except Exception as e:
        raise GraphQLError(e)

    return user_profile_obj

def register(register_data):
    user_data = register_data['user']
    user_profile_data = register_data['user_profile']

    user_obj = create_user(user_data)
    user_profile_obj = create_user_profile(user_obj, user_profile_data)

    return {
        'user': user_obj,
        'user_profile': user_profile_obj,
    }
