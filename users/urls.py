from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("profile/", views.user_profile, name="profile"),
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("logout/", views.user_logout, name="logout"),
    # -------friend requests-------
    path(
        "follow/<str:userID>",
        views.follow_user,
        name="follow_user",
    ),
    # --------public profile -------------,
    path(
        "profile/<str:userID>",
        views.user_public_profile,
        name="public_profile",
    ),
]
