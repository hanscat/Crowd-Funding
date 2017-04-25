# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, blank=True, null=True, default=None)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, default='')),
                ('encrypted', models.BooleanField(default=False)),
                ('encryptionKey', models.CharField(max_length=100, blank=True, default='')),
                ('filename', models.FileField(blank=True, upload_to='documents')),
            ],
            options={
                'db_table': 'file',
            },
        ),
        migrations.CreateModel(
            name='Group1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100, default='')),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'groups1',
            },
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('msg_content', models.CharField(max_length=1000)),
                ('receiver', models.ForeignKey(related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sender', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('role', models.CharField(max_length=20, choices=[('C', 'Company'), ('I', 'Investor'), ('N/A', 'not declared')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('owner', models.CharField(max_length=60, default='')),
                ('date', models.CharField(max_length=200, default=datetime.date.today)),
                ('title', models.CharField(max_length=100, default='')),
                ('company', models.CharField(max_length=60, default='')),
                ('phone', models.CharField(max_length=12, default='')),
                ('location', models.CharField(max_length=60, default='')),
                ('country', models.CharField(max_length=60, default='')),
                ('industry', models.CharField(max_length=60, default='')),
                ('projects', models.TextField(default='')),
                ('private', models.BooleanField()),
                ('files', models.ManyToManyField(blank=True, to='Lokahi_Fintech.File')),
            ],
            options={
                'db_table': 'report',
            },
        ),
        migrations.AddField(
            model_name='file',
            name='reports',
            field=models.ForeignKey(null=True, to='Lokahi_Fintech.Report'),
        ),
        migrations.AddField(
            model_name='document',
            name='report',
            field=models.ForeignKey(null=True, to='Lokahi_Fintech.Report'),
        ),
    ]
