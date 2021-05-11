from rest_framework import serializers
from .models import Weather, Location, Metric

class MetricSerializer(serializers.ModelSerializer):

    class Meta:
        model = Metric
        fields = ['name']

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = ['name']

class WeatherSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all(), source='location.name')
    metric = serializers.PrimaryKeyRelatedField(queryset=Metric.objects.all(), source='metric.name')

    class Meta:
        model = Weather
        fields = ['location', 'date', 'metric', 'value']
    
    def create(self, validated_data):
        validated_data['location'] = validated_data['location']['name']
        validated_data['metric'] = validated_data['metric']['name']
        return Weather.objects.create(**validated_data)