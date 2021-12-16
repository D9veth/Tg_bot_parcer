import telebot
import config
import requests
from telebot import types
from bs4 import BeautifulSoup
import time
# парс с сайтов

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
#Продуктовые
#Вкусвилл
vkusvill_prod = []
vkusvill_html = []
vkusvill_old_price = []
vkusvill_new_price = []
url_vv = 'https://vkusvill.ru/bonuses/'# Делаю парс из магазина Вкусвилл
html_vv = requests.get(url_vv).text
soup_vv = BeautifulSoup(html_vv, 'html.parser')

content_vv1 = soup_vv.find_all('div', class_="ProductCard__content")
content_vv2 = soup_vv.find_all('div', class_="ProductCard__price")

for article in content_vv1:
    tovar = article.find('a', class_='ProductCard__link js-datalayer-catalog-list-name').get('title')
    vkusvill_prod.append(tovar)
    html = 'https://vkusvill.ru' + article.find('a', class_='ProductCard__link js-datalayer-catalog-list-name').get('href')
    vkusvill_html.append(html)
for article in content_vv2:
    price_old = str(article.find('span', class_='js-datalayer-catalog-list-price-old hidden'))
    price_old=price_old[price_old.find('>')+1:]
    price_old=price_old[:price_old.find('<')]
    vkusvill_old_price.append(price_old)
    price_new = str(article.find('span', class_='js-datalayer-catalog-list-price hidden'))
    price_new = price_new[price_new.find('>') + 1:]
    price_new = price_new[:price_new.find('<')]
    vkusvill_new_price.append(price_new)


#Перекресток
perek_prod = []
perek_old_price = []
perek_new_price = []
perek_html=[]
url_per = 'https://www.perekrestok.ru/cat/d?orderBy=popularity&orderDirection=desc'
html_per = requests.get(url_per).text
soup_per = BeautifulSoup(html_per, 'html.parser')
counter=0
content_per1 = soup_per.find_all('div', class_="product-card-title__wrapper")
content_per2 = soup_per.find_all('div', class_='product-card__control')
content_per3 = str(soup_per.find_all('div', class_='catalog-content__list'))
for article in content_per1:
    tovar=str(article.find('div',class_='product-card__title'))
    tovar = tovar[tovar.find('>') + 1:]
    tovar = tovar[:tovar.find('<')]
    perek_prod.append(tovar)
    counter+=1
    if counter==10:
        break
counter=0
for article in content_per2:
    price_new=str(article.find('div', class_='price-new'))
    price_new = price_new[price_new.find('>') + 1:]
    price_new = price_new[:price_new.find('<')]
    price_old = str(article.find('div', class_='price-old'))
    price_old = price_old[price_old.find('>') + 1:]
    price_old = price_old[:price_old.find('<')]
    perek_new_price.append(price_new.replace('\xa0',' '))
    perek_old_price.append(price_old.replace('\xa0',' '))
    counter+=1
    if counter==10:
        break
while counter!=0:
    if content_per3[content_per3.find('href'):content_per3.find('<span')] != '':
        check=content_per3[content_per3.find('href'):content_per3.find('<span')]
        counter-=1
        html = 'https://www.perekrestok.ru' + check[check.find('/'):check.find('">')]
        perek_html.append(html)
    content_per3=content_per3[content_per3.find('<span')+4:]
#Магнолия
mag_prod = []
mag_html = []
mag_old_price = []
mag_new_price = []
url_mag = 'https://shop.mgnl.ru/catalog/super-aktsiya-skidka-50/'
html_mag = requests.get(url_mag).text
soup_mag = BeautifulSoup(html_mag, 'html.parser')
counter=0
content_mag1 = str(soup_mag.find_all('div', class_="ajax_load cur block"))
content_mag2 = str(soup_mag.find_all('div', class_="ajax_load cur block"))
counter=9
while counter!=0:
    if content_mag1[content_mag1.find('<a class="dark_link option-font-bold font_sm" href='):content_mag1.find('</span>')]!='':
        check=content_mag1[content_mag1.find('<a class="dark_link option-font-bold font_sm" href='):content_mag1.find('</span>')]
        html='https://shop.mgnl.ru'+check[check.find('href="')+6:check.find('"><')]
        mag_html.append(html)
        check=check[check.find('<span>')+6:]
        mag_prod.append(check)
        counter-=1
    content_mag1=content_mag1[content_mag1.find('</span>')+7:]
for i in range(20):
    if content_mag2[content_mag2.find('<span class="values_wrapper">'):content_mag2.find('</span> ')] != '':
        check=content_mag2[content_mag2.find('<span class="values_wrapper">'):content_mag2.find('</span> ')]
        check=check[check.find('">')+2:check.find('</')]
        if len(mag_old_price)==len(mag_new_price):
            mag_old_price.append(check)
        else:
            mag_new_price.append(check)
    content_mag2 = content_mag2[content_mag2.find('</span> ') + 8:]
#Метро
metro_prod= []
metro_html = []
metro_old_price = []
metro_new_price = []
url_mag = 'https://msk.metro-cc.ru/virtual/tovary_nedeli?itm_pm=ru%3Ancp%3Actr%3Ait%3A11%3A4&_ga=2.148296562.497639215.1638262985-825064516.1638262985'
html_mag = requests.get(url_mag)
soup_mag = BeautifulSoup(html_mag.text, 'lxml')
content_mag1 = soup_mag.find_all('div', class_='catalog-item')
counter==0
for article in content_mag1:
    price_old = str(article.find('div', class_='catalog-item_price-old'))
    if price_old != 'None':
        price_old = price_old[1:len(price_old) - 1]
        price_old = price_old[price_old.index('>') + 1:price_old.index('<')]
        price_old=price_old.replace('\t','')
        price_old=price_old.replace('\n','')
        metro_old_price.append(price_old)
        html = 'https://msk.metro-cc.ru' + article.find('a', class_='catalog-item_name').get('href')
        metro_html.append(html)

        text = str(article.find('a', class_='catalog-item_name'))
        text = text[1:len(text) - 1]
        text = text[text.index('>') + 1:text.index('<')]
        text=text.replace('\t','')
        text=text.replace(' ','',10)
        text=text.replace('\n','')
        metro_prod.append(text)

        price_new = str(article.find('div', class_='catalog-item_price-lvl_current'))

        price_new = price_new[1:len(price_new) - 1]
        price_new = price_new.replace(' ','')
        price_new = price_new[49::]
        price_new = price_new[0:price_new.index('<')]
        price_new=price_new.replace('\t','')
        price_new=price_new.replace('\n','')
        metro_new_price.append(price_new)
        counter+=1
    if counter==10:
        break

#Магазины одежды
#НАЙК
nike_prod = []
nike_html = []
nike_old_price = []
nike_new_price = []
url_nike = 'https://www.nike.com/ru/w/sale-3yaep'
html_nike = requests.get(url_nike).text
soup_nike = BeautifulSoup(html_nike, 'html.parser')
content_nike1 = soup_nike.find_all('div', class_="product-card__body")
counter=0
for article in content_nike1:
    tovar=str(article.find('div',class_='product-card__titles'))
    nike_html.append(article.find('a',class_='product-card__link-overlay').get('href'))
    tovar1=tovar[tovar.find('product-card__subtitle">'):]
    tovar1=tovar1[tovar1.find('">')+2:tovar1.find('</')]
    tovar2=article.find('div',class_='product-card__title').get('id')
    tovar= tovar1 +': '+tovar2
    nike_prod.append(tovar)
    counter+=1
    check=str(article.find('div',class_='product-card__price'))
    check1 =check[check.find('цена')+5:check.find(',')]
    check2=check[check.find('изначальная цена')+17:check.find('" ')]
    nike_new_price.append(check1)
    nike_old_price.append(check2)
    if counter==10:
        break
#ПУма
puma_prod = []
puma_html = []
puma_old_price = []
puma_new_price = []
url_puma = 'https://ru.puma.com/skidki.html'
html_puma = requests.get(url_puma).text
soup_puma = BeautifulSoup(html_puma, 'html.parser')
content_puma1 = str(soup_puma.find_all('div', class_="grid"))
content_puma2 = str(soup_puma.find_all('div', class_="product-item__details"))
counter=10
while counter!=0:
    if content_puma1[content_puma1.find('<a class="product-item__img-w" href='):content_puma1.find('" class="product-item__img')]!='':
        html=content_puma1[content_puma1.find('<a class="product-item__img-w" href='):content_puma1.find('" class="product-item__img')]
        counter -= 1
        puma_html.append(html[html.find('f="')+3:html.find('" t')])
        puma_prod.append(html[html.find('Изображение ')+len('Изображение '):])
    content_puma1=content_puma1[content_puma1.find('" class="product-item__img')+26:]
counter=20
check=0
while counter!=0:
    if content_puma2[content_puma2.find('<span class="price-wrapper" data-price-amount="'):content_puma2.find('" data-price-type=')]!='':
        price=content_puma2[content_puma2.find('<span class="price-wrapper" data-price-amount="'):content_puma2.find('" data-price-type=')]
        if check%2==0:
            puma_new_price.append(price[price.find('t="')+3:])
            check+=1
        else:
            puma_old_price.append(price[price.find('t="')+3:])
            check+=1
        counter-=1
    content_puma2=content_puma2[content_puma2.find('" data-price-type=')+18:]


#ПИЗДА ТЕБЕ ЕБАНАЯ МВИДЕО
mvideo_prod = []
mvideo_html = []
mvideo_old_price = []
mvideo_new_price = []
url_mvideo = 'https://www.mvideo.ru/promo/komputery-i-noutbuki-mark188276424'
html_mvideo = requests.get(url_mvideo, headers=headers)
soup_mvideo=html_mvideo.content.decode()
counter=10
while counter!=0:
    if soup_mvideo[soup_mvideo.find('<div class="fl-product-tile__picture-holder c-product-tile-picture__holder">'):soup_mvideo.find('"productCategoryId"')+len('"productCategoryId"')] != '':
        prod = soup_mvideo[soup_mvideo.find('<div class="fl-product-tile__picture-holder c-product-tile-picture__holder">'):soup_mvideo.find('"productCategoryId"')+len('"productCategoryId"')]
        html ='https://www.mvideo.ru/' + prod[prod.find('<a href="/')+len('<a href="/'):prod.find('" class="fl-product-tile-picture fl-product-tile')]
        mvideo_html.append(html)
        price_new = prod[prod.find('"productPriceLocal":')+len('"productPriceLocal":'):prod.find('"productId":')]
        print(price_new)
        prod=prod[prod.find('"productName": "')+len('"productName": "'):prod.find('"productCategoryId"')]
        prod=prod[:prod.find('",')]
        mvideo_prod.append(prod)
        counter -= 1
    soup_mvideo=soup_mvideo[soup_mvideo.find('"productCategoryId"')+len('"productCategoryId"'):]
soup_mvideo=html_mvideo.content.decode()

counter=10
while counter!=0:
    if soup_mvideo[soup_mvideo.find(''):soup_mvideo.find('')]:
        counter-=1
#Ювелирка
sokolov_prod = []
sokolov_html = []
sokolov_old_price = []
sokolov_new_price = []
url_sokolov = 'https://sokolov.ru/jewelry-catalog/sale50/sale60/sale70/'
html_sokolov = requests.get(url_sokolov).text
soup_sokolov = BeautifulSoup(html_sokolov, 'html.parser')
content_sokolov1 = str(soup_sokolov.find_all('div', class_="list"))
#print(content_sokolov1)
#Другие


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands = ['start'], content_types=['text'])
def welcome(message):

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
    try:
        if call.message :
            if call.data == 'food':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('ВкусВилл', callback_data='VV')
                item2 = types.InlineKeyboardButton('METRO', callback_data='MED')
                item4 = types.InlineKeyboardButton('Магнолия', callback_data='MAGAN')
                item5 = types.InlineKeyboardButton('Перекрёсток', callback_data='KREST')

                markup.add(item1, item2, item4, item5)
                bot.send_message(chat_id=call.message.chat.id,text = 'Выберете магазин:', reply_markup= markup)

            elif call.data == 'clothes':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('H&M', callback_data='HM')
                item2 = types.InlineKeyboardButton('Pull&Bear', callback_data='Pb')
                item3 = types.InlineKeyboardButton('Bershka', callback_data='BER')
                item4 = types.InlineKeyboardButton('Lamoda', callback_data='lama')
                item5 = types.InlineKeyboardButton('Puma', callback_data='kot')
                item6 = types.InlineKeyboardButton('Nike', callback_data='ekin')

                markup.add(item1, item2, item3, item4, item5, item6)
                bot.send_message(chat_id=call.message.chat.id, text='Выберете магазин:', reply_markup=markup)
            elif call.data == 'electrik':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('МВидео', callback_data='MV')
                item2 = types.InlineKeyboardButton('DNS', callback_data='DNS')
                item3 = types.InlineKeyboardButton('Ситилинк', callback_data='Siti')
                item4 = types.InlineKeyboardButton('re:Store', callback_data='res')
                item5 = types.InlineKeyboardButton('Bosh', callback_data='bosh')
                item6 = types.InlineKeyboardButton('Siemens', callback_data='siem')
                item7 = types.InlineKeyboardButton('Bork', callback_data='bork')
                item8 = types.InlineKeyboardButton('Dyson', callback_data='tyson')

                markup.add(item1, item2, item3, item4, item5, item6, item7, item8)
                bot.send_message(chat_id=call.message.chat.id, text='Выберете магазин:', reply_markup=markup)
            elif call.data == 'jewellery':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Московский ювелирный завод', callback_data='MUZ')
                item2 = types.InlineKeyboardButton('Адамас', callback_data='ADAM')
                item3 = types.InlineKeyboardButton('Sokolov', callback_data='Skolkovo')
                item4 = types.InlineKeyboardButton('SunLight', callback_data='SL')

                markup.add(item1, item2, item3, item4)
                bot.send_message(chat_id=call.message.chat.id, text='Выберете магазин:', reply_markup=markup)

            elif call.data == 'drugs':
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('36.6', callback_data='36.6')
                item2 = types.InlineKeyboardButton('iHerb', callback_data='iherb')
                item3 = types.InlineKeyboardButton('ЕАптека', callback_data='eeee')
                item4 = types.InlineKeyboardButton('Аптека.ру', callback_data='aru')
                item5 = types.InlineKeyboardButton('Аптеки столички', callback_data='stol')

                markup.add(item1, item2, item3, item4, item5)
                bot.send_message(chat_id=call.message.chat.id, text='Выберете магазин:', reply_markup=markup)
            elif call.data == 'VV':
                bot.send_message(chat_id=call.message.chat.id, text='Продукты:')
                for i in range(len(vkusvill_prod)):
                    txt=str(vkusvill_prod[i])+'\n'+'⛔'+'Старая цена:'+' '+'\u0336'.join(str(vkusvill_old_price[i]))+'\u0336'+'\n'+'✅'+'Новая цена:'+' '+str(vkusvill_new_price[i])+'\n'+'🌐'+'Ссылка:'+' '+str(vkusvill_html[i])
                    bot.send_message(chat_id=call.message.chat.id,text=txt)
                    time.sleep(0.5)
            elif call.data == 'MED':
                bot.send_message(chat_id=call.message.chat.id, text='Продукты:')
                for i in range(len(metro_prod)):
                    txt = str(metro_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(metro_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(metro_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(metro_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
            elif call.data == 'MAGAN':
                bot.send_message(chat_id=call.message.chat.id, text='Продукты:')
                for i in range(len(mag_prod)):
                    txt = str(mag_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(mag_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(mag_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(mag_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
            elif call.data == 'KREST':
                bot.send_message(chat_id=call.message.chat.id, text='Продукты:')
                for i in range(len(perek_prod)):
                    txt = str(perek_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(perek_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(perek_new_price[i])+'\n'+'🌐'+'Ссылка:'+' '+str(perek_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
            elif call.data == 'HM':
                bot.send_message(chat_id=call.message.chat.id, text='ты чё  богатый?')
            elif call.data == 'Pb':
                bot.send_message(chat_id=call.message.chat.id, text='ты чё  богатый?')
            elif call.data == 'BER':
                bot.send_message(chat_id=call.message.chat.id, text='ты чё бедный?')
            elif call.data == 'lama':
                bot.send_message(chat_id=call.message.chat.id, text='ты чёбедный?')
            elif call.data == 'kot':
                bot.send_message(chat_id=call.message.chat.id, text='Скидки в Puma')
                for i in range(len(puma_prod)):
                    txt = str(puma_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(puma_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(puma_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(puma_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
            elif call.data == 'ekin':
                bot.send_message(chat_id=call.message.chat.id, text='Скидки в Nike')
                for i in range(len(nike_prod)):
                    txt = str(nike_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(nike_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(nike_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(nike_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
            elif call.data == 'MV':
                bot.send_message(chat_id=call.message.chat.id, text='ты чё богатый?')
            elif call.data == 'res':
                bot.send_message(chat_id=call.message.chat.id, text='ты чё бедный?')
            elif call.data == 'DNS':
                bot.send_message(chat_id=call.message.chat.id, text='ты чё богатый?')
            elif call.data == 'Siti':
                bot.send_message(chat_id=call.message.chat.id, text='ты чё бедный?')
            elif call.data == 'bosh':
                bot.send_message(chat_id=call.message.chat.id, text='ты чё не бедный не богатый?')
            elif call.data == 'siem':
                bot.send_message(chat_id=call.message.chat.id, text='чел тыююю?')
            elif call.data == 'bork':
                bot.send_message(chat_id=call.message.chat.id, text='чел тыююю?')
            elif call.data == 'tyson':
                bot.send_message(chat_id=call.message.chat.id, text='чел тыююю?')
            elif call.data == 'MUZ':
                bot.send_message(chat_id=call.message.chat.id, text='ты чё  не бедный не богатый?')
            elif call.data == 'ADAM':
                bot.send_message(chat_id=call.message.chat.id, text='чел тыююю?')
            elif call.data == 'Skolkovo':
                bot.send_message(chat_id=call.message.chat.id, text='чел тыююю?')
            elif call.data == 'SL':
                bot.send_message(chat_id=call.message.chat.id, text='чел тыююю?')
            elif call.data == 'stol':
                bot.send_message(chat_id=call.message.chat.id, text='чел тыююю?')
            elif call.data == '36.6':
                bot.send_message(chat_id=call.message.chat.id, text='ты чё  не бедный не богатый?')
            elif call.data == 'iherb':
                bot.send_message(chat_id=call.message.chat.id, text='чел тыююю?')
            elif call.data == 'eeee':
                bot.send_message(chat_id=call.message.chat.id, text='чел тыююю?')
            elif call.data == 'aru':
                bot.send_message(chat_id=call.message.chat.id, text='чел тыююю?')

    except Exception as e:
        print(repr(e))



bot.polling(none_stop=True)