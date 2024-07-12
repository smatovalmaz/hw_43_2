from aiogram import types, Dispatcher
import random
from config import bot


games=['⚽', '🎰', '🏀', '🎯', '🎳', '🎲']

async def echo(message: types.Message):
    text=message.text

    if text.isdigit():
        await message.answer(int(text)**2)
    elif text=='game':
        randomm=random.choice(games)
        bott=await bot.send_dice(chat_id=message.from_user.id, emoji=randomm)
        users=await bot.send_dice(chat_id=message.from_user.id, emoji=randomm)
        await bot.send_message(
            chat_id=message.from_user.id,
            text=f'bot: {bott.dice.value}\n'
                 f'users: {users.dice.value}'
        )
        if users.dice.value < bott.dice.value:
            await message.answer('бот выиграл')
        elif bott.dice.value < users.dice.value:
            await message.answer('юзер выиграл')
        else:
            await message.answer('ничья')

    else:
        await message.answer(text)




def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo)