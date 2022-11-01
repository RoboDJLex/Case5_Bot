#______________________________TODOLIST__________________________________#
#1. Экспорт данных во флэт файл.
#2. Импорт данных из флэт файла в адекватно выглядящую анкету.
#3!!! Забивает на заполнение личностных данных и сразу переходит на вывод.
#4. В умениях на ввод принимает только первое видимое сообщение.

from turtle import goto
import telebot
from telebot import types
import models, inventory

bot = telebot.TeleBot("5620161730:AAEHy5MphcICV2Uo8izjqkAArQvGUL1vOXI", parse_mode=None)


def add_hard_skill(m, user):
        user.hard_skills.append(m.text)

def add_soft_skill(m, user):
        user.soft_skills.append(m.text)

def add_character(m, user):
        user.character.append(m.text)


@bot.message_handler(commands=["start"])
def start(m):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Ввести имя")
        item2=types.KeyboardButton("Добавить умения")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Привет!\nСоздай анкету.',  reply_markup=markup)
user = models.User
user.fullname = ''
user.soft_skills = []
user.hard_skills = []
user.character = []

@bot.message_handler(content_types=["text"])
def hadle_text(m):
        user.id = m.chat.id
        if m.text.strip() == 'Ввести имя' or m.text.strip() == 'Изменить имя':
                msg = bot.send_message (m.chat.id, 'Введите Фамилию и Имя', reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, Naming)
        if m.text.strip() == 'Добавить умения':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                
                for tag in inventory.soft_tags:
                        markup.add(types.KeyboardButton(tag))

                markup.add(types.KeyboardButton("Хард-скилы"))

                bot.send_message (m.chat.id, 'Выберите подходящие Вам софт-скилы', reply_markup=markup)
                while m.text != 'Хард-скилы':
                        bot.register_next_step_handler(m, add_soft_skill, user)
                        if m.text != 'Хард-скилы':
                                break


        if m.text.strip() == 'Хард-скилы':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

                for tag in inventory.hard_tags:
                        markup.add(types.KeyboardButton(tag))

                markup.add(types.KeyboardButton("Личностные"))

                bot.send_message (m.chat.id, 'Выберите подходящие Вам хард-скилы', reply_markup=markup)
                while m.text != 'Личностные':
                        bot.register_next_step_handler(m, add_hard_skill, user)
                        if m.text != 'Личностные':
                                break

        if m.text.strip() == 'Личностные':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

                for tag in inventory.character_tags:
                        markup.add(types.KeyboardButton(tag))

                markup.add(types.KeyboardButton("Сохранить"))

                bot.send_message (m.chat.id, 'Выберите подходящие Вам личностные качества', reply_markup=markup)
                while m.text != 'Сохранить':
                        bot.register_next_step_handler(m, add_character, user)
                        if m.text == 'Сохранить':
                                UserData(m)
                                break
        

def Naming(m):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Изменить имя")
        item2=types.KeyboardButton("Добавить умения")
        markup.add(item1)
        markup.add(item2)
        user.fullname = m.text.strip()
        bot.send_message (m.chat.id, 'Вас зовут: '+user.fullname, reply_markup=markup)

def UserData(m):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Изменить имя")
        item2=types.KeyboardButton("Добавить умения")
        markup.add(item1)
        markup.add(item2)
        bot.send_message (m.chat.id, 'Ваш ID: '+str(user.id), reply_markup=markup)
        bot.send_message (m.chat.id, 'Вас зовут: '+user.fullname)
        bot.send_message (m.chat.id, 'Ваши софт-скилы: '+' '.join(user.soft_skills))
        bot.send_message (m.chat.id, 'Ваши хард-скилы: '+' '.join(user.hard_skills))
        bot.send_message (m.chat.id, 'Ваши личностные качества: '+' '.join(user.character))

bot.infinity_polling()