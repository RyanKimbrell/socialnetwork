# Generated by Django 3.0.8 on 2020-09-04 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_follower_like_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='following',
        ),
        migrations.AddField(
            model_name='user',
            name='following',
            field=models.ManyToManyField(related_name='followers', to='network.Follower'),
        ),
    ]