# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 18:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_delete_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilestatus',
            old_name='pro',
            new_name='owner',
        ),
    ]
