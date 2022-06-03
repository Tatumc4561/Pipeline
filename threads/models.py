from django.db import models
from django.contrib.auth.models import User, Group
from users.models import Channel
import datetime
from django import template
from django.conf import settings

# Materialized Path tree
from treebeard.mp_tree import MP_Node
import datetime


# Pagination Template tags
register = template.Library()


# Create your models here.
class Thread(MP_Node):

    # User posts
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post")
    group = models.ForeignKey(
        Channel, on_delete=models.CASCADE, related_name="group_threads"
    )
    title = models.CharField(max_length=120, blank=True)
    text = models.CharField(max_length=400)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    created = models.DateTimeField(default=datetime.datetime.now)
    image = models.ImageField(upload_to="post_images", null=True, blank=True)

    # def posted_date(self):
    #     """Takes in Thread published date and calculates the hours/days in between then and the current time
    #     Returns:
    #         str: hours/days
    #     """
    #     current = str(datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"))

    #     post_date_year = str(self.created.year)
    #     post_date_month = str(self.created.month)
    #     post_date_day = str(self.created.day)
    #     post_date_hour = str(self.created.hour)
    #     post_date_minute = str(self.created.minute)
    #     post_date_second = str(self.created.second)

    #     post_date = f"{post_date_year}-{post_date_month}-{post_date_day} {post_date_hour}:{post_date_minute}:{post_date_second}"

    #     date_format_str = "%Y-%m-%d %H:%M:%S"

    #     start = datetime.datetime.strptime(current, date_format_str)
    #     end = datetime.datetime.strptime(post_date, date_format_str)

    #     # Get interval between two timstamps
    #     diff = start - end
    #     # Get interval between two timstamps in minutes
    #     difference = diff.total_seconds() / 60
    #     ans = f"{round(difference)} minutes ago"
    #     if difference >= 60:
    #         # Get interval between two timstamps in hours
    #         difference = diff.total_seconds() / 3600
    #         ans = f"{round(difference)} hours ago"
    #         if difference >= 48:
    #             # Get interval between two timstamps in days
    #             difference = diff.total_seconds() / 86400
    #             ans = f"{round(difference)} days ago"

    #     return f"{ans}"
    node_order_by = ["title", "likes", "group"]

    def __str__(self):
        return f"{self.path} - {self.title} {self.text}"
