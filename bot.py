import os
import asyncio
import logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F
from aiogram.filters import Text



load_dotenv()
TOKEN = os.environ["TOKEN"]
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN, parse_mode="HTML")
# Диспетчер
dp = Dispatcher()



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Я буду делать..."),
            types.KeyboardButton(text="Планов нет")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Расскажите что будете делать"
    )
    await message.answer("Какие планы на сегодня?", reply_markup=keyboard)

@dp.message(Text("Я буду делать..."))
async def got_what_todo(message: types.Message):
    await message.reply("Очередной продуктивный день!"
                        "Давай, поделись своими планами друг")

@dp.message(lambda message: message.text == "Планов нет")
async def without_what_todo(message: types.Message):
    await message.reply("Понятно! Отдых тоже необходим!")

@dp.message(Command("end"))
async def cmd_start(message: types.Message):
    await message.reply("Хорошая работа! "
                        "Осталось дело за малым — сделать, то что написано :)")
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())
