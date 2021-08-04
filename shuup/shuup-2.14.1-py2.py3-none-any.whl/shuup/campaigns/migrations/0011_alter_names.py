# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-14 10:47
from __future__ import unicode_literals

import django.core.validators
import django.db.models.deletion
import re
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0010_hourbasketcondition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketcampaign',
            name='active',
            field=models.BooleanField(default=False, help_text='Check this if the campaign is currently active. Please also set a start and end date.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='basketcampaign',
            name='end_datetime',
            field=models.DateTimeField(blank=True, help_text='The date and time the campaign ends. This is only applicable if the campaign is marked as active.', null=True, verbose_name='end date and time'),
        ),
        migrations.AlterField(
            model_name='basketcampaign',
            name='shop',
            field=models.ForeignKey(help_text='The shop where the campaign is active.', on_delete=django.db.models.deletion.CASCADE, to='shuup.Shop', verbose_name='shop'),
        ),
        migrations.AlterField(
            model_name='basketcampaign',
            name='start_datetime',
            field=models.DateTimeField(blank=True, help_text='The date and time the campaign starts. This is only applicable if the campaign is marked as active.', null=True, verbose_name='start date and time'),
        ),
        migrations.AlterField(
            model_name='basketcampaigntranslation',
            name='public_name',
            field=models.CharField(help_text='The campaign name to show in the store front.', max_length=120, verbose_name='public name'),
        ),
        migrations.AlterField(
            model_name='catalogcampaign',
            name='active',
            field=models.BooleanField(default=False, help_text='Check this if the campaign is currently active. Please also set a start and end date.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='catalogcampaign',
            name='end_datetime',
            field=models.DateTimeField(blank=True, help_text='The date and time the campaign ends. This is only applicable if the campaign is marked as active.', null=True, verbose_name='end date and time'),
        ),
        migrations.AlterField(
            model_name='catalogcampaign',
            name='shop',
            field=models.ForeignKey(help_text='The shop where the campaign is active.', on_delete=django.db.models.deletion.CASCADE, to='shuup.Shop', verbose_name='shop'),
        ),
        migrations.AlterField(
            model_name='catalogcampaign',
            name='start_datetime',
            field=models.DateTimeField(blank=True, help_text='The date and time the campaign starts. This is only applicable if the campaign is marked as active.', null=True, verbose_name='start date and time'),
        ),
        migrations.AlterField(
            model_name='catalogcampaigntranslation',
            name='public_name',
            field=models.CharField(blank=True, help_text='The campaign name to show in the store front.', max_length=120),
        ),
        migrations.AlterField(
            model_name='categoryproductsbasketcondition',
            name='categories',
            field=models.ManyToManyField(related_name='_categoryproductsbasketcondition_categories_+', to='shuup.Category', verbose_name='categories'),
        ),
        migrations.AlterField(
            model_name='categoryproductsbasketcondition',
            name='excluded_categories',
            field=models.ManyToManyField(blank=True, help_text="If the customer has even a single product in the basket from these categories this rule won't match thus the campaign cannot be applied to the basket.", related_name='_categoryproductsbasketcondition_excluded_categories_+', to='shuup.Category', verbose_name='excluded categories'),
        ),
        migrations.AlterField(
            model_name='hourbasketcondition',
            name='days',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')], verbose_name='days'),
        ),
        migrations.AlterField(
            model_name='hourbasketcondition',
            name='hour_end',
            field=models.TimeField(
                verbose_name='end time',
                help_text=(
                    '12pm is considered noon and 12am as midnight. '
                    'End time is not considered match.')),
        ),
        migrations.AlterField(
            model_name='hourbasketcondition',
            name='hour_start',
            field=models.TimeField(
                verbose_name='start time',
                help_text='12pm is considered noon and 12am as midnight.'),
        ),
        migrations.AlterField(
            model_name='hourcondition',
            name='days',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')], verbose_name='days'),
        ),
        migrations.AlterField(
            model_name='hourcondition',
            name='hour_end',
            field=models.TimeField(
                verbose_name='end time',
                help_text=(
                    '12pm is considered noon and 12am as midnight. '
                    'End time is not considered match.')),
        ),
        migrations.AlterField(
            model_name='hourcondition',
            name='hour_start',
            field=models.TimeField(
                verbose_name='start time',
                help_text='12pm is considered noon and 12am as midnight.'),
        ),
    ]
