from django.contrib import admin
from eventex.core.models import Speaker, Contact, Talk, Curse


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInline]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_viewer', 'website_link', 'phone', 'email']

    def website_link(self, obj):
        return '<a href="{0}">{0}</a>'.format(obj.website)
    website_link.short_description = 'website'
    website_link.allow_tags = True

    def photo_viewer(self, obj):
        return '<img style="border-radius:100%;" width="32px" src="{}" />'.format(obj.photo)
    photo_viewer.allow_tags = True
    photo_viewer.short_description = 'foto'

    def phone(self, obj):
        return obj.contact_set.phones().first()

    phone.short_description = 'telefone'

    def email(self, obj):
        return obj.contact_set.emails().first()
    email.short_description = 'e-mail'

admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk)
admin.site.register(Curse)
