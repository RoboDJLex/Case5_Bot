import telebot
from telebot import types

bot = telebot.TeleBot("5620161730:AAEHy5MphcICV2Uo8izjqkAArQvGUL1vOXI", parse_mode=None)

@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Ввести имя")
        item2=types.KeyboardButton("Добавить тег")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Привет!\nСоздай анкету.',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def hadle_text(m):
        if m.text.strip() == 'Ввести имя':
                bot.send_message (m.chat.id, 'Введи Фамилию и Имя')
        elif m.text.strip() == 'Добавить тег':
                bot.send_message (m.chat.id, 'Введи Теги')
bot.infinity_polling()