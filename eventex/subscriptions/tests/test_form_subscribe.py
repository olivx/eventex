from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    # 6 Testar se existe os forms
    def test_form_has_fields(self):
        """Form must have 4 fields name, cpf, email, phone"""
        form = SubscriptionForm()
        expect = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expect, list(form.fields))

    def test_cpf_is_valid(self):
        """CPF must have only digit"""
        form = self.make_validated_form(cpf='ABCD5678901')
        if form.is_valid():
            self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digitos(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_captilaze(self):
        """Name must be capitalized"""
        #THIAgo oliveira
        form =  self.make_validated_form(name="thiago oliveira")
        self.assertEquals('Thiago Oliveira', form.cleaned_data['name'])


    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        error_list = errors[field]
        exception = error_list[0]
        self.assertEquals(code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Thiago Oliveira', cpf='12345678901',
                     email='oliveiravicente.net@gmail.com',
                     phone='11-97051-3508')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form
