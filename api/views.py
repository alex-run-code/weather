from django.shortcuts import render
from rest_framework import generics
from .models import Weather, Location, Metric
from .serializers import WeatherSerializer
import json
import datetime
from django.http import HttpResponse

# Create your views here.


# a view to retrieve data via a GET method using the following filters :
# Start date, End Date, metric Type, Location
class ListWeatherData(generics.ListCreateAPIView):
    '''
    A view to retrieve data via a GET method using the following filters :
    Start date, End Date, metric Type, Location
    '''
    serializer_class = WeatherSerializer

    def get_queryset(self):
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        metric = self.request.GET.get('metric')
        location = self.request.GET.get('location')
        queryset = Weather.objects.all()
        if start_date is not None:
            queryset = queryset.filter(date__gte=start_date)
        if end_date is not None:
            queryset = queryset.filter(date__lte=end_date)
        if metric is not None:
            queryset = queryset.filter(metric__name=metric)
        if location is not None:
            queryset = queryset.filter(location__name=location)
        return queryset