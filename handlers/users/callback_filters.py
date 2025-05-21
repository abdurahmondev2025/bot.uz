from aiogram.types import CallbackQuery
from aiogram   import F,Router
from utils.statics.answers import ANSWER,ANSWER_2,ANSWER_3,ANSWER_4,ANSWER_5
callback_router=Router()


@callback_router.callback_query(F.data.startswith("k"))
async def inline_button(call:CallbackQuery):
    command = call.data
    if command == "kone":
        await call. message.answer(text=ANSWER)
    elif command == "ktwo":
        await call. message.answer(text=ANSWER_2)
    elif command == "kthree":
        await call. message.answer(text=ANSWER_3)
    elif command == "kfour":
        await call. message.answer(text=ANSWER_4)
    elif command == "kfive":
        await call. message.answer(text=ANSWER_5)
    else:
        await call.message.reply("Mavjud bo`lmagan kommandanda")
