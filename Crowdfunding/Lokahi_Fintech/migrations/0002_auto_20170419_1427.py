# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Lokahi_Fintech', '0001_initial'),
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
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100, default='')),
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
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('role', models.CharField(max_length=20, choices=[('C', 'Company'), ('I', 'Investor'), ('N/A', 'not declared')])),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='Company_Location',
            new_name='Company',
        ),
        migrations.RemoveField(
            model_name='report',
            name='Company_name',
        ),
        migrations.RemoveField(
            model_name='report',
            name='Company_phone',
        ),
        migrations.RemoveField(
            model_name='report',
            name='current_projects',
        ),
        migrations.RemoveField(
            model_name='report',
            name='file',
        ),
        migrations.RemoveField(
            model_name='report',
            name='sector',
        ),
        migrations.RemoveField(
            model_name='report',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.CharField(max_length=200, default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='report',
            name='title',
            field=models.CharField(max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='report',
            name='encrypted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='group',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
