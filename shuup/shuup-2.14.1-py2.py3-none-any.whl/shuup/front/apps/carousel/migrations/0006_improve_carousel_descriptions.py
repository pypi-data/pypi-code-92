# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-11-20 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0005_alter-external-url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slidetranslation',
            name='caption',
            field=models.CharField(blank=True, help_text="Text that describes the image. It is displayed on top of the image if 'Render image text' box is enabled in front-end. Also used for search engine purposes.", max_length=80, null=True, verbose_name='caption'),
        ),
        migrations.AlterField(
            model_name='slidetranslation',
            name='caption_text',
            field=models.TextField(blank=True, help_text="Caption text is displayed as secondary text on top of the image if 'Render image text' box is enabled in front-end for 'Carousel plugin' type (disabled for 'Banner box' type). It is also shown as a tooltip.", null=True, verbose_name='caption text'),
        ),
    ]
