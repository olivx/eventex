from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter somente numeros.', 'digits')
    if len(value) != 11:
        raise ValidationError('CPF deve conter onze digitos', 'length')
