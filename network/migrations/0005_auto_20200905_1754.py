# Generated by Django 3.0.8 on 2020-09-05 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_follower_following'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='following',
            new_name='followee',
        ),
    ]
