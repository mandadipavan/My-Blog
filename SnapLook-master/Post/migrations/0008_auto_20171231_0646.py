# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-31 06:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0007_auto_20171231_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 31, 6, 46, 1, 590006, tzinfo=utc)),
        ),
    ]
