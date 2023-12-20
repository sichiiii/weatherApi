# Сервис погоды
## _Django app + TG bot_


## Подготовка к запуску

Сервис требует версию Python => 3.10

Ввод телеграм-токена и апи-ключа к Яндекс.Погоде:
```sh
cd weatherApi
nano config.ini
```

Установка библиотек:
```sh
cd weatherApi
pip install -r requirements.txt
```

Импорт координатор городов (если потребуется, однако дефолтные данные уже в `cities_lat_lon.csv`):
```sh
cd weatherApi/weatherProject
python3 manage.py load_lat_lon
```

## Запуск

Запуск Django-сервера:

```sh
cd weatherProject
python3 manage.py runserver
```

## Запуск TG-бота:

```sh
cd bot
python3 bot.py
```

## Тестирование:
```sh
cd test
python3 test_weather.py
```

> Заметка: Django-сервер должен быть запущен.
