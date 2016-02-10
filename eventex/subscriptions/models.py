from django.db import models
from .validator import validate_cpf


class Subscription(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('cpf', max_length=11, validators=[validate_cpf])
    email = models.EmailField('e-mail', blank=True)
    phone = models.CharField('telefone', max_length=20, blank=True)
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    paid = models.BooleanField('pago',default=False)

    class Meta:
        verbose_name_plural = 'inscrções'
        verbose_name = 'inscrição'

    def __str__(self):
        return self.name.title()
