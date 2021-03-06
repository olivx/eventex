# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-11 23:51
from __future__ import unicode_literals

from django.db import migrations, models
import eventex.subscriptions.validator


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_subscription_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='cpf',
            field=models.CharField(max_length=11, validators=[eventex.subscriptions.validator.validate_cpf], verbose_name='cpf'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='e-mail'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(blank=True, max_length=20, verbose_name='telefone'),
        ),
    ]
