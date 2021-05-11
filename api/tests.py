from rest_framework.test import APITestCase
from django.shortcuts import reverse
from .models import Weather, Location, Metric
from .factories import WeatherFactory, LocationFactory, MetricFactory
import datetime
from .serializers import WeatherSerializer


class WeatherDataTestCase(APITestCase):
    def setUp(self):
        pass
        # LocationFactory(name='UK')
        # LocationFactory(name='England')
        # LocationFactory(name='Wales')
        # LocationFactory(name='Scotland')
        # MetricFactory(name=')
        # Location.objects.create(name='UK')
        # Location.objects.create(name='England')
        # Location.objects.create(name='Wales')
        # Location.objects.create(name='Scotland')
        # Metric.objects.create(name='Tmax')
        # Metric.objects.create(name='Tmin')
        # Metric.objects.create(name='Rainfall')

    def test_list_weather_data(self):
        '''
        Without specifying any filter, the endpoint should
        return all the weather data objects
        '''
        WeatherFactory(date=datetime.datetime(2020, 1, 1))
        WeatherFactory(date=datetime.datetime(2020, 2, 1))
        serializer = WeatherSerializer(Weather.objects.all(), many=True)

        r = self.client.get(reverse('weather-data'))
        self.assertEqual(r.status_code, 200)
        self.assertListEqual(serializer.data, r.data['results'])

    def test_filter_weather_data_by_date(self):
        '''
        Only the data within the specified date range should be returned
        '''
        WeatherFactory(date=datetime.datetime(2020, 1, 1))
        WeatherFactory(date=datetime.datetime(2021, 6, 1))
        start_date = "2019-12-01"
        end_date = "2020-02-01"
        serializer = WeatherSerializer(Weather.objects.filter(date__range=[start_date, end_date]), many=True)
        query = f"?&start_date={start_date}&end_date={end_date}"

        r = self.client.get(reverse('weather-data') + query)
        self.assertEqual(r.status_code, 200)
        self.assertListEqual(serializer.data, r.data['results'])

    def test_filter_weather_data_by_metric(self):
        '''
        Only the data with the specified metric should be returned
        '''
        WeatherFactory(metric__name='Tmax')
        WeatherFactory(metric__name='Tmin')
        WeatherFactory(metric__name='Rainfall')
        metric = 'Tmax'
        serializer = WeatherSerializer(Weather.objects.filter(metric__name='Tmax'), many=True)
        query = f"?&metric={metric}"

        r = self.client.get(reverse('weather-data') + query)
        self.assertEqual(r.status_code, 200)
        self.assertListEqual(serializer.data, r.data['results'])

    def test_filter_weather_data_by_location(self):
        '''
        Only the data with the specified location should be returned
        '''
        WeatherFactory(location__name='UK')
        WeatherFactory(location__name='England')
        location = 'UK'
        serializer = WeatherSerializer(Weather.objects.filter(location__name='UK'), many=True)
        query = f"?&location={location}"

        r = self.client.get(reverse('weather-data') + query)
        self.assertEqual(r.status_code, 200)
        self.assertListEqual(serializer.data, r.data['results'])

    def test_combined_filter(self):
        '''
        Only the data with the specified location and metric should be returned
        '''
        WeatherFactory(location__name='UK', metric__name='Tmax')
        WeatherFactory(location__name='UK', metric__name='Tmin')
        WeatherFactory(location__name='England', metric__name='Tmax')
        WeatherFactory(location__name='England', metric__name='Tmin')
        location = 'UK'
        metric = 'Tmin'
        serializer = WeatherSerializer(Weather.objects.filter(location__name='UK', metric__name='Tmin'), many=True)
        query = f"?&location={location}&metric={metric}"

        r = self.client.get(reverse('weather-data') + query)
        self.assertEqual(r.status_code, 200)
        self.assertListEqual(serializer.data, r.data['results'])


    def test_create_weather_data(self):
        '''
        A new weather data object should be created
        '''
        location = LocationFactory().id
        metric = MetricFactory().id
        weather = {"location":location,"date":"2022-02-01","metric":metric,"value":"22.2"}

        r = self.client.post(reverse('weather-data'), data=weather)
        self.assertEqual(r.status_code, 201)
        self.assertEqual(len(Weather.objects.all()), 1)

    def test_weather_data_missing_parameter(self):
        '''
        Metric is missing, so the object should not be created
        '''
        location = LocationFactory().id
        weather = {"location":location,"date":"2022-02-01","value":"22.2"}

        r = self.client.post(reverse('weather-data'), data=weather)
        self.assertEqual(r.status_code, 400)
        self.assertEqual(len(Weather.objects.all()), 0)



