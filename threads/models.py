from django.db import models
from users.models import *
from django.contrib.auth.models import Group, User

import datetime
from django import template
from django.conf import settings


register = template.Library()


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

    def posted_date(self):
        """Takes in Thread published date and calculates the hours/days in between then and the current time
        Returns:
            str: hours/days
        """
        current = str(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

        post_date_year = str(self.published_date.year)
        post_date_month = str(self.published_date.month)
        post_date_day = str(self.published_date.day)
        post_date_hour = str(self.published_date.hour)
        post_date_minute = str(self.published_date.minute)
        post_date_second = str(self.published_date.second)

        post_date = f"{post_date_year}-{post_date_month}-{post_date_day} {post_date_hour}:{post_date_minute}:{post_date_second}"

        date_format_str = "%Y-%m-%d %H:%M:%S"

        start = datetime.datetime.strptime(current, date_format_str)
        end = datetime.datetime.strptime(post_date, date_format_str)

        # Get interval between two timstamps
        diff = start - end
        # Get interval between two timstamps in minutes
        difference = diff.total_seconds() / 60
        ans = f"{round(difference)} minutes ago"
        if difference >= 60:
            # Get interval between two timstamps in hours
            difference = diff.total_seconds() / 3600
            ans = f"{round(difference)} hours ago"
            if difference >= 48:
                # Get interval between two timstamps in days
                difference = diff.total_seconds() / 86400
                ans = f"{round(difference)} days ago"

        return f"{ans}"

    def __str__(self):
        return f"{self.user}: {self.group} | {self.title} - {self.published_date} "
