# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0004_auto_20170429_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='encryptionKey',
            new_name='FileKey',
        ),
        migrations.AddField(
            model_name='file',
            name='report_id',
            field=models.CharField(max_length=10, default=''),
        ),
        migrations.AddField(
            model_name='report',
            name='ceo',
            field=models.CharField(max_length=60, default=''),
        ),
    ]
