from email.policy import default
import telebot
from telebot import types

bot = telebot.TeleBot("5620161730:AAEHy5MphcICV2Uo8izjqkAArQvGUL1vOXI", parse_mode=None)

@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Ввести имя", callback_data = "1")
        item2=types.KeyboardButton("Добавить тег", callback_data = "2")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Привет!\nСоздай анкету.',  reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_query(call):
        req = call.data.split('_')
        if req == '1':
                bot.send_message(m.chat.id, 'Введите имя')
        elif  req == '2':
                bot.send_message(m.chat.id, 'Введите теги')

bot.infinity_polling()