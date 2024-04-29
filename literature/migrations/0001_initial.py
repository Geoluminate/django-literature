# Generated by Django 4.2.9 on 2024-01-29 20:15

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import literature.utils
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="Collection",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("name", models.CharField(max_length=255, verbose_name="name")),
                ("description", models.TextField(verbose_name="description")),
            ],
            options={
                "verbose_name": "collection",
                "verbose_name_plural": "collections",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Literature",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified", models.DateTimeField(auto_now=True, verbose_name="modified")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("article", "article"),
                            ("article-journal", "journal article"),
                            ("article-magazine", "magazine article"),
                            ("article-newspaper", "newspaper article"),
                            ("bill", "bill"),
                            ("book", "book"),
                            ("broadcast", "broadcast"),
                            ("chapter", "chapter"),
                            ("dataset", "dataset"),
                            ("entry", "entry"),
                            ("entry-dictionary", "entry (dictionary)"),
                            ("entry-encyclopedia", "entry (encyclopedia)"),
                            ("figure", "figure"),
                            ("graphic", "graphic"),
                            ("interview", "interview"),
                            ("legal_case", "legal case"),
                            ("legislation", "legislation"),
                            ("manuscript", "manuscript"),
                            ("map", "map"),
                            ("motion_picture", "motion picture"),
                            ("musical_score", "musical score"),
                            ("pamphlet", "pamphlet"),
                            ("paper-conference", "paper conference"),
                            ("patent", "patent"),
                            ("personal_communication", "personal communication"),
                            ("post", "post"),
                            ("post-weblog", "blog post"),
                            ("report", "report"),
                            ("review", "review"),
                            ("review-book", "review book"),
                            ("song", "song"),
                            ("speech", "speech"),
                            ("thesis", "thesis"),
                            ("treaty", "treaty"),
                            ("webpage", "webpage"),
                        ],
                        max_length=255,
                        verbose_name="type",
                    ),
                ),
                (
                    "title",
                    models.TextField(
                        blank=True, help_text="Primary title of the item.", null=True, verbose_name="title"
                    ),
                ),
                ("abstract", models.TextField(blank=True, null=True, verbose_name="abstract")),
                (
                    "container_title",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Title of the container holding the item (e.g. the book title for a book chapter, the"
                            " journal title for a journal article; the album title for a recording; the session title"
                            " for multi-part presentation at a conference)."
                        ),
                        max_length=512,
                        null=True,
                        verbose_name="container title",
                    ),
                ),
                (
                    "pdf",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to=literature.utils.pdf_file_renamer,
                        validators=[django.core.validators.FileExtensionValidator(["pdf"])],
                        verbose_name="PDF",
                    ),
                ),
                (
                    "published",
                    models.DateField(
                        blank=True,
                        max_length=255,
                        null=True,
                        validators=[django.core.validators.MaxValueValidator(datetime.date.today)],
                        verbose_name="date published",
                    ),
                ),
                ("CSL", models.JSONField(blank=True, verbose_name="Citation Style Language")),
                (
                    "collections",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Add the entry to a collection.",
                        to="literature.collection",
                        verbose_name="collection",
                    ),
                ),
                (
                    "keyword",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="Keyword(s) or tag(s) attached to the item.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="key words",
                    ),
                ),
            ],
            options={
                "verbose_name": "literature",
                "verbose_name_plural": "literature",
                "ordering": ["created"],
                "default_related_name": "literature",
            },
        ),
        migrations.CreateModel(
            name="SupplementaryMaterial",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("file", models.FileField(upload_to="", verbose_name="file")),
                (
                    "literature",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="supplementary",
                        to="literature.literature",
                        verbose_name="literature",
                    ),
                ),
            ],
            options={
                "verbose_name": "supplementary material",
                "verbose_name_plural": "supplementary material",
            },
        ),
    ]