import requests
from .models import City
from configparser import ConfigParser


config_path = './config.ini'


class YandexWeather():
    def __init__(self):
        self.config = ConfigParser()
        self.config.read(config_path)

    def get_city_weather(self, city: City):
        try:
            r = requests.get(
                f"https://api.weather.yandex.ru/v2/forecast?lat={city.latitude}&lon={city.longitude}&lang=ru_RU",
                headers={'X-Yandex-API-Key': self.config['API']['YANDEX_API_KEY']}
            )
            return r.json()['fact']
        except Exception as ex:
            print(str(ex))
