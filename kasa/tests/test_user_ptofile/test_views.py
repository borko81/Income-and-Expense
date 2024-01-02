from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse


class TestUserProfile(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(username="testuser", password="Dummy@123")
        self.response_show = self.client.get(reverse("user_profile:profile"))

    def test_show_usersprofile_without_login(self):
        self.assertEqual(self.response_show.status_code, 302)

    def test_show_usersprofile_with_login(self):
        self.client.force_login(self.user)
        self.assertEqual(
            self.client.get(reverse("user_profile:profile")).status_code, 200
        )
