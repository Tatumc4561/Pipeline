# Generated by Django 4.0.4 on 2022-05-17 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='mario.jpg', null=True, upload_to='avatars'),
        ),
    ]