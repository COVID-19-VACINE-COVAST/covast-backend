from django.contrib import admin

from member.models.token import Token
from member.models.user import User
from member.models.user_profile import UserProfile


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass
