from django.contrib import admin
from django.conf import settings

from ..core.models import Event, Customer, Place, City, FederativeUnit, Source

admin.site.site_title = settings.ADMIN_SITE_TITLE
admin.site.site_header = settings.ADMIN_SITE_HEADER
admin.site.index_title = settings.ADMIN_INDEX_TITLE


@admin.register(FederativeUnit)
class FederativeUnitModelAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Place)
class PlaceModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Source)
class SourceModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventModelAdmin(admin.ModelAdmin):
    filter_horizontal = ('registrations',)
    prepopulated_fields = {'slug': ("title", "subtitle")}
