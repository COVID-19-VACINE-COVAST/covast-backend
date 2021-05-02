from member.models.token import Token
from member.models.user import User

from utils.libs import GraphQLError


def get_token_by_login_data(login_data: dict):
    username = login_data['username']
    password = login_data['password']

    try:
        user_obj = User.objects.get(username=username)

        if not user_obj.check_password(password):
            raise GraphQLError('Wrong password')

        token_obj = Token.objects.get(user=user_obj)
    except User.DoesNotExist:
        raise GraphQLError('Wrong username')
    except Token.DoesNotExist:
        raise GraphQLError('Token is not exists')
    except Exception as e:
        raise GraphQLError(e)

    return token_obj
