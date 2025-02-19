# Generated by Django 5.1.6 on 2025-02-19 08:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Users",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("address", models.TextField()),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("pincode", models.CharField(max_length=10)),
                ("username", models.CharField(max_length=50, unique=True)),
                (
                    "usertype",
                    models.CharField(
                        choices=[("Doctor", "Doctor"), ("Patient", "Patient")],
                        max_length=10,
                    ),
                ),
                ("password", models.CharField(max_length=100)),
            ],
        ),
    ]
