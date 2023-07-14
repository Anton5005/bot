import Oror
from datetime import datetime
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


# створення бота
bot = Bot('5887488636:AAEtc9otfhVPvaOOOrazVPOJeUKyKCFFiPA')
dp = Dispatcher(bot)

@dp.message_handler(commands=['web'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Відкрити веб сторінку', web_app=WebAppInfo(url='https://www.google.com')))
    await message.answer('Привіт', reply_markup=markup)

# функція для повернення команди 
@dp.message_handler(commands=['start'])
async def start(message: types.Message):                                         
    await bot.send_message(message.chat.id, "Ви запустили бота")


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    urlbtn = types.InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/')
    switch = types.InlineKeyboardButton(text='Вибрати чат', switch_inline_query='/start')
    btn = types.InlineKeyboardButton(text='CallBack', callback_data='btn')
    kb.add(urlbtn, switch, btn)
    await bot.send_message(message.chat.id, 'Message', reply_markup=kb)


@dp.callback_query_handler(lambda callback: callback.data)
async def check_callback_data(callback_query: types.CallbackQuery):
    if callback_query.data == 'btn':
        await bot.send_message(callback_query.message.chat.id, "Callback button clicked ")


@dp.message_handler(commands=['button'])
async def button(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton(text='Згоден')
    btn2 = types.KeyboardButton(text='Не згоден')
    kb.add(btn1, btn2)
    await bot.send_message(message.chat.id, 'Запущено допоміжну клавіатуру', reply_markup=kb)


@dp.message_handler(commands=['history'])
async def history(message: types.Message):
    result = Oror.history(str(message.chat.id))
    text = result[0]
    messenger_channel_id = result[1]
    await bot.send_message(messenger_channel_id, text)


@dp.message_handler(commands=['delete'])
async def delete(message: types.Message):
    Oror.delete(str(message.chat.id))
    await bot.send_message(message.chat.id, "Історію очищено")


@dp.message_handler()
async def message(message: types.Message):
    date = message.date
    datetime_obj = datetime.fromtimestamp(date.timestamp())
    result = Oror.message(str(message.from_user.id), message.from_user.username, str(message.chat.id), message.chat.type, message.text, datetime_obj)
    text = result[0]
    messenger_channel_id = result[1]
    await bot.send_message(messenger_channel_id, text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
