# Generated by Django 3.2.4 on 2021-06-28 15:55

import ckeditor_uploader.fields

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import aa_forum.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="General",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "AA-Forum",
                "permissions": (
                    ("basic_access", "Can access the AA-Forum module"),
                    (
                        "manage_forum",
                        "Can manage the AA-Forum module (Category, topics and messages)",
                    ),
                ),
                "managed": False,
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Board",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=254)),
                (
                    "slug",
                    models.SlugField(allow_unicode=True, max_length=254, unique=True),
                ),
                ("description", models.TextField(blank=True)),
                ("order", models.IntegerField(db_index=True, default=999999)),
            ],
            options={
                "verbose_name": "board",
                "verbose_name_plural": "boards",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=254, unique=True)),
                (
                    "slug",
                    models.SlugField(allow_unicode=True, max_length=254, unique=True),
                ),
                ("is_collapsible", models.BooleanField(default=False)),
                ("order", models.IntegerField(db_index=True, default=999999)),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time_posted", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("time_modified", models.DateTimeField(auto_now=True)),
                ("message", ckeditor_uploader.fields.RichTextUploadingField()),
                ("message_plaintext", models.TextField(blank=True)),
            ],
            options={
                "verbose_name": "message",
                "verbose_name_plural": "messages",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Setting",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("variable", models.CharField(max_length=254, unique=True)),
                ("value", models.TextField()),
            ],
            options={
                "verbose_name": "setting",
                "verbose_name_plural": "settings",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=254)),
                (
                    "slug",
                    models.SlugField(allow_unicode=True, max_length=254, unique=True),
                ),
                ("is_sticky", models.BooleanField(db_index=True, default=False)),
                ("is_locked", models.BooleanField(db_index=True, default=False)),
                (
                    "board",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="topics",
                        to="aa_forum.board",
                    ),
                ),
                (
                    "first_message",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        help_text="Shortcut for better performance",
                        null=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="+",
                        to="aa_forum.message",
                    ),
                ),
                (
                    "last_message",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        help_text="Shortcut for better performance",
                        null=True,
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        related_name="+",
                        to="aa_forum.message",
                    ),
                ),
            ],
            options={
                "verbose_name": "topic",
                "verbose_name_plural": "topics",
                "default_permissions": (),
            },
        ),
        migrations.CreateModel(
            name="PersonalMessage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("time_sent", models.DateTimeField(auto_now_add=True)),
                ("subject", models.CharField(max_length=254)),
                (
                    "slug",
                    models.SlugField(allow_unicode=True, max_length=254, unique=True),
                ),
                ("message", models.TextField(blank=True)),
                ("is_read", models.BooleanField(default=False)),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=models.SET(aa_forum.models.get_sentinel_user),
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=models.SET(aa_forum.models.get_sentinel_user),
                        related_name="+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "personal message",
                "verbose_name_plural": "personal messages",
                "default_permissions": (),
            },
        ),
        migrations.AddField(
            model_name="message",
            name="topic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="aa_forum.topic",
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="user_created",
            field=models.ForeignKey(
                on_delete=models.SET(aa_forum.models.get_sentinel_user),
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="message",
            name="user_updated",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=models.SET(aa_forum.models.get_sentinel_user),
                related_name="+",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.CreateModel(
            name="LastMessageSeen",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message_time", models.DateTimeField()),
                (
                    "topic",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="aa_forum.topic"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "default_permissions": (),
            },
        ),
        migrations.AddField(
            model_name="board",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="boards",
                to="aa_forum.category",
            ),
        ),
        migrations.AddField(
            model_name="board",
            name="first_message",
            field=models.ForeignKey(
                default=None,
                editable=False,
                help_text="Shortcut for better performance",
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="+",
                to="aa_forum.message",
            ),
        ),
        migrations.AddField(
            model_name="board",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                related_name="aa_forum_boards_group_restriction",
                to="auth.Group",
            ),
        ),
        migrations.AddField(
            model_name="board",
            name="last_message",
            field=models.ForeignKey(
                default=None,
                editable=False,
                help_text="Shortcut for better performance",
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="+",
                to="aa_forum.message",
            ),
        ),
        migrations.AddField(
            model_name="board",
            name="parent_board",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="child_boards",
                to="aa_forum.board",
            ),
        ),
        migrations.AddConstraint(
            model_name="topic",
            constraint=models.UniqueConstraint(
                fields=("board", "subject"), name="fpk_topic"
            ),
        ),
        migrations.AddIndex(
            model_name="lastmessageseen",
            index=models.Index(
                fields=["topic", "user", "message_time"],
                name="lastmessageseen_compounded",
            ),
        ),
        migrations.AddConstraint(
            model_name="board",
            constraint=models.UniqueConstraint(
                fields=("category", "name"), name="fpk_board"
            ),
        ),
    ]
