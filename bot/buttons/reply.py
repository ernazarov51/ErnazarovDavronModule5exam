from aiogram.utils.keyboard import ReplyKeyboardBuilder,KeyboardButton
from aiogram.types import ReplyKeyboardMarkup
async def create_button(buttons_str: str, design: str):
    buttons=buttons_str.split(',')
    design=map(int,design.split(','))
    rkb=ReplyKeyboardBuilder()
    for i in buttons:
        rkb.add(KeyboardButton(text=i))
    rkb.adjust(*design)

    return rkb.as_markup(resize_keyboard=True)

reply_button=ReplyKeyboardBuilder()
reply_button.add(KeyboardButton(text="📲 Telefon raqamni yuborish",request_contact=True))

cities=ReplyKeyboardBuilder()
cities.add(KeyboardButton(text="⬅️ Орқага"),
           KeyboardButton(text="Farg'ona"),
           KeyboardButton(text="Andijon"),
           KeyboardButton(text="Namangan"),
           KeyboardButton(text="Samarqand"),
           KeyboardButton(text="Qarshi"),
           KeyboardButton(text="Jizzah"),
           KeyboardButton(text="Qo'qon"),
           KeyboardButton(text="Toshkent"),
           KeyboardButton(text="Buxoro"),
           KeyboardButton(text="Navoiy"),
           KeyboardButton(text="Nukus"),
           KeyboardButton(text="Margilan"))
cities.adjust(1,2,2,2,2,2,2)
cities.as_markup(resize_keyboard=True)

jins_rkb=ReplyKeyboardBuilder()
jins_rkb.add(KeyboardButton(text="Erkak"),
             KeyboardButton(text="Ayol"),
             KeyboardButton(text="⬅️ Орқага"))

jins_rkb.adjust(2,1)
jins_rkb.as_markup(resize_keyboard=True)
