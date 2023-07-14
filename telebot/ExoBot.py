import telebot 

bot = telebot.TeleBot('5831486734:AAGLPj77zzky_CZO7cvygiFnnT7GwmJyUaY')

#відповідає на команду
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Hello")

#exo comand
@bot.message_handler(commands=['return'])
def start(message):
    bot.send_message(message.chat.id,message.text)

#вивід всієї інформації при вводі команди /information
@bot.message_handler(commands=['information'])
def start(message):
    bot.send_message(message.chat.id,message)

@bot.message_handler(func=lambda message: message.text =='1')
def start(message):
    bot.reply_to(message,message.text)


bot.polling()















