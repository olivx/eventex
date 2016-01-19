from django.test import TestCase
from eventex.subscriptions.models import Subscrition
from datetime import datetime


class SubcriptionModelTest(TestCase):

    def setUp(self):

        self.obj = Subscrition(
            name = 'thiago oliveira',
            cpf = 12345678901,
            email = 'oliveiravicente.net@gmail.com',
            phone = '011-97051-3508'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscrition.objects.exists())

    def test_created_at(self):
        ''' Subscrition Must have an auto created_at attrib '''
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('Thiago Oliveira', str(self.obj))
