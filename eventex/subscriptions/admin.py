from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscrition


class SubscriptionsModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cpf', 'phone', 'created_at', 'subscribe_today')
    search_fields = ('nome', 'email', 'cpf', 'phone', 'created_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at',)

    def subscribe_today(self, obj):
        return obj.created_at.date() == now().date()

    subscribe_today.short_description = 'escritos hoje?'
    subscribe_today.boolean = True

admin.site.register(Subscrition, SubscriptionsModelAdmin)
