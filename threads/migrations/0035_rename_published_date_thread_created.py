# Generated by Django 4.0.4 on 2022-05-28 01:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('threads', '0034_threadcomment_delete_thread_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='published_date',
            new_name='created',
        ),
    ]
