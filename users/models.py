from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default="sun.png", upload_to="avatars", null=True)
    friends = models.ManyToManyField(User, blank=True, related_name="friends")


class Friend_Request(models.Model):
    from_username = models.ForeignKey(
        User, related_name="from_user", on_delete=models.CASCADE
    )
    to_username = models.ForeignKey(
        User, related_name="to_user", on_delete=models.CASCADE
    )
