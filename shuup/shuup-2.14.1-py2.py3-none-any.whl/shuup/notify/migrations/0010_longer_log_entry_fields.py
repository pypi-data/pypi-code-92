# Generated by Django 2.2.17 on 2021-01-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_notify', '0009_move_body_template_to_email_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scriptlogentry',
            name='identifier',
            field=models.CharField(blank=True, db_index=True, max_length=256, verbose_name='identifier'),
        ),
        migrations.AlterField(
            model_name='scriptlogentry',
            name='message',
            field=models.CharField(max_length=1024, verbose_name='message'),
        ),
    ]
