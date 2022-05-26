from django.contrib import admin
from .models import *

from treebeard.admin import TreeAdmin

# Register your models here.


class ThreadCommentAdmin(TreeAdmin):
    list_display = ("parent_thread", "user", "likes", "created")
    list_filter = ["user", "created", "likes"]


admin.site.register(ThreadComment, ThreadCommentAdmin)


admin.site.register(Thread)
