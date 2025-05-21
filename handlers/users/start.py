from aiogram.types import Message
from aiogram import html,Router
from aiogram.filters import CommandStart
from keyboards.default.button import default_keyboard
start_router=Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!", reply_markup=default_keyboard)
