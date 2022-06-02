from django.contrib import admin
from .models import *

from treebeard.admin import TreeAdmin

# Register your models here.


class ThreadAdmin(TreeAdmin):
    # how it is displayed in admin panel
    list_display = ("path", "title", "group", "user", "likes", "created")
    # filter options
    list_filter = ["title", "group", "user", "created", "likes"]


# register Thread_Comment adding in ThreadCommentAdmin
admin.site.register(Thread, ThreadAdmin)
