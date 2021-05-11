from django.core.management.base import BaseCommand
from django.utils import timezone
import requests
from api.models import Weather, Location, Metric
import datetime
from django.shortcuts import reverse
import json

class Command(BaseCommand):
    help = 'Populate the database'
    
    def create_initial_locations(self):
        Location.objects.create(name='UK')
        Location.objects.create(name='England')
        Location.objects.create(name='Scotland')
        Location.objects.create(name='Wales')
        return 'Locations created : UK, England, Scotland, Wales'
    
    def create_initial_metrics(self):
        Metric.objects.create(name='Tmax')
        Metric.objects.create(name='Tmin')
        Metric.objects.create(name='Rainfall')
        return 'Metrics created : Tmax, Tmin, Rainfall'

    def handle(self, *args, **kwargs):
        locations = Location.objects.all()
        metrics = Metric.objects.all()
        for location in locations:
            for metric in metrics:
                url = f'https://storage.googleapis.com/kisanhub-interview-question-data/metoffice/{metric.name}-{location.name}.json'
                response = requests.get(url)
                if response.status_code == 200:
                    for j, data in enumerate(response.json()):
                        print(f'location : {location.name}')
                        print(f'metric : {metric.name}')
                        print(f'value: {data["value"]}')
                        print(f'data : {j+1}/{len(response.json())}')
                        weather = {}
                        weather['location'] = location.id
                        weather['date'] = f"{data['year']}-{data['month']}-01"
                        weather['metric'] = metric.id
                        weather['value'] = data['value']
                        base_url = 'http://127.0.0.1:8000'
                        requests.post(base_url + reverse('weather-data'), data=weather)