import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os
import asyncio

API_TOKEN = "1160086050:AAF54-FHpGmoqoQI5MnQipruax7vm_uenI0"

logging.basicConfig(level=logging.DEBUG)

event_loop = asyncio.get_event_loop()

storage = MemoryStorage()
bot = Bot(token=API_TOKEN, loop=event_loop)
dp = Dispatcher(bot, storage=storage)
db = event_loop.run_until_complete(create_pool())


if __name__ == "__main__":
    from handlers.commands_bot import dp
    executor.start_polling(dp, loop=event_loop, skip_updates=True)
