# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-03 21:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0029_merge_20171201_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='capsule',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comment',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='letter',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='media',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]