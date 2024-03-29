# Generated by Django 5.0 on 2023-12-28 19:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("income_expense", "0005_rename_type_types"),
    ]

    operations = [
        migrations.AlterField(
            model_name="typeolddata",
            name="old_type",
            field=models.CharField(
                choices=[
                    ("Income", "Income"),
                    ("Expence", "Expence"),
                    ("Income/Excome", "Income/Excome"),
                    ("Begin", "Begin"),
                ],
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="types",
            name="type_name",
            field=models.CharField(
                choices=[
                    ("Income", "Income"),
                    ("Expence", "Expence"),
                    ("Income/Excome", "Income/Excome"),
                    ("Begin", "Begin"),
                ],
                max_length=15,
            ),
        ),
    ]
