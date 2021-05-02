import graphene

from django.core.exceptions import ValidationError
from django.db import transaction
from django.db.models import F

from post.models.review import Review
from post.models.comment import Comment
from post.models.reaction import Reaction
from post.mutations.inputs import CreateReactionInput, UpdateReactionInput, DestroyReactionInput
from post.schemas import ReactionType

from utils.decorators import login_required


class CreateReactionMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        create_reaction_data = CreateReactionInput(required=True)

    success = graphene.Boolean()
    reaction = graphene.Field(ReactionType)

    @classmethod
    @login_required
    def mutate(cls, root, info, token, **input):
        user_obj = info.context.user
        create_reaction_data = input['create_reaction_data']

        try:
            with transaction.atomic():
                if create_reaction_data.get('review'):
                    review_obj = Review.objects.get(uid=create_reaction_data['review'])
                    create_reaction_data['review'] = review_obj
                elif create_reaction_data.get('comment'):
                    comment_obj = Comment.objects.get(uid=create_reaction_data['comment'])
                    create_reaction_data['comment'] = comment_obj
                else:
                    raise ValidationError('ReviewUid or CommentUid is required')

                create_reaction_data['user'] = user_obj
                reaction_obj = Reaction.objects.create(**create_reaction_data)

                if create_reaction_data.get('review'):
                    if reaction_obj.kind == 0:
                        review_obj.unlike = F('unlike') + 1
                    elif reaction_obj.kind == 1:
                        review_obj.like = F('like') + 1

                    review_obj.save()
                elif create_reaction_data.get('comment'):
                    if reaction_obj.kind == 0:
                        comment_obj.unlike = F('unlike') + 1
                    elif comment_obj.kind == 1:
                        comment_obj.like = F('like') + 1

                    comment_obj.save()

            return cls(success=True, reaction=reaction_obj)
        except Review.DoesNotExist:
            raise ValidationError('Review not found')
        except Comment.DoesNotExist:
            raise ValidationError('Comment not found')
        except Exception as e:
            raise ValidationError(e)


class UpdateReactionMutation(graphene.Mutation):
    class Arguments:
        token = graphene.String(required=True)
        update_reaction_data = UpdateReactionInput(required=True)

    success = graphene.Boolean()

    @classmethod
    @login_required
    def mutate(cls, root, info, token, **input):
        user_obj = info.context.user
        update_reaction_data = input['update_reaction_data']

        try:
            if update_reaction_data.get('review_uid'):
                review_obj = Review.objects.get(uid=update_reaction_data['review_uid'])
                reaction_obj = Reaction.objects.get(review=review_obj, user=user_obj)

                with transaction.atomic():
                    reaction_obj.kind = update_reaction_data['kind']
                    reaction_obj.save()

                    if update_reaction_data['kind'] == 0:
                        review_obj.like = F('like') - 1
                        review_obj.unlike = F('unlike') + 1
                    elif update_reaction_data['kind'] == 1:
                        review_obj.unlike = F('unlike') - 1
                        review_obj.like = F('like') + 1
                    else:
                        raise ValidationError('Kind must be 0 or 1')

                    review_obj.save()
            elif update_reaction_data.get('comment_uid'):
                comment_obj = Comment.objects.get(uid=update_reaction_data['comment_uid'])
                reaction_obj = Reaction.objects.get(comment=comment_obj, user=user_obj)

                with transaction.atomic():
                    reaction_obj.kind = update_reaction_data['kind']
                    reaction_obj.save()

                    if update_reaction_data['kind'] == 0:
                        comment_obj.like = F('like') - 1
                        comment_obj.unlike = F('unlike') + 1
                    elif update_reaction_data['kind'] == 1:
                        comment_obj.unlike = F('unlike') - 1
                        comment_obj.like = F('like') + 1
                    else:
                        raise ValidationError('Kind must be 0 or 1')

                    comment_obj.save()
            else:
                raise ValidationError('ReviewUid or CommentUid is required')

            return cls(success=True)
        except Review.DoesNotExist:
            raise ValidationError('Review not found')
        except Comment.DoesNotExist:
            raise ValidationError('Comment not found')
        except Exception as e:
            raise ValidationError(e)


class Mutation(graphene.ObjectType):
    create_reaction = CreateReactionMutation.Field()
    update_reaction = UpdateReactionMutation.Field()
