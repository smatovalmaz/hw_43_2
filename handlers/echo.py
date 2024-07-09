from aiogram import types, Dispatcher


async def echo(message: types.Message):
    text=message.text

    if text.isdigit():
        await message.answer(int(text)**2)
    else:
        await message.answer(text)

    # def send_file(file_path):
    #     print(f"Sending file: {file_path}")

    #
    # message1 = 5
    # message2 = "Hello, world!"
    # file_path = "example.txt"
    #
    # result1 = message_handler(message1)
    # result2 = message_handler(message2)
    #
    # print(f"Result 1: {result1}")
    # print(f"Result 2: {result2}")
    #
    # send_file(file_path)




def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo)