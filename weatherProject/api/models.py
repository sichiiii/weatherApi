from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone


class City(models.Model):
    name = models.CharField(max_length=255)
    temperature = models.CharField(max_length=255, null=True, blank=True)
    humidity = models.CharField(max_length=255, null=True, blank=True)
    wind_speed = models.CharField(max_length=255, null=True, blank=True)
    last_updated = models.DateTimeField(default=datetime.now(tz=timezone.utc)-timedelta(minutes=31))
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
