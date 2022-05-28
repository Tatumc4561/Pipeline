from django.urls import path
from . import views


app_name = "threads"

urlpatterns = [
    path("", views.index, name="index"),
    # -------post creation---------
    path("createthread/", views.create_thread, name="create_thread"),
    path("submit/", views.submit_thread, name="submit_thread"),
    path("delete/<int:thread_id>", views.delete_thread, name="delete_thread"),
    path("like/<int:thread_id>", views.like_thread, name="like_thread"),
    path("dislike/<int:thread_id>", views.dislike_thread, name="dislike_thread"),
    # ----------pub profile ------------
    # path("publike/<int:thread_id>", views.publike_thread, name="publike_thread"),
    # -----------post commenting ---------------------
    path("read_thread/<int:thread_id>", views.read_thread, name="read_thread"),
    path("comment/<int:thread_id>", views.comment_thread, name="comment_thread"),
    path(
        "commenthhh/<int:thread_id>",
        views.comment_thread_child,
        name="comment_thread_child",
    ),
    path("like-/<int:item_id>", views.like_comment, name="like_comment"),
    path("dislike-/<int:item_id>", views.dislike_comment, name="dislike_comment"),
]
