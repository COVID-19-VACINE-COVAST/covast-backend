from django.core.validators import ValidationError

from member.models.token import Token


def login_required(func):
    def wrapper(cls, root, info, **kwargs):
        try:
            key = kwargs.get('token')
            token_obj = Token.objects.get(key=key)
            if token_obj.user.is_authenticated:
                info.context.user = token_obj.user
            else:
                raise Token.DoesNotExist

        except Token.DoesNotExist:
            raise ValidationError('Authentication failed')
        except Exception as e:
            raise ValidationError(e)
        
        return func(cls, root, info, **kwargs)
    return wrapper
