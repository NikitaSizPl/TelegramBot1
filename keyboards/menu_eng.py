from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data_base import sql


def torty_assort_eng() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Back ↩️', callback_data='back_assort_eng')
    for i in sql.get_eng_cakes():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'tort_eng_{i[0]}'))
    btn_assort.add(btn_back)
    return btn_assort


def bent_assort_eng() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Back ↩️', callback_data='back_assort_eng')
    for i in sql.get_eng_bent():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'bent_eng_{i[0]}'))
    btn_assort.add(btn_back)
    return btn_assort


def mak_assort_eng() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Back ↩️', callback_data='back_assort_eng')
    for i in sql.get_eng_mak():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'mak_eng_{i[0]}'))
    btn_assort.add(btn_back)
    return btn_assort
