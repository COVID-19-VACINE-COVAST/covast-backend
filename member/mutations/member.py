import graphene

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.db import transaction

from member.models.user import User
from member.models.token import Token
from member.models.user_profile import UserProfile
from member.mutations.inputs import UserInput, UserProfileInput


class RegisterMutation(graphene.Mutation):
    class Arguments:
        user_profile_data = UserProfileInput(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, user_profile_data):
        user_data = user_profile_data.user
        try:
            with transaction.atomic():
                user_obj = User.objects.create(**user_data)
                validate_password(user_data.password, user_obj)
                user_obj.set_password(user_data.password)

                user_obj.save()

                user_profile_data['user'] = user_obj

                UserProfile.objects.create(**user_profile_data)
        except Exception as e:
            raise ValidationError(e)

        return cls(success=True)


class LoginMutation(graphene.Mutation):
    class Arguments:
        user_input = UserInput(required=True)

    success = graphene.Boolean()
    token = graphene.String()

    @classmethod
    def mutate(cls, root, info, user_input):
        try:
            user_obj = User.objects.get(username=user_input.username)
            validate_password(user_input.password, user_obj)

            token = Token.objects.get(user=user_obj)
        except User.DoesNotExist:
            raise ValidationError('User not found')
        except Token.DoesNotExist:
            raise ValidationError('Token not found')
        except Exception as e:
            raise ValidationError(e)
        
        return cls(success=True, token=token)


class Mutation(graphene.ObjectType):
    register = RegisterMutation.Field()
    login = LoginMutation.Field()
