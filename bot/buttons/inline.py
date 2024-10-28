from aiogram.utils.keyboard import InlineKeyboardBuilder,InlineKeyboardButton

ikb_main=InlineKeyboardBuilder()
ikb_main.add(InlineKeyboardButton(text="Test",callback_data="test"))

admin_main_ikb=InlineKeyboardBuilder()
admin_main_ikb.add(InlineKeyboardButton(text="🍿 Kinolar",callback_data="adminkino"))
admin_main_ikb.add(InlineKeyboardButton(text="👤 Foydalanuvchilar",callback_data="adminuserdeeds"))

admin_kino_ikb=InlineKeyboardBuilder()
admin_kino_ikb.add(InlineKeyboardButton(text="🎥 Kinolar royxati", switch_inline_query_current_chat='admin-kinolar'))
admin_kino_ikb.add(InlineKeyboardButton(text="⬆️🎞️ Kino qo'shish",callback_data="adminqosh"))
admin_kino_ikb.add(InlineKeyboardButton(text="🗑️ Kino O'chirish",callback_data="adminoch"))
admin_kino_ikb.add(InlineKeyboardButton(text="📊 Statistika",callback_data="statistika_kino"))
admin_kino_ikb.add(InlineKeyboardButton(text="↩️ orqaga",callback_data="adminback"))
admin_kino_ikb.adjust(2,2,1)

kino_qosh_stop_ikb=InlineKeyboardBuilder()
kino_qosh_stop_ikb.add(InlineKeyboardButton(text="❌ Bekor qilish",callback_data="kino_qosh_otmen"))

conf_ikb=InlineKeyboardBuilder()
conf_ikb.add(InlineKeyboardButton(text="✅ Saqlash",callback_data='tasdiqlash'),
             InlineKeyboardButton(text="❌ Bekor qilish",callback_data='bekor'))
conf_ikb.adjust(2)


back_kb=InlineKeyboardBuilder()
back_kb.add(InlineKeyboardButton(text="❌ Bekor qilish",callback_data='orqaga'))

kino_ochir_ikb=InlineKeyboardBuilder()
kino_ochir_ikb.add(InlineKeyboardButton(text="🔢 Kino kodi",callback_data="id_och"),
                   InlineKeyboardButton(text="🔡 Kino nomi",callback_data="nom_och"),
                   InlineKeyboardButton(text="⬅️ Back",callback_data='orqaga'))

admin_user_main_ikb=InlineKeyboardBuilder()
admin_user_main_ikb.add(InlineKeyboardButton(text="🔒 Statistika",callback_data="user_stat"),
                        InlineKeyboardButton(text="🚫  Cheklash",callback_data='user_blok'),
                        InlineKeyboardButton(text="📥 Murojaatlar",callback_data='messages'),
                        InlineKeyboardButton(text="👥 A'zolar",switch_inline_query_current_chat='admin-users'),
                        InlineKeyboardButton(text="⬅️ Orqaga",callback_data="adminback"),
                        )
admin_user_main_ikb.adjust(2,2,1)


