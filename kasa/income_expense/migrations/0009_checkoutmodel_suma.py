# Generated by Django 5.0 on 2023-12-29 19:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("income_expense", "0008_alter_newactionmodel_date_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="checkoutmodel",
            name="suma",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
