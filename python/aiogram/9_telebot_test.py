from telebot import TeleBot, types
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
DEBUG = config.get('DEFAULT', 'debug')
BOT_TOKEN = config.get('BOT', 'token')
MY_ID = config.get('BOT', 'my_id')


bot = TeleBot(BOT_TOKEN)


def send_message(id, text):
    bot.send_message(id, text)


send_message(MY_ID, 'hello world')

