# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0010_auto_20170425_0630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='key',
            field=models.BinaryField(null=True, max_length=10000, blank=True),
        ),
    ]
