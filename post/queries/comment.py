import graphene

from django.core.exceptions import ValidationError

from post.models.comment import Comment
from post.schemas import CommentType

from utils.decorators import login_required


class Query(graphene.ObjectType):
    get_comment_list = graphene.List(CommentType, token=graphene.String(required=True),
                                     review_uid=graphene.UUID(required=True))
    get_comment_detail = graphene.Field(CommentType, token=graphene.String(required=True),
                                        comment_uid=graphene.UUID(required=True))

    @classmethod
    @login_required
    def resolve_get_comment_list(cls, root, info, token, review_uid):
        return Comment.objects.filter(review__uid=review_uid)

    @classmethod
    @login_required
    def resolve_get_comment_detail(cls, root, info, token, comment_uid):
        try:
            return Comment.objects.get(uid=comment_uid)
        except Comment.DoesNotExist:
            raise ValidationError('Comment not found')