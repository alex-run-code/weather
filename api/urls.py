from django.urls import path, include
from . import views

urlpatterns = [
    path('weather', views.ListWeatherData.as_view(), name='weather-data'),
]