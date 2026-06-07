from django.contrib import admin
from .models import Provinsi, Regencies, Districts, Villages


@admin.register(Provinsi)
class ProvinsiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'alt_name', 'latitude', 'longitude')
    search_fields = ('name', 'alt_name')
    list_filter = ('name',)


@admin.register(Regencies)
class RegenciesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'province_id',
        'name',
        'alt_name',
        'latitude',
        'longitude'
    )
    search_fields = ('name', 'alt_name')


@admin.register(Districts)
class DistrictsAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'regency_id',
        'name',
        'alt_name',
        'latitude',
        'longitude'
    )
    search_fields = ('name', 'alt_name')


@admin.register(Villages)
class VillagesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'district_id',
        'name',
        'latitude',
        'longitude'
    )
    search_fields = ('name',)