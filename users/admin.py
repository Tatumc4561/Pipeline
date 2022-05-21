from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import *


# Remove fields from User, AuthorAdmin page


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = "users"


class FollowingInline(admin.StackedInline):
    model = Following
    fk_name = "user_follower"
    verbose_name_plural = "people I am following"


class FollowerInline(admin.StackedInline):
    model = Following
    fk_name = "target_following"
    verbose_name_plural = "my followers"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (
        CustomUserInline,
        FollowingInline,
        FollowerInline,
    )


# Re-register UserAdmin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Following)
