from django.contrib import admin

# Register your models here.
from . models import *

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['car_brand', 'model', 'body_index', 'version', 'year_start_production', 'year_end_production',
                    'engine', 'engine_displacement', 'power_hp']
    ordering = ['car_brand']
    search_fields = ['car_brand', 'model', 'body_index', 'version']

