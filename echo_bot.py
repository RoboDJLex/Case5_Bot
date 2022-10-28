from asyncio.windows_events import NULL
from re import X
import telebot
from telebot import types
import models

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
        user = models.User
        user.id = m.chat.id
        bot.send_message (m.chat.id, 'Ваш ID:'+str(m.chat.id))
        if m.text.strip() == 'Ввести имя':
                msg = bot.send_message (m.chat.id, 'Введи Фамилию и Имя', reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, UserName)
                user.fullname=m.text
        elif m.text.strip() == 'Добавить тег':
                bot.send_message (m.chat.id, 'Введи Теги')

def UserName(m):
        bot.send_message (m.chat.id, 'Вас зовут:'+m.text)

bot.infinity_polling()