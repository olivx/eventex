from django.conf import settings
from django.core import mail
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, resolve_url as r
from django.template.loader import render_to_string
from eventex.subscriptions.forms import SubscriptionForm
from eventex.subscriptions.models import Subscription


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
    subscription = Subscription.objects.create(**form.cleaned_data)
    _send_mail('Confirmação de Inscrição!',
               settings.DEFAULT_FROM_MAIL,
               subscription.email, 'subscriptions/subscription_message.txt',
               {'subscription': subscription})

    return HttpResponseRedirect(r('subscriptions:detail', subscription.pk))


def new(request):
    return render(request, 'subscriptions/subscription_form.html',
                  {'form': SubscriptionForm()})


def detail(request, pk):
    try:
        subscription = Subscription.objects.get(pk=pk)
    except Subscription.DoesNotExist:
        raise Http404

    return render(request, 'subscriptions/subscription_detail.html',
                  {'subscription': subscription})


def _send_mail(subject, from_, to, tamplate_name, context):
    body = render_to_string(tamplate_name, context)
    mail.send_mail(subject, body, from_, ['contato@eventex.com', to])
