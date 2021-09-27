"""
    This is a echo bot.
    It echoes any incoming text messages.
    """
import wikipedia

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1925944793:AAH0TQDEMCxND4Nrt9xdGiAEjtdFvcxMpXQ'

wikipedia.set_lang('uz')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)

        await message.answer(respond)

    except:
        await message.answer("Bunday maqola topilmadi.Iltimos boshqa mavzuni kiriting!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
