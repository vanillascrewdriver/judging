# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-14 15:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
