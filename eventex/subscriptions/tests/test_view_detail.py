from django.test import TestCase
from django.shortcuts import resolve_url as r
from eventex.subscriptions.models import Subscription

class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription.objects.create(
            name='Thiago Oliveira',
            cpf='12345678901',
            email='oliveiravicente.net@gmail.com',
            phone='11-97051-3508'
        )
        self.resp = self.client.get(r('subscriptions:detail', self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template_datail(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_isInstace_subscription(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html_detail(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected)

class SubscriptionDetailInvalidUrl(TestCase):

    def test_invalid_detail(self):
        """Url invalid 404 status code"""
        resp = self.client.get(r('subscriptions:detail', 0))
        self.assertEqual(404, resp.status_code)