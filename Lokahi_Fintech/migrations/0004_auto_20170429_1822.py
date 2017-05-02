# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0003_message_unread'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(default=None, blank=True, null=True),
        ),
    ]
