from django.core.management.base import BaseCommand
from api.models import Weather, Location, Metric



class Command(BaseCommand):
    help = 'Create initial metrics and locations'

    def handle(self, *args, **kwargs):
        Location.objects.create(name='UK')
        Location.objects.create(name='England')
        Location.objects.create(name='Scotland')
        Location.objects.create(name='Wales')
        Metric.objects.create(name='Tmax')
        Metric.objects.create(name='Tmin')
        Metric.objects.create(name='Rainfall')
        return 'Created: UK, England, Scotland, Wales, Tmax, Tmin, Rainfall'