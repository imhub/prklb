# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-22 22:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0011_auto_20170323_0040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='albumlinks',
            name='album',
        ),
        migrations.DeleteModel(
            name='AlbumLinks',
        ),
    ]
