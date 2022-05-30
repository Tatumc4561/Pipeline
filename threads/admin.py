from django.contrib import admin
from .models import *

from treebeard.admin import TreeAdmin

# Register your models here.


class ThreadCommentAdmin(TreeAdmin):
    # how it is displayed in admin panel
    list_display = ("path", "title", "user", "likes", "created")
    # filter options
    list_filter = ["title", "user", "created", "likes"]


# register Thread_Comment adding in ThreadCommentAdmin
admin.site.register(Thread, ThreadCommentAdmin)
