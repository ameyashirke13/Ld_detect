# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-03 10:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_document_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='username',
        ),
    ]
