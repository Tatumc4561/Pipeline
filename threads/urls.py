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
]
