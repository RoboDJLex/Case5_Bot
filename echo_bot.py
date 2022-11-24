import telebot
from telebot import types
import models, inventory

bot = telebot.TeleBot("5620161730:AAEHy5MphcICV2Uo8izjqkAArQvGUL1vOXI", parse_mode=None)

user = models.User
user.fullname = ''
user.soft_skills = []
user.hard_skills = []
user.character = []

@bot.message_handler(commands=["start"])
def start(m):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Ввести имя")
        item2=types.KeyboardButton("Добавить умения")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Привет!\nСоздай анкету.',  reply_markup=markup)

@bot.message_handler(content_types=["text"])
def handle_text(m):
        user.id = m.chat.id
        if m.text.strip() == 'Ввести имя' or m.text.strip() == 'Изменить имя':
                msg = bot.send_message (m.chat.id, 'Введите Фамилию и Имя', reply_markup=types.ReplyKeyboardRemove())

                bot.register_next_step_handler(msg, Naming)

        if m.text.strip() == 'Добавить умения':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                
                for tag in inventory.soft_tags:
                        markup.add(types.KeyboardButton(tag))

                markup.add(types.KeyboardButton("Далее"))

                bot.send_message (m.chat.id, 'Выберите подходящие Вам софт-скилы', reply_markup=markup)

                add_soft_skill(m)

def Naming(m):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Изменить имя")
        item2=types.KeyboardButton("Добавить умения")
        markup.add(item1)
        markup.add(item2)
        user.fullname = m.text.strip()
        bot.send_message (m.chat.id, 'Вас зовут: '+user.fullname, reply_markup=markup)
        
def add_soft_skill(m):
        if m.text=='Далее':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                
                for tag in inventory.hard_tags:
                        markup.add(types.KeyboardButton(tag))

                markup.add(types.KeyboardButton("Следующее"))

                bot.send_message (m.chat.id, 'Выберите подходящие Вам хард-скилы', reply_markup=markup)
                add_hard_skill(m)
        else:
                user.soft_skills.append(m.text)

                msg=bot.send_message (m.chat.id, 'Ваши софт-скилы: '+' '.join(user.soft_skills))
                
                bot.register_next_step_handler(msg, add_soft_skill)

def add_hard_skill(m):
        if m.text=='Следующее':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                
                for tag in inventory.character_tags:
                        markup.add(types.KeyboardButton(tag))

                markup.add(types.KeyboardButton("Сохранить"))

                bot.send_message (m.chat.id, 'Выберите подходящие Вам личностные качества', reply_markup=markup)
                add_character(m)
        else:
                msg=bot.send_message (m.chat.id, 'Ваши хард-скилы: '+' '.join(user.hard_skills))

                user.hard_skills.append(m.text)

                bot.register_next_step_handler(msg, add_hard_skill)

def add_character(m):
        if m.text=='Сохранить':
                UserData(m, user)
        else:
                msg=bot.send_message (m.chat.id, 'Ваши личностные качества: '+' '.join(user.character))

                user.character.append(m.text)

                bot.register_next_step_handler(msg, add_character)


def UserData(m, user):
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

#bot.enable_save_next_step_handlers(delay=0.5)

#bot.load_next_step_handlers()

bot.infinity_polling()