# Generated by Django 4.0.4 on 2022-05-17 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='avatars/mario.jpg', null=True, upload_to='avatars'),
        ),
    ]
