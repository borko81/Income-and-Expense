# Generated by Django 5.0 on 2023-12-28 18:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("income_expense", "0004_typeolddata"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Type",
            new_name="Types",
        ),
    ]
