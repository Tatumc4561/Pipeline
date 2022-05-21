# Generated by Django 4.0.3 on 2022-05-21 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_customuser_my_followers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='my_followers',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_followers', to='users.myfollowings'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='my_followings',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_followings', to='users.myfollowings'),
        ),
    ]