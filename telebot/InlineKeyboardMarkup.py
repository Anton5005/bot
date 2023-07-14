import telebot 
from telebot import types

bot = telebot.TeleBot('5831486734:AAGLPj77zzky_CZO7cvygiFnnT7GwmJyUaY')

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    urlbtn = types.InlineKeyboardButton(text = 'YouTube', url='https://www.youtube.com/')
    
    switch = types.InlineKeyboardButton(text = 'Вибрати чат', switch_inline_query='/start')

    btn = types.InlineKeyboardButton(text = 'CallBack', callback_data='btn')

    kb.add(urlbtn,switch,btn)
    bot.send_message(message.chat.id,'Message',reply_markup=kb)


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn':
        bot.send_message(callback.message.chat.id, "Callback button clicked ")




bot.polling()