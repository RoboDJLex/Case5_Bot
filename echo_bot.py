import telebot
from telebot import types
import models, inventory

bot = telebot.TeleBot("5620161730:AAEHy5MphcICV2Uo8izjqkAArQvGUL1vOXI", parse_mode=None)

@bot.message_handler(commands=["start"])
def start(m):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Ввести имя")
        item2=types.KeyboardButton("Добавить умения")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(m.chat.id, 'Привет!\nСоздай анкету.',  reply_markup=markup)
user = models.User
user.soft_skills = []
user.hard_skills = []
user.character = []
@bot.message_handler(content_types=["text"])
def hadle_text(m):
        user.id = m.chat.id
        if m.text.strip() == 'Ввести имя' or m.text.strip() == 'Изменить имя':
                msg = bot.send_message (m.chat.id, 'Введите Фамилию и Имя', reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, UserData)
                user.fullname = m.text
        if m.text.strip() == 'Добавить умения':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                
                for tag in inventory.soft_tags:
                        markup.add(types.KeyboardButton(tag))

                markup.add(types.KeyboardButton("Далее"))

                bot.send_message (m.chat.id, 'Выберите подходящие Вам софт-скилы', reply_markup=markup)
                while m.text.strip()!= 'Далее':
                        user.soft_skills.append(m.text)

        if m.text.strip() == 'Далее':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

                for tag in inventory.hard_tags:
                        markup.add(types.KeyboardButton(tag))

                markup.add(types.KeyboardButton("Следующее"))

                bot.send_message (m.chat.id, 'Выберите подходящие Вам хард-скилы', reply_markup=markup)
                while m.text.strip()!= 'Следующее':
                        user.hard_skills.append(m.text)

        if m.text.strip() == 'Следующее':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

                for tag in inventory.character_tags:
                        markup.add(types.KeyboardButton(tag))

                markup.add(types.KeyboardButton("Завершить"))

                bot.send_message (m.chat.id, 'Выберите подходящие Вам личностные качества', reply_markup=markup)
                while m.text.strip()!= 'Завершить':
                        user.character.append(m.text)
                #UserData(m)
        

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


#______________________________TODOLIST__________________________________#
#1. Подписи к кнопкам софт/хард скилов и личностных.
#2. Экспорт данных во флэт файл.
#3. Импорт данных из флэт файла в адекватно выглядящую анкету.
#4. 