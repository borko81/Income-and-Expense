from django import forms

from . import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.UserProfile
        fields = "telephone town description".split()
