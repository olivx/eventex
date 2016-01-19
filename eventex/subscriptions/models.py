from django.db import models


class Subscrition(models.Model):
    name = models.CharField('nome', max_length=100)
    cpf = models.CharField('cpf', max_length=11)
    email = models.EmailField('e-mail')
    phone = models.CharField('telefone', max_length=20)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'inscrções'
        verbose_name = 'inscrição'

    def __str__(self):
        return self.name.title()
