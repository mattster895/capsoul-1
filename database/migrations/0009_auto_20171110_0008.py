# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 00:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20171103_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
