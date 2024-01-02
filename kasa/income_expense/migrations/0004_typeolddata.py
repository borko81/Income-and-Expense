# Generated by Django 5.0 on 2023-12-28 18:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("income_expense", "0003_type"),
    ]

    operations = [
        migrations.CreateModel(
            name="TypeOldData",
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
                ("old_name", models.CharField(max_length=32, unique=True)),
                (
                    "old_type",
                    models.CharField(
                        choices=[
                            ("Income", "income"),
                            ("Expence", "expense"),
                            ("Income/Excome", "income/expense"),
                            ("Begin", "begin"),
                        ],
                        max_length=15,
                    ),
                ),
                ("date_updated", models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
