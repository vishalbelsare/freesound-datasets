# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-19 13:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0033_auto_20170919_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='is_trustable',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='is_trustable',
        ),
    ]
