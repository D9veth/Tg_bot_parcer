from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest
from pathlib import Path
import unittest
import time
import requests
from unittest.mock import patch
import main_pars
from main_pars import pars_vv,pars_gor,pars_tts,pars_asna,pars_mag,pars_puma,pars_metro,pars_perek,pars_mvideo,pars_nike,pars_lamoda,pars_sokolov,pars_eladarado,pars_restore
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36'}
# Введите ваши API ID, hash and session name
api_id = int('')
api_hash = ""
client = TelegramClient('', api_id, api_hash)


client.start()

class Test(unittest.TestCase):
    @patch('requests.get', return_value=(Path('data/vv.html').read_text('utf-8')))
    def test_vv(self,html_vv):
        a,b,c,d = pars_vv()
        self.assertEqual(len(a),len(b))
        self.assertEqual(len(c),len(d))
        self.assertEqual(len(b),len(c))
        self.assertEqual(pars_vv()[2][0],'52')
        self.assertEqual(pars_vv()[3][0],'40')

    def test_per(self):
        a,b,c,d = pars_perek()
        self.assertEqual(len(a),len(b))
    def test_per2(self):
        a,b,c,d = pars_perek()
        self.assertEqual(len(c),len(d))
    def test_per3(self):
        a,b,c,d = pars_perek()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/perek.html').read_text('utf-8')))
    def test_per4(self, html_per):
        self.assertEqual(pars_perek()[3][0], '59,90 ₽')
    @patch('requests.get', return_value=(Path('data/perek.html').read_text('utf-8')))
    def test_per5(self, html_per):
        self.assertEqual(pars_perek()[1][0], 'https://www.perekrestok.ru/cat/114/p/moloko-pasterizovannoe-domik-v-derevne-2-5-930ml-3255206')

    def test_mag(self):
        a,b,c,d = pars_mag()
        self.assertEqual(len(a),len(b))
    def test_mag2(self):
        a,b,c,d = pars_mag()
        self.assertEqual(len(c),len(d))
    def test_mag3(self):
        a,b,c,d = pars_mag()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/maga.html').read_text('utf-8')))
    def test_mag4(self, html_mag):
        self.assertEqual(pars_mag()[2][4], '149Р')
    @patch('requests.get', return_value=(Path('data/maga.html').read_text('utf-8')))
    def test_mag5(self, html_mag):
        self.assertEqual(pars_mag()[1][4],'https://shop.mgnl.ru/catalog/pashtet-govyazhiy-100g-zh-b-setra/')

    def test_metro(self):
        a,b,c,d = pars_metro()
        self.assertEqual(len(a),len(b))
    def test_metro2(self):
        a,b,c,d = pars_metro()
        self.assertEqual(len(c),len(d))
    def test_metro3(self):
        a,b,c,d = pars_metro()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/metro.html').read_text('utf-8')))
    def test_metro4(self, html_metro):
        self.assertEqual(pars_metro()[1][6], 'https://msk.metro-cc.ru/virtual/tovary_nedeli/metro-professional-polotenca-2-sloya-slozhenie-vzz-200l-h-5-pachek')
    @patch('requests.get', return_value=(Path('data/metro.html').read_text('utf-8')))
    def test_metro5(self, html_metro):
        self.assertEqual(pars_metro()[3][2], '1099')

    def test_mvideo(self):
        a,b,c,d = pars_mvideo()
        self.assertEqual(len(a),len(b))
    def test_mvideo2(self):
        a,b,c,d = pars_mvideo()
        self.assertEqual(len(c),len(d))
    def test_mvideo3(self):
        a,b,c,d = pars_mvideo()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/mvideo.html').read_text('utf-8')))
    def test_mvideo4(self, html_mvideo):
        self.assertEqual(pars_mvideo()[2][4], '58499.00')
    @patch('requests.get', return_value=(Path('data/mvideo.html').read_text('utf-8')))
    def test_mvideo5(self, html_mvideo):
        self.assertEqual(pars_mvideo()[1][5], 'https://www.mvideo.ru/products/noutbuk-apple-macbook-air-13-m1-8-256-gold-30053779')

    def test_restore(self):
        a,b,c,d = pars_restore()
        self.assertEqual(len(a),len(b))
    def test_restore2(self):
        a,b,c,d = pars_restore()
        self.assertEqual(len(c),len(d))
    def test_restore3(self):
        a,b,c,d = pars_restore()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/restore.html').read_text('utf-8')))
    def test_restore4(self, html_restore):
        self.assertEqual(pars_restore()[3][6],'2 990')
    @patch('requests.get', return_value=(Path('data/restore.html').read_text('utf-8')))
    def test_restore5(self, html_restore):
        self.assertEqual(pars_restore()[0][4], 'Чехол-конверт Apple MagSafe для iPhone 12/12 Pro, кожа, «балтийский синий»')

    def test_eldorado(self):
        a,b,c,d = pars_eladarado()
        self.assertEqual(len(a),len(b))
    def test_eldorado2(self):
        a,b,c,d = pars_eladarado()
        self.assertEqual(len(c),len(d))
    def test_eldorado3(self):
        a,b,c,d = pars_eladarado()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/eldorado.html').read_text('windows-1251')))
    def test_eldorado4(self, html_eldarado):
        self.assertEqual(pars_eladarado()[2][1],'34999')
    @patch('requests.get', return_value=(Path('data/eldorado.html').read_text('windows-1251')))
    def test_eldorado5(self, html_eldarado):
        self.assertEqual(pars_eladarado()[1][0], 'https://www.eldorado.ru/cat/detail/kholodilnik-samsung-rb41r7747dx/')

    def test_nike(self):
        a,b,c,d = pars_nike()
        self.assertEqual(len(a),len(b))
    def test_nike2(self):
        a,b,c,d = pars_nike()
        self.assertEqual(len(c),len(d))
    def test_nike3(self):
        a,b,c,d = pars_nike()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/nike.html').read_text('utf-8')))
    def test_nike4(self, html_nike):
        self.assertEqual(pars_nike()[1][6],'https://www.nike.com/ru/t/мужской-свитшот-с-начесом-и-молнией-на-половину-длины-sportswear-club-87fKqC/DD4732-010')
    @patch('requests.get', return_value=(Path('data/nike.html').read_text('utf-8')))
    def test_nike5(self, html_nike):
        self.assertEqual(pars_nike()[3][2], '4 380 ₽')

    def test_lamoda(self):
        a,b,c,d = pars_lamoda()
        self.assertEqual(len(a),len(b))
    def test_lamoda2(self):
        a,b,c,d = pars_lamoda()
        self.assertEqual(len(d),len(c))
    def test_lamoda3(self):
        a,b,c,d = pars_lamoda()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/lamoda.html').read_text('utf-8')))
    def test_lamoda4(self, html_lamoda):
        self.assertEqual(pars_lamoda()[1][6],'https://www.lamoda.ru/p/mp002xm0s9kl/clothes-oodji-dzhinsy/')
    @patch('requests.get', return_value=(Path('data/lamoda.html').read_text('utf-8')))
    def test_lamoda5(self, html_lamoda):
        self.assertEqual(pars_lamoda()[3][2], '31500 ')

    def test_puma(self):
        a,b,c,d = pars_puma()
        self.assertEqual(len(a),len(b))
    def test_puma2(self):
        a,b,c,d = pars_puma()
        self.assertEqual(len(d),len(c))
    def test_puma3(self):
        a,b,c,d = pars_puma()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/puma.html').read_text('utf-8')))
    def test_puma4(self, html_puma):
        self.assertEqual(pars_puma()[0][5],'Puma Штаны Summer Luxe T7 Pants')
    @patch('requests.get', return_value=(Path('data/puma.html').read_text('utf-8')))
    def test_puma5(self, html_puma):
        self.assertEqual(pars_puma()[3][2], '3990')

    def test_sokolov(self):
        a,b,c,d = pars_sokolov()
        self.assertEqual(len(a),len(b))
    def test_sokolov2(self):
        a,b,c,d = pars_sokolov()
        self.assertEqual(len(d),len(c))
    def test_sokolov3(self):
        a,b,c,d = pars_sokolov()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/sokolov.html').read_text('utf-8')))
    def test_sokolov4(self, html_sokolov):
        self.assertEqual(pars_sokolov()[1][3],'https://sokolov.ru/jewelry-catalog/product/1011545-3/')
    @patch('requests.get', return_value=(Path('data/sokolov.html').read_text('utf-8')))
    def test_sokolov5(self, html_sokolov):
        self.assertEqual(pars_sokolov()[2][3], '59990')

    def test_366(self):
        a,b,c,d = pars_tts()
        self.assertEqual(len(a),len(b))
    def test_3662(self):
        a,b,c,d = pars_tts()
        self.assertEqual(len(d),len(c))
    def test_3663(self):
        a,b,c,d = pars_tts()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/366.html').read_text('utf-8')))
    def test_3664(self, html_tts):
        self.assertEqual(pars_tts()[3][1],'1822₽')
    @patch('requests.get', return_value=(Path('data/366.html').read_text('utf-8')))
    def test_3665(self, html_tts):
        self.assertEqual(pars_tts()[0][2], 'Дона таблетки 750 мг 180 шт')

    def test_goz(self):
        a,b,c,d = pars_gor()
        self.assertEqual(len(a),len(b))
    def test_goz2(self):
        a,b,c,d = pars_gor()
        self.assertEqual(len(d),len(c))
    def test_goz3(self):
        a,b,c,d = pars_gor()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/goz.html').read_text('utf-8')))
    def test_goz4(self, html_goz):
        self.assertEqual(pars_gor()[3][2],'579,70 ₽')
    @patch('requests.get', return_value=(Path('data/goz.html').read_text('utf-8')))
    def test_goz5(self, html_goz):
        self.assertEqual(pars_gor()[2][3], '678 ₽')

    def test_asna(self):
        a,b,c,d = pars_asna()
        self.assertEqual(len(a),len(b))
    def test_asna2(self):
        a,b,c,d = pars_asna()
        self.assertEqual(len(d),len(c))
    def test_asna3(self):
        a,b,c,d = pars_asna()
        self.assertEqual(len(b),len(c))
    @patch('requests.get', return_value=(Path('data/asna.html').read_text('utf-8')))
    def test_asna4(self, html_asna):
        self.assertEqual(pars_asna()[1][6],'https://ishimbaj.asna.ru/cards/teraflyu_limon_n10_poroshok_famar.html')
    @patch('requests.get', return_value=(Path('data/asna.html').read_text('utf-8')))
    def test_asna5(self, html_asna):
        self.assertEqual(pars_asna()[3][5], '1.5% баллами «Огонь»')

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