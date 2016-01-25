from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribeMail(TestCase):


    def setUp(self):
        data = dict(name='Thiago Oliveira', cpf='12345678901',
                    email='oliveiravicente.net@gmail.com', phone='11-97051-3508')
        self.resp = self.client.post(r('subscriptions:new'), data)
        self.mail = mail.outbox[0]

    def test_subcription_mail(self):
        """ Mail Expect   """

        self.assertEqual(self.mail.subject, 'Confirmação de Inscrição!')
        self.assertEqual(self.mail.from_email, 'oliveiravicente.net@gmail.com')
        self.assertEqual(self.mail.to, ['contato@eventex.com', 'oliveiravicente.net@gmail.com'])


    def test_mail_body(self):

        contexts = [
            'Thiago Oliveira',
            '12345678901',
            'oliveiravicente.net@gmail.com',
            '11-97051-3508'
        ]

        for context in contexts:
            with self.subTest():
                self.assertIn(context, self.mail.body)

