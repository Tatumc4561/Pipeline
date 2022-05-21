from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    followers = models.ManyToManyField(
        "Followers", blank=True, related_name="user_followers", symmetrical=False
    )
    following = models.ManyToManyField(
        "Following", blank=True, related_name="user_followings", symmetrical=False
    )


class Following(models.Model):
    following = models.ForeignKey(
        User, related_name="following", on_delete=models.CASCADE
    )


class Followers(models.Model):
    follower = models.ForeignKey(
        User, related_name="follower", on_delete=models.CASCADE
    )
