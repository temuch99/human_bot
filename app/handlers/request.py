from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from app.database import session
from app.utils.formats import Fio, Number, Surname
from app.searcher import Searcher

import json
import time

class OrderRequest(StatesGroup):
    waiting_for_request = State()


async def request_start(message: types.Message, state: FSMContext):
    await message.answer(
        """
        Указанный бот позволяет искать лиц. Чтобы начать поиск введите /request.
        """,
        reply_markup=types.ReplyKeyboardRemove()
    )

async def request(message: types.Message):
    await message.answer("""
        Введите ФИО человек, название организации или идентификатор:\nДоступные форматы ФИО: Иванов Иван Иванович, Иванов И.И.\nТелефонных номеров: 79*********
        """)
    await OrderRequest.waiting_for_request.set()


async def request_chosen(message: types.Message, state: FSMContext):
    if not Fio.check(message.text) and not Number.check(message.text) and not Surname.check(message.text):
        await message.answer("Пожалуйста, введите корректные данные")
        return
    
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Здесь осуществляется поиск
    results = Searcher.execute(session, message.text.lower())
    file_name = int(time.time())
    with open('tmp/{}.json'.format(file_name), 'w') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    # Здесь можно ввести иные типы запросов в виде инлайн кнопок
    # for result in results:
    #     keyboard.add(types.InlineKeyboardButton(text=json.dumps(result)))

    await message.answer_document(open('tmp/{}.json'.format(file_name), 'r'))
    await message.answer(
        f"Выберите, что делать дальше или введите следующий запрос",
        reply_markup=keyboard
    )
    await OrderRequest.waiting_for_request.set()

async def request_cancel(message: types.Message):
    await message.answer(
        """Чтобы продолжить выполнение запросов введите /request""",
        reply_markup=types.ReplyKeyboardRemove
    )


def register_handlers(dp: Dispatcher):
    dp.register_message_handler(request_start, commands="start", state="*")
    dp.register_message_handler(request, commands="request", state="*")
    dp.register_message_handler(request_chosen, state=OrderRequest.waiting_for_request)
    dp.register_message_handler(request_cancel, commands="cancel", state="*")   
