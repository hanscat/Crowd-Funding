# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0005_auto_20170424_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, related_name='sender'),
        ),
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateField(default=None, null=True, blank=True),
        ),
    ]
