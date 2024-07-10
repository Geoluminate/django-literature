# Generated by Django 5.0.6 on 2024-06-26 13:49

import django.db.models.deletion
import literature.utils
import partial_date.fields
import sortedm2m.fields
import taggit.managers
from django.db import migrations, models


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
            name="Name",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("family", models.CharField(blank=True, max_length=255, null=True, verbose_name="family name")),
                ("given", models.CharField(blank=True, max_length=255, null=True, verbose_name="given name")),
                ("suffix", models.CharField(blank=True, max_length=255, null=True, verbose_name="suffix")),
                (
                    "dropping_particle",
                    models.CharField(blank=True, max_length=255, null=True, verbose_name="dropping particle"),
                ),
                (
                    "non_dropping_particle",
                    models.CharField(blank=True, max_length=255, null=True, verbose_name="non-dropping particle"),
                ),
                ("literal", models.CharField(blank=True, max_length=255, null=True, verbose_name="literal")),
            ],
            options={
                "verbose_name": "name",
                "verbose_name_plural": "names",
            },
        ),
        migrations.CreateModel(
            name="NameThrough",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("author", "Author"),
                            ("collection_editor", "Collection Editor"),
                            ("composer", "Composer"),
                            ("container_author", "Container Author"),
                            ("editor", "Editor"),
                            ("editorial_director", "Editorial Director"),
                            ("illustrator", "Illustrator"),
                            ("interviewer", "Interviewer"),
                            ("original_author", "Original Author"),
                            ("recipient", "Recipient"),
                            ("translator", "Translator"),
                        ],
                        max_length=18,
                        verbose_name="type",
                    ),
                ),
                ("order", models.PositiveIntegerField(verbose_name="order")),
            ],
            options={
                "verbose_name": "name through",
                "verbose_name_plural": "names through",
                "ordering": ["order"],
            },
        ),
        migrations.CreateModel(
            name="SupplementaryMaterial",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified", models.DateTimeField(auto_now=True, verbose_name="modified")),
                ("file", models.FileField(upload_to=literature.utils.suppfile_upload_path, verbose_name="file")),
            ],
            options={
                "verbose_name": "supplementary material",
                "verbose_name_plural": "supplementary material",
            },
        ),
        migrations.CreateModel(
            name="Literature",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            (
                                "Academic and Professional",
                                [
                                    ("paper-conference", "Conference paper"),
                                    ("dataset", "Dataset"),
                                    ("article-journal", "Journal Article"),
                                    ("report", "Report"),
                                    ("standard", "Standard"),
                                ],
                            ),
                            (
                                "Books and Written Works",
                                [
                                    ("book", "Book"),
                                    ("chapter", "Book chapter"),
                                    ("classic", "Classic work"),
                                    ("collection", "Collection of works"),
                                    ("manuscript", "Manuscript"),
                                    ("thesis", "Thesis"),
                                ],
                            ),
                            (
                                "Legislation and Legal",
                                [
                                    ("bill", "Legislative bill"),
                                    ("hearing", "Congressional hearing"),
                                    ("legal_case", "Legal case"),
                                    ("legislation", "Legislation"),
                                    ("patent", "Patent"),
                                    ("regulation", "Regulation"),
                                    ("treaty", "Treaty"),
                                ],
                            ),
                            (
                                "Media and Communication",
                                [
                                    ("broadcast", "Broadcast"),
                                    ("interview", "Interview"),
                                    ("article-magazine", "Magazine Article"),
                                    ("article-newspaper", "Newspaper Article"),
                                    ("speech", "Speech"),
                                ],
                            ),
                            (
                                "Visual and Creative",
                                [
                                    ("figure", "Figure or illustration"),
                                    ("graphic", "Graphic work"),
                                    ("map", "Map"),
                                    ("motion_picture", "Motion picture"),
                                    ("musical_score", "Musical score"),
                                    ("performance", "Live performance"),
                                    ("software", "Software"),
                                    ("song", "Song"),
                                ],
                            ),
                            (
                                "Periodicals and Reviews",
                                [
                                    ("periodical", "Generic periodical"),
                                    ("review", "Review"),
                                    ("review-book", "Book review"),
                                ],
                            ),
                            (
                                "Digital and Online Content",
                                [("post", "Blog post"), ("post-weblog", "Weblog post"), ("webpage", "Webpage")],
                            ),
                            (
                                "Miscellaneous",
                                [
                                    ("article", "Generic Article"),
                                    ("document", "Generic Document"),
                                    ("entry", "Generic Entry"),
                                    ("entry-dictionary", "Dictionary Entry"),
                                    ("entry-encyclopedia", "Encyclopedia Entry"),
                                    ("event", "Event"),
                                    ("pamphlet", "Pamphlet"),
                                    ("personal_communication", "Personal communication"),
                                ],
                            ),
                        ],
                        max_length=22,
                        verbose_name="type",
                    ),
                ),
                ("abstract", models.TextField(blank=True, null=True, verbose_name="abstract")),
                (
                    "annote",
                    models.TextField(
                        blank=True,
                        help_text=(
                            "Short markup, decoration, or annotation to the item (e.g., to indicate items included in a"
                            " review); For descriptive text (e.g., in an annotated bibliography), use note instead"
                        ),
                        null=True,
                        verbose_name="annotation",
                    ),
                ),
                (
                    "archive",
                    models.CharField(
                        blank=True,
                        help_text="Archive where the item is stored",
                        max_length=255,
                        null=True,
                        verbose_name="archive name",
                    ),
                ),
                (
                    "archive_collection",
                    models.CharField(
                        blank=True,
                        help_text="Collection within the archive where the item is stored",
                        max_length=255,
                        null=True,
                        verbose_name="archive collection",
                    ),
                ),
                (
                    "archive_location",
                    models.CharField(
                        blank=True,
                        help_text="Storage location within an archive (e.g. a box and folder number)",
                        max_length=255,
                        null=True,
                        verbose_name="archive location",
                    ),
                ),
                (
                    "archive_place",
                    models.CharField(
                        blank=True,
                        help_text="Geographic location of the archive",
                        max_length=255,
                        null=True,
                        verbose_name="archive place",
                    ),
                ),
                (
                    "authority",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Issuing or judicial authority (e.g. “USPTO” for a patent, “Fairfax Circuit Court” for a"
                            " legal case)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="authority",
                    ),
                ),
                (
                    "call_number",
                    models.CharField(
                        blank=True,
                        help_text="Used to locate the item within a library",
                        max_length=255,
                        null=True,
                        verbose_name="call number",
                    ),
                ),
                (
                    "chapter_number",
                    models.CharField(
                        blank=True,
                        help_text="Chapter number (e.g. chapter number in a book; track number on an album)",
                        max_length=255,
                        null=True,
                        verbose_name="chapter number",
                    ),
                ),
                (
                    "citation_key",
                    models.CharField(
                        blank=True,
                        help_text="Unique key used to reference the citation in text.",
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="citation key",
                    ),
                ),
                (
                    "collection_number",
                    models.CharField(
                        blank=True,
                        help_text="Identifiying number within the collection",
                        max_length=255,
                        null=True,
                        verbose_name="collection number",
                    ),
                ),
                (
                    "collection_title",
                    models.CharField(
                        blank=True,
                        help_text="Title of the collection holding the item",
                        max_length=255,
                        null=True,
                        verbose_name="collection title",
                    ),
                ),
                (
                    "container_title",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "The title of the larger work that contains the work being cited. E.g. the title of a book,"
                            " journal, website, etc."
                        ),
                        max_length=512,
                        null=True,
                        verbose_name="title",
                    ),
                ),
                (
                    "container_title_short",
                    models.CharField(
                        blank=True,
                        help_text="Short/abbreviated form of the container title",
                        max_length=255,
                        null=True,
                        verbose_name="short title",
                    ),
                ),
                (
                    "custom",
                    models.JSONField(blank=True, default=dict, help_text="Custom fields", verbose_name="custom"),
                ),
                (
                    "DOI",
                    models.CharField(
                        blank=True, help_text="Digital Object Identifier", max_length=255, null=True, verbose_name="DOI"
                    ),
                ),
                (
                    "dimensions",
                    models.CharField(
                        blank=True,
                        help_text="Physical (e.g. size) or temporal (e.g. running time) dimensions of the item",
                        max_length=255,
                        null=True,
                        verbose_name="dimensions",
                    ),
                ),
                (
                    "division",
                    models.CharField(
                        blank=True,
                        help_text="Minor subdivision of a court with a jurisdiction for a legal item",
                        max_length=255,
                        null=True,
                        verbose_name="division",
                    ),
                ),
                (
                    "edition",
                    models.CharField(
                        blank=True,
                        help_text="Edition of the container holding the item",
                        max_length=255,
                        null=True,
                        verbose_name="edition",
                    ),
                ),
                (
                    "event",
                    models.CharField(
                        blank=True,
                        help_text="Deprecated legacy variant of event-title",
                        max_length=255,
                        null=True,
                        verbose_name="event",
                    ),
                ),
                (
                    "event_title",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Name of the event related to the item (e.g. the conference name when citing a conference"
                            " paper; the meeting where presentation was made)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="event title",
                    ),
                ),
                (
                    "event_place",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Geographic location of the event related to the item (e.g. “Amsterdam, The Netherlands”)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="event place",
                    ),
                ),
                (
                    "genre",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Class or sub-type of the item (e.g. “Doctoral dissertation” for a PhD thesis; “NIH"
                            " Publication” for an NIH technical report)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="sub-type",
                    ),
                ),
                (
                    "ISBN",
                    models.CharField(
                        blank=True,
                        help_text="International Standard Book Number",
                        max_length=255,
                        null=True,
                        verbose_name="ISBN",
                    ),
                ),
                (
                    "ISSN",
                    models.CharField(
                        blank=True,
                        help_text="International Standard Serial Number",
                        max_length=255,
                        null=True,
                        verbose_name="ISSN",
                    ),
                ),
                (
                    "issue",
                    models.CharField(
                        blank=True,
                        help_text="Issue number of the item or container holding the item",
                        max_length=255,
                        null=True,
                        verbose_name="issue",
                    ),
                ),
                (
                    "jurisdiction",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Geographic scope of relevance (e.g. “US” for a US patent; the court hearing a legal case)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="jurisdiction",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "The language of the item; Should be entered as an ISO 639-1 two-letter language code (e.g."
                            " “en”, “zh”), optionally with a two-letter locale code (e.g. “de-DE”, “de-AT”)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="language",
                    ),
                ),
                (
                    "license",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "The license information applicable to an item (e.g. the license an article or software is"
                            " released under; the copyright information for an item; the classification status of a"
                            " document)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="license",
                    ),
                ),
                (
                    "locator",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "A cite-specific pinpointer within the item (e.g. a page number within a book, or a volume"
                            " in a multi-volume work)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="locator",
                    ),
                ),
                (
                    "medium",
                    models.CharField(
                        blank=True,
                        help_text="Description of the item’s format or medium (e.g. “CD”, “DVD”, “Album”, etc.)",
                        max_length=255,
                        null=True,
                        verbose_name="medium",
                    ),
                ),
                (
                    "note",
                    models.TextField(
                        blank=True,
                        help_text="Descriptive text or notes about an item (e.g. in an annotated bibliography)",
                        null=True,
                        verbose_name="note",
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        blank=True,
                        help_text="Number identifying the item (e.g. a report number)",
                        max_length=255,
                        null=True,
                        verbose_name="number",
                    ),
                ),
                (
                    "number_of_pages",
                    models.CharField(
                        blank=True,
                        help_text="Total number of pages of the cited item",
                        max_length=255,
                        null=True,
                        verbose_name="number of pages",
                    ),
                ),
                (
                    "number_of_volumes",
                    models.CharField(
                        blank=True,
                        help_text="Total number of volumes in the container holding the item",
                        max_length=255,
                        null=True,
                        verbose_name="total volumes",
                    ),
                ),
                (
                    "original_publisher",
                    models.CharField(
                        blank=True,
                        help_text="Original publisher, for items that have been republished by a different publisher",
                        max_length=255,
                        null=True,
                        verbose_name="publisher name",
                    ),
                ),
                (
                    "original_publisher_place",
                    models.CharField(
                        blank=True,
                        help_text="Geographic location of the original publisher (e.g. “London, UK”)",
                        max_length=255,
                        null=True,
                        verbose_name="original publisher place",
                    ),
                ),
                (
                    "original_title",
                    models.CharField(
                        blank=True,
                        help_text="Title of the original version of the item (e.g. for a translated work)",
                        max_length=255,
                        null=True,
                        verbose_name="original title",
                    ),
                ),
                (
                    "page",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Range of pages the item (e.g. a journal article) covers in a container (e.g. a journal"
                            " issue)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="page range",
                    ),
                ),
                (
                    "page_first",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "First page of the range of pages the item (e.g. a journal article) covers in a container"
                            " (e.g. a journal issue)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="page",
                    ),
                ),
                (
                    "part_number",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Number of the specific part of the item being cited (e.g. part 2 of a journal article);"
                            " Use part-title for the title of the part, if any"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="part number",
                    ),
                ),
                (
                    "part_title",
                    models.CharField(
                        blank=True,
                        help_text="Title of the part of the item being cited (e.g. “Introduction” for a book chapter)",
                        max_length=255,
                        null=True,
                        verbose_name="part title",
                    ),
                ),
                (
                    "PMCID",
                    models.CharField(
                        blank=True, help_text="PubMed Central ID", max_length=255, null=True, verbose_name="PMCID"
                    ),
                ),
                (
                    "PMID",
                    models.CharField(blank=True, help_text="PubMed ID", max_length=255, null=True, verbose_name="PMID"),
                ),
                (
                    "printing_number",
                    models.CharField(
                        blank=True,
                        help_text="Printing number of the item or container holding the item",
                        max_length=255,
                        null=True,
                        verbose_name="printing number",
                    ),
                ),
                ("publisher", models.CharField(blank=True, max_length=255, null=True, verbose_name="publisher name")),
                (
                    "publisher_place",
                    models.CharField(
                        blank=True,
                        help_text="Geographic location of the publisher",
                        max_length=255,
                        null=True,
                        verbose_name="publisher place",
                    ),
                ),
                (
                    "references",
                    models.TextField(
                        blank=True,
                        help_text=(
                            "Resources related to the procedural history of a legal case or legislation; Can also be"
                            " used to refer to the procedural history of other items (e.g. “Conference canceled” for a"
                            " presentation accepted as a conference that was subsequently canceled; details of a"
                            " retraction or correction notice)"
                        ),
                        null=True,
                        verbose_name="references",
                    ),
                ),
                (
                    "reviewed_genre",
                    models.CharField(
                        blank=True,
                        help_text="Type of the item being reviewed by the current item (e.g. book, film)",
                        max_length=255,
                        null=True,
                        verbose_name="reviewed genre",
                    ),
                ),
                (
                    "reviewed_title",
                    models.CharField(
                        blank=True,
                        help_text="Title of the item being reviewed by the current item",
                        max_length=255,
                        null=True,
                        verbose_name="reviewed title",
                    ),
                ),
                (
                    "scale",
                    models.CharField(
                        blank=True,
                        help_text="Scale of the item (e.g. “1:100,000” for a map)",
                        max_length=255,
                        null=True,
                        verbose_name="scale",
                    ),
                ),
                (
                    "section",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Section of the item or container holding the item (e.g. “§2.0.1” for a law; “politics” for"
                            " a newspaper article)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="section",
                    ),
                ),
                (
                    "source",
                    models.CharField(
                        blank=True,
                        help_text="Source from whence the item originates (e.g. a library catalog or database)",
                        max_length=255,
                        null=True,
                        verbose_name="source",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Publication status of the item (e.g. “forthcoming”; “in press”; “advance online"
                            " publication”; “retracted”)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="status",
                    ),
                ),
                (
                    "supplement_number",
                    models.CharField(
                        blank=True,
                        help_text=(
                            "Supplement number of the item or container holding the item (e.g. for secondary legal"
                            " items that are regularly updated between editions)"
                        ),
                        max_length=255,
                        null=True,
                        verbose_name="supplement number",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=1000, null=True, verbose_name="title")),
                (
                    "title_short",
                    models.CharField(
                        blank=True,
                        help_text="Short/abbreviated form of title",
                        max_length=255,
                        null=True,
                        verbose_name="title short",
                    ),
                ),
                (
                    "URL",
                    models.CharField(
                        blank=True, help_text="Uniform Resource Locator", max_length=255, null=True, verbose_name="URL"
                    ),
                ),
                (
                    "version",
                    models.CharField(
                        blank=True,
                        help_text="Version of the item (e.g. “2.0.9” for a software program)",
                        max_length=255,
                        null=True,
                        verbose_name="version",
                    ),
                ),
                (
                    "volume",
                    models.CharField(
                        blank=True, help_text="Volume number", max_length=255, null=True, verbose_name="number"
                    ),
                ),
                (
                    "volume_title",
                    models.CharField(
                        blank=True,
                        help_text="Title of the volume of the item or container holding the item",
                        max_length=255,
                        null=True,
                        verbose_name="title",
                    ),
                ),
                (
                    "volume_title_short",
                    models.CharField(
                        blank=True,
                        help_text="Short/abbreviated form of volume-title",
                        max_length=255,
                        null=True,
                        verbose_name="Short title",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="created")),
                ("modified", models.DateTimeField(auto_now=True, verbose_name="modified")),
                (
                    "file",
                    models.FileField(
                        blank=True, null=True, upload_to=literature.utils.file_upload_path, verbose_name="file"
                    ),
                ),
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
                "verbose_name": "literature item",
                "verbose_name_plural": "literature items",
                "ordering": ["created"],
                "default_related_name": "literature",
            },
        ),
        migrations.CreateModel(
            name="Date",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("accessed", "Accessed"),
                            ("container", "Container"),
                            ("event_date", "Event Date"),
                            ("issued", "Issued"),
                            ("original_date", "Original Date"),
                            ("submitted", "Submitted"),
                        ],
                        max_length=13,
                        verbose_name="type",
                    ),
                ),
                ("begin", partial_date.fields.PartialDateField(blank=True, null=True, verbose_name="date")),
                ("end", partial_date.fields.PartialDateField(blank=True, null=True, verbose_name="date to")),
                ("season", models.CharField(blank=True, max_length=255, null=True, verbose_name="season")),
                ("circa", models.BooleanField(default=False, verbose_name="circa")),
                (
                    "item",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="dates",
                        to="literature.literature",
                        verbose_name="item",
                    ),
                ),
            ],
            options={
                "verbose_name": "date",
                "verbose_name_plural": "dates",
            },
        ),
        migrations.AddConstraint(
            model_name="name",
            constraint=models.CheckConstraint(
                check=models.Q(("family__isnull", False), ("literal__isnull", False), _connector="OR"),
                name="family_or_literal",
            ),
        ),
        migrations.AddField(
            model_name="literature",
            name="author",
            field=sortedm2m.fields.SortedManyToManyField(
                blank=True,
                help_text="Author(s) of the item.",
                related_name="authors",
                to="literature.name",
                verbose_name="author",
            ),
        ),
        migrations.AddField(
            model_name="namethrough",
            name="literature",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="name_through",
                to="literature.literature",
                verbose_name="literature",
            ),
        ),
        migrations.AddField(
            model_name="namethrough",
            name="name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="name_through",
                to="literature.name",
                verbose_name="name",
            ),
        ),
        migrations.AddField(
            model_name="literature",
            name="names",
            field=models.ManyToManyField(
                blank=True,
                help_text="Authors, editors, etc.",
                through="literature.NameThrough",
                to="literature.name",
                verbose_name="names",
            ),
        ),
        migrations.AddField(
            model_name="supplementarymaterial",
            name="literature",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="supplementary",
                to="literature.literature",
                verbose_name="literature",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="date",
            unique_together={("item", "type")},
        ),
        migrations.AlterUniqueTogether(
            name="namethrough",
            unique_together={("name", "literature")},
        ),
    ]