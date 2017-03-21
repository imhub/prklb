# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-20 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20170316_0911'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechRiderArch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archrider', models.FileField(blank=True, null=True, upload_to='', verbose_name='Technical Rider in archive')),
            ],
            options={
                'verbose_name': 'Technical Rider',
                'verbose_name_plural': 'Technical Riders',
            },
        ),
        migrations.CreateModel(
            name='TechRiderImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgrider', models.ImageField(blank=True, upload_to='', verbose_name='TechRider Img')),
            ],
            options={
                'verbose_name': 'Technical Rider Image',
                'verbose_name_plural': 'Technocal Rider Images',
            },
        ),
        migrations.RemoveField(
            model_name='homepageinitialsettings',
            name='rider',
        ),
    ]
