from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest
import unittest
import time

from main_pars import pars_vv,pars_gor,pars_tts,pars_asna,pars_mag,pars_puma,pars_metro,pars_perek,pars_mvideo,pars_nike,pars_lamoda,pars_sokolov,pars_eladarado,pars_restore
# Введите ваши API ID, hash and session name
api_id = int('')
api_hash = ""
client = TelegramClient('Свое имя', api_id, api_hash)


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

    def test_per(self):
        a,b,c,d = pars_perek()
        self.assertEqual(len(a),len(b))
    def test_per2(self):
        a,b,c,d = pars_perek()
        self.assertEqual(len(c),len(d))
    def test_per3(self):
        a,b,c,d = pars_perek()
        self.assertEqual(len(b),len(c))

    def test_mag(self):
        a,b,c,d = pars_mag()
        self.assertEqual(len(a),len(b))
    def test_mag2(self):
        a,b,c,d = pars_mag()
        self.assertEqual(len(c),len(d))
    def test_mag3(self):
        a,b,c,d = pars_mag()
        self.assertEqual(len(b),len(c))

    def test_metro(self):
        a,b,c,d = pars_metro()
        self.assertEqual(len(a),len(b))
    def test_metro2(self):
        a,b,c,d = pars_metro()
        self.assertEqual(len(c),len(d))
    def test_metro3(self):
        a,b,c,d = pars_metro()
        self.assertEqual(len(b),len(c))

    def test_mvideo(self):
        a,b,c,d = pars_mvideo()
        self.assertEqual(len(a),len(b))
    def test_mvideo2(self):
        a,b,c,d = pars_mvideo()
        self.assertEqual(len(c),len(d))
    def test_mvideo3(self):
        a,b,c,d = pars_mvideo()
        self.assertEqual(len(b),len(c))

    def test_restore(self):
        a,b,c,d = pars_restore()
        self.assertEqual(len(a),len(b))
    def test_restore2(self):
        a,b,c,d = pars_restore()
        self.assertEqual(len(c),len(d))
    def test_restore3(self):
        a,b,c,d = pars_restore()
        self.assertEqual(len(b),len(c))

    def test_eldorado(self):
        a,b,c,d = pars_eladarado()
        self.assertEqual(len(a),len(b))
    def test_eldorado2(self):
        a,b,c,d = pars_eladarado()
        self.assertEqual(len(c),len(d))
    def test_eldorado3(self):
        a,b,c,d = pars_eladarado()
        self.assertEqual(len(b),len(c))

    def test_nike(self):
        a,b,c,d = pars_nike()
        self.assertEqual(len(a),len(b))
    def test_nike2(self):
        a,b,c,d = pars_nike()
        self.assertEqual(len(c),len(d))
    def test_nike3(self):
        a,b,c,d = pars_nike()
        self.assertEqual(len(b),len(c))

    def test_lamoda(self):
        a,b,c,d = pars_lamoda()
        self.assertEqual(len(a),len(b))
    def test_lamoda2(self):
        a,b,c,d = pars_lamoda()
        self.assertEqual(len(d),len(c))
    def test_lamoda3(self):
        a,b,c,d = pars_lamoda()
        self.assertEqual(len(b),len(c))

    def test_puma(self):
        a,b,c,d = pars_puma()
        self.assertEqual(len(a),len(b))
    def test_puma2(self):
        a,b,c,d = pars_puma()
        self.assertEqual(len(d),len(c))
    def test_puma3(self):
        a,b,c,d = pars_puma()
        self.assertEqual(len(b),len(c))

    def test_sokolov(self):
        a,b,c,d = pars_sokolov()
        self.assertEqual(len(a),len(b))
    def test_sokolov2(self):
        a,b,c,d = pars_sokolov()
        self.assertEqual(len(d),len(c))
    def test_sokolov3(self):
        a,b,c,d = pars_sokolov()
        self.assertEqual(len(b),len(c))

    def test_366(self):
        a,b,c,d = pars_tts()
        self.assertEqual(len(a),len(b))
    def test_3662(self):
        a,b,c,d = pars_tts()
        self.assertEqual(len(d),len(c))
    def test_3663(self):
        a,b,c,d = pars_tts()
        self.assertEqual(len(b),len(c))

    def test_goz(self):
        a,b,c,d = pars_gor()
        self.assertEqual(len(a),len(b))
    def test_goz2(self):
        a,b,c,d = pars_gor()
        self.assertEqual(len(d),len(c))
    def test_goz3(self):
        a,b,c,d = pars_gor()
        self.assertEqual(len(b),len(c))

    def test_asna(self):
        a,b,c,d = pars_asna()
        self.assertEqual(len(a),len(b))
    def test_asna2(self):
        a,b,c,d = pars_asna()
        self.assertEqual(len(d),len(c))
    def test_asna3(self):
        a,b,c,d = pars_asna()
        self.assertEqual(len(b),len(c))
    def testStart(self):
        try:
            client.send_message('@post_project_bot', '/start')
            time.sleep(2)
            messages = client.get_messages('@post_project_bot')
            for message in client.get_messages('@post_project_bot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Добро пожаловать,(Свое Имя)\nЗдесь вы можете узнать, наиболее продоваемые товары, товары со скидками'
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

