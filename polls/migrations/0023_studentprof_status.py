# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-12 07:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0022_dictation'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprof',
            name='status',
            field=models.TextField(blank=True, null=True),
        ),
    ]
