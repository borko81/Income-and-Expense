# Generated by Django 5.0 on 2023-12-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("income_expense", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkoutmodel",
            name="description",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
