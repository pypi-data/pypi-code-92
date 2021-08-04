# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-12-14 10:47
from __future__ import unicode_literals

import django.db.models.deletion
import enumfields.fields
import filer.fields.image
from django.conf import settings
from django.db import migrations, models

import shuup.front.apps.carousel.models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='is_arrows_visible',
            field=models.BooleanField(default=True, help_text='When checked, navigational arrows are shown on the carousel allowing for customers to go back and forward.', verbose_name='show navigation arrows'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='name',
            field=models.CharField(help_text='The carousel name use for carousel configuration.', max_length=50, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='pause_on_hover',
            field=models.BooleanField(default=True, help_text='When checked, the carousel cycling pauses on mouse over.', verbose_name='pause on hover'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='use_dot_navigation',
            field=models.BooleanField(default=True, help_text='When checked, navigational indicator dots are shown.', verbose_name='show navigation dots'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='available_from',
            field=models.DateTimeField(blank=True, help_text='Set the date and time from which this slide should be visible in the carousel. This is useful to advertise sales campaigns or other time-sensitive marketing.', null=True, verbose_name='available from'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='available_to',
            field=models.DateTimeField(blank=True, help_text='Set the date and time from which this slide should be visible in the carousel. This is useful to advertise sales campaigns or other time-sensitive marketing.', null=True, verbose_name='available to'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='category_link',
            field=models.ForeignKey(blank=True, help_text='Set the product category page that should be shown when this slide is clicked, if any.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shuup.Category', verbose_name='category link'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='cms_page_link',
            field=models.ForeignKey(blank=True, help_text='Set the web page that should be shown when the slide is clicked, if any.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shuup_simple_cms.Page', verbose_name='cms page link'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='ordering',
            field=models.IntegerField(blank=True, default=0, help_text='Set the numeric order in which this slide should appear relative to other slides in this carousel.', null=True, verbose_name='ordering'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='product_link',
            field=models.ForeignKey(blank=True, help_text='Set the product detail page that should be shown when this slide is clicked, if any.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shuup.Product', verbose_name='product link'),
        ),
        migrations.AlterField(
            model_name='slide',
            name='target',
            field=enumfields.fields.EnumIntegerField(default=0, enum=shuup.front.apps.carousel.models.LinkTargetType, help_text='Set this to current if clicking on this slide should open a new browser tab.', verbose_name='link target'),
        ),
        migrations.AlterField(
            model_name='slidetranslation',
            name='caption',
            field=models.CharField(blank=True, help_text='Text that describes the image. Used for search engine purposes.', max_length=80, null=True, verbose_name='caption'),
        ),
        migrations.AlterField(
            model_name='slidetranslation',
            name='external_link',
            field=models.CharField(blank=True, help_text='Set the external site that should be shown when this slide is clicked, if any.', max_length=160, null=True, verbose_name='external link'),
        ),
        migrations.AlterField(
            model_name='slidetranslation',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, help_text='The slide image to show.', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='filer.Image', verbose_name='image'),
        ),
    ]
