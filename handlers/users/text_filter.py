from aiogram import F, Router
from aiogram.types import Message

from keyboards.default.button import default_keyboard
from keyboards.inline.button import url_keyboard, inline_keyboard
from utils.statics.keyboards import ABOUT_US, ADDRESS, CONTACT, COURSE, FAQ
from utils.statics.answers import ANSWER, KUESTION, ANSWER_5, ANSWER_2, ANSWER_3, ANSWER_4, TELEGRAPH_LINK

router = Router()


@router.message(F.text == ABOUT_US)
async def about_us(message: Message):
    file_id = 'AgACAgIAAxkBAVmz62d-nh-ymfRuMWE9wxjjCp-73YbIAALF6DEbiPL5S5O9tmeAmHHFAQADAgADcwADNgQ'

    await message.answer_photo(photo=file_id, caption='Biz ziyo school maktabida IT sohasini o`rgatamiz')


@router.message(F.text == ADDRESS)
async def about_us(message: Message):
    Latitude = 41.409436
    Longitude = 69.307917
    await message.answer_location(latitude=Latitude, longitude=Longitude)
    await message.answer('ziyo o`quv markazi')


@router.message(F.location)
async def handle_location(message: Message):
    lat, long = message.location.latitude, message.location.longitude
    await (f"{lat},{long}")


@router.message(F.text == CONTACT)
async def about_num(message: Message):
    contact = '+998882909709'
    await message.answer_contact(phone_number=contact, first_name='Admin', last_name='Asil')


@router.message(F.text == COURSE)
async def send_coourse_data(message: Message):
    filem_id = 'AgACAgIAAxkBAVmzAmd-mEM485XnB4Jvmv9ke9ix6-cqAAKP6DEbiPL5SxS29AuSeg9NAQADAgADcwADNgQ'

    await message.answer_photo(photo=filem_id, caption='ziyo school kurslari!', reply_markup=url_keyboard)

'marcdown'
@router.message(F.text == FAQ)
async def send_faq(message: Message):
    await message.answer(text=KUESTION, reply_markup=inline_keyboard)

    await message.answer(text=TELEGRAPH_LINK)

# @router.message(F.text==)
@router.message(F.text.startswith("/kuiz"))
async def send_answer_one(message: Message):
    command = message.text
    if command == "/kuiz_1":
        await  message.answer(text=ANSWER)
    elif command == "/kuiz_2":
        await  message.answer(text=ANSWER_2)
    elif command == "/kuiz_3":
        await  message.answer(text=ANSWER_3)
    elif command == "/kuiz_4":
        await  message.answer(text=ANSWER_4)
    elif command == "/kuiz_5":
        await  message.answer(text=ANSWER_5)
    else:
        await message.reply("Mavjud bo`lmagan kommand")
