import telebot 

bot = telebot.TeleBot('5831486734:AAGLPj77zzky_CZO7cvygiFnnT7GwmJyUaY')

#comands
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,"Comands")

@bot.message_handler(regexp=r'[0-9]+')
def start(message):
    bot.send_message(message.chat.id,"regexp")

# chat_types
@bot.message_handler(chat_types=['private'])
def start(message):
    bot.send_message(message.chat.id,message.chat.type)

#content_types
@bot.message_handler(content_types=['photo'])
def start(message):
    bot.send_message(message.chat.id,"Content_types: photo")

# regexp
@bot.message_handler(regexp=r'[0-9]+')
def start(message):
    bot.send_message(message.chat.id,"regexp")

#func 
@bot.message_handler(func=lambda x:'a')
def start(message):
    bot.send_message(message.chat.id,"func")

bot.polling()

#їх можна перечислювати через кому
#comands
# chat_types
#content_types
# regexp
#func 