import graphene

from member.mutations.member import Mutation as MemberMutation


class Query(graphene.ObjectType):
    pass


class Mutation(MemberMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(mutation=Mutation)
