from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars", blank=True)

    # symetrical, one may be following the other
    my_followers = models.OneToOneField(
        "MyFollowings",
        blank=True,
        related_name="user_followers",
        on_delete=models.CASCADE,
    )

    # symetrical, one may be following the other
    my_followings = models.OneToOneField(
        "MyFollowings",
        blank=True,
        related_name="user_followings",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"{self.user}"


class MyFollowings(models.Model):
    follower = models.ForeignKey(
        User, related_name="user_followers", on_delete=models.CASCADE, null=True
    )

    following = models.ForeignKey(
        User, related_name="user_followings", on_delete=models.CASCADE, null=True
    )

    class Meta:
        unique_together = ("follower", "following")

    def __str__(self):
        return f"{self.follower} follows {self.following}"


# class MyFollowers(models.Model):
#     follower = models.ForeignKey(
#         User, related_name="user_followers", on_delete=models.CASCADE, null=True
#     )

#     def __str__(self):
#         return f"{self.follow}"
