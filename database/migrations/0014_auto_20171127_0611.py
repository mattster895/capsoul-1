# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 06:11
from __future__ import unicode_literals

import database.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_merge_20171121_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capsule',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='capsule',
            name='letters',
        ),
        migrations.RemoveField(
            model_name='capsule',
            name='contributors',
        ),
        migrations.AddField(
            model_name='capsule',
            name='contributors',
            field=models.ManyToManyField(related_name='contributors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='media',
            field=models.FileField(blank=True, upload_to=database.models._upload_path),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='capsule',
            name='recipients',
        ),
        migrations.AddField(
            model_name='capsule',
            name='recipients',
            field=models.ManyToManyField(related_name='recipients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, upload_to=database.models._upload_path),
        ),
    ]