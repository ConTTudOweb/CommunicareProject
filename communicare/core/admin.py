from django.contrib import admin
from django.conf import settings
from django.utils.safestring import mark_safe

from ..core.models import Event, Customer, Place, City, FederativeUnit, Source, Testimony

admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.index_title = settings.ADMIN_INDEX_TITLE


@admin.register(FederativeUnit)
class FederativeUnitModelAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityModelAdmin(admin.ModelAdmin):
    search_fields = ('name', 'uf__initials')
    ordering = ('name',)


@admin.register(Place)
class PlaceModelAdmin(admin.ModelAdmin):
    autocomplete_fields = ('city',)


@admin.register(Source)
class SourceModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    autocomplete_fields = ('city',)


class RegistrationInline(admin.TabularInline):
    model = Event.registrations.through
    extra = 0
    autocomplete_fields = ('customer',)
    readonly_fields = ('contract_sent', 'send_contract')
    fields = ('customer', 'contract_sent', 'send_contract')

    class Media:
        js = ("admin/js/send_contract.js",
              "js/jquery/jquery.js")

    def send_contract(self, obj):
        return mark_safe('<a href="javascript:void(0)" onclick="send_contract('+str(obj.pk)+')">Enviar contrato</a>')

    send_contract.short_description = ""


@admin.register(Event)
class EventModelAdmin(admin.ModelAdmin):
    inlines = [
        RegistrationInline,
    ]
    prepopulated_fields = {'slug': ("title", "subtitle")}


@admin.register(Testimony)
class TestimonyModelAdmin(admin.ModelAdmin):
    list_display = ('customer',)
