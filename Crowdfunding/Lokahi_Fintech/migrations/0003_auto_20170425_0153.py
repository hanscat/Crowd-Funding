# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0002_auto_20170425_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='filename',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
    ]
