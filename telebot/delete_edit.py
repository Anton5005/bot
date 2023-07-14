import telebot 

bot = telebot.TeleBot('5831486734:AAGLPj77zzky_CZO7cvygiFnnT7GwmJyUaY')


@bot.message_handler(commands=['delete'])
def delete(message):
    bot.delete_message(message.chat.id,message.id)

@bot.message_handler(commands=['edit'])
def delete(message):
    message1 = bot.send_message(message.chat.id,'hi')
    bot.edit_message_text(chat_id=message.chat.id,message_id=message.id, text="edit")


bot.polling()