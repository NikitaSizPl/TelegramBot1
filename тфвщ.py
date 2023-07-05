async def tort_rus_assort(call: CallbackQuery) -> None:
    if call.data == 'tort_rus_0':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus())
    elif call.data == 'tort_rus_1':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus(call))
    elif call.data == 'trus_Banan':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus(call))
    elif call.data == 'trus_Czekol':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus(call))
    elif call.data == 'trus_Jogurt':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus(call))
    elif call.data == 'trus_fistaszka':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus(call))
    elif call.data == 'trus_Oreo':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus(call))
    elif call.data == 'trus_banan':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus(call))
    elif call.data == 'trus_Marchewka':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus(call))
    elif call.data == 'trus_Banan-karmel':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus(call))
    elif call.data == 'trus_Gruszka-dor':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus(call))
    elif call.data == 'trus_Miodownik':
        await call.message.edit_reply_markup(reply_markup=zakaz.language_zakaz.zakaz_rus(call))
    else:
        await call.message.edit_reply_markup(reply_markup=None)