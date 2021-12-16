import telebot
import config
import requests
from telebot import types
from bs4 import BeautifulSoup
import time


# парс с сайтов

headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'}

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
metro_old = []
metro_new = []
url_mag = 'https://msk.metro-cc.ru/virtual/tovary_nedeli?itm_pm=ru%3Ancp%3Actr%3Ait%3A11%3A4&_ga=2.148296562.497639215.1638262985-825064516.1638262985'
html_mag = requests.get(url_mag)
soup_mag = BeautifulSoup(html_mag.text, 'lxml')
content_mag1 = soup_mag.find_all('div', class_='catalog-item')
counter=0
for article in content_mag1:
    price_old = str(article.find('div', class_='catalog-item_price-old'))
    if price_old != 'None':
        price_old = price_old[1:len(price_old) - 1]
        price_old = price_old[price_old.index('>') + 1:price_old.index('<')]
        price_old=price_old.replace('\t','')
        price_old=price_old.replace('\n','')
        metro_old.append(price_old)
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
        metro_new.append(price_new)
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
#Ламода
lamoda_prod = []
lamoda_html = []
lamoda_old_price = []
lamoda_new_price = []
url_lamoda = 'https://www.lamoda.ru/c/4152/default-men/?display_locations=outlet&is_sale=1&zbs_content=outl_m_cats_769275_ru_2604_outlet_brands_m'
html_lamoda = requests.get(url_lamoda).text
soup_lamoda = BeautifulSoup(html_lamoda, 'html.parser')
content_lamoda1 = str(soup_lamoda.find_all('div', class_="products-catalog__list"))
counter=10
while counter!=0:
    if content_lamoda1[content_lamoda1.find(',"price":"'):content_lamoda1.find('"}]')]!='':
        price=content_lamoda1[content_lamoda1.find(',"price":"'):content_lamoda1.find('"}]')]
        lamoda_new_price.append(price[price.find(':"')+2:])
        counter-=1
    content_lamoda1=content_lamoda1[content_lamoda1.find('"}]')+3:]
counter=10
content_lamoda1 = str(soup_lamoda.find_all('div', class_="products-catalog__list"))
while counter!=0:
    if content_lamoda1[content_lamoda1.find('data-price-origin="'):content_lamoda1.find('" data-season=')]!='':
        price=content_lamoda1[content_lamoda1.find('data-price-origin="'):content_lamoda1.find('" data-season=')]
        lamoda_old_price.append(price[price.find('="')+2:])
        counter-=1
    content_lamoda1=content_lamoda1[content_lamoda1.find('" data-season=')+len('" data-season='):]
counter=10
content_lamoda1 = str(soup_lamoda.find_all('div', class_="products-catalog__list"))
while counter!=0:
    if content_lamoda1[content_lamoda1.find('href="'):content_lamoda1.find('/">')+1]!='':
        price=content_lamoda1[content_lamoda1.find('href="'):content_lamoda1.find('/">')+1]
        lamoda_html.append('https://www.lamoda.ru/'+price[7:])
        counter-=1
    content_lamoda1=content_lamoda1[content_lamoda1.find('/">')+len('/">'):]
counter=10
content_lamoda1 = str(soup_lamoda.find_all('div', class_="products-catalog__list"))
while counter!=0:
    if content_lamoda1[content_lamoda1.find('products-list-item__brand">'):content_lamoda1.find('</span></div></a>')]!='':
        price=content_lamoda1[content_lamoda1.find('products-list-item__brand">'):content_lamoda1.find('</span></div></a>')]
        price=price.replace('\n','')
        price = price.replace('\t', '')
        price = price.replace(' ', '',16)
        price=(price[price.find('d">')+len('d">'):price.find('<span')]+'/'+price[price.find('e">') + len('e">'):]).replace(' ','',35)
        lamoda_prod.append(price)
        counter-=1
    content_lamoda1=content_lamoda1[content_lamoda1.find('</span></div></a>')+len('</span></div></a>'):]
#Электроника
#restore
restore_prod = []
restore_html = []
restore_old_price = []
restore_new_price = []
url_restore = 'https://re-store.ru/sale/'
html_restore = requests.get(url_restore).text
soup_restore = BeautifulSoup(html_restore, 'html.parser')
content_restore1 = str(soup_restore.find_all('div', class_="catalog-items by-tile catalog__items"))
counter=12
while counter!=0:
    if content_restore1[content_restore1.find('<a class="catalog-item__link" href="'):content_restore1.find('"></a>')]!='':
        html=content_restore1[content_restore1.find('<a class="catalog-item__link" href="'):content_restore1.find('"></a>')]
        restore_html.append(('https://re-store.ru/'+str(html[html.find('f="')+4:])))
        counter-=1
    content_restore1=content_restore1[content_restore1.find('"></a>')+len('"></a>'):]
content_restore1 = str(soup_restore.find_all('div', class_="catalog-items by-tile catalog__items"))
counter=12
while counter!=0:
    if content_restore1[content_restore1.find('class="actual-price')+len('class="actual-price'):content_restore1.find('<link href="')]!='':
        price=content_restore1[content_restore1.find('class="actual-price'):content_restore1.find('<link href="')].replace('\xa0',' ')
        restore_new_price.append(price[price.find('itemprop="price">')+len('itemprop="price">'):price.find('</span>')])
        restore_old_price.append(price[price.find('catalog__item-price--old">')+len('catalog__item-price--old">'):price.find(' ₽</span>')])
        counter-=1
    content_restore1=content_restore1[content_restore1.find('<link href="')+len('<link href="'):]
content_restore1 = str(soup_restore.find_all('div', class_="catalog-items by-tile catalog__items"))
counter=12
while counter!=0:
    if content_restore1[content_restore1.find('class="clamp catalog__item-title">'):content_restore1.find('</span>\n</div>')]!='':
        prod=content_restore1[content_restore1.find('class="clamp catalog__item-title">')+len('class="clamp catalog__item-title">'):content_restore1.find('</span>\n</div>')]
        restore_prod.append(prod)
        counter-=1
    content_restore1=content_restore1[content_restore1.find('</span>\n</div>')+len('</span>\n</div>'):]
content_restore1 = str(soup_restore.find_all('div', class_="catalog-items by-tile catalog__items"))




#re:store
#жду код миши



#Аптека
#36.6
tts_prod = []
tts_html = []
tts_old_price = []
tts_new_price = []
url_tts = 'https://366.ru/c/wow-cena/'
html_tts = requests.get(url_tts).text
soup_tts = BeautifulSoup(html_tts, 'html.parser')
content_tts = str(soup_tts.find_all('div', class_="js-product-list-wrapper js-product-list-ave"))
counter = 0
while counter!=20:
    if content_tts[content_tts.find(' data-gtm-name="')+len(' data-gtm-name=')+1:content_tts.find('" data-gtm-position=')]!= '' and content_tts[content_tts.find('href="') + len('href="'):content_tts.find('">')] !='' and content_tts[content_tts.find('<span class="price price__old">')+len('<span class="price price__old">'):content_tts.find('<form action="/cart/add" ')+len('<form action="/cart/add" ')]!='':
        tts_prod.append(content_tts[content_tts.find(' data-gtm-name="')+len(' data-gtm-name=')+1:content_tts.find('" data-gtm-position=')])
        tts_html.append('https://366.ru'+content_tts[content_tts.find('href="') + len('href="'):content_tts.find('">\n')])
        new_price = content_tts[content_tts.find('<span class="price price__with_discount">')+len('<span class="price price__with_discount">'):content_tts.find('<span class="price price__old">')]
        old_price = content_tts[content_tts.find('<span class="price price__old">')+len('<span class="price price__old">'):content_tts.find('<form action="/cart/add" ')]
        new_price = new_price.replace('</span>','').replace('\t', '').replace(' ', '').replace('\n', '').replace('\xa0','')
        old_price = old_price.replace('</span>','').replace(' ', '').replace('</div>', '').replace('\t', '').replace('\n', '').replace('\xa0','')
        tts_old_price.append(old_price)
        tts_new_price.append(new_price)
    content_tts = content_tts[content_tts.find('" data-gtm-position=')+len('" data-gtm-position=')::]
    counter+=1

#asna
asna_prod = []
asna_html = []
asna_old_price = []
asna_new_price = []
url_asna = 'https://ishimbaj.asna.ru/sales/actions/'
html_asna = requests.get(url_asna).text
soup_asna = BeautifulSoup(html_asna, 'html.parser')
content_asna1 = soup_asna.find_all('a', class_="product_name__VzTPG")
content_asna2 = soup_asna.find_all('span', class_="catalogPrice_price__TRAFl")
content_asna3 = soup_asna.find_all('span',class_='Tooltip_root__ft_kM')

for article in content_asna1:
    asna_html.append('https://ishimbaj.asna.ru'+str(article.get('href')))
    article = str(article)
    article = article[1:len(article)-1]
    article = article[article.find('>')+1:article.find('<')]
    asna_prod.append(article)
for article in content_asna2:
    article = str(article)
    article = article[1:len(article)-1]
    article = article[article.find('>')+1:article.find('<')]
    asna_old_price.append(article)
for article in content_asna3:
    article = str(article)
    article = article[article.find('<span>')+len('<span>'):article.find('</span>')]
    asna_new_price.append(article)

gor_prod = []
gor_html = []
gor_old_price = []
gor_new_price = []
url_gor = 'https://gorzdrav.org/category/skidka-do-15/'
html_gor = requests.get(url_gor).text
soup_gor = BeautifulSoup(html_gor, 'html.parser')
content_gor1 = soup_gor.find_all('div', class_='c-prod-item__title')
content_gor2 = soup_gor.find_all('span', class_='b-price b-price--last')
content_gor3 = soup_gor.find_all('span', class_='b-price b-price--discount')
content_gor4 = soup_gor.find_all('a', class_='c-prod-item__link js-product-details-link')
counter = 0
for article in content_gor1:
    article = str(article)
    article = article[1:len(article)]
    article = article[article.find('div class="c-prod-item__title">')+len('div class="c-prod-item__title">'):article.find('</div>')]
    article = article.replace('\t','').replace('\n','').replace('                        ','').replace('\xa010000\xa0','')
    gor_prod.append(article)
    counter+=1
for article in content_gor2:
    article = str(article)
    article = article[1:len(article)]
    article = article[article.find('span class="b-price b-price--last">') + len('span class="b-price b-price--last">'):article.find('</span')]
    article = article.replace('\t', '').replace('\n', '').replace('                ', '').replace('\xa0', '')
    gor_old_price.append(article)
for article in content_gor3:
    article = str(article)
    article = article[1:len(article)]
    article = article[article.find('span class="b-price b-price--discount">') + len('span class="b-price b-price--discount">'):article.find('</span')]
    article = article.replace('\t', '').replace('\n', '').replace('            ', '').replace('\xa0', '')
    gor_new_price.append(article)
for article in content_gor4:
    article = article.get('href')
    gor_html.append('https://gorzdrav.org'+article)

#Ювелирка

#Cколково
#Жду код от миши
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
                item2 = types.InlineKeyboardButton('Перекресток', callback_data='PR')
                item4 = types.InlineKeyboardButton('Магнолия', callback_data='MAGA')
                item5 = types.InlineKeyboardButton('Метро', callback_data='METRO')

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

                markup.add(item1, item4)
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
                time.sleep(1)
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти во ВкусВилле:')
                for i in range(len(vkusvill_prod)):
                    txt=str(vkusvill_prod[i])+'\n'+'⛔'+'Старая цена:'+' '+'\u0336'.join(str(vkusvill_old_price[i]))+'\u0336'+'\n'+'✅'+'Новая цена:'+' '+str(vkusvill_new_price[i])+'\n'+'🌐'+'Ссылка:'+' '+str(vkusvill_html[i])
                    bot.send_message(chat_id=call.message.chat.id,text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)

            elif call.data == 'PR':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                time.sleep(1)
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в Перекрестке:')
                for i in range(len(metro_prod)):
                    txt = str(metro_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(metro_old[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(metro_new[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(metro_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)

            elif call.data == 'MAGA':
                bot.send_message(chat_id=call.message.chat.id, text='Подождите загружаем скидки:')
                time.sleep(1)
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
                time.sleep(1)
                bot.send_message(chat_id=call.message.chat.id, text='Вот какие скидки нам удалось найти в METRO:')
                for i in range(len(perek_prod)):
                    txt = str(perek_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(perek_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(perek_new_price[i])+'\n'+'🌐'+'Ссылка:'+' '+str(perek_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)

            elif call.data == 'kot':
                bot.send_message(chat_id=call.message.chat.id, text='Скидки в пуме')
                for i in range(len(puma_prod)):
                    txt = str(puma_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(puma_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(puma_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(puma_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)

            elif call.data == 'ekin':
                for i in range(len(nike_prod)):
                    txt = str(nike_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(nike_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(nike_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(nike_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)

            elif call.data == '36.6':
                for i in range(len(tts_prod)):
                    txt = str(tts_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(tts_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(tts_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(tts_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == 'asna':
                for i in range(len(tts_prod)):
                    txt = str(asna_prod[i]) + '\n' + '✅' + 'Цена:' + ' ' + ''.join(str(asna_old_price[i])) + '' + '\n' + '💳' + 'Начисляемые баллы:' + ' ' + str(asna_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(asna_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == 'gor':
                for i in range(len(gor_prod)):
                    txt = str(gor_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(gor_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(gor_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(gor_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == 'lam':
                for i in range(len(lamoda_prod)):
                    txt = str(lamoda_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(lamoda_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(lamoda_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(lamoda_html[i])
                    bot.send_message(chat_id=call.message.chat.id, text=txt)
                    time.sleep(0.5)
                markup = types.InlineKeyboardMarkup(row_width=1)
                item1 = types.InlineKeyboardButton('Хочу ещё!', callback_data='/restart')
                markup.add(item1)
                bot.send_message(chat_id=call.message.chat.id, text='Хотите больше скидок?', reply_markup=markup)
            elif call.data == 'res':
                for i in range(len(restore_prod)):
                    txt = str(restore_prod[i]) + '\n' + '⛔' + 'Старая цена:' + ' ' + '\u0336'.join(str(restore_old_price[i])) + '\u0336' + '\n' + '✅' + 'Новая цена:' + ' ' + str(restore_new_price[i]) + '\n' + '🌐' + 'Ссылка:' + ' ' + str(restore_html[i])
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