from django.core import mail
from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


class SubscribeGet(TestCase):

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

    # Tets csrf no form
    def test_csrf(self):
        """Must contains csrf_token"""
        self.assertContains(self.reps, "csrfmiddlewaretoken")

    #Testar oque contem no html do templates
    def test_fields(self):
        """Must contains html inputs forms, name, cpf, emial, telefone"""
        tags = (
            ('<form', 1),
            ('<input', 6),
            ('type="text"', 3),
            ('type="email"', 1),
            ('type="submit"', 1),
        )
        for text, number in tags:
            with self.subTest():
                 self.assertContains(self.reps, text, number)



class SubcribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Thiago Oliveira', cpf='12345678901',
                    email='oliveiravicente.net@gmail.com', phone='11-97051-3508')
        self.resp = self.client.post('/inscricao/', data)

    def test_redirect_subscription(self):
        '''Valid Post should redirect to /Inscricao/1/ status code redirect 302'''
        self.assertEqual(302, self.resp.status_code)
        self.assertRedirects(self.resp, '/inscricao/1/')

    def test_send_email_subscription(self):
        """ Send email """
        self.assertEqual(1, len(mail.outbox))

    def test_save_subcrition(self):
        self.assertTrue(Subscription.objects.exists())



class SubscribePostInvalid(TestCase):


    def setUp(self):
        self.resp = self.client.post('/inscricao/', {})

    def test_post(self):
        """Invalid POST should not Redirection"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp,
                                'subscriptions/subscription_form.html')

    def test_has_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, SubscriptionForm)

    def test_has_erros(self):
        form = self.resp.context['form']
        self.assertTrue(form.errors)

    def test_dont_save_subcrition(self):
        self.assertFalse(Subscription.objects.exists())

class SubscribeSucessMessage(TestCase):

    def setUp(self):
        data = dict(name='Thiago Oliveira', cpf='12345678901',
                    email='oliveiravicente.net@gmail.com', phone='11-97051-3508')
        self.resp = self.client.post('/incricao/', data, follow=True)

    def tets_sucess_message(self):
        self.assertContains(self.resp, 'Inscrição Realizada com sucesso!')










