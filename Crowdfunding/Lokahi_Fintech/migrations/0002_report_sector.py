# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-26 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='sector',
            field=models.CharField(default='', max_length=60),
        ),
    ]
