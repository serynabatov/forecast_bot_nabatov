from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from handlers.keyboard.callback import remember_callback

choice = InlineKeyboardMarkup(
           inline_keyboard = [
                  [
                     InlineKeyboardButton(text="Ввести название города и узнать погоду",
                                            callback_data = remember_callback.new(item_name="First"))
                  ],
                  [
                     InlineKeyboardButton(text="Отмена", 
                                          callback_data=remember_callback.new(item_name="Abort"))
                  ]
           ]
    

)

yes_or_no = InlineKeyboardMarkup(
             inline_keyboard = [
                [
                   InlineKeyboardButton(text="Продолжим", 
                                     callback_data=remember_callback.new(item_name="Yep"))
		],
                [
                   InlineKeyboardButton(text="Остановись",
                                     callback_data=remember_callback.new(item_name="Nope"))
		]
             ]
)
