# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 08:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secrets', '0003_auto_20161117_0006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secret',
            old_name='userkey',
            new_name='secret_user',
        ),
    ]
