from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars", blank=True)
    my_followers = models.ManyToManyField(
        to="self",
        through="Following",
        related_name="user_followers",
        symmetrical=False,
    )


class Following(models.Model):
    user_follower = models.ForeignKey(
        User, related_name="follower", on_delete=models.CASCADE, default=None
    )
    target_following = models.ForeignKey(
        User, related_name="followings", on_delete=models.CASCADE
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                name="unique_follow", fields=["user_follower", "target_following"]
            ),
            models.CheckConstraint(
                name="check_unique",
                check=~models.Q(user_follower=models.F("target_following")),
            ),
        ]
