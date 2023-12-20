from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from .models import City
from datetime import datetime, timedelta
from .yandex_weather import YandexWeather
from urllib.parse import unquote
from .serializers import WeatherSerializer
from django.utils import timezone

yandex_weather = YandexWeather()


@api_view(['GET'])
@renderer_classes([JSONRenderer])
def weather(request):
    try:
        parsed_city_name = unquote(request.GET.get('city'))

        city = City.objects.get(name=parsed_city_name)

        if datetime.now(tz=timezone.utc) - city.last_updated > timedelta(minutes=30):
            weather_data = yandex_weather.get_city_weather(city)
            weather_json = {
                'temperature': str(weather_data['temp']) + ' °C',
                'humidity': str(weather_data['humidity']) + ' мм рт.ст.',
                'wind_speed': str(weather_data['wind_speed']) + ' м/с'
            }

            serializer = WeatherSerializer(weather_json, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            weather_json = {
                'temperature': city.temperature,
                'humidity': city.humidity,
                'wind_speed': city.wind_speed
            }
            serializer = WeatherSerializer(weather_json, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(str(e))
        return Response(status=status.HTTP_400_BAD_REQUEST)
