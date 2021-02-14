import graphene

from django.core.exceptions import ValidationError

from post.models.comment import Comment
from post.models.review import Review
from post.mutations.inputs import CreateCommentInput, UpdateCommentInput, DestroyCommentInput
from post.schemas import CommentType

from utils.decorators import login_required


class CreateCommentMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        create_comment_data = CreateCommentInput(required=True)

    success = graphene.Boolean()
    comment = graphene.Field(CommentType)

    @classmethod
    @login_required
    def mutate(cls, root, info, token, create_comment_data):
        user_obj = info.context.user
        try:
            review_obj = Review.objects.get(uid=create_comment_data['review_uid'])
        except Review.DoesNotExist:
            raise ValidationError('Review not found')
        create_comment_data['user'] = user_obj
        create_comment_data['review'] = review_obj

        comment_obj = Comment.objects.create(**create_comment_data)

        return cls(succes=True, comment=comment_obj)


class UpdateCommentMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        update_comment_data = UpdateCommentInput(required=True)

    success = graphene.Boolean()

    @classmethod
    @login_required
    def mutate(cls, root, info, token, update_comment_data):
        comment_uid = update_comment_data.pop('comment_uid')
        comment_obj = Comment.objects.filter(uid=comment_uid)

        if comment_obj.is_exists():
            comment_obj[0].update(**update_comment_data)
        else:
            raise ValidationError('Comment not found')

        return cls(success=True)


class DestroyCommentMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        destroy_comment_data = DestroyCommentInput(required=True)

    success = graphene.Boolean()

    @classmethod
    @login_required
    def mutate(cls, root, info, token, destroy_comment_data):
        comment_uid = destroy_comment_data['comment_uid']
        try:
            comment_obj = Comment.objects.get(uid=comment_uid)
        except Comment.DoesNotExist:
            raise ValidationError('Comment not found')

        comment_obj.delete()

        return cls(success=True)


class Mutation(graphene.ObjectType):
    create_comment = CreateCommentMutation.Field()
    update_comment = UpdateCommentMutation.Field()
    destroy_comment = DestroyCommentMutation.Field()
