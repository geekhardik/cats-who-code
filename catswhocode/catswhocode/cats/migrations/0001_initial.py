# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 05:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_last_updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('photo', models.ImageField(upload_to='photos')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('likes', models.PositiveSmallIntegerField(default=0)),
                ('attribution', models.CharField(blank=True, max_length=255)),
                ('approved', models.BooleanField(default=True)),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='members.Member')),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
    ]
