from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_menu() -> InlineKeyboardMarkup:
    st_menu = InlineKeyboardMarkup(row_width=1)
    btn_strmenu = InlineKeyboardButton(text='Меню', callback_data='pod_menu')
    btn_cancel = InlineKeyboardButton(text='Отмена', callback_data='back_cancel')
    st_menu.add(btn_strmenu, btn_cancel)
    return st_menu


def pod_menu() -> InlineKeyboardMarkup:
    pd_menu = InlineKeyboardMarkup(row_width=2)
    btn_assort = InlineKeyboardButton(text="Ассортимент", callback_data="assort")
    btn_freedata = InlineKeyboardButton(text="Свободные даты", callback_data="freedata")
    btn_back = InlineKeyboardButton(text="Назад ↩️", callback_data="back_menu")
    pd_menu.add(btn_assort, btn_freedata).add(btn_back)
    return pd_menu


def assort() -> InlineKeyboardMarkup:
    asort = InlineKeyboardMarkup(row_width=1)
    kb_torty = InlineKeyboardButton(text='Торты', callback_data='ass_torty')
    tortybent = InlineKeyboardButton(text='Бенто-торты', callback_data='ass_bento')
    makaron = InlineKeyboardButton(text='Макарон', callback_data='ass_makaron')
    chiz = InlineKeyboardButton(text='Чизкейки', callback_data='ass_chiz')
    desert = InlineKeyboardButton(text='Десерты', callback_data='ass_desert')
    back = InlineKeyboardButton(text="Назад ↩️", callback_data='back_pod_menu')
    asort.add(kb_torty, tortybent, makaron, chiz, desert, back)
    return asort


def kb_torty() -> InlineKeyboardMarkup:
    kbl_torty = InlineKeyboardMarkup(row_width=1)
    bttn1 = InlineKeyboardButton(text='New Snickers', callback_data='tor_Snick')
    bttn2 = InlineKeyboardButton(text='Truskawka w smiewtance', callback_data='tor_Truskawka')
    bttn3 = InlineKeyboardButton(text='Banan-slony karmel-pekan', callback_data='tor_Banan')
    bttn4 = InlineKeyboardButton(text='Tropikalny', callback_data='tor_Tropikalny')
    bttn5 = InlineKeyboardButton(text='Czekolada-wisnia', callback_data='tor_Czekol')
    bttn6 = InlineKeyboardButton(text='Jogurt porzeczkowy', callback_data='tor_Jogurt')
    bttn7 = InlineKeyboardButton(text='Czekolada-pomarancza', callback_data='tor_pomarancza')
    bttn8 = InlineKeyboardButton(text='Fistashka malina', callback_data='tor_fistaszka')
    bttn9 = InlineKeyboardButton(text='Oreo', callback_data='tor_Oreo')
    bttn10 = InlineKeyboardButton(text='Karmelowa gruszka', callback_data='tor_gruszka')
    bttn11 = InlineKeyboardButton(text='Marchewka-pomarancza', callback_data='tor_Marchewka')
    bttn12 = InlineKeyboardButton(text='Banan-karmel-orzech wloski', callback_data='tor_Banan-karmel')
    bttn13 = InlineKeyboardButton(text='Gruszka-dor blue', callback_data='tor_Gruszka-dor')
    bttn14 = InlineKeyboardButton(text='Miodownik', callback_data='tor_Miodownik')
    bttn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort')
    kbl_torty.add(bttn1, bttn2, bttn3, bttn4, bttn5, bttn6, bttn7, bttn8, bttn9, bttn10, bttn11, bttn12, bttn13, bttn14,
                  bttn_back)
    return kbl_torty


def bento_torty() -> InlineKeyboardMarkup:
    kbl_bento = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text='Wanilia truskawka', callback_data='ben_Wanilia')
    btn2 = InlineKeyboardButton(text='Czekolada wisnia', callback_data='ben_Czekolada')
    btn3 = InlineKeyboardButton(text='Karamel banan', callback_data='ben_Karamel')
    btn4 = InlineKeyboardButton(text='Karmel slony karamel orzeszki', callback_data='ben_Orzeszki')
    btn5 = InlineKeyboardButton(text='Biala czekolada borowka', callback_data='ben_Biala')
    btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort')
    kbl_bento.add(btn1, btn2, btn3, btn4, btn5, btn_back)
    return kbl_bento


def makarony() -> InlineKeyboardMarkup:
    kbl_makaron = InlineKeyboardMarkup(row_width=1)
    button_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort')
    kbl_makaron.add(button_back)
    return kbl_makaron


def chizkek() -> InlineKeyboardMarkup:
    kbl_сziz = InlineKeyboardMarkup(row_width=1)
    button1_111 = InlineKeyboardButton(text='New York', callback_data='btn_NewYork')
    button2_122 = InlineKeyboardButton(text='Czekoladowy', callback_data='btn_Czekoladowy')
    button3_133 = InlineKeyboardButton(text='Malina parmezan', callback_data='btn_Malina')
    button4_144 = InlineKeyboardButton(text='Gruszka-dor blue', callback_data='btn_Gruszka')
    button_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort')
    kbl_сziz.add(button1_111, button2_122, button3_133, button4_144, button_back)
    return kbl_сziz


def deserty() -> InlineKeyboardMarkup:
    kbl_deserty = InlineKeyboardMarkup(row_width=1)
    cakepop = InlineKeyboardButton(text='Cake Pops - Eskimo', callback_data='btn_cakepop')
    cupcak = InlineKeyboardButton(text='Cupcakes', callback_data='btn_Cupcak')
    mini = InlineKeyboardButton(text='Mini Pavlove', callback_data='btn_Mini')
    tiramisu = InlineKeyboardButton(text='Tiramisu', callback_data='btn_Tiramisu')
    tortSloiczku = InlineKeyboardButton(text='Tort w sloiczku', callback_data='btn_tortSloiczku')
    cukerroboty = InlineKeyboardButton(text='Cukierki wlasnej roboty', callback_data='btn_cukerroboty')
    ciasteczka = InlineKeyboardButton(text='Ciasteczka', callback_data='btn_Ciasteczka')
    btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort')
    kbl_deserty.add(cakepop, cupcak, mini, tiramisu, tortSloiczku, cukerroboty, ciasteczka, btn_back)
    return kbl_deserty


def zakaz() -> InlineKeyboardMarkup:
    kb_zakaz = InlineKeyboardMarkup(row_width=2)
    btn1 = InlineKeyboardButton(text='Заказать', callback_data='zakaz')
    btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_kb_torty')
    kb_zakaz.add(btn1, btn_back)
    return kb_zakaz
