from aiogram import types
from aiogram.utils import executor

import buttons
from config import dp, bot, Admin
import logging
from handlers import commands, echo, quiz, FSM_shop

async def on_startup(_):
    for i in Admin:
        await bot.send_message(chat_id=i, text='Bot started',
                               reply_markup=buttons.start_buttons)
async def on_shutdown(_):
    for i in Admin:
        await bot.send_message(chat_id=i, text='Bot stoped')


commands.register_commands(dp)
quiz.register_quiz(dp)
FSM_shop.register_fsm_for_user(dp)


# Эхо функция вызывать самым последним
echo.register_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)