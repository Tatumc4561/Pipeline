from django.db import models
from users.models import *
from django.contrib.auth.models import Group, User


# Create your models here.
class Thread(models.Model):
    # user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post")
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="group_post"
    )
    title = models.CharField(max_length=120)
    text = models.CharField(max_length=400)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="post_images", null=True, blank=True)

    def __str__(self):
        return f"{self.user}: {self.group} | {self.title} - {self.published_date} "
