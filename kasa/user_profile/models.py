from django.db import models

from django.contrib.auth.models import User


TOWN_CHOICES = (
    ("UNKNOWN", "Unknown"),
    ("Velingrad", "Velingrad"),
    ("Plovdiv", "Plovdiv"),
    ("Sofia", "Sofia"),
    ("Varna", "Varna"),
)


class UserProfile(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=15)
    town = models.CharField(max_length=15, choices=TOWN_CHOICES, default="UNKNOWN")
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user_id.username
