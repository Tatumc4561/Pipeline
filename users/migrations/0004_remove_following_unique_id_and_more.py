# Generated by Django 4.0.3 on 2022-05-21 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_following_unique_followers_and_more'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='following',
            name='unique_id',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='my_followers',
            field=models.ManyToManyField(related_name='user_followers', through='users.Following', to='users.customuser'),
        ),
        migrations.AddConstraint(
            model_name='following',
            constraint=models.UniqueConstraint(fields=('id', 'user_follower', 'target_following'), name='unique_id'),
        ),
    ]
