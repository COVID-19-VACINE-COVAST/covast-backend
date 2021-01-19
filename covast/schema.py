import graphene

from member.queries.member import Query as MemberQuery

from member.mutations.member import Mutation as MemberMutation


class Query(MemberQuery, graphene.ObjectType):
    pass


class Mutation(MemberMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
