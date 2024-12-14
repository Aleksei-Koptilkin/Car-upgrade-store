from django.contrib import admin

# Register your models here.
from . models import *

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_brand', 'model', 'body_index', 'version', 'year_start_production', 'year_end_production',
                    'weight']
    ordering = ['car_brand']
    search_fields = ['car_brand', 'model', 'body_index', 'version']


@admin.register(Engine)
class EngineAdmin(admin.ModelAdmin):
    list_display = ['engine_name', 'engine_brand', 'displacement', 'power_hp', 'boost_type', 'weight',]
    ordering = ['engine_brand', 'engine_name']
    search_fields = ['engine_name', 'engine_brand',]

