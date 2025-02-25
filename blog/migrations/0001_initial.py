# Generated by Django 5.1.6 on 2025-02-24 16:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("text", models.TextField()),
                ("img", models.ImageField(blank=True, null=True, upload_to="images/")),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("author", models.CharField(max_length=50)),
                ("uploaded", models.BooleanField()),
            ],
        ),
    ]
