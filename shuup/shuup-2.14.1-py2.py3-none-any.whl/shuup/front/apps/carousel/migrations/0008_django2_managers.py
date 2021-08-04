# Generated by Django 2.2.14 on 2020-07-23 08:48

import django.db.models.deletion
import parler.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0007_rename_available_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slidetranslation',
            name='master',
            field=parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='carousel.Slide'),
        ),
    ]
