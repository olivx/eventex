from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionsTests(TestCase):

    #0 instacia de requete
    def setUp(self):
        self.reps = self.client.get('/inscricao/')

    # 1 testar se existe a url
    def test_get(self):
        """Get '/inscricao/' must return status code 200"""
        self.assertEqual(200, self.reps.status_code)

    # 2 Testar se existe o template
    def test_template(self):
        """Must use subscriptions/subscription_form.html"""
        self.assertTemplateUsed(self.reps, 'subscriptions/subscription_form.html')

    # 3 Testar oque contem no html do templates
    def test_html(self):
        """Must cntains html inputs forms, name, cpf, emial, telefone"""
        self.assertContains(self.reps,'<form')
        self.assertContains(self.reps,'<input',6)
        self.assertContains(self.reps,'type="text"',3)
        self.assertContains(self.reps,'type="email"')
        self.assertContains(self.reps,'type="submit"')

    # 4 Testar csrf
    def test_csrf(self):
        """Must contains csrf_token"""
        self.assertContains(self.reps, "csrfmiddlewaretoken")

    # 5 Testar se existe um form
    def test_form(self):
        """Must have subscription from"""
        form = self.reps.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    # 6 Testar se existe os forms
    def test_form_has_fields(self):
        """Form must have 4 fields nome, cpf, email, phone"""
        form = self.reps.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))