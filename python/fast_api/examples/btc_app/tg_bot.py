import telebot
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
BOT_TOKEN = config.get('DEFAULT','bot_token')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет из 2023')


bot.infinity_polling()