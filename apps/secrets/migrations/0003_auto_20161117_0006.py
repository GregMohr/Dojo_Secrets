# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginreg', '0002_auto_20161115_1100'),
        ('secrets', '0002_secret_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='secret',
            name='likes',
        ),
        migrations.AddField(
            model_name='secret',
            name='like_users',
            field=models.ManyToManyField(related_name='user_likes', to='loginreg.User'),
        ),
    ]
