# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0006_auto_20170424_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='to_encrypt',
            field=models.BooleanField(default=False),
        ),
    ]
