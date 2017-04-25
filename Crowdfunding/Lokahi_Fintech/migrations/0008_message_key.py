# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0007_message_to_encrypt'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='key',
            field=models.CharField(null=True, max_length=10000, blank=True),
        ),
    ]
