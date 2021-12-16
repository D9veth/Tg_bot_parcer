import telebot
import config
from telebot import types
import time
from main_pars import pars_vv,pars_gor,pars_tts,pars_asna,pars_mag,pars_puma,pars_metro,pars_perek,pars_mvideo,pars_nike,pars_lamoda,pars_sokolov,pars_eladarado,pars_restore

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands = ['start'], content_types=['text'])
def welcome(message):
    '''
        Данная функция отвечает за отправку приветственного сообщения для пользователя, в котором он может выбрать тип магазина
    '''
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton('Продуктовые магазины', callback_data='food')
    item2 = types.InlineKeyboardButton('Магазины одежды',callback_data='clothes')
    item3 = types.InlineKeyboardButton('Магазины электроники',callback_data='electrik')
    item4 = types.InlineKeyboardButton('Ювелирные магазины',callback_data='jewellery')
    item5 = types.InlineKeyboardButton('Аптеки',callback_data='drugs')

    markup.add(item1,item2,item3,item4,item5)
    bot.send_message(message.chat.id,'Добро пожаловать,{0.first_name}!\nЗдесь вы можете узнать, наиболее продоваемые товары, товары со скидками'.format(
                         message.from_user, bot.get_me()),reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def reply(call):
    '''
        Данная функция отвечает за отправку сообщения с выбором магазина, с отправкой скидок товара из магазина выбранного пользователём и за отправку сообщения с повторным выбором типа магазина
    '''
    try:
        if call.message :
            if call.data == 'food':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('ВкусВилл', callback_data='VV')
                item2 = types.InlineKeyboardButton('Перекресток', callback_data='PR')
                item4 = types.InlineKeyboardButton('Магнолия', callback_data='MAGA')
                item5 = types.InlineKeyboardButton('METRO', callback_data='METRO')

                markup.add(item1, item2, item4, item5)
                bot.send_message(chat_id=call.message.chat.id,text = 'Выберете магазин:', reply_markup= markup)

            elif call.data == 'clothes':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item5 = types.InlineKeyboardButton('Puma', callback_data='kot')
                item6 = types.InlineKeyboardButton('Nike', callback_data='ekin')
                item7 = types.InlineKeyboardButton('Ламода', callback_data='lam')

                markup.add(item5, item6, item7)
                bot.send_message(chat_id=call.message.chat.id, text='Выберете магазин:', reply_markup=markup)
            elif call.data == 'electrik':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('МВидео', callback_data='MV')
                item4 = types.InlineKeyboardButton('re:Store', callback_data='res')
                item2 = types.InlineKeyboardButton('Eldorado', callback_data='old')
                markup.add(item1, item4, item2)
                bot.send_message(chat_id=call.message.chat.id, text='Выберете магазин:', reply_markup=markup)
            elif call.data == 'jewellery':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item3 = types.InlineKeyboardButton('Sokolov', callback_data='Skolkovo')

                markup.add(item3)
                bot.send_message(chat_id=call.message.chat.id, text='Выберете магазин:', reply_markup=markup)

            elif call.data == 'drugs':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('36.6', callback_data='36.6')
                item2 = types.InlineKeyboardButton('asna', callback_data='asna')
                item3 = types.InlineKeyboardButton('Горздрав', callback_data='gor')
                markup.add(item1,item2,item3)
                bot.send_message(chat_id=call.message.chat.id, text='Выберете магазин:', reply_markup=markup)

            elif call.data == 'VV':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                vkusvill_prod,vkusvill_html,vkusvill_old_price,vkusvill_new_price = pars_vv()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти во ВкусВилле:')
                for i in range(len(vkusvill_prod)):
                    txt=str(vkusvill_prod[i])+'\n'+'⛔'+'Старая цена:'+' '+'\u0336'.join(str(vkusvill_old_price[i]))+'\u0336'+'\n'+'✅'+'Новая цена:'+' '+str(vkusvill_new_price[i])+'\n'+'🌐'+'Ссылка:'+' '+str(vkusvill_html[i])
                    bot.send_message(chat_id=call.message.chat.id,text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == 'MV':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                mvideo_prod,mvideo_html,mvideo_old_price,mvideo_new_price = pars_mvideo()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти во МВидео:')
                for i in range(len(mvideo_prod)):
                    txt=str(mvideo_prod[i])+'\n'+'⛔'+'Старая цена:'+' '+'\u0336'.join(str(mvideo_old_price[i]))+'\u0336'+'\n'+'✅'+'Новая цена:'+' '+str(mvideo_new_price[i])+'\n'+'🌐'+'Ссылка:'+' '+str(mvideo_html[i])
                    bot.send_message(chat_id=call.message.chat.id,text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)

            elif call.data == 'PR':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                perek_prod,perek_html,perek_old_price,perek_new_price = pars_perek()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в Перекрестке:')
                for i in range(len(perek_prod)):
                    txt = str(perek_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(perek_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(perek_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(perek_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)

            elif call.data == 'MAGA':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                mag_prod,mag_html,mag_old_price,mag_new_price = pars_mag()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в Магнолии:')
                for i in range(len(mag_prod)):
                    txt = str(mag_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(mag_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(mag_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(mag_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)

            elif call.data == 'METRO':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                metro_prod,metro_html,metro_old_price,metro_new_price = pars_metro()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в METRO:')
                for i in range(len(metro_prod)):
                    txt = str(metro_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(metro_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(metro_new_price[i])+'\n'+'🌐'+'Ссылка:'+' '+str(metro_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)

            elif call.data == 'kot':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                puma_prod, puma_html, puma_old_price, puma_new_price = pars_puma()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в Puma:')
                for i in range(len(puma_prod)):
                    txt = str(puma_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(puma_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(puma_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(puma_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)

            elif call.data == 'ekin':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                nike_prod, nike_html, nike_old_price, nike_new_price = pars_nike()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в Nike:')
                for i in range(len(nike_prod)):
                    txt = str(nike_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(nike_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(nike_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(nike_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)

            elif call.data == '36.6':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                tts_prod, tts_html, tts_old_price, tts_new_price = pars_tts()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в Аптека 36.6:')
                for i in range(len(tts_prod)):
                    txt = str(tts_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(tts_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(tts_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(tts_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == 'asna':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                asna_prod, asna_html, asna_old_price, asna_new_price = pars_asna()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в Аптека asna:')
                for i in range(len(asna_prod)):
                    txt = str(asna_prod[i]) + '\n' + '✅' + 'Цена:' + ' ' + ''.join(str(asna_old_price[i])) + '' + '\n' + '💳' + 'Начисляемые баллы:' + ' ' + str(asna_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(asna_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == 'gor':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                gor_prod, gor_html, gor_old_price, gor_new_price = pars_gor()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в Аптека Горздрав:')
                for i in range(len(gor_prod)):
                    txt = str(gor_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(gor_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(gor_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(gor_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == 'lam':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                lamoda_prod, lamoda_html, lamoda_old_price, lamoda_new_price = pars_lamoda()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в Ламоде:')
                for i in range(len(lamoda_prod)):
                    txt = str(lamoda_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(lamoda_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(lamoda_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(lamoda_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == 'res':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                restore_prod, restore_html, restore_old_price, restore_new_price = pars_restore()
                bot.send_message(chat_id=call.message.chat.id,text='Вот какие скидки нам удалось найти в re:Store:')
                for i in range(len(restore_prod)):
                    txt = str(restore_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(restore_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(restore_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(restore_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == 'old':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                eladarado_prod, eladarado_html, eldarado_old_price, eldarado_new_price = pars_eladarado()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в Эльдарадо:')
                for i in range(len(eladarado_prod)):
                    txt = str(eladarado_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(eldarado_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(eldarado_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(eladarado_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == 'Skolkovo':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                sokolov_prod, sokolov_html, sokolov_old_price, sokolov_new_price = pars_sokolov()
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в Эльдарадо:')
                for i in range(len(sokolov_prod)):
                    txt = str(sokolov_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(sokolov_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(sokolov_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(sokolov_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == '/restart':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Продуктовые магазины', callback_data='food')
                item2 = types.InlineKeyboardButton('Магазины одежды', callback_data='clothes')
                item3 = types.InlineKeyboardButton('Магазины электроники', callback_data='electrik')
                item4 = types.InlineKeyboardButton('Ювелирные магазины', callback_data='jewellery')
                item5 = types.InlineKeyboardButton('Аптеки', callback_data='drugs')
                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(chat_id = call.message.chat.id,text = 'Выберите категорию в которой мы будем искать вам скидки:'.format(call.message.from_user, bot.get_me()), reply_markup=markup)

    except Exception as e:
        print(repr(e))



bot.polling(none_stop=True)