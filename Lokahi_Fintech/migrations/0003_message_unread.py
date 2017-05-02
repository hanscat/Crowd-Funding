# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0002_profile_unread_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='unread',
            field=models.BooleanField(default=True),
        ),
    ]
