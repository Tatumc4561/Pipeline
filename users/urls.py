from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("profile/<str:userID>", views.user_profile, name="profile"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("logout/", views.user_logout, name="logout"),
    path("update/", views.user_update, name="user_update"),
    # -------friend requests-------
    path(
        "follow/<str:userID>",
        views.follow_user,
        name="follow_user",
    ),
    # --------public profile -------------
    path(
        "pub_profile/<str:userID>",
        views.user_public_profile,
        name="public_profile",
    ),
    # ---------Group Page -----------------
    path(
        "groups/<str:groupID>",
        views.group_page,
        name="group_page",
    ),
    path("register_group/", views.group_register, name="group_register"),
    path(
        "join/<str:groupID>",
        views.join_group,
        name="join_group",
    ),
]
