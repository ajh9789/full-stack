# Generated by Django 4.2.5 on 2023-09-13 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_user', '0005_user_post_liked'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='post_liked',
            new_name='posts_liked',
        ),
    ]
