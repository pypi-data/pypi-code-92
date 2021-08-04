# Generated by Django 2.2.18 on 2021-04-27 13:10

import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup', '0085_longer_order_line_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='max_choices',
            field=models.PositiveIntegerField(default=1, help_text='Maximum amount of choices that user can choose from existing options. This field has affect only for choices type.', verbose_name='max choices'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='min_choices',
            field=models.PositiveIntegerField(default=0, help_text='Minimum amount of choices that user can choose from existing options. This field has affect only for choices type.', verbose_name='min choices'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='ordering',
            field=models.IntegerField(default=0, help_text='The ordering in which your attribute will be displayed.'),
        ),
        migrations.CreateModel(
            name='AttributeChoiceOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='shuup.Attribute', verbose_name='attribute')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.AddField(
            model_name='productattribute',
            name='chosen_options',
            field=models.ManyToManyField(to='shuup.AttributeChoiceOption', verbose_name='chosen options'),
        ),
        migrations.CreateModel(
            name='AttributeChoiceOptionTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(help_text='The attribute choice option name. ', max_length=256, verbose_name='name')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='shuup.AttributeChoiceOption')),
            ],
            options={
                'verbose_name': 'attribute choice option Translation',
                'db_table': 'shuup_attributechoiceoption_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
