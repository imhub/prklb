# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-02 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20170201_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Заголовок'),
        ),
    ]