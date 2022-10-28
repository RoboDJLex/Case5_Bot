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
                bot.register_next_step_handler(msg, UserData)
                user.fullname=m.text
        elif m.text.strip() == 'Добавить умения':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1=types.KeyboardButton("1")
                item2=types.KeyboardButton("2")
                item3=types.KeyboardButton("3")
                item4=types.KeyboardButton("4")
                item5=types.KeyboardButton("5")
                item6=types.KeyboardButton("6")
                item7=types.KeyboardButton("7")
                item8=types.KeyboardButton("8")
                item9=types.KeyboardButton("9")
                item10=types.KeyboardButton("10")
                item11=types.KeyboardButton("Далее")
                markup.add(item1)
                markup.add(item2)
                markup.add(item3)
                markup.add(item4)
                markup.add(item5)
                markup.add(item6)
                markup.add(item7)
                markup.add(item8)
                markup.add(item9)
                markup.add(item10)
                markup.add(item11)
                msg = bot.send_message (m.chat.id, 'Выберите подходящие Вам софт-скилы', reply_markup=markup)

def UserData(m):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Изменить имя")
        item2=types.KeyboardButton("Добавить теги")
        markup.add(item1)
        markup.add(item2)
        bot.send_message (m.chat.id, 'Вас зовут:'+m.text, reply_markup=markup)

bot.infinity_polling()