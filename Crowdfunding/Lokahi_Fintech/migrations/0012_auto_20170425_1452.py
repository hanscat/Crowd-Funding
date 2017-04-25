# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0011_auto_20170425_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='key',
            field=models.TextField(blank=True, max_length=10000, null=True),
        ),
    ]
