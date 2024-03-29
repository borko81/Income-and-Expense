# Generated by Django 5.0 on 2023-12-25 08:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user_profile", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="town",
            field=models.CharField(
                choices=[
                    ("UNKNOWN", "Unknown"),
                    ("Velingrad", "Velingrad"),
                    ("Plovdiv", "Plovdiv"),
                    ("Sofia", "Sofia"),
                    ("Varna", "Varna"),
                ],
                default="UNKNOWN",
                max_length=15,
            ),
        ),
    ]
