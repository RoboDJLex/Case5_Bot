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
                item1=types.KeyboardButton("Умение слушать")
                item2=types.KeyboardButton("Аргументация")
                item3=types.KeyboardButton("Самопрезентация")
                item4=types.KeyboardButton("Командная работа")
                item5=types.KeyboardButton("Клиентоориентированность")
                item6=types.KeyboardButton("Стрессоустойчивость")
                item7=types.KeyboardButton("Тайм-менеджмент")
                item8=types.KeyboardButton("Энтузиазм")
                item9=types.KeyboardButton("Креативное мышление")
                item10=types.KeyboardButton("Планирование")
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
                item1=types.KeyboardButton("Social Media")
                item2=types.KeyboardButton("Trello")
                item3=types.KeyboardButton("Machine Learning")
                item4=types.KeyboardButton("Big Data")
                item5=types.KeyboardButton("Python")
                item6=types.KeyboardButton("C++")
                item7=types.KeyboardButton("Java")
                item8=types.KeyboardButton("Flutter")
                item9=types.KeyboardButton("Kotlin")
                item10=types.KeyboardButton("MySQL")
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
                while m.text.strip()!= 'Следующее':
                        user.hard_skills.append(m.text)
        if m.text.strip() == 'Следующее':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1=types.KeyboardButton("Уверенность в себе")
                item2=types.KeyboardButton("Креативность")
                item3=types.KeyboardButton("Строгость")
                item4=types.KeyboardButton("Стремление к победе")
                item5=types.KeyboardButton("Знание особенностей работы")
                item6=types.KeyboardButton("Справедливость")
                item7=types.KeyboardButton("Тактичность")
                item8=types.KeyboardButton("Исполнительность")
                item9=types.KeyboardButton("Принципиальность")
                item10=types.KeyboardButton("Настойчивость")
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