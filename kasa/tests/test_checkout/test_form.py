from django.test import TestCase
from income_expense.forms import CheckOutForm
from income_expense.models import CheckOutModel


class TestCheckOutForm(TestCase):
    def setUp(self):
        self.form = CheckOutForm(data={})

    def test_create_form_without_data(self):
        self.assertFalse(self.form.is_valid())

    def test_create_form_with_data(self):
        form = CheckOutForm(data={"name": "First", "description": "Something"})
        self.assertTrue(form.is_valid())
        form.save()
        checkout = CheckOutModel.objects.get(id=1)
        self.assertEqual(checkout.name, "First")
        self.assertEqual(checkout.description, "Something")
