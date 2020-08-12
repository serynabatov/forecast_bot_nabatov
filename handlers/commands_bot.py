from aiogram import types
from main_func import bot, dp, storage, event_loop
from handlers.keyboard.keyboard import choice, yes_or_no
from handlers.machine_state import Machine_State
from modes.CurrentWeather import Current_Weather
from aiogram.dispatcher import FSMContext


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message, loop=event_loop):
    await message.reply(text="""Здравствуйте!\n
Я бот, который подсказывает Вам погоду!\n""", reply=False)
    await send_menu(message=message)


@dp.message_handler(commands=['help'])
async def send_menu(message: types.Message, loop=event_loop):
    await message.reply(text="""Давайте дружить! Вот, что я могу:
          /start - начало работы со мной
          /help - справка (Вы на нее сейчас смотрите!)
          /mode - режим предсказывания погоды\n""", reply=False)


@dp.message_handler(commands=['mode'])
async def get_mode(message: types.Message, loop=event_loop):
    await message.answer(text="""Выберите режим моей работы!\n
1 - Введите имя города, и вы получите информацию о погоде""",
    reply_markup=choice)


@dp.callback_query_handler(text_contains="First")
async def prepare_to_get_first(call: types.CallbackQuery, loop=event_loop):
    await call.answer(cache_time=30)
    await call.message.answer("Введите название города")
    await call.message.edit_reply_markup(reply_markup=None)
    await Machine_State.Q1.set()


@dp.message_handler(content_types=['text'], state=Machine_State.Q1)
async def first_mode(message: types.Message, state: FSMContext, loop=event_loop):
    cur = Current_Weather(message.text)
    answer = cur.get_weather()
    if type(answer) == str:
        await message.answer(answer, reply=False)
    else:
        await state.finish()
        await message.answer(text="Температура - {}, давление - {},скорость ветра - {}".format(
                                                                   answer[0], answer[1], answer[2]), 
                             reply_markup=yes_or_no)


@dp.callback_query_handler(text_contains="Yep")
async def continue_messaging(call: types.CallbackQuery, loop=event_loop):
    await call.answer(cache_time=30)
    await call.message.edit_reply_markup(reply_markup=None)
    await get_mode(call.message)


@dp.callback_query_handler(text_contains="Nope")
async def stop_messaging(call: types.CallbackQuery, loop=event_loop):
    await call.answer(cache_time=30)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer("Возвращайтесь!")


@dp.callback_query_handler(text_contains="Abort")
async def cancel(call: types.CallbackQuery, loop=event_loop):
    await call.answer(cache_time=30)
    await call.message.edit_reply_markup(reply_markup=None)
    await call.answer("Не та команда? С кем не бывало")

