# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lokahi_Fintech', '0002_auto_20170419_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, blank=True, null=True, default=None)),
                ('encrypted', models.BooleanField(default=False)),
                ('filename', models.FileField(upload_to='documents')),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='encrypted',
        ),
        migrations.AddField(
            model_name='file',
            name='report',
            field=models.ForeignKey(null=True, to='Lokahi_Fintech.Report'),
        ),
    ]
