import graphene

from django.core.exceptions import ValidationError

from post.models.review import Review
from post.mutations.inputs import CreateReviewInput, UpdateReviewInput, DestroyReviewInput
from post.schemas import ReviewType

from utils.decorators import login_required


class CreateReviewMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        create_review_data = CreateReviewInput(required=True)

    success = graphene.Boolean()
    review = graphene.Field(ReviewType)

    @classmethod
    @login_required
    def mutate(cls, root, info, token, create_review_data):
        user_obj = info.context.user
        create_review_data['user'] = user_obj

        review_obj = Review.objects.create(**create_review_data)

        return cls(success=True, review=review_obj)


class UpdateReviewMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        update_review_data = UpdateReviewInput(required=True)

    success = graphene.Boolean()

    @classmethod
    @login_required
    def mutate(cls, root, info, token, update_review_data):
        review_uid = update_review_data.pop('review_uid')
        review_obj = Review.objects.filter(uid=review_uid)

        if review_obj.exists():
            review_obj.update(**update_review_data)
        else:
            raise ValidationError('Review not found')

        return cls(success=True)


class DestroyReviewMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        destroy_review_data = DestroyReviewInput(required=True)

    success = graphene.Boolean()

    @classmethod
    @login_required
    def mutate(cls, root, info, token, destroy_review_data):
        review_uid = destroy_review_data['review_uid']
        review_obj = Review.objects.get(uid=review_uid)
        review_obj.delete()

        return cls(success=True)


class Mutation(graphene.ObjectType):
    create_review = CreateReviewMutation.Field()
    update_review = UpdateReviewMutation.Field()
    destroy_review = DestroyReviewMutation.Field()
