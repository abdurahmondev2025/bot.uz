from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from utils.statics.keyboards import ABOUT_US,ADDRESS,CONTACT,COURSE,My_CONTACT,MY_LOCATION,FAQ

default_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton(text=ABOUT_US),
        KeyboardButton(text=ADDRESS),
        KeyboardButton(text=CONTACT),
        KeyboardButton(text=COURSE),

    ],
    [
        KeyboardButton(text=My_CONTACT, request_contact=True),
        KeyboardButton(text=MY_LOCATION, request_location=True)
    ],
    [
        KeyboardButton(text=FAQ)
    ]

])