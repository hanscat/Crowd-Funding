# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Lokahi_Fintech', '0003_auto_20170423_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content', models.TextField()),
                ('time', models.DateField()),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='receiver')),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='sender')),
            ],
        ),
    ]
