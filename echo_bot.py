import telebot
from telebot import types
import models

bot = telebot.TeleBot("5620161730:AAEHy5MphcICV2Uo8izjqkAArQvGUL1vOXI", parse_mode=None)

@bot.message_handler(commands=["start"])
def start(m, res=False):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Ввести имя")
        item2=types.KeyboardButton("Добавить умения")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Привет!\nСоздай анкету.',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def hadle_text(m):
        user = models.User
        user.id = m.chat.id
        bot.send_message (m.chat.id, 'Ваш ID:'+str(m.chat.id))
        if m.text.strip() == 'Ввести имя' or m.text.strip() == 'Изменить имя':
                msg = bot.send_message (m.chat.id, 'Введите Фамилию и Имя', reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, UserName)
                user.fullname=m.text
        elif m.text.strip() == 'Добавить умения':
                msg = bot.send_message (m.chat.id, 'Введите soft skills', reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, UserSkills)
                user.fullname=m.text

def UserName(m):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Изменить имя")
        item2=types.KeyboardButton("Добавить умения")
        markup.add(item1)
        markup.add(item2)
        bot.send_message (m.chat.id, 'Вас зовут:'+m.text, reply_markup=markup)

bot.infinity_polling()