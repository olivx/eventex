from django import forms
from .models import Subscription
from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter somente numeros.', 'digits')
    if len(value) != 11:
        raise ValidationError('CPF deve conter 11 numeros.', 'length')


class SubscriptionFormOld(forms.Form):
    name = forms.CharField(label="Nome")
    cpf = forms.CharField(label="CPF", validators=[validate_cpf])
    email = forms.EmailField(label="Email", required=False)
    phone = forms.CharField(label="Telefone", required=False)

    def clean_name(self):
        name = self.cleaned_data.get('name')

        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        if not self.cleaned_data.get('email') and \
           not self.cleaned_data.get('phone'):
            raise ValidationError('E-mail ou Telefone deve ser informado.')

        return self.cleaned_data

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('name', 'cpf', 'email', 'phone')

    def clean_name(self):
        name = self.cleaned_data.get('name')
        words = [w.capitalize() for w in name.split()]
        return ' '.join(words)

    def clean(self):
        if not self.cleaned_data.get('email') and \
            not self.cleaned_data.get('phone'):
            raise ValidationError('E-mail ou Telefone deve ser informado.')

        return self.cleaned_data


