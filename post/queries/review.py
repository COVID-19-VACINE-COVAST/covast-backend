import graphene

from django.core.exceptions import ValidationError

from post.models.review import Review
from post.schemas import ReviewType

from utils.decorators import login_required


class Query(graphene.ObjectType):
    get_review_list = graphene.List(ReviewType, token=graphene.String(required=True))
    get_review_detail = graphene.Field(ReviewType, token=graphene.String(required=True),
                                       review_uid=graphene.UUID(required=True))
    get_my_review_list = graphene.List(ReviewType, token=graphene.String(required=True))

    @classmethod
    @login_required
    def resolve_get_review_list(cls, root, info, token):
        return Review.objects.all()

    @classmethod
    @login_required
    def resolve_get_review_detail(cls, root, info, token, review_uid):
        try:
            return Review.objects.get(uid=review_uid)
        except Review.DoesNotExist:
            raise ValidationError('Review not found')

    @classmethod
    @login_required
    def resolve_get_my_review_list(cls, root, info, token):
        user_obj = info.context.user
        return Review.objects.filter(user=user_obj)
