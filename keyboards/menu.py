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

