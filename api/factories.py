import factory
from . import models
import datetime
import random
import decimal


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Location
        django_get_or_create = ('name',)

    name = random.choice(['UK', 'England', 'Scotland', 'Wales'])

class MetricFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Metric
        django_get_or_create = ('name',)

    name = random.choice(['Tmax', 'Tmin', 'Rainfall'])

class WeatherFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Weather

    location = factory.SubFactory(LocationFactory)
    metric = factory.SubFactory(MetricFactory)
    date = datetime.date(2020, 1, 1)
    value = decimal.Decimal(random.randrange(100, 1000))/100