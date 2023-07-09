import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram import F

from config_reader import config


logging.basicConfig(level=logging.INFO)
bot = Bot(token=config.bot_token.get_secret_value(), parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_test1(message: types.Message):
    await message.reply("""
            Привет! Какие планы на день?
    """)


@dp.message(F.text)
async def task_answer(message: types.Message):
    await message.reply("Отлично, Хотите добавить описание?")
