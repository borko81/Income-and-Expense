from django.test import TestCase
from django.db import IntegrityError

from income_expense.models import CheckOutModel


class CheckOutModelTest(TestCase):
    def test_successfully_create(self):
        c = CheckOutModel.objects.create(name="First", description="Something")
        self.assertEqual(c.name, "First")

    def test_try_to_save_not_unique_name_shoud_raise_error(self):
        CheckOutModel.objects.create(name="First", description="Something")
        with self.assertRaises(
            IntegrityError,
            msg="UNIQUE constraint failed: income_expense_checkoutmodel.name",
        ):
            c = CheckOutModel.objects.create(name="First", description="Something")
            self.assertEqual(len(CheckOutModel.objects.all()), 1)
