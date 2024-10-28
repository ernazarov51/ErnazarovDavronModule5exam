import asyncio
import datetime

from aiogram import Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.buttons.reply import create_button, reply_button, cities, jins_rkb
from aiogram.types import Message, CallbackQuery,ContentType
from db.service import CRUD
from db.models import Models
from utils.config import CF as conf
from bot.buttons.inline import ikb_main, admin_main_ikb
from aiogram.fsm.state import State,StatesGroup

class StartState(StatesGroup):
    create_user=State()
    adress=State()


async def start_register(dp: Dispatcher, bot):
    @dp.message(CommandStart())
    async def start(message: Message,state: FSMContext):
        await bot.send_message(chat_id=message.chat.id,text="Diqqat! Telefon raqamingiz o'zgartirilgach, sizning Akkauntingizga eski raqamdan kirish imkoniyati boshqa mavjud bo'lmaydi.",reply_markup=reply_button.as_markup())
        await state.set_state(StartState.create_user)

    @dp.message(StartState.create_user,F.content_type == ContentType.CONTACT)
    async def create_user(message: Message,state: FSMContext):
        phone_number=message.contact.phone_number
        first_name=message.from_user.first_name
        user_name=message.from_user.username
        CRUD(Models.User).add(phone_number=phone_number,first_name=first_name,user_name=user_name)
        shaharlar = "⬅️ Орқага,Farg'ona,Andijon,Namangan,Samarqand,Qarshi,Jizzah,Qo'qon,Toshkent,Buxoro,Navoiy,Nukus,Margilan"
        await bot.send_message(chat_id=message.chat.id, text=shaharlar,
                               reply_markup=cities.as_markup())
        await state.set_state(StartState.adress)

    @dp.message(StartState.adress,F.text=='⬅️ Орқага')
    @dp.message(F.text=="Farg'ona")
    @dp.message(F.text=="Andijon")
    @dp.message(F.text=="Namangan")
    @dp.message(F.text=="Samarqand")
    @dp.message(F.text=="Qarshi")
    @dp.message(F.text=="Jizzah")
    @dp.message(F.text=="Qo'qon")
    @dp.message(F.text=="Toshkent")
    @dp.message(F.text=="Buxoro")
    @dp.message(F.text=="Navoiy")
    @dp.message(F.text=="Nukus")
    @dp.message(F.text=="Margilan")
    async def adress(message: Message,state: FSMContext):
        await bot.send_message(chat_id=message.chat.id,text="Jins kiriting:",reply_markup=jins_rkb.as_markup())








