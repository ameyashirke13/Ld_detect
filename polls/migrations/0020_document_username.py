# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-03 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_remove_document_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='username',
            field=models.TextField(blank=True, null=True),
        ),
    ]