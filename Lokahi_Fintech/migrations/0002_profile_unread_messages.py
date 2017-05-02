# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='unread_messages',
            field=models.IntegerField(default=0),
        ),
    ]
