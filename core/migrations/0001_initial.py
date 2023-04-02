# Generated by Django 4.1.7 on 2023-03-19 15:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                ("name", models.CharField(max_length=100, unique=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("title", models.CharField(max_length=100)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "numberInStock",
                    models.IntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MaxValueValidator(100),
                            django.core.validators.MinValueValidator(1),
                        ],
                    ),
                ),
                (
                    "dailyRentalRate",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=3,
                        validators=[
                            django.core.validators.MaxValueValidator(10),
                            django.core.validators.MinValueValidator(0),
                        ],
                    ),
                ),
                ("publishDate", models.DateField(blank=True, null=True)),
                ("liked", models.BooleanField(default=False)),
                (
                    "genre",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="genre",
                        to="core.genre",
                    ),
                ),
            ],
        ),
    ]
