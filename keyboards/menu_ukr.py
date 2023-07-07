from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data_base import sql


def torty_assort_ukr() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort_ukr')
    for i in sql.get_ukr_cakes():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'tort_ukr_{i[2]}'))
    btn_assort.add(btn_back)
    return btn_assort


def bent_assort_ukr() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort_ukr')
    for i in sql.get_ukr_bent():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'bent_ukr_{i[2]}'))
    btn_assort.add(btn_back)
    return btn_assort


def mak_assort_ukr() -> InlineKeyboardMarkup:
    btn_assort = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text='Назад ↩️', callback_data='back_assort_ukr')
    for i in sql.get_ukr_mak():
        btn_assort.add(InlineKeyboardButton(f'{i[1]}', callback_data=f'mak_ukr_{i[2]}'))
    btn_assort.add(btn_back)
    return btn_assort
