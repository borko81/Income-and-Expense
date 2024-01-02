from django.test import TestCase
from django.contrib.auth.models import User
from user_profile.models import UserProfile


class UserProfileTest(TestCase):
    def setUp(self):
        User.objects.create(username="borko", password="borko")

    def test_create_new_record(self):
        u = User.objects.get(id=1)
        r = UserProfile(user_id=u, telephone="035988", town="Velingrad")
        self.assertEqual(str(r), "borko")
        self.assertEqual(r.telephone, "035988")

    def test_create_new_record_with_not_valid_town_shoud_raise_error(self):
        u = User.objects.get(id=1)
        r = UserProfile(user_id=u, telephone="035988", town="Velingr")
        self.assertNotEqual(r.town, "Velingrad")
