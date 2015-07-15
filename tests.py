import os
import sys
import json
from django.test.utils import setup_test_environment
from django.core.urlresolvers import reverse
from django.core.management import call_command

from urllib.request import urlopen
import urllib
import re
import requests

#New Imports
from django.utils import unittest
from django.test import TestCase
from django.http import HttpResponse
from unittest import main, TestCase

from json import dumps, loads

from django.test import TestCase
from app.models import *


try:
    from urllib.request import urlopen, Request
except:
    from urllib2 import *

#from tastypie.test import ResourceTestCase

import json
#import watson
#end New Imports

    # -----------
    # TestModels
    # -----------

class ModelTestCase(TestCase):
    def test_champion_model1(self):
        champtest = {"Nidalee": {"role": "Assassin", "name": "Nidalee"}}
        self.assertEqual(champtest['Nidalee']['name'], "Nidalee")
        self.assertEqual(champtest['Nidalee']['role'], "Assassin")

    """def test_champion_model2(self):
        cs = open("app/database/champions")
        champion_test_dict = json.load(cs)
        cs.close()
        champtest1 = champion_test_dict
        self.assertEqual(champtest1['Nidalee']['name'], "Nidalee")
        self.assertEqual(champtest1['Nidalee']['role'], "Assassin")"""

    def test_champion_model3(self):
        champurl = 'http://leagueofdowning.link/api/champions/76'
        champinfo = urlopen(champurl).info()
        raw_champ = urlopen(champurl).read().decode(champinfo.get_content_charset('utf8'))
        champ = json.loads(raw_champ) 
        self.assertEqual(champ['name'], "Nidalee")
        self.assertEqual(champ['role'], "Assassin")

    def test_player_model1(self):
        playertest = {"4347": {"role": "Support", "ign": "viviD"}}
        self.assertEqual(playertest['4347']['ign'], "viviD")
        self.assertEqual(playertest['4347']['role'], "Support")

    """def test_player_model2(self):
        ps = open("app/database/players")
        player_test_dict = json.load(ps)
        ps.close()
        playertest1 = player_test_dict
        self.assertEqual(playertest1['4347']['ign'], "viviD")
        self.assertEqual(playertest1['4347']['role'], "Support")"""

    def test_player_model3(self):
        playerurl = 'http://leagueofdowning.link/api/players/4347'
        playerinfo = urlopen(playerurl).info()
        raw_player = urlopen(playerurl).read().decode(playerinfo.get_content_charset('utf8'))
        player1 = json.loads(raw_player) 
        self.assertEqual(player1['ign'], "viviD")
        self.assertEqual(player1['role'], "Support")

    def test_item_model1(self):
        itemtest = {"3266": {"image": "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/3266.png", "name": "Enchantment: Captain"}}
        self.assertEqual(itemtest['3266']['name'], "Enchantment: Captain")
        self.assertEqual(itemtest['3266']['image'], "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/3266.png")

   """ def test_item_model2(self):
        ts = open("app/database/items")
        item_test_dict = json.load(ts)
        ts.close()
        itemtest = item_test_dict
        self.assertEqual(itemtest['3266']['name'], "Enchantment: Captain")
        self.assertEqual(itemtest['3266']['image'], "http://ddragon.leagueoflegends.com/cdn/5..1/img/item/3266.png")"""

    def test_item_model3(self):
        itemurl = 'http://leagueofdowning.link/api/items/3266'
        iteminfo = urlopen(itemurl).info()
        raw_item = urlopen(itemurl).read().decode(iteminfo.get_content_charset('utf8'))
        item1 = json.loads(raw_item) 
        self.assertEqual(item1['name'], "Enchantment: Captain")
        self.assertEqual(item1['image'], "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/3266.png")

# ----
# main
# ----

if __name__ == "__main__":
    main()

