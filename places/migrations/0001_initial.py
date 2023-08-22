# Generated by Django 4.2.4 on 2023-08-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Image",
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
                ("title", models.CharField(max_length=128, unique=True)),
                ("imgs", models.ImageField(blank=True, null=True, upload_to="images/")),
            ],
        ),
        migrations.CreateModel(
            name="PlaceName",
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
                ("title", models.CharField(max_length=128, unique=True)),
                ("description_short", models.TextField(blank=True, null=True)),
                ("description_long", models.TextField(blank=True, null=True)),
                ("coordinates", models.TextField(blank=True, null=True)),
            ],
        ),
    ]