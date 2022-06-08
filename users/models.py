from django.db import models
from django.contrib.auth.models import User


# from groups.models import *
# from threads.models import Thread


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(
        upload_to="avatars", blank=True, default="images/mario_mushroom.png"
    )
    my_followers = models.ManyToManyField(
        "self",
        through="Following",
        related_name="user_followers",
        symmetrical=False,
        blank=False,
    )
    my_groups = models.ManyToManyField(
        "self",
        through="JoinGroup",
        related_name="my_user_groups",
        symmetrical=False,
        blank=False,
    )


class Following(models.Model):
    user_follower = models.ForeignKey(
        User, related_name="follower", on_delete=models.CASCADE
    )
    target_following = models.ForeignKey(
        User, related_name="followings", on_delete=models.CASCADE
    )

    class Meta:
        # setup unique relationship
        constraints = [
            models.UniqueConstraint(
                name="unique_follow", fields=["user_follower", "target_following"]
            ),
            # check value of unique relationship
            models.CheckConstraint(
                name="check_unique",
                check=~models.Q(user_follower=models.F("target_following")),
            ),
        ]


class Channel(models.Model):
    # channel name
    name = models.CharField(max_length=120, null=True)
    # associated threads

    threads = models.ManyToManyField(
        "self",
        through="threads.Thread",
        related_name="channel_threads",
        symmetrical=False,
        blank=False,
    )
    # group mascot

    avatar = models.ImageField(upload_to="group_avatars", blank=True)
    group_users = models.ManyToManyField(
        User,
        through="JoinGroup",
        related_name="group_members",
        symmetrical=False,
        blank=False,
    )

    def member_names(self):
        a = Channel.objects.get(name=self)

        members = []
        for x in a.group_users.all():
            members.append(x)
        return members

    def member_count(self):
        z = Channel.objects.get(name=self)

        y = z.group_users.count()
        if y > 1:
            return f"{y} members"
        else:
            return f"{y} member"

    def __str__(self):
        return f"{self.name}"


class JoinGroup(models.Model):
    join_group = models.ForeignKey(
        User, related_name="join_a_group", on_delete=models.CASCADE
    )
    target_group = models.ForeignKey(
        Channel, related_name="add_to_group", on_delete=models.CASCADE
    )

    class Meta:
        # setup unique relationship
        constraints = [
            models.UniqueConstraint(
                name="unique_togroup", fields=["join_group", "target_group"]
            ),
            # check value of unique relationship
            models.CheckConstraint(
                name="check_group",
                check=~models.Q(join_group=models.F("target_group")),
            ),
        ]


# manage.py migrate [-h] [--noinput] [--database DATABASE] [--fake] [--fake-initial] [--plan] [--run-syncdb] [--check] [--version] [-v {0,1,2,3}] [--settings SETTINGS] [--pythonpath PYTHONPATH] [--traceback]
#                          [--no-color] [--force-color] [--skip-checks]
#                          [app_label] [migration_name]
