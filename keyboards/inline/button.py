from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="❓kuiz 1", callback_data="kone"),
    ],
    [
        InlineKeyboardButton(text="❓kuiz 2", callback_data="ktwo"),
    ],
    [
        InlineKeyboardButton(text="❓kuiz 3", callback_data="kthree"),
    ],
    [
        InlineKeyboardButton(text="❓kuiz 4", callback_data="kfour"),
    ],
    [
        InlineKeyboardButton(text="❓kuiz 5", callback_data="qfive")
    ]
])
url_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Telegram', url='https://t.me/@ziyo_school'),
        InlineKeyboardButton(text='Instagram', url='https://instagram.com/@ziyo_school')
    ]
])
