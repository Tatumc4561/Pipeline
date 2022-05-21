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


class FollowersInline(admin.StackedInline):
    model = Followers
    fk_name = "follower"


class FollowingInline(admin.StackedInline):
    model = Following
    fk_name = "following"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (
        CustomUserInline,
        FollowersInline,
        FollowingInline,
    )


# Re-register UserAdmin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Following)
admin.site.register(Followers)
