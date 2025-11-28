import telebot
from telebot import types
import os
bot = telebot.TeleBot('TOKEN')
menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
a = types.KeyboardButton('Расписание на пн')
b = types.KeyboardButton('Время на пн')
c = types.KeyboardButton('Расписание на вт')
j = types.KeyboardButton('Расписание на ср')
d = types.KeyboardButton('Время на вт,ср')
e = types.KeyboardButton('Расписание на чт')
f = types.KeyboardButton('Время на чт')
g = types.KeyboardButton('Расписание на пт')
i = types.KeyboardButton('Время на пт')
menu.add(a, b, c, j, d, e, f, g, i)  
back = types.ReplyKeyboardMarkup(resize_keyboard=True)
back_button = types.KeyboardButton('Назад')
back.add(back_button)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет!', reply_markup = menu)
@bot.message_handler(func=lambda message: message.text == 'Расписание на пн')
def send_monday_schedule(message):
    try:
        with open('raspisanie_pn.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption='Расписание на понедельник')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Файл не найден')
@bot.message_handler(func=lambda message: message.text == 'Время на пн')
def send_monday_time(message):
    bot.send_message(message.chat.id, 'Время пар на понедельник:\n 8:00-8:45\n .....:')
@bot.message_handler(func=lambda message: message.text == 'Расписание на вт')
def send_tue_schedule(message):
    try:
        with open('raspisanie_vt.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption='Расписание на вторник')
    except FileNotFoundError:
         bot.send_message(message.chat.id, 'Файл не найден')
@bot.message_handler(func=lambda message: message.text == 'Расписание на ср')
def send_wed_schedule(message):
    try:
        with open('raspisanie_sr.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption='Расписание на среду')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Файл не найден')
        
@bot.message_handler(func=lambda message: message.text == 'Время на вт,ср')
def send_tue_wed_time(message):
    bot.send_message(message.chat.id, 'Время пар на вторник и среду:\n 8:30-10:05\n ....')
@bot.message_handler(func=lambda message: message.text == 'Расписание на чт')
def send_thursday_schedule(message):
    try:
        with open('raspisanie_chetverg.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption='Расписание на четверг')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Файл с расписанием не найден')
@bot.message_handler(func=lambda message: message.text == 'Время на чт')
def send_thursday_time(message):
    bot.send_message(message.chat.id, 'Время пар на четверг:\n 8:30-10:05\n Перемена 20 мин\n ....')
@bot.message_handler(func=lambda message: message.text == 'Расписание на пт')
def send_friday_schedule(message):
    try:
        with open('raspisanie_pt.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption='Расписание на пятницу')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Файл с расписанием не найден')
@bot.message_handler(func=lambda message: message.text == 'Время на пт')
def send_friday_time(message):
    bot.send_message(message.chat.id, ' Время пар на пятницу:\n 8:30-10:05\n ......')





bot.infinity_polling()

