from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '5184036850:AAGVJYNDWkrpkSa1LW4AsaKlKpclQCF3BoU'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        f"Привет {message.from_user.full_name}!"
        )

@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True)
