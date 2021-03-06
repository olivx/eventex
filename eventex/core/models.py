from django.db import models
from django.shortcuts import resolve_url as r
from eventex.core.manage import KindContactQuerySet, PeriodManager


class Speaker(models.Model):
    name = models.CharField('nome', max_length=255)
    slug = models.SlugField('slug')
    photo = models.URLField('foto')
    website = models.URLField('site', blank=True)
    description = models.TextField('descrição', blank=True)

    class Meta:
        verbose_name = 'palestrante'
        verbose_name_plural = 'palestrantes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return r('speaker_detail', slug=self.slug)


class Contact(models.Model):
    EMAIL = 'E'
    PHONE = 'P'
    KINDS = (
        (EMAIL, 'Email'),
        (PHONE, 'Telefone'),
    )
    speaker = models.ForeignKey('Speaker', verbose_name='Palestrante')
    kind = models.CharField('Tipo Contato', max_length=1, choices=KINDS)
    value = models.CharField('Valor', max_length=255)

    objects = KindContactQuerySet.as_manager()

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return str(self.value)


class Activicty(models.Model):
    title = models.CharField('titulo', max_length=200)
    start = models.TimeField('inicio', blank=True, null=True)
    description = models.TextField('descrição', blank=True)
    speakers = models.ManyToManyField('Speaker', verbose_name='palestrantes', blank=True)

    objects = PeriodManager()

    class Meta:
        abstract = True
        verbose_name = 'palestra'
        verbose_name_plural = 'palestras'

    def __str__(self):
        return self.title

class Talk(Activicty):
    pass

class Curse(Activicty):
    slot = models.IntegerField()

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
