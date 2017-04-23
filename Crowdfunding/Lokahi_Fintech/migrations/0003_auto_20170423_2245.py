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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(blank=True, default=None, max_length=100, null=True)),
                ('encrypted', models.BooleanField(default=False)),
                ('filename', models.FileField(upload_to='documents')),
            ],
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.DeleteModel(
            name='Investor',
        ),
        migrations.RemoveField(
            model_name='report',
            name='encrypted',
        ),
        migrations.AddField(
            model_name='file',
            name='report',
            field=models.ForeignKey(to='Lokahi_Fintech.Report', null=True),
        ),
    ]
