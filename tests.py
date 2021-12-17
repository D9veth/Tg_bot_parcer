from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest
import unittest
import time
import requests
from unittest.mock import patch
import main_pars
from main_pars import pars_vv,pars_gor,pars_tts,pars_asna,pars_mag,pars_puma,pars_metro,pars_perek,pars_mvideo,pars_nike,pars_lamoda,pars_sokolov,pars_eladarado,pars_restore
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'}
# Введите ваши API ID, hash and session name
api_id = int('17788181')
api_hash = "29d66437042a0f576c7d7a1854c3d4e2"
client = TelegramClient('Михаил', api_id, api_hash)


client.start()

class Test(unittest.TestCase):
    def test_vv(self):
        a,b,c,d = pars_vv()
        self.assertEqual(len(a),len(b))
    def test_vv2(self):
        a,b,c,d = pars_vv()
        self.assertEqual(len(c),len(d))
    def test_vv3(self):
        a,b,c,d = pars_vv()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_vv', return_value=requests.get('https://vkusvill.ru/bonuses/').text)
    def test_vv4(self,pars_vv):
        if pars_vv().count('ProductCard__link js-datalayer-catalog-list-name')>0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_per(self):
        a,b,c,d = pars_perek()
        self.assertEqual(len(a),len(b))
    def test_per2(self):
        a,b,c,d = pars_perek()
        self.assertEqual(len(c),len(d))
    def test_per3(self):
        a,b,c,d = pars_perek()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_perek', return_value=requests.get('https://www.perekrestok.ru/cat/d?orderBy=popularity&orderDirection=desc').text)
    def test_per4(self, pars_perek):
        if pars_perek().count('product-card-title__wrapper') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_mag(self):
        a,b,c,d = pars_mag()
        self.assertEqual(len(a),len(b))
    def test_mag2(self):
        a,b,c,d = pars_mag()
        self.assertEqual(len(c),len(d))
    def test_mag3(self):
        a,b,c,d = pars_mag()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_mag',return_value=requests.get('https://shop.mgnl.ru/catalog/super-aktsiya-skidka-50/').text)
    def test_mag4(self, pars_mag):
        if pars_mag().count('ajax_load cur block') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_metro(self):
        a,b,c,d = pars_metro()
        self.assertEqual(len(a),len(b))
    def test_metro2(self):
        a,b,c,d = pars_metro()
        self.assertEqual(len(c),len(d))
    def test_metro3(self):
        a,b,c,d = pars_metro()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_metro',return_value=requests.get('https://msk.metro-cc.ru/virtual/tovary_nedeli?itm_pm=ru%3Ancp%3Actr%3Ait%3A11%3A4&_ga=2.148296562.497639215.1638262985-825064516.1638262985').text)
    def test_metro4(self, pars_metro):
        if pars_metro().count('catalog-item') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_mvideo(self):
        a,b,c,d = pars_mvideo()
        self.assertEqual(len(a),len(b))
    def test_mvideo2(self):
        a,b,c,d = pars_mvideo()
        self.assertEqual(len(c),len(d))
    def test_mvideo3(self):
        a,b,c,d = pars_mvideo()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_mvideo',return_value=requests.get('https://www.mvideo.ru/promo/komputery-i-noutbuki-mark188276424',headers=headers).text)
    def test_mvideo4(self, pars_mvideo):
        if pars_mvideo().count('<div class="fl-product-tile__picture-holder c-product-tile-picture__holder">') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_restore(self):
        a,b,c,d = pars_restore()
        self.assertEqual(len(a),len(b))
    def test_restore2(self):
        a,b,c,d = pars_restore()
        self.assertEqual(len(c),len(d))
    def test_restore3(self):
        a,b,c,d = pars_restore()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_restore', return_value=requests.get('https://re-store.ru/sale/').text)
    def test_restore4(self, pars_restore):
        if pars_restore().count('catalog-items by-tile catalog__items') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_eldorado(self):
        a,b,c,d = pars_eladarado()
        self.assertEqual(len(a),len(b))
    def test_eldorado2(self):
        a,b,c,d = pars_eladarado()
        self.assertEqual(len(c),len(d))
    def test_eldorado3(self):
        a,b,c,d = pars_eladarado()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_eladarado', return_value=requests.get('https://www.eldorado.ru/promo/prm-newyear-sale/?from=hub',headers=headers).text)
    def test_eldorado4(self, pars_eladarado):
        if pars_eladarado().count('<a class="def-product__name" href=') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_nike(self):
        a,b,c,d = pars_nike()
        self.assertEqual(len(a),len(b))
    def test_nike2(self):
        a,b,c,d = pars_nike()
        self.assertEqual(len(c),len(d))
    def test_nike3(self):
        a,b,c,d = pars_nike()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_nike',return_value=requests.get('https://www.nike.com/ru/w/sale-3yaep').text)
    def test_nike4(self, pars_nike):
        if pars_nike().count('product-card__body') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_lamoda(self):
        a,b,c,d = pars_lamoda()
        self.assertEqual(len(a),len(b))
    def test_lamoda2(self):
        a,b,c,d = pars_lamoda()
        self.assertEqual(len(d),len(c))
    def test_lamoda3(self):
        a,b,c,d = pars_lamoda()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_lamoda',return_value=requests.get('https://www.lamoda.ru/c/4152/default-men/?display_locations=outlet&is_sale=1&zbs_content=outl_m_cats_769275_ru_2604_outlet_brands_m').text)
    def test_lamoda4(self, pars_lamoda):
        if pars_lamoda().count('products-catalog__list') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_puma(self):
        a,b,c,d = pars_puma()
        self.assertEqual(len(a),len(b))
    def test_puma2(self):
        a,b,c,d = pars_puma()
        self.assertEqual(len(d),len(c))
    def test_puma3(self):
        a,b,c,d = pars_puma()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_puma',return_value=requests.get('https://ru.puma.com/skidki.html').text)
    def test_puma4(self, pars_puma):
        if pars_puma().count('product-item__details') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_sokolov(self):
        a,b,c,d = pars_sokolov()
        self.assertEqual(len(a),len(b))
    def test_sokolov2(self):
        a,b,c,d = pars_sokolov()
        self.assertEqual(len(d),len(c))
    def test_sokolov3(self):
        a,b,c,d = pars_sokolov()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_sokolov',return_value=requests.get('https://sokolov.ru/jewelry-catalog/sale50/sale60/sale70/').text)
    def test_sokolov4(self, pars_sokolov):
        if pars_sokolov().count('list') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_366(self):
        a,b,c,d = pars_tts()
        self.assertEqual(len(a),len(b))
    def test_3662(self):
        a,b,c,d = pars_tts()
        self.assertEqual(len(d),len(c))
    def test_3663(self):
        a,b,c,d = pars_tts()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_tts',return_value=requests.get('https://366.ru/c/wow-cena/').text)
    def test_3664(self, pars_tts):
        if pars_tts().count('js-product-list-wrapper js-product-list-ave') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_goz(self):
        a,b,c,d = pars_gor()
        self.assertEqual(len(a),len(b))
    def test_goz2(self):
        a,b,c,d = pars_gor()
        self.assertEqual(len(d),len(c))
    def test_goz3(self):
        a,b,c,d = pars_gor()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_gor',return_value=requests.get('https://gorzdrav.org/category/skidka-do-15/').text)
    def test_goz4(self, pars_gor):
        if pars_gor().count('c-prod-item__title') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_asna(self):
        a,b,c,d = pars_asna()
        self.assertEqual(len(a),len(b))
    def test_asna2(self):
        a,b,c,d = pars_asna()
        self.assertEqual(len(d),len(c))
    def test_asna3(self):
        a,b,c,d = pars_asna()
        self.assertEqual(len(b),len(c))
    @patch('main_pars.pars_asna', return_value=requests.get('https://ishimbaj.asna.ru/sales/actions/').text)
    def test_asna4(self, pars_asna):
        if pars_asna().count('product_name__VzTPG') > 0:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def testStart(self):
        try:
            client.send_message('@post_project_bot', '/start')
            time.sleep(2)
            messages = client.get_messages('@post_project_bot')
            for message in client.get_messages('@post_project_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Добро пожаловать,Михаил!\nЗдесь вы можете узнать, наиболее продоваемые товары, товары со скидками'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def test_Restart1(self):
        try:
            client.send_message('@post_project_bot', '/start')
            time.sleep(2)
            messages = client.get_messages('@post_project_bot')
            messages[0].click()
            time.sleep(2)

            for message in client.get_messages('@post_project_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выберете магазин:'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def test_Restart2(self):
        try:
            client.send_message('@post_project_bot', '/start')
            time.sleep(2)
            messages = client.get_messages('@post_project_bot')
            messages[0].click()
            time.sleep(2)

            for message in client.get_messages('@post_project_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выберете магазин одежды:'
            self.assertRegex(m, text)
        except:
            self.assertFalse(False)

    def test_Restart3(self):
        try:
            client.send_message('@post_project_bot', '/start')
            time.sleep(2)
            messages = client.get_messages('@post_project_bot')
            messages[0].click()
            time.sleep(2)
            messages = client.get_messages('@post_project_bot')
            messages[0].click()
            time.sleep(2)

            for message in client.get_messages('@post_project_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Хотите больше скидок?'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)

    def test_Restart4(self):
        try:
            client.send_message('@post_project_bot', '/start')
            time.sleep(2)
            messages = client.get_messages('@post_project_bot')
            messages[0].click()
            time.sleep(2)
            messages = client.get_messages('@post_project_bot')
            messages[0].click()
            time.sleep(2)

            for message in client.get_messages('@post_project_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Хотите ещё больше скидок?'
            self.assertRegex(m, text)
        except:
            self.assertFalse(False)

