import graphene


class UserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)


class UserProfileInput(graphene.InputObjectType):
    last_name = graphene.String(required=True)
    first_name = graphene.String(required=True)
    birth = graphene.Date(required=True)
    sex = graphene.Int(required=True)


class RegisterInput(graphene.InputObjectType):
    user = UserInput(required=True)
    user_profile = UserProfileInput(required=True)


class LoginInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)
