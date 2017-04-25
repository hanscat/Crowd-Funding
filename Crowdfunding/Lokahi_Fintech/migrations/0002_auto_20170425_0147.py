# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='encryptionKey',
            field=models.CharField(max_length=100, blank=True, default=''),
        ),
        migrations.AddField(
            model_name='file',
            name='reports',
            field=models.ManyToManyField(to='Lokahi_Fintech.Report'),
        ),
        migrations.AlterField(
            model_name='file',
            name='name',
            field=models.CharField(max_length=100, default=''),
        ),
    ]
