from django.contrib import admin, messages
from django.conf import settings
from django.contrib.admin import SimpleListFilter
from django.utils.safestring import mark_safe

from ..core.models import Event, Customer, Place, City, FederativeUnit, Source, Testimony, Registration

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
    list_display = ('title', 'subtitle', 'start_date')


@admin.register(Testimony)
class TestimonyModelAdmin(admin.ModelAdmin):
    list_display = ('customer',)
    autocomplete_fields = ('customer',)


@admin.register(Registration)
class RegistrationModelAdmin(admin.ModelAdmin):
    class EventFilter(SimpleListFilter):
        title = Event._meta.verbose_name
        parameter_name = 'event'

        def lookups(self, request, model_admin):
            events = set([r for r in Event.objects.all()])
            return [(r.id, str(r)) for r in events]

        def queryset(self, request, queryset):
            if self.value():
                return queryset.filter(event__id__exact=self.value())
            else:
                messages.add_message(request, messages.WARNING, 'Escolha um ' + self.title)
                return queryset.filter(event__id__exact=0)
    list_filter = (EventFilter,)
    search_fields = ('customer__name',)
    list_display = ('customer', 'contract_sent', 'financial_generated', 'financial_observations', 'nf_status')
