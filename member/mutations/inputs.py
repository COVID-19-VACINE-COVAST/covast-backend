import graphene


class UserInput(graphene.InputObjectType):
    username = graphene.String(required=True)
    password = graphene.String(required=True)


class UserProfileInput(graphene.InputObjectType):
    user = UserInput(required=True)
    last_name = graphene.String(required=True)
    first_name = graphene.String(required=True)
    birth = graphene.Date(required=True)
    sex = graphene.Int(required=True)
