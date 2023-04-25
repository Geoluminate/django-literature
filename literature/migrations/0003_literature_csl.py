# Generated by Django 4.2 on 2023-04-21 15:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("literature", "0002_alter_literature_published"),
    ]

    operations = [
        migrations.AddField(
            model_name="literature",
            name="CSL",
            field=models.JSONField(blank=True, default={}, verbose_name="Citation Style Language"),
            preserve_default=False,
        ),
    ]