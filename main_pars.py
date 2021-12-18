from bs4 import BeautifulSoup
import requests

# парс с сайтов
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'}

#Продуктовые
#Вкусвилл
def pars_vv():
    '''
        Данная функция парсит скидки с сайта vkusvill.ru, vkusvill_prod - массив для названий продуктов, vkusvill_html - массив для ссылок для данных товаров, vkusvill_old_price - массив для старых цен товаров, vkusvill_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    vkusvill_prod = []
    vkusvill_html = []
    vkusvill_old_price = []
    vkusvill_new_price = []
    url_vv = 'https://vkusvill.ru/bonuses/'# Делаю парс из магазина Вкусвилл
    html_vv = requests.get(url_vv)
    if type(html_vv)==str:
        soup_vv = BeautifulSoup(html_vv, 'html.parser')
    else:
        soup_vv = BeautifulSoup(html_vv.text, 'html.parser')

    content_vv1 = soup_vv.find_all('div', class_="ProductCard__content")
    content_vv2 = soup_vv.find_all('div', class_="ProductCard__price")

    for article in content_vv1:
        tovar = article.find('a', class_='ProductCard__link js-datalayer-catalog-list-name').get('title')
        vkusvill_prod.append(str(tovar).replace('\xa0',''))
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

    return vkusvill_prod, vkusvill_html, vkusvill_old_price,vkusvill_new_price
#Перекресток
def pars_perek():
    '''
        Данная функция парсит скидки с сайта perekrestok.ru, perek_prod - массив для названий продуктов, perek_html - массив для ссылок для данных товаров, perek_old_price - массив для старых цен товаров, perek_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    perek_prod = []
    perek_old_price = []
    perek_new_price = []
    perek_html=[]
    url_per = 'https://www.perekrestok.ru/cat/d?orderBy=popularity&orderDirection=desc'
    html_per = requests.get(url_per)
    if type(html_per)==str:
        soup_per = BeautifulSoup(html_per, 'html.parser')
    else:
        soup_per = BeautifulSoup(html_per.text, 'html.parser')
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
    return perek_prod, perek_html, perek_old_price, perek_new_price
#Магнолия
def pars_mag():
    '''
        Данная функция парсит скидки с сайта shop.mgnl.ru, mag_prod - массив для названий продуктов, mag_html - массив для ссылок для данных товаров, mag_old_price - массив для старых цен товаров, mag_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    mag_prod = []
    mag_html = []
    mag_old_price = []
    mag_new_price = []
    url_mag = 'https://shop.mgnl.ru/catalog/super-aktsiya-skidka-50/'
    html_mag = requests.get(url_mag)
    if type(html_mag)==str:
        soup_mag = BeautifulSoup(html_mag, 'html.parser')
    else:
        soup_mag = BeautifulSoup(html_mag.text, 'html.parser')
    content_mag1 = str(soup_mag.find_all('div', class_="ajax_load cur block"))
    content_mag2 = str(soup_mag.find_all('div', class_="ajax_load cur block"))
    counter=10
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
    return mag_prod, mag_html, mag_old_price, mag_new_price
#Метро
def pars_metro():
    '''
        Данная функция парсит скидки с сайта msk.metro-cc.ru, metro_prod - массив для названий продуктов, metro_html - массив для ссылок для данных товаров, metro_old - массив для старых цен товаров, metro_new - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    metro_prod= []
    metro_html = []
    metro_old = []
    metro_new = []
    url_mag = 'https://msk.metro-cc.ru/virtual/tovary_nedeli?itm_pm=ru%3Ancp%3Actr%3Ait%3A11%3A4&_ga=2.148296562.497639215.1638262985-825064516.1638262985'
    html_mag = requests.get(url_mag)
    if type(html_mag)==str:
        soup_mag = BeautifulSoup(html_mag, 'html.parser')
    else:
        soup_mag = BeautifulSoup(html_mag.text, 'html.parser')
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
    return metro_prod, metro_html, metro_old, metro_new
#Магазины одежды
#НАЙК
def pars_nike():
    '''
        Данная функция парсит скидки с сайта nike.com, nike_prod - массив для названий продуктов, nike_html - массив для ссылок для данных товаров, nike_old_price - массив для старых цен товаров, nike_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    nike_prod = []
    nike_html = []
    nike_old_price = []
    nike_new_price = []
    url_nike = 'https://www.nike.com/ru/w/sale-3yaep'
    html_nike = requests.get(url_nike)
    if type(html_nike)==str:
        soup_nike = BeautifulSoup(html_nike, 'html.parser')
    else:
        soup_nike = BeautifulSoup(html_nike.text, 'html.parser')
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
    return nike_prod, nike_html, nike_old_price, nike_new_price
#Пума
def pars_puma():
    '''
        Данная функция парсит скидки с сайта ru.puma.com, puma_prod - массив для названий продуктов, puma_html - массив для ссылок для данных товаров, puma_old_price - массив для старых цен товаров, puma_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    puma_prod = []
    puma_html = []
    puma_old_price = []
    puma_new_price = []
    url_puma = 'https://ru.puma.com/skidki.html'
    html_puma = requests.get(url_puma)
    if type(html_puma)==str:
        soup_puma = BeautifulSoup(html_puma, 'html.parser')
    else:
        soup_puma = BeautifulSoup(html_puma.text, 'html.parser')
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
    return puma_prod, puma_html, puma_old_price, puma_new_price
#Ламода
def pars_lamoda():
    '''
        Данная функция парсит скидки с сайта lamoda.ru, lamoda_prod - массив для названий продуктов, lamoda_html - массив для ссылок для данных товаров, lamoda_old_price - массив для старых цен товаров, lamoda_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    lamoda_prod = []
    lamoda_html = []
    lamoda_old_price = []
    lamoda_new_price = []
    url_lamoda = 'https://www.lamoda.ru/c/4152/default-men/?display_locations=outlet&is_sale=1&zbs_content=outl_m_cats_769275_ru_2604_outlet_brands_m'
    html_lamoda = requests.get(url_lamoda)
    if type(html_lamoda)==str:
        soup_lamoda = BeautifulSoup(html_lamoda, 'html.parser')
    else:
        soup_lamoda = BeautifulSoup(html_lamoda.text, 'html.parser')
    content_lamoda1 = str(soup_lamoda.find_all('div', class_="products-catalog__list"))
    counter = 10
    while counter != 0:
        if content_lamoda1[content_lamoda1.find('data-price-origin="'):content_lamoda1.find('data-season=')] != '':
            price = content_lamoda1[
                    content_lamoda1.find('data-price-origin="') + len('data-price-origin="'):content_lamoda1.find(
                        'data-season=')].replace('" ', '')
            lamoda_old_price.append(price)
            counter -= 1
        content_lamoda1 = content_lamoda1[content_lamoda1.find('data-season=') + len('data-season='):]
    counter = 10
    content_lamoda1 = str(soup_lamoda.find_all('div', class_="products-catalog__list"))
    while counter != 0:
        if content_lamoda1[
           content_lamoda1.find('data-name="') + len('data-name="'):content_lamoda1.find('data-price-origin=')] != '':
            price = content_lamoda1[
                    content_lamoda1.find('data-name="') + len('data-name="'):content_lamoda1.find('data-price-origin=')]
            price = price[price.find('data-price="') + len('data-price="'):]
            lamoda_new_price.append(price.replace('"', ''))
            counter -= 1
        content_lamoda1 = content_lamoda1[content_lamoda1.find('data-price-origin=') + len('data-price-origin='):]
    counter = 10
    content_lamoda1 = str(soup_lamoda.find_all('div', class_="products-catalog__list"))
    while counter != 0:
        if content_lamoda1[
           content_lamoda1.find('href="') + len('href="'):content_lamoda1.find('<div class="to-favorites')] != '':
            html = content_lamoda1[
                   content_lamoda1.find('href="') + len('href="'):content_lamoda1.find('<div class="to-favorites')]
            lamoda_html.append('https://www.lamoda.ru' + html.replace('">\n', ''))
            counter -= 1
        content_lamoda1 = content_lamoda1[
                          content_lamoda1.find('<div class="to-favorites') + len('<div class="to-favorites'):]
    counter = 10
    content_lamoda1 = str(soup_lamoda.find_all('div', class_="products-catalog__list"))
    while counter != 0:
        if content_lamoda1[
           content_lamoda1.find('products-list-item__brand">') + len(
               'products-list-item__brand">'):content_lamoda1.find(
               '</span></div></a><div class="groups-by-sku groups-by-sku_hidden">')] != '':
            price = content_lamoda1[content_lamoda1.find('products-list-item__brand">') + len(
                'products-list-item__brand">'):content_lamoda1.find(
                '</span></div></a><div class="groups-by-sku groups-by-sku_hidden">')]
            price1 = price[:price.find('<sp')].replace(' ', '').replace('\n', '').replace('\t', '')
            price2 = price[price.find('">') + 2:].replace('\n', '').replace('\t', '')
            price2 = price2[:price2.find('</span></div>')].replace(' ', '', 20)
            lamoda_prod.append(price1 + ' ' + price2)
            counter -= 1
        content_lamoda1 = content_lamoda1[content_lamoda1.find('</span></div></a><div class="') + len('</span></div></a><div class="'):]
    return lamoda_prod, lamoda_html, lamoda_old_price, lamoda_new_price
#Электроника
#Мвидео
def pars_mvideo():
    '''
        Данная функция парсит скидки с сайта mvideo.ru, mvideo_prod - массив для названий продуктов, mvideo_html - массив для ссылок для данных товаров, mvideo_old_price - массив для старых цен товаров, mvideo_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    mvideo_prod = []
    mvideo_html = []
    mvideo_old_price = []
    mvideo_new_price = []
    url_mvideo = 'https://www.mvideo.ru/promo/komputery-i-noutbuki-mark188276424'
    html_mvideo = requests.get(url_mvideo, headers=headers)
    if type(html_mvideo)==str:
        soup_mvideo = html_mvideo
        soup_mvideo2=html_mvideo
    else:
        soup_mvideo = html_mvideo.content.decode()
        soup_mvideo2 = html_mvideo.content.decode()
    counter=10
    while counter!=0:
        if soup_mvideo[soup_mvideo.find('<div class="fl-product-tile__picture-holder c-product-tile-picture__holder">'):soup_mvideo.find('"productCategoryId"')+len('"productCategoryId"')] != '':
            prod = soup_mvideo[soup_mvideo.find('<div class="fl-product-tile__picture-holder c-product-tile-picture__holder">'):soup_mvideo.find('"productCategoryId"')+len('"productCategoryId"')]
            html ='https://www.mvideo.ru/' + prod[prod.find('<a href="/')+len('<a href="/'):prod.find('" class="fl-product-tile-picture fl-product-tile')]
            mvideo_html.append(html)
            price_new = prod[prod.find('"productPriceLocal": "')+len('"productPriceLocal": "'):prod.find('"productId":')]
            price_new = price_new[:price_new.find('",')].replace('\n\t','')
            mvideo_new_price.append(price_new)
            prod=prod[prod.find('"productName": "')+len('"productName": "'):prod.find('"productCategoryId"')]
            prod=prod[:prod.find('",')]
            mvideo_prod.append(prod)
            counter -= 1
        soup_mvideo=soup_mvideo[soup_mvideo.find('"productCategoryId"')+len('"productCategoryId"'):]
    soup_mvideo=soup_mvideo2
    counter=10
    while counter!=0:
        if soup_mvideo[soup_mvideo.find('eventProductPrice')+len('eventProductPrice'):soup_mvideo.find('eventProductBrand')]:
            price_old=soup_mvideo[soup_mvideo.find('eventProductPrice')+len('eventProductPrice'):soup_mvideo.find('eventProductBrand')]
            price_old=price_old[price_old.find("': '")+len("': '"):price_old.find("',")]
            mvideo_old_price.append(price_old)
            counter-=1
        soup_mvideo=soup_mvideo[soup_mvideo.find('eventProductBrand')+len('eventProductBrand'):]
    return mvideo_prod, mvideo_html, mvideo_old_price, mvideo_new_price
#re:Store
def pars_restore():
    '''
        Данная функция парсит скидки с сайта re-store.ru, restore_prod - массив для названий продуктов, restore_html - массив для ссылок для данных товаров, restore_old_price - массив для старых цен товаров, restore_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    restore_prod = []
    restore_html = []
    restore_old_price = []
    restore_new_price = []
    url_restore = 'https://re-store.ru/sale/'
    html_restore = requests.get(url_restore)
    if type(html_restore)==str:
        soup_restore = BeautifulSoup(html_restore, 'html.parser')
    else:
        soup_restore = BeautifulSoup(html_restore.text, 'html.parser')
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
    return restore_prod, restore_html, restore_old_price, restore_new_price
#eldarado
def pars_eladarado():
    '''
        Данная функция парсит скидки с сайта eldorado.ru, eladarado_prod - массив для названий продуктов, eladarado_html - массив для ссылок для данных товаров, eldarado_old_price - массив для старых цен товаров, eldarado_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    eladarado_prod = []
    eladarado_html = []
    eldarado_old_price = []
    eldarado_new_price = []
    url_eldarado = 'https://www.eldorado.ru/promo/prm-newyear-sale/?from=hub'
    html_eldarado = requests.get(url_eldarado, headers=headers)
    if type(html_eldarado)==str:
        soup_eldarado = html_eldarado
    else:
        soup_eldarado = html_eldarado.content.decode('windows-1251')
    counter = 0
    while counter!=11:
        item = soup_eldarado[soup_eldarado.find('<a class="def-product__name" href=')+len('<a class="def-product__name" href='):soup_eldarado.find('                      </div> -->')]
        href = (item[:item.find(' title')])
        href = 'https://www.eldorado.ru'+href[1:len(href)-1]
        old_price = item[item.find('<span class="def-product__old-price-text">')+len('<span class="def-product__old-price-text">'):item.find('<span class="rubl">')]
        old_price = old_price.replace('&nbsp;','')
        new_price = item[item.find(' data-new-price=')+len(' data-new-price='):item.find(' >- 600<')]
        new_price = new_price.replace('&nbsp;','').replace('"','')
        name = item[item.find(' target="_blank">')+len(' target="_blank">'):item.find('</a>')]
        eladarado_prod.append(name)
        eladarado_html.append(href)
        eldarado_old_price.append(old_price)
        eldarado_new_price.append(new_price)
        counter+=1
        soup_eldarado = soup_eldarado[soup_eldarado.find('                        <li class="def-product"')+len('                        <li class="def-product"'):]
    eladarado_prod = eladarado_prod[1:]
    eladarado_html = eladarado_html[1:]
    eldarado_new_price = eldarado_new_price[1:]
    eldarado_old_price = eldarado_old_price[1:]
    return eladarado_prod, eladarado_html, eldarado_old_price, eldarado_new_price

#Аптека
#36.6
def pars_tts():
    '''
        Данная функция парсит скидки с сайта 366.ru, tts_prod - массив для названий продуктов, tts_html - массив для ссылок для данных товаров, tts_old_price - массив для старых цен товаров, tts_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    tts_prod = []
    tts_html = []
    tts_old_price = []
    tts_new_price = []
    url_tts = 'https://366.ru/c/wow-cena/'
    html_tts = requests.get(url_tts)
    if type(html_tts)==str:
        soup_tts = BeautifulSoup(html_tts, 'html.parser')
    else:
        soup_tts = BeautifulSoup(html_tts.text, 'html.parser')
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
    return tts_prod, tts_html, tts_old_price, tts_new_price
#asna
def pars_asna():
    '''
        Данная функция парсит скидки с сайта ishimbaj.asna.ru, asna_prod - массив для названий продуктов, asna_html - массив для ссылок для данных товаров, asna_old_price - массив для старых цен товаров, asna_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    asna_prod = []
    asna_html = []
    asna_old_price = []
    asna_new_price = []
    url_asna = 'https://ishimbaj.asna.ru/sales/actions/'
    html_asna = requests.get(url_asna)
    if type(html_asna)==str:
        soup_asna = BeautifulSoup(html_asna, 'html.parser')
    else:
        soup_asna = BeautifulSoup(html_asna.text, 'html.parser')
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
    return asna_prod, asna_html, asna_old_price, asna_new_price
#Горздрав
def pars_gor():
    '''
        Данная функция парсит скидки с сайта gorzdrav.org, gor_prod - массив для названий продуктов, gor_html - массив для ссылок для данных товаров, gor_old_price - массив для старых цен товаров, gor_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    gor_prod = []
    gor_html = []
    gor_old_price = []
    gor_new_price = []
    url_gor = 'https://gorzdrav.org/category/skidka-do-15/'
    html_gor = requests.get(url_gor)
    if type(html_gor)==str:
        soup_gor = BeautifulSoup(html_gor, 'html.parser')
    else:
        soup_gor = BeautifulSoup(html_gor.text, 'html.parser')
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
    return gor_prod, gor_html, gor_old_price, gor_new_price
#Ювелирка
#Cколково
def pars_sokolov():
    '''
        Данная функция парсит скидки с сайта sokolov.ru, sokolov_prod - массив для названий продуктов, sokolov_html - массив для ссылок для данных товаров, sokolov_old_price - массив для старых цен товаров, sokolov_new_price - массив для новых цен товаров
        Первый цикл отвечает за поиск: названия продукта и ссылки на данный продукт
        Второй цикл отвечает за поиск: старой и новой цены
        В функцию ничего не входит
        Функция возвращает 4 массива с информацией о продукте, а именно название товара, ссылку на него, новую и старую цены
    '''
    sokolov_prod = []
    sokolov_html = []
    sokolov_old_price = []
    sokolov_new_price = []
    url_sokolov = 'https://sokolov.ru/jewelry-catalog/sale50/sale60/sale70/'
    html_sokolov = requests.get(url_sokolov)
    if type(html_sokolov)==str:
        soup_sokolov = BeautifulSoup(html_sokolov, 'html.parser')
    else:
        soup_sokolov = BeautifulSoup(html_sokolov.text, 'html.parser')
    content_sokolov1 = str(soup_sokolov.find_all('div', class_="list"))
    counter=10
    while counter!=0:
        if content_sokolov1[content_sokolov1.find('<span class="product-description" data-product-name="')+len('<span class="product-description" data-product-name="'):content_sokolov1.find('</span>\n<div class="product-characteristics">')]!='':
            prod=content_sokolov1[content_sokolov1.find('<span class="product-description" data-product-name="')+len('<span class="product-description" data-product-name="'):content_sokolov1.find('</span>\n<div class="product-characteristics">')]
            sokolov_prod.append(prod[:prod.find('">')])
            counter-=1
        content_sokolov1=content_sokolov1[content_sokolov1.find('</span>\n<div class="product-characteristics">')+len('</span>\n<div class="product-characteristics">'):]
    content_sokolov1 = str(soup_sokolov.find_all('div', class_="list"))
    counter=10
    while counter!=0:
        if content_sokolov1[content_sokolov1.find('<div class="price main" data-product-price="')+len('<div class="price main" data-product-price="'):content_sokolov1.find('<span class="price sale"')]!='':
            price=content_sokolov1[content_sokolov1.find('<div class="price main" data-product-price="')+len('<div class="price main" data-product-price="'):content_sokolov1.find('<span class="price sale"')]
            price1=price[:price.find('">')]
            price2=price[price.find('data-product-old-price="')+len('data-product-old-price="'):]
            price2=price2[:price2.find('.00')]
            sokolov_new_price.append(price1)
            sokolov_old_price.append(price2)
            counter-=1
        content_sokolov1=content_sokolov1[content_sokolov1.find('<span class="price sale"')+len('<span class="price sale"'):]
    content_sokolov1 = str(soup_sokolov.find_all('div', class_="list"))
    counter=10
    while counter!=0:
        if content_sokolov1[content_sokolov1.find('" href="')+len('" href="'):content_sokolov1.find('<button aria-label=')]!='':
            html=content_sokolov1[content_sokolov1.find('" href="')+len('" href="'):content_sokolov1.find('<button aria-label=')]
            sokolov_html.append('https://sokolov.ru'+html.replace('">','').replace('\n',''))
            counter-=1
        content_sokolov1=content_sokolov1[content_sokolov1.find('<button aria-label=')+len('<button aria-label='):]
    return sokolov_prod, sokolov_html, sokolov_old_price, sokolov_new_price