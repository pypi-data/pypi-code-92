# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-24 05:43


import simple_history.models

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterprise', '0001_squashed_0092_auto_20200312_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='CornerstoneEnterpriseCustomerConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('active', models.BooleanField(help_text='Is this configuration active?')),
                ('transmission_chunk_size', models.IntegerField(default=500, help_text='The maximum number of data items to transmit to the integrated channel with each request.')),
                ('cornerstone_base_url', models.CharField(blank=True, help_text='The base URL used for API requests to Cornerstone, i.e. https://portalName.csod.com', max_length=255, verbose_name='Cornerstone Base URL')),
                ('enterprise_customer', models.OneToOneField(help_text='Enterprise Customer associated with the configuration.', on_delete=django.db.models.deletion.CASCADE, to='enterprise.EnterpriseCustomer')),
            ],
        ),
        migrations.CreateModel(
            name='CornerstoneGlobalConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('completion_status_api_path', models.CharField(help_text='The API path for making completion POST requests to Cornerstone.', max_length=255, verbose_name='Completion Status API Path')),
                ('oauth_api_path', models.CharField(help_text='The API path for making OAuth-related POST requests to Cornerstone. This will be used to gain the OAuth access token which is required for other API calls.', max_length=255, verbose_name='OAuth API Path')),
                ('changed_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Changed by')),
            ],
        ),
        migrations.CreateModel(
            name='CornerstoneLearnerDataTransmissionAudit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('user_guid', models.CharField(max_length=255)),
                ('enterprise_course_enrollment_id', models.PositiveIntegerField(blank=True, null=True)),
                ('course_id', models.CharField(help_text="The course run's key which is used to uniquely identify the course for Cornerstone.", max_length=255)),
                ('session_token', models.CharField(max_length=255)),
                ('callback_url', models.CharField(max_length=255)),
                ('subdomain', models.CharField(max_length=255)),
                ('course_completed', models.BooleanField(default=False, help_text="The learner's course completion status transmitted to Cornerstone.")),
                ('completed_timestamp', models.DateTimeField(blank=True, help_text='Date time when user completed course', null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('error_message', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cornerstone_transmission_audit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalCornerstoneEnterpriseCustomerConfiguration',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('active', models.BooleanField(help_text='Is this configuration active?')),
                ('transmission_chunk_size', models.IntegerField(default=500, help_text='The maximum number of data items to transmit to the integrated channel with each request.')),
                ('cornerstone_base_url', models.CharField(blank=True, help_text='The base URL used for API requests to Cornerstone, i.e. https://portalName.csod.com', max_length=255, verbose_name='Cornerstone Base URL')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('enterprise_customer', models.ForeignKey(blank=True, db_constraint=False, help_text='Enterprise Customer associated with the configuration.', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='enterprise.EnterpriseCustomer')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical cornerstone enterprise customer configuration',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.AlterUniqueTogether(
            name='cornerstonelearnerdatatransmissionaudit',
            unique_together=set([('user', 'course_id')]),
        ),
    ]
