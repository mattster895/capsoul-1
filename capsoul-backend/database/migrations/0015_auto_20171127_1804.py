# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-27 18:04
from __future__ import unicode_literals

import database.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_auto_20171127_0611'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letters',
            fields=[
                ('lid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('title', models.CharField(default='', max_length=255)),
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.FileField(blank=True, upload_to=database.models._upload_path)),
            ],
        ),
        migrations.AlterField(
            model_name='capsule',
            name='contributors',
            field=models.ManyToManyField(related_name='capsule_contributors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='letter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='letters', to='database.Letters'),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='media',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='media', to='database.Media'),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='capsule_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='recipients',
            field=models.ManyToManyField(related_name='capsule_recipients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='capsule',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AddField(
            model_name='media',
            name='cid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cid_of_media', to='database.Capsule'),
        ),
        migrations.AddField(
            model_name='media',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='media_owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='letters',
            name='cid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cid_of_letter', to='database.Capsule'),
        ),
        migrations.AddField(
            model_name='letters',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='letter_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]