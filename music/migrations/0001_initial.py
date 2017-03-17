# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-16 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Release title')),
                ('title_uk', models.CharField(max_length=200, null=True, verbose_name='Release title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='Release title')),
                ('title_de', models.CharField(max_length=200, null=True, verbose_name='Release title')),
                ('title_pl', models.CharField(max_length=200, null=True, verbose_name='Release title')),
                ('kind', models.CharField(max_length=200, verbose_name='Release type - Album, Single, EP etc.')),
                ('kind_uk', models.CharField(max_length=200, null=True, verbose_name='Release type - Album, Single, EP etc.')),
                ('kind_en', models.CharField(max_length=200, null=True, verbose_name='Release type - Album, Single, EP etc.')),
                ('kind_de', models.CharField(max_length=200, null=True, verbose_name='Release type - Album, Single, EP etc.')),
                ('kind_pl', models.CharField(max_length=200, null=True, verbose_name='Release type - Album, Single, EP etc.')),
                ('notes', models.TextField(verbose_name='Release notes')),
                ('notes_uk', models.TextField(null=True, verbose_name='Release notes')),
                ('notes_en', models.TextField(null=True, verbose_name='Release notes')),
                ('notes_de', models.TextField(null=True, verbose_name='Release notes')),
                ('notes_pl', models.TextField(null=True, verbose_name='Release notes')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Album cover')),
                ('release_date', models.DateField(verbose_name='Release Date')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='Published, date')),
            ],
            options={
                'verbose_name_plural': 'Albums',
                'verbose_name': 'Album',
            },
        ),
    ]