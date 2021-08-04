# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-06-19 15:39
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


def forwards_func(apps, schema_editor):
    """
    Convert pages to GDPR user consent documents
    """
    user_consent_document_model = apps.get_model("shuup_gdpr", "GDPRUserConsentDocument")
    gdpr_user_consent_model = apps.get_model("shuup_gdpr", "GDPRUserConsent")
    reversion_version_model = apps.get_model("reversion", "Version")

    for consent in gdpr_user_consent_model.objects.all():
        consents = set()
        for page_id in consent.documents.values_list("id", flat=True):
            version = reversion_version_model.objects.filter(object_id=page_id).first()
            if version:
                doc = user_consent_document_model.objects.create(page_id=page_id, version=version)
                consents.add(doc.id)

        consent.consents = consents


def backwards_func(apps, schema_editor):
    """
    Convert GDPR user consent documents to pages
    """
    gdpr_user_consent_model = apps.get_model("shuup_gdpr", "GDPRUserConsent")

    for consent in gdpr_user_consent_model.objects.all():
        page_ids = set()
        for consent_document in consent.consents.values_list("id", flat=True):
            page_ids.add(consent_document.page.id)

        consent.documents = page_ids


class Migration(migrations.Migration):

    dependencies = [
        ('reversion', '0001_squashed_0004_auto_20160611_1202'),
        ('shuup_simple_cms', '0007_gdpr'),
        ('shuup_gdpr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GDPRUserConsentDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shuup_simple_cms.Page')),
                ('version', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reversion.Version')),
            ],
        ),
        migrations.AlterModelOptions(
            name='gdprcookiecategory',
            options={'verbose_name': 'GDPR cookie category', 'verbose_name_plural': 'GDPR cookie categories'},
        ),
        migrations.AlterModelOptions(
            name='gdprcookiecategorytranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'GDPR cookie category Translation'},
        ),
        migrations.AlterModelOptions(
            name='gdprsettings',
            options={'verbose_name': 'GDPR settings', 'verbose_name_plural': 'GDPR settings'},
        ),
        migrations.AlterModelOptions(
            name='gdprsettingstranslation',
            options={'default_permissions': (), 'managed': True, 'verbose_name': 'GDPR settings Translation'},
        ),
        migrations.AlterModelOptions(
            name='gdpruserconsent',
            options={'verbose_name': 'GDPR user consent', 'verbose_name_plural': 'GDPR user consents'},
        ),
        migrations.AddField(
            model_name='gdpruserconsent',
            name='consents',
            field=models.ManyToManyField(
                blank=True, editable=False, to='shuup_gdpr.GDPRUserConsentDocument', verbose_name='consent documents'
            )
        ),
        migrations.RunPython(forwards_func, backwards_func),
        migrations.RemoveField(
            model_name='gdpruserconsent',
            name='documents',
        )
    ]
