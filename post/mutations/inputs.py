import graphene

from post.models.comment import Comment
from post.models.reaction import Reaction


class CreateReviewInput(graphene.InputObjectType):
    vaccine_kind = graphene.String(required=True)
    contents = graphene.String(required=True)


class UpdateReviewInput(graphene.InputObjectType):
    review_uid = graphene.UUID(required=True)
    vaccine_kind = graphene.String()
    contents = graphene.String()


class DestroyReviewInput(graphene.InputObjectType):
    review_uid = graphene.UUID(required=True)


class CreateCommentInput(graphene.InputObjectType):
    review_uid = graphene.UUID(required=True)
    contents = graphene.String(required=True)


class UpdateCommentInput(graphene.InputObjectType):
    comment_uid = graphene.UUID(required=True)
    contents = graphene.String(required=True)


class DestroyCommentInput(graphene.InputObjectType):
    comment_uid = graphene.UUID(required=True)


class CreateReactionInput(graphene.InputObjectType):
    review = graphene.UUID()
    comment = graphene.UUID()
    kind = graphene.Int(required=True)


class UpdateReactionInput(graphene.InputObjectType):
    review_uid = graphene.UUID()
    comment_uid = graphene.UUID()
    kind = graphene.Int(required=True)


class DestroyReactionInput(graphene.InputObjectType):
    review_uid = graphene.UUID()
    comment_uid = graphene.UUID()
