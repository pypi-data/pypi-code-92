# Generated by Django 3.2.6 on 2021-08-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128)),
                ('slug', models.SlugField(unique=True)),
                ('sql', models.TextField(blank=True)),
                ('notes', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Query',
                'verbose_name_plural': 'Queries',
                'abstract': False,
            },
        ),
    ]
