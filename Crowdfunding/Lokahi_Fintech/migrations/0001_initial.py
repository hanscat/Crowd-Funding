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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(default=None, null=True, max_length=100, blank=True)),
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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('encrypted', models.BooleanField(default=False)),
                ('encryptionKey', models.CharField(default='', blank=True, max_length=100)),
                ('filename', models.FileField(blank=True, upload_to='documents')),
            ],
            options={
                'db_table': 'file',
            },
        ),
        migrations.CreateModel(
            name='Group1',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('owner', models.CharField(default='', max_length=100)),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'groups1',
            },
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('content', models.TextField(max_length=500)),
                ('time', models.DateField(null=True, default=None, blank=True)),
                ('to_encrypt', models.BooleanField(default=False)),
                ('key', models.TextField(null=True, max_length=10000, blank=True)),
                ('receiver', models.ForeignKey(related_name='receiver', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(related_name='sender', null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('role', models.CharField(choices=[('C', 'Company'), ('I', 'Investor'), ('N/A', 'not declared')], max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('owner', models.CharField(default='', max_length=60)),
                ('date', models.CharField(default=datetime.date.today, max_length=200)),
                ('title', models.CharField(default='', max_length=100)),
                ('company', models.CharField(default='', max_length=60)),
                ('phone', models.CharField(default='', max_length=12)),
                ('location', models.CharField(default='', max_length=60)),
                ('country', models.CharField(default='', max_length=60)),
                ('industry', models.CharField(default='', max_length=60)),
                ('projects', models.TextField(default='')),
                ('private', models.BooleanField()),
                ('files', models.ManyToManyField(to='Lokahi_Fintech.File', blank=True)),
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
