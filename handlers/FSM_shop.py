from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import buttons

class Shop(StatesGroup):
    model_name = State()
    size = State()
    category = State()
    price = State()
    photo = State()
    submit = State()

async def fsm_start(message: types.Message):
    await Shop.model_name.set()
    await message.answer(text="Введите название модели:", reply_markup=buttons.cancel)

async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['model_name'] = message.text

    await Shop.next()
    await message.answer(text='Введите свой размер:')


async def load_size(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['size'] = message.text

    await Shop.next()
    await message.answer(text='Введите категорию:')


async def load_category(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['category'] = message.text

    await Shop.next()
    await message.answer(text='Введите цену:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text

    await Shop.next()
    await message.answer(text='Отправьте фото:')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[-1].file_id


    keyword = InlineKeyboardMarkup(row_width=2)
    yes_button = InlineKeyboardButton(text='Yes', callback_data='confirm_yes')
    no_button = InlineKeyboardButton(text='No', callback_data='confirm_no')
    keyword.add(yes_button,no_button)

    await Shop.next()
    await message.answer_photo(photo=data['photo'],
                               caption=f"Название модели - {data['model_name']}\n"
                                       f"Размер - {data['size']}\n"
                                       f"Категория - {data['category']}\n"
                                       f"Цена - {data['price']}\n\n"
                                       f"<b>Верные данные ?</b>",
                               reply_markup=keyword, parse_mode=types.ParseMode.HTML)

async def submit (callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.data == 'confirm_yes':
        await callback_query.answer('Отлично! Вы купили товар', reply_markup=buttons.start_buttons )
        await state.finish()
    elif callback_query.data == 'confirm_no':
        await callback_query.message.answer('Отменено', reply_markup=buttons.start_buttons )
        await state.finish()
    else:
        await callback_query.message.answer(text='Нажмите на кнопку!')


async def cancel_fms(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer(text='Отменено')



def register_fsm_for_user(dp: Dispatcher):
    dp.register_message_handler(cancel_fms,Text(equals='Отмена',
                                                ignore_case=True), state='*')
    dp.register_message_handler(fsm_start, commands=['shop'])
    dp.register_message_handler(load_name, state=Shop.model_name)
    dp.register_message_handler(load_size, state=Shop.size)
    dp.register_message_handler(load_category, state=Shop.category)
    dp.register_message_handler(load_price, state=Shop.price)
    dp.register_message_handler(load_photo, state=Shop.photo, content_types=['photo'])
    dp.register_callback_query_handler(submit, state=Shop.submit)