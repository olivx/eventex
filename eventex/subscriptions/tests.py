from django.core import mail
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
        """Form must have 4 fields name, cpf, email, phone"""
        form = self.reps.context['form']
        self.assertSequenceEqual(['name', 'cpf', 'email', 'phone'], list(form.fields))



class SubcriptionPostTest(TestCase):

    def setUp(self):
        data = dict(name='Thiago Oliveira', cpf='12345678901',
                    email='oliveiravicente.net@gmail.com', phone='11-97051-3508')
        self.resp = self.client.post('/inscricao/', data)

    def test_redirect_incricao(self):
        '''Valued Post should redirect to Inscricao'''
        self.assertEqual(302, self.resp.status_code)

    def test_send_email_inscricao(self):
        self.assertEqual(1, len(mail.outbox))

    def test_subcription_mail_expect(self):

        expect = mail.outbox[0]
        self.assertEqual(expect.subject, 'Confirmação de Inscrição!')
        self.assertEqual(expect.from_email, 'oliveiravicente.net@gmail.com')
        self.assertEqual(expect.to, ['contato@eventex.com', 'oliveiravicente.net@gmail.com'])

        self.assertIn('Thiago Oliveira', expect.body)
        self.assertIn('12345678901', expect.body)
        self.assertIn('oliveiravicente.net@gmail.com', expect.body)
        self.assertIn('11-97051-3508', expect.body)

class SubscriptionInvalidPost(TestCase):

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

class SubscriptionMessages(TestCase):

    def setUp(self):
        data = dict(name='Thiago Oliveira', cpf='12345678901',
                    email='oliveiravicente.net@gmail.com', phone='11-97051-3508')
        self.resp = self.client.post('/incricao/', data, follow=True)

    def tets_sucess_message(self):
        self.assertContains(self.resp, 'Inscrição Realizada com sucesso!')










