# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-24 16:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20170120_2136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Familia Perkalaba news', 'verbose_name_plural': 'Familia Perkalaba news'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='brief_title',
        ),
    ]