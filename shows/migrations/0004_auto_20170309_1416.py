# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-09 14:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_auto_20170309_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Published, date'),
        ),
    ]
