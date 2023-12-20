from rest_framework import serializers
from .models import City


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['temperature', 'humidity', 'wind_speed']
