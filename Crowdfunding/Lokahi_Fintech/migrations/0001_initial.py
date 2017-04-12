# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('Company_name', models.CharField(max_length=60)),
                ('Company_phone', models.CharField(max_length=12)),
                ('Company_Location', models.CharField(max_length=60)),
                ('sector', models.CharField(max_length=60)),
                ('Industry', models.CharField(max_length=60)),
                ('current_projects', models.TextField()),
                ('file', models.FileField(upload_to='', blank=True)),
                ('encrypted', models.BooleanField()),
                ('private', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
