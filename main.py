from config import dp
from aiogram.utils import executor
from handlers import commands, echo
import logging

commands.register_commands(dp)



# Эхо функция вызывать самым последним
echo.register_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)