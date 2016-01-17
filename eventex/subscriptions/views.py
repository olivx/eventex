from django.contrib import messages
from django.core import mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscrition

from django.conf import settings

def subscribe(request):

    if request.method == 'POST':
        return create(request)
    else:
        return new(request)


def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html',
                      {'form': form})

    _send_mail('Confirmação de Inscrição!',
               settings.DEFAULT_FROM_MAIL,
               form.cleaned_data['email'], 'subscriptions/subscription_message.txt',
               form.cleaned_data)
    Subscrition.objects.create(**form.cleaned_data)

    messages.success(request, 'Inscrição Realizada com sucesso!')
    return HttpResponseRedirect('/inscricao/')


def new(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})


def _send_mail(subject, from_, to, tamplate_name, context):
    body = render_to_string(tamplate_name, context)
    mail.send_mail(subject, body, from_, ['contato@eventex.com', to])

