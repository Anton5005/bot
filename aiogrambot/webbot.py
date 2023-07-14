import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.utils.exceptions import Unauthorized
from aiogram.utils.markdown import hbold

# Replace YOUR_TOKEN with your bot token from BotFather
bot = Bot(token='5833356332:AAHgEjX51ReShVrx2J9yrx6NfG9OJ1Yt2gI')
dp = Dispatcher(bot, storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)


class ConfirmDelete(StatesGroup):
    delete = State()

@dp.message_handler(commands=['web'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Відкрити веб сторінку', web_app=WebAppInfo(url='https://www.google.com')))
    await message.answer('Привіт', reply_markup=markup)
    

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привіт! Щоб видалити всі повідомлення з чату, напишіть команду /delete.")


@dp.message_handler(commands=['delete'])
async def cmd_delete(message: types.Message):
    try:
        await message.reply("Ви впевнені, що хочете видалити всі повідомлення з чату?",
                            reply_markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                            .add(types.KeyboardButton("Так, видалити всі повідомлення"))
                            .add(types.KeyboardButton("Ні, не видаляти нічого")))
        await ConfirmDelete.delete.set()
    except Unauthorized:
        await message.reply("Я не можу видалити повідомлення з цього чату, оскільки не маю необхідних прав.")


@dp.message_handler(state=ConfirmDelete.delete, content_types=types.ContentTypes.TEXT)
async def process_delete_confirmation(message: types.Message, state: FSMContext):
    if message.text == "Так, видалити всі повідомлення":
        try:
            async for msg in bot.iter_history(chat_id=message.chat.id):
                await bot.delete_message(chat_id=message.chat.id, message_id=msg.message_id)
            await message.reply("Усі повідомлення з чату були видалені.")
        except Unauthorized:
            await message.reply("Я не можу видалити повідомлення з цього чату, оскільки не маю необхідних прав.")
    else:
        await message.reply("Видалення повідомлень з чату було скасовано.")
    await state.finish()


@dp.message_handler(commands=['delete_all'])
async def delete_all_messages(message: types.Message):
    await message.answer("Підтвердьте видалення усіх повідомлень з чату. Щоб підтвердити, надішліть команду /confirm_deletion")
    
@dp.message_handler(commands=['confirm_deletion'])
async def process_delete_confirmation(message: types.Message):
    # Отримуємо всі повідомлення з чату
    async for msg in bot.iter_history(chat_id=message.chat.id):
        # Видаляємо кожне повідомлення        
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
