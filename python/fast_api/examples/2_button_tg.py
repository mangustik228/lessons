import telebot
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
BOT_TOKEN = config.get('BOT', 'bot_token')
ADMIN_ID = config.getint('BOT', 'admin_id')
bot = telebot.TeleBot(BOT_TOKEN)

users = [
    {
        "id":1,
        "name":"Annaasdfasdfasdfasdf",
        "nick":"Anny42",
        "balance": 15300
     },

    {
        "id":2,
        "name":"Dima",
        "nick":"dimon2319",
        "balance": 160.23
     },
    {
        "id":3,
        "name":"Vladimir",
        "nick":"Vova777",
        "balance": 200.1
     }
]

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Кошелек')
    btn2 = telebot.types.KeyboardButton('Перевести')
    btn3 = telebot.types.KeyboardButton('История')
    markup.add(btn1, btn2, btn3)
    text = f'Привет {message.from_user.full_name}'
    bot.send_message(message.chat.id, text, reply_markup=markup)



@bot.message_handler(regexp='Кошелек')
def wallet(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Меню')
    markup.add(btn1)
    balance = 0 
    text = f'Ваш баланс: {balance}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(regexp='Перевести')
def transaction(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Меню')
    markup.add(btn1)
    text = f'Введите адрес кошелька куда хотите перевести'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(regexp="История")
def history(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Меню')
    markup.add(btn1)
    transactions = ['1','2','3']
    symb = '\n'
    text = f'Ваши транзакции:\n{symb.join(transactions)}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(regexp='Меню')
def menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Кошелек')
    btn2 = telebot.types.KeyboardButton('Перевести')
    btn3 = telebot.types.KeyboardButton('История')
    markup.add(btn1, btn2, btn3)
    text = 'Главное меню'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(regexp='Я в консоли')
def print_me(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Меню')
    markup.add(btn1)
    print(message.from_user.to_dict())
    text = f'Ты: {message.from_user.to_dict()}'
    bot.send_message(message.chat.id, text, reply_markup=markup)


def check_admin(message):
    return message.from_user.id == ADMIN_ID and message.text.lower() == 'админка' 

@bot.message_handler(func=check_admin)
def admin_panel(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Общий баланс')
    btn2 = telebot.types.KeyboardButton('Все юзеры')
    markup.add(btn1, btn2)
    text = f'Админ-панель'
    bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.message_handler(func=lambda message: message.from_user.id == ADMIN_ID and message.text == "Все юзеры")
def all_users(message):
    get_all_users(message)


def get_all_users(msg):
    text = f'Юзеры'
    inline_markup = telebot.types.InlineKeyboardMarkup(row_width=5)
    for user in users:
        inline_markup.add(\
            telebot.types.InlineKeyboardButton(\
            text=f'Юзер: {user.get("name")}',
            callback_data=f'user_{user.get("id")}'))
    if isinstance(msg, telebot.types.Message):
        bot.send_message(msg.chat.id, text, reply_markup=inline_markup)
    elif isinstance(msg, telebot.types.CallbackQuery):
        bot.edit_message_text(text="Юзеры:",
                              chat_id=msg.message.chat.id,
                              message_id=msg.message.message_id,
                              reply_markup=inline_markup)  # прикрепляем нашу разметку к ответному сообщению

def get_users_info(call):
    user_id = call.data.split('_')[1]
    inline_markup = telebot.types.InlineKeyboardMarkup()
    for user in users:
        if str(user['id'] == user_id):
            inline_markup.add(telebot.types.InlineKeyboardButton(text="Назад", callback_data='users'),
                                telebot.types.InlineKeyboardButton(text="Удалить юзера", callback_data=f'delete_user_{user_id}'
                                ))
            bot.edit_message_text(text=f'Данные по юзеру:\n'
                                        f'ID: {user["id"]}\n'
                                        f'Имя: {user["name"]}\n'
                                        f'Ник: {user["nick"]}\n'
                                        f'Баланс: {user["balance"]}\n',
                                        chat_id=call.message.chat.id,
                                        message_id=call.message.message_id,
                                        reply_markup=inline_markup
                                        )
            break


def delete_user(user_id):
    for i, user in enumerate(users):
        if user['id'] == user_id:
            print(f'delete user - {user["name"]}')
            users.pop(i)


# Принимает от CallbackQuery()
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    query_type = call.data.split('_')[0]
    if query_type == 'user':
        get_users_info(call)
        print(type(call))
    if query_type == 'users':
        get_all_users(call)
    if query_type == 'delete' and call.data.split('_')[1] == 'user':
        user_id = int(call.data.split('_')[2])
        delete_user(user_id)
        get_all_users(call)

@bot.message_handler(func=lambda message: message.from_user.id == ADMIN_ID and message.text == "Общий баланс")
def total_balance(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('Меню')
    btn2 = telebot.types.KeyboardButton('Админка')
    markup.add(btn1, btn2)
    balance = 0
    for user in users:
        balance += user['balance']
    text = f'Общий баланс: {balance}'
    bot.send_message(message.chat.id, text, reply_markup=markup)

bot.infinity_polling()