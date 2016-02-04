from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscription


class SubscriptionsModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribe_today', 'paid')
    search_fields = ('name', 'email', 'cpf', 'phone', 'created_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_filter = ('paid', 'created_at')

    actions = ['mark_as_paid']

    def mark_as_paid(self, request, queryset):
        count = queryset.update(paid=True)

        if count == 1:
            msg = '{} inscrição foi marcada como paga.'
        else:
            msg = '{} inscrições foram marcadas como pagas.'

        self.message_user(request, msg.format(count))

    mark_as_paid.short_description = 'Marcar como pago'

    def subscribe_today(self, obj):
        return obj.created_at.date() == now().date()

    subscribe_today.short_description = 'escritos hoje?'
    subscribe_today.boolean = True


admin.site.register(Subscription, SubscriptionsModelAdmin)
