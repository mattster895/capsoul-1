# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 04:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0024_auto_20171128_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_verified',
            field=models.BooleanField(default=False, verbose_name='verified'),
        ),
    ]