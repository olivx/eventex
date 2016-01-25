from django.test import TestCase
from django.shortcuts import resolve_url as r

class HomeTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('home'))

    def test_get(self):
        """Must be code 200 when acess the home page"""
        self.assertEquals(200, self.resp.status_code)

    def test_template(self):
        """Template in use must index.html"""
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_link_inscricao(self):
        """Test if link from subscription href=/inscricao/"""
        expected = 'href="{}"'.format(r('subscriptions:new'))
        self.assertContains(self.resp, expected)
