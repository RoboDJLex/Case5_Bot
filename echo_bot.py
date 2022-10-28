from asyncio.windows_events import NULL
import telebot
from telebot import types
import models

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
user.soft_skills = NULL
user.hard_skills = NULL
user.character = NULL
@bot.message_handler(content_types=["text"])
def hadle_text(m):
        user.id = m.chat.id
        if m.text.strip() == 'Ввести имя' or m.text.strip() == 'Изменить имя':
                msg = bot.send_message (m.chat.id, 'Введите Фамилию и Имя', reply_markup=types.ReplyKeyboardRemove())
                bot.register_next_step_handler(msg, UserData)
                user.fullname=m.text
        if m.text.strip() == 'Добавить умения':
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
                bot.send_message (m.chat.id, 'Выберите подходящие Вам софт-скилы', reply_markup=markup)
                while m.text.strip()!= 'Далее':
                        user.soft_skills.append(m.text)
        if m.text.strip() == 'Далее':
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
                item11=types.KeyboardButton("Следующее")
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
                bot.send_message (m.chat.id, 'Выберите подходящие Вам хард-скилы', reply_markup=markup)
                while m.text.strip()!= 'Следубщее':
                        user.hard_skills.append(m.text)
        if m.text.strip() == 'Следующее':
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
                item11=types.KeyboardButton("Завершить")
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
                bot.send_message (m.chat.id, 'Выберите подходящие Вам личностные качества', reply_markup=markup)
                while m.text.strip()!= 'Завершить':
                        user.character.append(m.text)
        return UserData

def UserData(m):
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("Изменить имя")
        item2=types.KeyboardButton("Добавить теги")
        markup.add(item1)
        markup.add(item2)
        bot.send_message (m.chat.id, 'Ваш ID: '+user.id+'\nВас зовут: '+user.fullname+'\nВаши софт-скилы: '+user.soft_skills+'\nВаши хард-скилы: '+user.hard_skills+'\nВаши личностные качества: '+user.character, reply_markup=markup)

bot.infinity_polling()


#______________________________TODOLIST__________________________________#
#1. Подписи к кнопкам софт/хард скилов и личностных.
#2. Экспорт данных во флэт файл.
#3. Импорт данных из флэт файла в адекватно выглядящую анкету.
#4. 