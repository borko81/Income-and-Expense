from django.test import TestCase, Client
from django.contrib.auth.models import User
from user_profile.forms import ProfileForm


class TestFormCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.form = ProfileForm()
        self.user = User.objects.create(username="borko", password="borko")

    def test_all_fields_in_form_exists(self):
        self.assertIn("telephone", self.form.fields)
        self.assertIn("description", self.form.fields)
        self.assertIn("town", self.form.fields)
        self.assertNotIn("user_id", self.form.fields)

    def test_form_without_data(self):
        form = ProfileForm(data={})
        self.assertFalse(form.is_valid())

    def test_form_with_correct_data(self):
        form = ProfileForm(
            data={
                "user_id": self.user,
                "telephone": "0885577",
                "town": "Velingrad",
            }
        )
        self.assertTrue(form.is_valid())
