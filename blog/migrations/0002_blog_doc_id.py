# Generated by Django 5.1.6 on 2025-02-24 17:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="doc_id",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
