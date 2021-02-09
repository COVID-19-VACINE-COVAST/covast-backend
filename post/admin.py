from django.contrib import admin

from post.models.comment import Comment
from post.models.reaction import Reaction
from post.models.review import Review


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Reaction)
class ReactionAdmin(admin.ModelAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass
