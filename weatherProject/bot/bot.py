import os
import telebot
import requests

from configparser import ConfigParser

config_path = '../config.ini'
config = ConfigParser()
config.read(config_path)
BOT_TOKEN = config['BOT']['TOKEN']

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Отправь мне город, а я подскажу погоду")


@bot.message_handler(content_types=['text'])
def get_message(message):
    mes = message.text

    city_name = mes[0].upper() + mes[1:].lower()
    weather_data = requests.get(url='http://127.0.0.1:8000/api/weather?city=' + city_name).json()

    rus_weather = f'Погода в {city_name}:\n\n{weather_data["temperature"]}\n{weather_data["humidity"]}\n{weather_data["wind_speed"]}'
    bot.reply_to(message, rus_weather)


bot.infinity_polling()
