import graphene

from member.mutations.inputs import RegisterInput, LoginInput

from utils.libs.member import register, get_token_by_login_data


class RegisterMutation(graphene.Mutation):
    class Arguments:
        register_data = RegisterInput(required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, register_data):
        register(register_data)

        return cls(success=True)


class LoginMutation(graphene.Mutation):
    class Arguments:
        login_data = LoginInput(required=True)

    success = graphene.Boolean()
    token = graphene.String()

    @classmethod
    def mutate(cls, root, info, login_data):
        token_obj = get_token_by_login_data(login_data)

        return cls(success=True, token=token_obj)


class Mutation(graphene.ObjectType):
    register = RegisterMutation.Field()
    login = LoginMutation.Field()
