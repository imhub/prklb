# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20170320_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='techriderarch',
            options={'verbose_name': 'Technical Rider in archive', 'verbose_name_plural': 'Technical Riders in archive'},
        ),
        migrations.AddField(
            model_name='techriderimg',
            name='comment',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Rider Specification'),
        ),
    ]