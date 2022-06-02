from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib.contenttypes.admin import GenericTabularInline

from threads.models import Thread

from .models import *


# Remove fields from User, AuthorAdmin page


# Define an inline admin descriptor for Customuser model
# which adds all the fields to current user model
class CustomUserInline(admin.StackedInline):
    model = CustomUser
    can_delete = False
    verbose_name_plural = "users"


class FollowingInline(admin.TabularInline):
    model = Following
    fk_name = "user_follower"
    verbose_name_plural = "people I am following"
    extra = 0  # remove extra empty fields


class FollowerInline(admin.TabularInline):
    model = Following
    fk_name = "target_following"
    verbose_name_plural = "my followers"
    extra = 0  # remove extra empty fields


class JoinGroupInline(admin.TabularInline):
    model = JoinGroup
    fk_name = "join_group"
    verbose_name_plural = "my groups"
    extra = 0  # remove extra empty fields


# add Field
class ThreadGroupInline(admin.TabularInline):
    model = Thread
    extra = 0  # remove extra empty fields


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (
        CustomUserInline,
        FollowingInline,
        FollowerInline,
        JoinGroupInline,
        ThreadGroupInline,
    )


# add Field
class TargetGroupInline(admin.TabularInline):
    model = JoinGroup
    fk_name = "target_group"
    extra = 0  # remove extra empty fields


# add Fields to Channel
class ChannelAdmin(admin.ModelAdmin):
    inlines = (TargetGroupInline, ThreadGroupInline)


# Re-register UserAdmin

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Following)
admin.site.register(Channel, ChannelAdmin)
admin.site.register(JoinGroup)
