# Generated by Django 5.1.1 on 2024-10-04 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("literature", "0002_rename_key_literatureitem_citation_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="literatureitem",
            name="citation_key",
            field=models.CharField(max_length=255, unique=True, verbose_name="key"),
        ),
        migrations.AlterField(
            model_name="literatureitem",
            name="title",
            field=models.CharField(blank=True, db_index=True, max_length=1000, null=True),
        ),
    ]