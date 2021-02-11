import graphene

from django.core.exceptions import ValidationError

from post.models.reaction import Reaction
from post.schemas import ReactionType

from utils.decorators import login_required


class Query(graphene.ObjectType):
    get_reaction_list = graphene.List(ReactionType, token=graphene.String(required=True), review_uid=graphene.UUID(),
                                      comment_uid=graphene.UUID())
    get_reaction_detail = graphene.Field(Reaction, token=graphene.String(required=True),
                                         reaction_uid=graphene.UUID(required=True))
    get_like_reaction_list = graphene.List(ReactionType, token=graphene.String(required=True), review_uid=graphene.UUID(),
                                           comment_uid=graphene.UUID())
    get_unlike_reaction_list = graphene.List(ReactionType, token=graphene.String(required=True), review_uid=graphene.UUID(),
                                             comment_uid=graphene.UUID())

    @classmethod
    @login_required
    def resolve_get_reaction_list(cls, root, info, token, review_uid=None, comment_uid=None):
        if review_uid:
            return Reaction.objects.filter(review__uid=review_uid)
        elif comment_uid:
            return Reaction.objects.filter(comment__uid=comment_uid)
        else:
            raise ValidationError('ReviewUid or CommentUid is required')

    @classmethod
    @login_required
    def resolve_get_reaction_detail(cls, root, info, token, reaction_uid):
        try:
            return Reaction.objects.get(uid=reaction_uid)
        except Reaction.DoesNotExist:
            raise ValidationError('Reaction not found')

    @classmethod
    @login_required
    def resolve_get_like_reaction_list(cls, root, info, token, review_uid=None, comment_uid=None):
        if review_uid:
            return Reaction.objects.filter(review__uid=review_uid, kind=1)
        elif comment_uid:
            return Reaction.objects.filter(comment__uid=comment_uid, kind=1)
        else:
            raise ValidationError('ReviewUid or CommentUid is required')

    @classmethod
    @login_required
    def resolve_get_unlike_reaction_list(cls, root, info, token, review_uid=None, comment_uid=None):
        if review_uid:
            return Reaction.objects.filter(review__uid=review_uid, kind=0)
        elif comment_uid:
            return Reaction.objects.filter(comment__uid=comment_uid, kind=0)
        else:
            raise ValidationError('ReviewUid or CommentUid is required')
