# Generated by Django 4.0.4 on 2022-05-17 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, default='media/images/avatars/mario.jpg', upload_to='avatars'),
        ),
    ]
