# Generated by Django 5.0 on 2023-12-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("income_expense", "0009_checkoutmodel_suma"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newactionmodel",
            name="description",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
