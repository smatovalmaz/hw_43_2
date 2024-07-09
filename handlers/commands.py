from aiogram.types import InputFile
from aiogram import types, Dispatcher
from config import bot

import glob
import random
import os


async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Привет! {message.from_user.first_name}')



async def mem(message: types.Message):
    path = 'media/'
    files = glob.glob(os.path.join(path + '*'))
    random_photo = random.choice(files)

    await bot.send_photo(chat_id=message.from_user.id,
                         photo=InputFile(random_photo))


async def file(message: types.Message):
    file_path='/Users/almsm10/PycharmProjects/hw_telegrambot/config.py'
    with open(file_path, 'rb') as file:
        await bot.send_document(message.from_user.id, file)

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'начало'])
    dp.register_message_handler(mem, commands=['mem', 'мем'])
    dp.register_message_handler(file, commands=['file'])

