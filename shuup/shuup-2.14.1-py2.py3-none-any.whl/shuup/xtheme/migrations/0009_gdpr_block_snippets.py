# Generated by Django 2.2.24 on 2021-07-06 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_xtheme', '0008_longer_log_entry_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='name',
            field=models.CharField(default='Untitled', max_length=50, verbose_name='snippet name'),
        ),
    ]
