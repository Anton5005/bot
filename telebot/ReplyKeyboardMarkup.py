import telebot 
from telebot import types

bot = telebot.TeleBot('5831486734:AAGLPj77zzky_CZO7cvygiFnnT7GwmJyUaY')


@bot.message_handler(commands=['Button'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=1)
    btn1 = types.KeyboardButton(text = 'Button1')
    btn2 = types.KeyboardButton(text = 'Button2')
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id,'1',reply_markup=kb)




bot.polling()