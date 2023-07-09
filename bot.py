import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
load_dotenv()
TOKEN = os.environ["TOKEN"]
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN, parse_mode="HTML")
# Диспетчер
dp = Dispatcher()



@dp.message(Command("start"))
async def cmd_test1(message: types.Message):
    await message.reply("""
            Привет! Какие планы на день?
    """)
@dp.message(F.text)
async def task_answer(message: types.Message):
    await message.reply("Отлично, Хотите добавить описание?")
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
