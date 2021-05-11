from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Metric(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Weather(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    metric = models.ForeignKey(Metric, on_delete=models.CASCADE)
    date = models.DateField(blank=True, null=True)
    value = models.FloatField(max_length=200)

    class Meta:
        unique_together = ('location', 'date', 'metric')

    def __str__(self):
        return str(self.location) + ' / ' + str(self.date) + ' / ' + str(self.metric)
