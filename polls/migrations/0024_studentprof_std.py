# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-13 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0023_studentprof_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprof',
            name='std',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
