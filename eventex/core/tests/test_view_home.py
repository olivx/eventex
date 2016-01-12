from django.test import TestCase

# Create your tests here.
from django.test import TestCase

class test_index(TestCase):



    def test_link_inscricao(self):
        response = self.client.get('/')
        self.assertContains(response, 'href="/inscricao/"')
