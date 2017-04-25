# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0008_message_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='key',
            field=models.TextField(max_length=10000, blank=True, null=True),
        ),
    ]
