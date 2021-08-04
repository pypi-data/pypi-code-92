# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-24 01:18
from __future__ import unicode_literals

import django.db.models.deletion
import enumfields.fields
import jsonfield.fields
from django.conf import settings
from django.db import migrations, models
from enumfields import Enum

import shuup.simple_cms.models
import shuup.utils.analog


class NullEnum(Enum):
    NULL = 0


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shuup_simple_cms', '0006_add_shop_constraints'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageLogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('identifier', models.CharField(blank=True, max_length=64, verbose_name='identifier')),
                ('kind', enumfields.fields.EnumIntegerField(default=0, enum=shuup.utils.analog.LogEntryKind, verbose_name='log entry kind')),
                ('extra', jsonfield.fields.JSONField(blank=True, null=True, verbose_name='extra data')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='page',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='deleted'),
        ),
        migrations.AddField(
            model_name='page',
            name='page_type',
            field=enumfields.fields.EnumIntegerField(db_index=True, default=0, enum=NullEnum, verbose_name='page type'),
        ),
        migrations.AddField(
            model_name='pagelogentry',
            name='target',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_entries', to='shuup_simple_cms.Page', verbose_name='target'),
        ),
        migrations.AddField(
            model_name='pagelogentry',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]
