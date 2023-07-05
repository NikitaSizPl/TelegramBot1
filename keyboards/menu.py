from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data_base import sql


def start_lang() -> InlineKeyboardMarkup:
    lang_menu = InlineKeyboardMarkup(row_width=1)
    btn_rus = InlineKeyboardButton(text='Русский 🇷🇺', callback_data='lang_btn_rus')
    btn_urk = InlineKeyboardButton(text='Український 🇺🇦', callback_data='lang_btn_ukr')
    btn_pl = InlineKeyboardButton(text='Polski 🇵🇱', callback_data='lang_btn_pl')
    btn_eng = InlineKeyboardButton(text='English 🇬🇧', callback_data='lang_btn_eng')
    lang_menu.add(btn_rus, btn_urk, btn_pl, btn_eng)
    return lang_menu


class language_assort:
    def __init__(self):
        self.kb_language = None

    def pod_menu_rus(self) -> InlineKeyboardMarkup:
        self.kb_language = InlineKeyboardMarkup(row_width=1)
        kb_torty = InlineKeyboardButton(text='Торты', callback_data='rus_ass_torty')
        tortybent = InlineKeyboardButton(text='Бенто-торты', callback_data='rus_ass_bento')
        makaron = InlineKeyboardButton(text='Макарон', callback_data='rus_ass_makaron')
        # desert = InlineKeyboardButton(text='Десерты', callback_data='ass_desert')
        back = InlineKeyboardButton(text="Назад ↩️", callback_data='back_lang_menu')
        self.kb_language.insert(kb_torty).add(tortybent, makaron, back)
        return self.kb_language

    def pod_menu_ukr(self) -> InlineKeyboardMarkup:
        self.kb_language = InlineKeyboardMarkup(row_width=1)
        kb_torty = InlineKeyboardButton(text='Торти', callback_data='ukr_ass_torty')
        tortybent = InlineKeyboardButton(text='Бенто-торти', callback_data='ukr_ass_bento')
        makaron = InlineKeyboardButton(text='Макарони', callback_data='ukr_ass_makaron')
        # desert = InlineKeyboardButton(text='Десерты', callback_data='ass_desert')
        back = InlineKeyboardButton(text="Назад ↩️", callback_data='back_lang_menu')
        self.kb_language.insert(kb_torty).add(tortybent, makaron, back)
        return self.kb_language

    def pod_menu_pl(self) -> InlineKeyboardMarkup:
        self.kb_language = InlineKeyboardMarkup(row_width=1)
        kb_torty = InlineKeyboardButton(text='Tort', callback_data='pl_ass_torty')
        tortybent = InlineKeyboardButton(text='Bento-tort', callback_data='pl_ass_bento')
        makaron = InlineKeyboardButton(text='Makaron', callback_data='pl_ass_makaron')
        # desert = InlineKeyboardButton(text='Десерты', callback_data='ass_desert')
        back = InlineKeyboardButton(text="Powrót ↩️", callback_data='back_lang_menu')
        self.kb_language.insert(kb_torty).add(tortybent, makaron, back)
        return self.kb_language

    def pod_menu_eng(self) -> InlineKeyboardMarkup:
        self.kb_language = InlineKeyboardMarkup(row_width=1)
        kb_torty = InlineKeyboardButton(text='Cakes', callback_data='eng_ass_torty')
        tortybent = InlineKeyboardButton(text='Bento-cakes', callback_data='eng_ass_bento')
        makaron = InlineKeyboardButton(text='Makaron', callback_data='eng_ass_makaron')
        # desert = InlineKeyboardButton(text='Десерты', callback_data='ass_desert')
        back = InlineKeyboardButton(text="Back ↩️", callback_data='back_lang_menu')
        self.kb_language.insert(kb_torty).add(tortybent, makaron, back)
        return self.kb_languag


class language_assort_torty:
    def __init__(self):
        self.btn_assort_torty = None

    def torty_assort_pl(self) -> InlineKeyboardMarkup:
        self.btn_assort_torty = InlineKeyboardMarkup(row_width=1)
        bttn1 = InlineKeyboardButton(text='Snickers', callback_data='tor_Snick')
        bttn2 = InlineKeyboardButton(text='Truskawki w śmietanie', callback_data='tor_Truskawka')
        bttn3 = InlineKeyboardButton(text='Banan - Solony Karmel-orzech', callback_data='tor_Banan')
        bttn5 = InlineKeyboardButton(text='Czekolada Wiśnia', callback_data='tor_Czekol')
        bttn6 = InlineKeyboardButton(text='Jogurt czarna porzeczka', callback_data='tor_Jogurt')
        bttn8 = InlineKeyboardButton(text='Pistacja malina', callback_data='tor_fistaszka')
        bttn9 = InlineKeyboardButton(text='Oreo', callback_data='tor_Oreo')
        bttn10 = InlineKeyboardButton(text='Banan', callback_data='tor_banan')
        bttn11 = InlineKeyboardButton(text='Marchewka z pomarańczą', callback_data='tor_Marchewka')
        bttn12 = InlineKeyboardButton(text='Banan-karmel-orzech', callback_data='tor_Banan-karmel')
        bttn13 = InlineKeyboardButton(text='Gruszka Dor-Blue', callback_data='tor_Gruszka-dor')
        bttn14 = InlineKeyboardButton(text='Miodownik', callback_data='tor_Miodownik')
        bttn_back = InlineKeyboardButton(text='Powrót ↩️', callback_data='back_assort_pl')
        self.btn_assort_torty.add(bttn1, bttn2, bttn3, bttn5, bttn6, bttn8, bttn9, bttn10, bttn11, bttn12,
                                  bttn13,
                                  bttn14,
                                  bttn_back)
        return self.btn_assort_torty

    def torty_assort_eng(self) -> InlineKeyboardMarkup:
        self.btn_assort_torty = InlineKeyboardMarkup(row_width=1)
        bttn1 = InlineKeyboardButton(text='Snickers', callback_data='tor_Snick')
        bttn2 = InlineKeyboardButton(text='Strawberries in cream', callback_data='tor_Truskawka')
        bttn3 = InlineKeyboardButton(text='Banana - salted caramel - nut', callback_data='tor_Banan')
        bttn5 = InlineKeyboardButton(text='Chocolate cherry', callback_data='tor_Czekol')
        bttn6 = InlineKeyboardButton(text='Yogurt black currant', callback_data='tor_Jogurt')
        bttn8 = InlineKeyboardButton(text='Pistachio raspberry', callback_data='tor_fistaszka')
        bttn9 = InlineKeyboardButton(text='Oreo', callback_data='tor_Oreo')
        bttn10 = InlineKeyboardButton(text='Banan', callback_data='tor_banan')
        bttn11 = InlineKeyboardButton(text='Carrot with orange', callback_data='tor_Marchewka')
        bttn12 = InlineKeyboardButton(text='Banana - caramel - walnut', callback_data='tor_Banan-karmel')
        bttn13 = InlineKeyboardButton(text='Pear Dor-Blue', callback_data='tor_Gruszka-dor')
        bttn14 = InlineKeyboardButton(text='Medovik', callback_data='tor_Miodownik')
        bttn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort_eng')
        self.btn_assort_torty.add(bttn1, bttn2, bttn3, bttn5, bttn6, bttn8, bttn9, bttn10, bttn11, bttn12,
                                  bttn13,
                                  bttn14,
                                  bttn_back)
        return self.btn_assort_torty


class language_assort_bentotorty:
    def __init__(self):
        self.btn_assort_bentotorty = None

    def bento_torty_pl(self) -> InlineKeyboardMarkup:
        self.btn_assort_bentotorty = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton(text='Truskawka waniliowa', callback_data='bpl_Wanilia')
        btn2 = InlineKeyboardButton(text='Czekolada Wiśnia', callback_data='bpl_Czekolada')
        btn3 = InlineKeyboardButton(text='Banan karmel', callback_data='bpl_Karamel')
        btn4 = InlineKeyboardButton(text='Banan - Solony Karmel-orzech', callback_data='bpl_Orzeszki')
        btn5 = InlineKeyboardButton(text='Biała czekolada borówka', callback_data='bpl_Biala')
        btn_back = InlineKeyboardButton(text='Powrót ↩️', callback_data='back_assort_pl')
        self.btn_assort_bentotorty.add(btn1, btn2, btn3, btn4, btn5, btn_back)
        return self.btn_assort_bentotorty

    def bento_torty_eng(self) -> InlineKeyboardMarkup:
        self.btn_assort_bentotorty = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton(text='Vanilla strawberries', callback_data='beng_Wanilia')
        btn2 = InlineKeyboardButton(text='Chocolate cherry', callback_data='beng_Czekolada')
        btn3 = InlineKeyboardButton(text='Banana caramel', callback_data='beng_Karamel')
        btn4 = InlineKeyboardButton(text='Banana - salted caramel - nut', callback_data='beng_Orzeszki')
        btn5 = InlineKeyboardButton(text='White chocolate blueberry', callback_data='beng_Biala')
        btn_back = InlineKeyboardButton(text='Back ↩️', callback_data='back_assort_eng')
        self.btn_assort_bentotorty.add(btn1, btn2, btn3, btn4, btn5, btn_back)
        return self.btn_assort_bentotorty


class language_assort_makarony:
    def __init__(self):
        self.btn_assort_makarony = None

    def makarony_pl(self) -> InlineKeyboardMarkup:
        self.btn_assort_makarony = InlineKeyboardMarkup(row_width=1)
        bttn1 = InlineKeyboardButton(text='Snickers', callback_data='mak_Snick')
        bttn2 = InlineKeyboardButton(text='Ferrero', callback_data='mak_Ferrero')
        bttn3 = InlineKeyboardButton(text='Bounty', callback_data='mak_Bounty')
        bttn4 = InlineKeyboardButton(text='Raffaello', callback_data='mak_Raffaello')
        bttn5 = InlineKeyboardButton(text='Podwójny Solony Karmel', callback_data='mak_Double_karam')
        bttn6 = InlineKeyboardButton(text='Capuccino - Baileys', callback_data='mak_Capuccino_Baileys')
        bttn7 = InlineKeyboardButton(text='Lawendowy Raf', callback_data='mak_Raf')
        bttn8 = InlineKeyboardButton(text='Gruszka - Dor Blue', callback_data='mak_DorBlue')
        bttn9 = InlineKeyboardButton(text='Miód czekoladowy z wiśniami', callback_data='mak_Szkolad_wisznia')
        bttn10 = InlineKeyboardButton(text='Lawenda brzoskwinia', callback_data='mak_Lavanda_pers')
        bttn11 = InlineKeyboardButton(text='Sernik-borówka', callback_data='mak_Chiz_golub')
        bttn12 = InlineKeyboardButton(text='Truskawkowy milkshake', callback_data='mak_Klubnika_szejk')
        bttn13 = InlineKeyboardButton(text='Limonkowo-truskawkowe', callback_data='mak_Laim_klubnika')
        bttn14 = InlineKeyboardButton(text='Czekoladowy banan', callback_data='mak_Szokolad_banan')
        bttn15 = InlineKeyboardButton(text='Pistacja wiśnia', callback_data='mak_Fistaszka')
        bttn16 = InlineKeyboardButton(text='Plombir-Mango & marakuja', callback_data='mak_Plombir')
        bttn17 = InlineKeyboardButton(text='Cytryna Kurd', callback_data='mak_Limon')
        bttn_back = InlineKeyboardButton(text='Powrót ↩️', callback_data='back_assort_pl')
        self.btn_assort_makarony.add(bttn1, bttn2, bttn3, bttn4, bttn5, bttn6, bttn7, bttn8, bttn9, bttn10, bttn11,
                                     bttn12,
                                     bttn13, bttn14, bttn15, bttn16, bttn17,
                                     bttn_back)
        return self.btn_assort_makarony

    def makarony_eng(self) -> InlineKeyboardMarkup:
        self.btn_assort_makarony = InlineKeyboardMarkup(row_width=1)
        bttn1 = InlineKeyboardButton(text='Snickers', callback_data='mak_Snick')
        bttn2 = InlineKeyboardButton(text='Ferrero', callback_data='mak_Ferrero')
        bttn3 = InlineKeyboardButton(text='Bounty', callback_data='mak_Bounty')
        bttn4 = InlineKeyboardButton(text='Raffaello', callback_data='mak_Raffaello')
        bttn5 = InlineKeyboardButton(text='Double salted caramel', callback_data='mak_Double_karam')
        bttn6 = InlineKeyboardButton(text='Capuccino - Baileys', callback_data='mak_Capuccino_Baileys')
        bttn7 = InlineKeyboardButton(text='Lavender Raf', callback_data='mak_Raf')
        bttn8 = InlineKeyboardButton(text='Pear - Dor Blue', callback_data='mak_DorBlue')
        bttn9 = InlineKeyboardButton(text='Chocolate honey cake with cherries', callback_data='mak_Szkolad_wisznia')
        bttn10 = InlineKeyboardButton(text='Lavender peach', callback_data='mak_Lavanda_pers')
        bttn11 = InlineKeyboardButton(text='Blueberry cheesecake', callback_data='mak_Chiz_golub')
        bttn12 = InlineKeyboardButton(text='Strawberry milkshake', callback_data='mak_Klubnika_szejk')
        bttn13 = InlineKeyboardButton(text='Lime strawberries', callback_data='mak_Laim_klubnika')
        bttn14 = InlineKeyboardButton(text='Chocolate banana', callback_data='mak_Szokolad_banan')
        bttn15 = InlineKeyboardButton(text='Pistachio cherry', callback_data='mak_Fistaszka')
        bttn16 = InlineKeyboardButton(text='Ice cream-mango & passion fruit', callback_data='mak_Plombir')
        bttn17 = InlineKeyboardButton(text='Lemon Kurd', callback_data='mak_Limon')
        bttn_back = InlineKeyboardButton(text='Back ↩️', callback_data='back_assort_eng')
        self.btn_assort_makarony.add(bttn1, bttn2, bttn3, bttn4, bttn5, bttn6, bttn7, bttn8, bttn9, bttn10, bttn11,
                                     bttn12, bttn13, bttn14, bttn15, bttn16, bttn17, bttn_back)
        return self.btn_assort_makarony
