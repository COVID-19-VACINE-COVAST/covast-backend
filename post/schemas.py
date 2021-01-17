from graphene_django.types import DjangoObjectType

from post.models.comment import Comment
from post.models.reaction import Reaction
from post.models.review import Review


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ('user', 'review', 'uid', 'contents', 'like', 'unlike', )


class ReactionType(DjangoObjectType):
    class Meta:
        model = Reaction
        fields = ('user', 'review', 'comment', 'kind', )


class ReviewType(DjangoObjectType):
    class Meta:
        model = Review
        fields = ('user', 'uid', 'vaccine_kind', 'contents', 'like', 'unlike', )
