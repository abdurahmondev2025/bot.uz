
from aiogram import F,Router
from aiogram.types import Message
filters_router=Router()



@filters_router.message(F.contact | F.location)
async  def about_us(message:Message):
   await message.answer('👍️️️️ Qabul qilindi rahmat!')


