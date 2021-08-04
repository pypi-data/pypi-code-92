# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-24 21:27
from __future__ import unicode_literals

import django.db.models.deletion
import parler.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shuup_simple_cms', '0007_gdpr'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shuup', '0044_add_media'),
    ]

    operations = [
        migrations.CreateModel(
            name='GDPRCookieCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('always_active', models.BooleanField(default=False, verbose_name='always active')),
                ('cookies', models.TextField(help_text='Comma separated list of cookies names, prefix or suffix that will be included in this category, e.g. _ga, mysession, user_c_', verbose_name='cookies used')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gdpr_cookie_categories', to='shuup.Shop')),
            ],
            options={
                'verbose_name': 'gdpr cookie category',
                'verbose_name_plural': 'gdpr cookie categories',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GDPRCookieCategoryTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('how_is_used', models.TextField(blank=True, help_text='Describe the purpose of this category of cookies and how it is used.', verbose_name='how we use')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup_gdpr.GDPRCookieCategory')),
            ],
            options={
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'gdpr cookie category Translation',
                'managed': True,
                'db_table': 'shuup_gdpr_gdprcookiecategory_translation',
            },
        ),
        migrations.CreateModel(
            name='GDPRSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False, help_text='Define if the GDPR is active.', verbose_name='enabled')),
                ('shop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gdpr_settings', to='shuup.Shop')),
            ],
            options={
                'verbose_name': 'gdpr settings',
                'verbose_name_plural': 'gdpr settings',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='GDPRSettingsTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('cookie_banner_content', models.TextField(blank=True, help_text='The text to be presented to users in a pop-up warning.', verbose_name='cookie banner content')),
                ('cookie_privacy_excerpt', models.TextField(blank=True, help_text='The summary text to be presented about cookie privacy.', verbose_name='cookie privacy excerpt')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup_gdpr.GDPRSettings')),
            ],
            options={
                'db_tablespace': '',
                'default_permissions': (),
                'verbose_name': 'gdpr settings Translation',
                'managed': True,
                'db_table': 'shuup_gdpr_gdprsettings_translation',
            },
        ),
        migrations.CreateModel(
            name='GDPRUserConsent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='created on', db_index=True)),
                ('documents', models.ManyToManyField(blank=True, editable=False, to='shuup_simple_cms.Page', verbose_name='consent documents')),
                ('shop', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='gdpr_consents', to='shuup.Shop')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='gdpr_consents', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'gdpr user consent',
                'verbose_name_plural': 'gdpr user consents',
            },
        ),
        migrations.AlterUniqueTogether(
            name='gdprsettingstranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='gdprcookiecategorytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]
