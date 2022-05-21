# Generated by Django 4.0.3 on 2022-05-21 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_myfollowings_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='my_followers',
        ),
        migrations.AddField(
            model_name='customuser',
            name='my_followers',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_followers', to='users.myfollowings'),
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='my_followings',
        ),
        migrations.AddField(
            model_name='customuser',
            name='my_followings',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_followings', to='users.myfollowings'),
        ),
    ]
