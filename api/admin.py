from django.contrib import admin
from api.models import Weather, Metric, Location
# Register your models here.


class WeatherAdmin(admin.ModelAdmin):
    list_display = ['location', 'date', 'metric', 'value']

admin.site.register(Weather, WeatherAdmin)

class MetricAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Metric, MetricAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Location, LocationAdmin)