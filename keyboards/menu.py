from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_lang() -> InlineKeyboardMarkup:
    lang_menu = InlineKeyboardMarkup(row_width=1)
    btn_rus = InlineKeyboardButton(text='Русский 🇷🇺', callback_data='lang_btn_rus')
    btn_urk = InlineKeyboardButton(text='Український 🇺🇦', callback_data='lang_btn_ukr')
    btn_pl = InlineKeyboardButton(text='Polski 🇵🇱', callback_data='lang_btn_pl')
    #btn_eng = InlineKeyboardButton(text='English 🇬🇧', callback_data='lang_btn_eng')
    lang_menu.add(btn_rus)
    return lang_menu


class language_assort:
    def __init__(self):
        self.kb_language = None

    def pod_menu_rus(self) -> InlineKeyboardMarkup:
        self.kb_language = InlineKeyboardMarkup(row_width=1)
        btn_text = {'Торты': 'rus_ass_torty', 'Бенто-торты': 'rus_ass_bento', 'Макарон': 'rus_ass_makaron'}
        back = InlineKeyboardButton(text="Назад ↩️", callback_data='back_lang_menu')
        for key, value in btn_text.items():
            self.kb_language.add(InlineKeyboardButton(f'{key}', callback_data=f'{value}'))
        self.kb_language.add(back)
        return self.kb_language

    def pod_menu_ukr(self) -> InlineKeyboardMarkup:
        self.kb_language = InlineKeyboardMarkup(row_width=1)
        btn_text = {'Торти': 'ukr_ass_torty', 'Бенто-торти': 'ukr_ass_bento', 'Макарони': 'ukr_ass_makaron'}
        back = InlineKeyboardButton(text="Назад ↩️", callback_data='back_lang_menu')
        for key, value in btn_text.items():
            self.kb_language.add(InlineKeyboardButton(f'{key}', callback_data=f'{value}'))
        self.kb_language.add(back)
        return self.kb_language

    def pod_menu_pl(self) -> InlineKeyboardMarkup:
        self.kb_language = InlineKeyboardMarkup(row_width=1)
        btn_text = {'Tort': 'pl_ass_torty', 'Bento-torty': 'pl_ass_bento', 'Makaron': 'pl_ass_makaron'}
        back = InlineKeyboardButton(text="Powrót ↩️", callback_data='back_lang_menu')
        for key, value in btn_text.items():
            self.kb_language.add(InlineKeyboardButton(f'{key}', callback_data=f'{value}'))
        self.kb_language.add(back)
        return self.kb_language

    def pod_menu_eng(self) -> InlineKeyboardMarkup:
        self.kb_language = InlineKeyboardMarkup(row_width=1)
        btn_text = {'Cakes': 'eng_ass_torty', 'Bento-cakes': 'eng_ass_bento', 'Makaron': 'eng_ass_makaron'}
        back = InlineKeyboardButton(text="Back ↩️", callback_data='back_lang_menu')
        for key, value in btn_text.items():
            self.kb_language.add(InlineKeyboardButton(f'{key}', callback_data=f'{value}'))
        self.kb_language.add(back)
        return self.kb_language
