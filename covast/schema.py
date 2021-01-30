import graphene

from member.schemas import *
from post.schemas import *

from inoculation.queires.hospital import Query as HospitalQuery
from inoculation.queires.reservation import Query as ReservationQuery
from inoculation.queires.vaccine import Query as VaccineQuery

from member.queries.member import Query as MemberQuery
from member.mutations.member import Mutation as MemberMutation

from post.queries.comment import Query as CommentQuery
from post.queries.reaction import Query as ReactionQuery
from post.queries.review import Query as ReviewQuery
from post.mutations.comment import Mutation as CommentMutation
from post.mutations.reaction import Mutation as ReactionMutation
from post.mutations.review import Mutation as ReviewMutation


class Query(HospitalQuery, ReservationQuery, VaccineQuery,
            MemberQuery,
            CommentQuery, ReactionQuery, ReviewQuery,
            graphene.ObjectType):
    pass


class Mutation(MemberMutation,
               CommentMutation, ReactionMutation, ReviewMutation,
               graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
