# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(null=True, blank=True, max_length=100, default=None)),
                ('encrypted', models.BooleanField(default=False)),
                ('file', models.FileField(upload_to='documents')),
            ],
            options={
                'db_table': 'document',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('encrypted', models.NullBooleanField(default=False)),
                ('encryptionKey', models.CharField(blank=True, max_length=100, default='')),
                ('file', models.FileField(blank=True, upload_to='Lokahi_Fintech/static/documents/')),
                ('actualurl', models.TextField(default='')),
            ],
            options={
                'db_table': 'file',
            },
        ),
        migrations.CreateModel(
            name='Group1',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'groups1',
            },
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=500)),
                ('time', models.DateField(null=True, blank=True, default=None)),
                ('to_encrypt', models.BooleanField(default=False)),
                ('key', models.TextField(null=True, blank=True, max_length=10000)),
                ('receiver', models.ForeignKey(related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(null=True, related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_investor', models.BooleanField(default=False)),
                ('company', models.CharField(null=True, max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, default='')),
                ('company', models.CharField(max_length=60, default='')),
                ('owner', models.CharField(max_length=60, default='')),
                ('phone', models.CharField(max_length=12, default='')),
                ('location', models.CharField(max_length=60, default='')),
                ('country', models.CharField(max_length=60, default='')),
                ('industry', models.CharField(max_length=60, default='')),
                ('sector', models.CharField(max_length=60, default='')),
                ('projects', models.TextField(default='')),
                ('created_at', models.DateTimeField(verbose_name='Date Created', default=datetime.datetime.now)),
                ('encryptionKey', models.CharField(blank=True, max_length=100, default='')),
                ('is_private', models.NullBooleanField(default=False)),
                ('is_encrypted', models.NullBooleanField(default=False)),
                ('files', models.ManyToManyField(to='Lokahi_Fintech.File', default='none')),
            ],
            options={
                'db_table': 'report',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='report',
            field=models.ForeignKey(null=True, to='Lokahi_Fintech.Report'),
        ),
    ]
