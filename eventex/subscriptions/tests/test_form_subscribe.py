from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):

    def setUp(self):
        self.form = SubscriptionForm()

    def test_form(self):
        """Must have subscription from"""
        self.assertIsInstance(self.form, SubscriptionForm)

    # 6 Testar se existe os forms
    def test_form_has_fields(self):
        """Form must have 4 fields name, cpf, email, phone"""
        expect = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expect, list(self.form.fields))
