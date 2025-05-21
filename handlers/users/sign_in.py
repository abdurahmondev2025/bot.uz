from email.policy import default
from idlelib.window import add_windows_to_menu

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from state.state import FormState


register_router=Router()

@register_router.message(Command("register"))
async def register_start(message:Message,state:FSMContext):
    await message.answer("Ismingizni kiriting,")
    await state.set_state(FormState.full_name)

@register_router.message(FormState.full_name)
async def get_fullname(message:Message,state:FSMContext):
    full_name=message.text
    await state.update_data(full_name=full_name)
    await message.answer("Telefon raqamingizni yuboring.")
    await state.set_state(FormState.phone)

@register_router.message(FormState.phone)
async def get_phone_number(message:Message,state:FSMContext):
    phone=message.text
    await state.update_data(phone=phone)
    await message.answer("Tug`ilgan kuningizni kiriting: dd.mm.yy:")
    await state.set_state(FormState.birthday)

@register_router.message(FormState.birthday)
async def get_birthday(message:Message,state:FSMContext):
    birthday=message.text
    await state.update_data(birthday=birthday)
    await message.answer("Manzillingizni kiriting:Viloyat,Tuman,uymanzil")
    await state.set_state(FormState.address)


@register_router.message(FormState.address)
async def get_birthday(message: Message, state: FSMContext):
    address = message.text
    await state.update_data(address=address)
    await message.answer("Emaillingizni kiriting:")
    await state.set_state(FormState.email)

@register_router.message(FormState.email)
async def get_email(message:Message, state: FSMContext):
    email= message.text
    await state.update_data(email=email)
    await message.answer("Passport raqamingizni kiriting:")
    await state.set_state(FormState.passport)

@register_router.message(FormState.passport)
async def get_passport(message:Message,state:FSMContext):
    passport=message.text
    await state.update_data(passport=passport)



    datas = await state.get_data()
    full_name=datas.get("full_name")
    phone=datas.get("phone")
    birthday=datas.get("birthday")
    address=datas.get("address")
    email=datas.get("email")
    passport=datas.get("passport")
    await message.answer("Ro`yhatdan o`tish muvaffaqiyatli yakunlandi.")
    await message.answer("Register natijasi:\n"
                         f"1.Fullname: {full_name}\n"
                         f"2.Phone {phone}\n"
                         f"3.Birthday {birthday}\n"
                         f"4.Address {address}\n"
                         f"5.Email {email}\n"
                         f"6.Passport {passport}")
    await state.clear()
