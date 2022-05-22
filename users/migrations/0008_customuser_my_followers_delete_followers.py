# Generated by Django 4.0.3 on 2022-05-21 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_customuser_my_followers_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='my_followers',
            field=models.ManyToManyField(related_name='user_followers', through='users.Following', to='users.customuser'),
        ),
        migrations.DeleteModel(
            name='Followers',
        ),
    ]