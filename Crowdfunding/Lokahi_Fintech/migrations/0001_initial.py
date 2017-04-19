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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, blank=True, null=True, default=None)),
                ('encrypted', models.BooleanField(default=False)),
                ('file', models.FileField(upload_to='documents')),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100, blank=True, null=True, default=None)),
                ('encrypted', models.BooleanField(default=False)),
                ('filename', models.FileField(upload_to='documents')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100, default='')),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
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
                ('date', models.CharField(max_length=200, default=datetime.date.today)),
                ('title', models.CharField(max_length=100, default='')),
                ('Company', models.CharField(max_length=60)),
                ('Industry', models.CharField(max_length=60)),
                ('private', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='report',
            field=models.ForeignKey(null=True, to='Lokahi_Fintech.Report'),
        ),
    ]
