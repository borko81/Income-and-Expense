from django import forms
from . import models


class CheckOutForm(forms.ModelForm):
    class Meta:
        model = models.CheckOutModel
        fields = "name description".split()


class TypeForm(forms.ModelForm):
    class Meta:
        model = models.Types
        fields = "name description type_name".split()


class NewActionForm(forms.ModelForm):
    class Meta:
        model = models.NewActionModel
        fields = "from_user to_user type_action suma description".split()
