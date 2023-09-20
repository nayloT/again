from config import Config
from aiogram import Bot, types, Dispatcher, executor


BOT_TOKEN = Config.BOT_TOKEN
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer('Здравствуй, дорогой пользователь!\nИспользуй команду /about для того, чтобы узнать о функциях бота.')


@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    await message.answer('Это бот, созданный учеником 10 класса. Бот готов помогать Вам!')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)