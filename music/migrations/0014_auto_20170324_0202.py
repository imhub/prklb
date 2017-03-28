# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-24 00:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0013_buylinks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buylinks',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buylinks', to='music.Album', verbose_name='album'),
        ),
    ]
