import os
import sys
import json
from django.test.utils import setup_test_environment
from django.core.urlresolvers import reverse
from django.core.management import call_command

#New Imports
from django.utils import unittest
from django.test import TestCase
from django.http import HttpResponse

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
    # -------------
    # Champion_model
    # -------------

    def test_champion_model1(self):
        #Dictionary Key: Champion Name
        #Dictionary Value: [picture, champion_role, champion_lane, champion_counters, champion_items]
        champion_test_dict1 = {"dr_mundo": ["http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/DrMundo.png", "fighter", "top", ["olaf", "kog_maw", "trundle"], ["sunfire_cape", "spirit_visage", "randuins_omen"]]}

        Champion.objects.create(champions_name="dr_mundo", picture = "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/DrMundo.png", champion_role = "fighter", champion_lane = "top", champion_counters = ["olaf", "kog_maw", "trundle"], champion_items = ["sunfire_cape", "spirit_visage", "randuins_omen"])
 
        Champion_Mundo = Champion.objects.get(champion_name="dr_mundo")
        self.assertEqual(Champion_Mundo.champion_name, "dr_mundo")
        self.assertEqual(Champion_Mundo.picture, "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/DrMundo.png")
        self.assertEqual(Champion_Mundo.champion_role, "fighter")
        self.assertEqual(Champion_Mundo.champion_lane, "top")
        self.assertEqual(Champion_Mundo.champion_counters, ["olaf", "kog_maw", "trundle"])
        self.assertEqual(Champion_Mundo.champion_items, ["sunfire_cape", "spirit_visage", "randuins_omen"])

    def test_champion_model2(self):
        #Dictionary Key: Champion Name
        #Dictionary Value: [picture, champion_role, champion_lane, champion_counters, champion_items]

        champion_test_dict2 = {"dr_mundo": ["http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/DrMundo.png", "fighter", "top", ["olaf", "kog_maw", "trundle"], ["sunfire_cape", "spirit_visage", "randuins_omen"]], "azir": ["http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Azir.png", "mage", "mid", ["ziggs", "talon", "xerath"], ["sorcerer's shoes", "athenes", "rabadons"]]}


        Champion.objects.create(champion_name="dr_mundo", picture=champion_test_dict2["dr_mundo"][0], champion_role=champion_test_dict2["dr_mundo"][1], champion_lane=champion_test_dict2["dr_mundo"][2], champion_counters=champion_test_dict2["dr_mundo"][3], champion_items=champion_test_dict2["dr_mundo"][4])
        Champion.objects.create(champion_name="azir", picture=champion_test_dict2["azir"][0], champion_role=champion_test_dict2["azir"][1], champion_lane=champion_test_dict2["azir"][2], champion_counters=champion_test_dict2["azir"][3], champion_items=champion_test_dict2["azir"][4])

        Champion_Mundo = Champion.objects.get(champion_name="dr_mundo")
        self.assertEqual(Champion_Mundo.champion_name, "dr_mundo")
        self.assertEqual(Champion_Mundo.picture, "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/DrMundo.png")
        self.assertEqual(Champion_Mundo.champion_role, "fighter")
        self.assertEqual(Champion_Mundo.champion_lane, "top")
        self.assertEqual(Champion_Mundo.champion_counters, ["olaf", "kog_maw", "trundle"])
        self.assertEqual(Champion_Mundo.champion_items, ["sunfire_cape", "spirit_visage"])

        Champion_Azir = Champion.objects.get(champion_name="azir")
        self.assertEqual(Champion_Azir.champion_name, "azir")
        self.assertEqual(Champion_Azir.picture, "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Azir.png")
        self.assertEqual(Champion_Azir.champion_role, "mage")
        self.assertEqual(Champion_Azir.champion_lane, "mid")
        self.assertEqual(Champion_Azir.champion_counters, ["ziggs", "talon", "xerath"])
        self.assertEqual(Champion_Azir.champion_items, ["sorcerer's shoes", "athenes", "rabadons"])

    


    def test_champion_model3(self):
    #Dictionary Key: Champion Name
        #Dictionary Value: [picture, champion_role, champion_lane, champion_counters, champion_items]

        champion_test_dict3 = {"dr_mundo": ["http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/DrMundo.png", "fighter", "top", ["olaf", "kog_maw", "trundle"], ["sunfire_cape", "spirit_visage", "randuins_omen"]], "azir": ["http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Azir.png", "mage", "mid", ["ziggs", "talon", "xerath"], ["sorcerer's shoes", "athenes", "rabadons"]], "ezreal" : ["http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Ezreal.png", "adc", "bot", ["draven", "graves", "missfortune"], ["berserkers", "trinity", "bloodthirster"]]}

        Champion.objects.create(champion_name="ezreal", picture=champion_test_dict3["ezreal"][0], champion_role=champion_test_dict3["ezreal"][1], champion_lane=champion_test_dict3["ezreal"][2], champion_counters=champion_test_dict3["ezreal"][3], champion_items=champion_test_dict3["ezreal"][4])

        Champion_Mundo = Champion.objects.get(champion_name="dr_mundo")
        self.assertEqual(Champion_Mundo.champion_name, "dr_mundo")
        self.assertEqual(Champion_Mundo.picture, "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/DrMundo.png")
        self.assertEqual(Champion_Mundo.champion_role, "fighter")
        self.assertEqual(Champion_Mundo.champion_lane, "top")
        self.assertEqual(Champion_Mundo.champion_counters, ["olaf", "kog_maw", "trundle"])
        self.assertEqual(Champion_Mundo.champion_items, ["sunfire_cape", "spirit_visage"])

        Champion_Azir = Champion.objects.get(champion_name="azir")
        self.assertEqual(Champion_Azir.champion_name, "azir")
        self.assertEqual(Champion_Azir.picture, "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Azir.png")
        self.assertEqual(Champion_Azir.champion_role, "mage")
        self.assertEqual(Champion_Azir.champion_lane, "mid")
        self.assertEqual(Champion_Azir.champion_counters, ["ziggs", "talon", "xerath"])
        self.assertEqual(Champion_Azir.champion_items, ["sorcerer's shoes", "athenes", "rabadons"])

        Champion_Ezreal = Champion.objects.get(champion_name="ezreal")
        self.assertEqual(Champion_Ezreal.champion_name, "ezreal")
        self.assertEqual(Champion_Ezreal.picture, "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Ezreal.png")
        self.assertEqual(Champion_Ezreal.champion_role, "adc")
        self.assertEqual(Champion_Ezreal.champion_lane, "bot")
        self.assertEqual(Champion_Ezreal.champion_counters, ["draven", "graves", "missfortune"])
        self.assertEqual(Champion_Ezreal.champion_items, ["berserkers", "trinity", "bloodthirster"])
            
            

    # -------------
    # Player_model
    # -------------

    def test_player_model1(self):
        #Dictionary Key: Player name
        #Dictionary Value: [age, position, total wins, season wins, season losses, team]

        Player.objects.create(player_name = "balls", player_age = "21", position = "top", total_wins = "3", season_wins = "3" , season_losses = "9", team = "c9")

        Player_Balls = Player.objects.get(player_name="balls")
        self.assertEqual(Player_Balls.player_name, "balls")
        self.assertEqual(Player_Balls.player_age, "21")
        self.assertEqual(Player_Balls.position, "top")
        self.assertEqual(Player_Balls.total_wins, "3")
        self.assertEqual(Player_Balls.season_wins, "3")
        self.assertEqual(Player_Balls.season_losses, "9")
        self.assertEqual(Player_Balls.team, "c9")

    def test_player_model2(self):
        #Dictionary Key: Player name
        #Dictionary Value: [age, position, total wins, season wins, season losses, team]

        player_test_dict2 = {"balls": ["21", "top", "3", "3", "9", "c9"]}

        Player.objects.create(player_name = "balls", player_age=player_test_dict2["balls"][0], position = player_test_dict2["balls"][1], total_wins = player_test_dict2["balls"][2], season_wins = player_test_dict2["balls"][3], season_losses = player_test_dict2["balls"][4], team = player_test_dict2["balls"][5])

        Player_Balls = Player.objects.get(player_name="balls")
        self.assertEqual(Player_Balls.player_name, "balls")
        self.assertEqual(Player_Balls.player_age, "21")
        self.assertEqual(Player_Balls.position, "top")
        self.assertEqual(Player_Balls.total_wins, "3")
        self.assertEqual(Player_Balls.season_wins, "3")
        self.assertEqual(Player_Balls.season_losses, "9")
        self.assertEqual(Player_Balls.team, "c9")

    def test_player_model3(self):
        #Dictionary Key: Player name
        #Dictionary Value: [age, position, total wins, season wins, season losses, team]

        player_test_dict3 = {"balls": ["21", "top", "3", "3", "9", "c9"], "doublelift": ["21", "adc", "7", "7", "5", "clg"]}

        Player.objects.create(player_name = "balls", player_age=player_test_dict3["balls"][0], position = player_test_dict3["balls"][1], total_wins = player_test_dict3["balls"][2], season_wins = player_test_dict3["balls"][3], season_losses = player_test_dict3["balls"][4], team = player_test_dict3["balls"][5])

        Player.objects.create(player_name = "doublelift", player_age=player_test_dict3["doublelift"][0], position = player_test_dict3["doublelift"][1], total_wins = player_test_dict3["doublelift"][2], season_wins = player_test_dict3["doublelift"][3], season_losses = player_test_dict3["doublelift"][4], team = player_test_dict3["doublelift"][5])

        Player_Balls = Player.objects.get(player_name="balls")
        self.assertEqual(Player_Balls.player_name, "balls")
        self.assertEqual(Player_Balls.player_age, "21")
        self.assertEqual(Player_Balls.position, "top")
        self.assertEqual(Player_Balls.total_wins, "3")
        self.assertEqual(Player_Balls.season_wins, "3")
        self.assertEqual(Player_Balls.season_losses, "9")
        self.assertEqual(Player_Balls.team, "c9")

        Player_Doublelift = Player.objects.get(player_name="doublelift")
        self.assertEqual(Player_Doublelift.player_name, "doublelift")
        self.assertEqual(Player_Doublelift.player_age, "21")
        self.assertEqual(Player_Doublelift.position, "adc")
        self.assertEqual(Player_Doublelift.total_wins, "7")
        self.assertEqual(Player_Doublelift.season_wins, "7")
        self.assertEqual(Player_Doublelift.season_losses, "5")
        self.assertEqual(Player_Doublelift.team, "clg")

    # -------------
    # Item_model
    # -------------

    def test_item_model1(self):
        #Dictionary Key: Item name
        #Dictionary Value: [stats, recfor, cost, recipe]

        item_test_dict1 = { "athenes" : [ ["ap", "mr", "cdr", "bmr"], "mage", "2700", ["codex", "chalice"]]}

        Item.objects.create(item_name = "athenes", stats = ["ap", "mr", "cdr", "bmr"], recfor = "mage", cost = "2700", recipe = ["codex", "chalice"])
        Item_Athenes = Items.objects.get(item_name = "athenes")
        self.assertEqual(Item_Athenes.stats, ["ap", "mr", "cdr", "bmr"])
        self.assertEqual(Item_Athenes.recfor, "mage")
        self.assertEqual(Item_Athenes.cost, "2700")
        self.assertEqual(Item_Athenes.recipe, ["codex", "chalice"])

    def test_item_model2(self):
        #Dictionary Key: Item name
        #Dictionary Value: [stats, recfor, cost, recipe]

        item_test_dict2 = { "athenes" : [ ["ap", "mr", "cdr", "bmr"], "mage", "2700", ["codex", "chalice"]]}

        Item.objects.create(item_name = "athenes", stats = item_test_dict2["athenes"][0], recfor = item_test_dict2["athenes"][1], cost = item_test_dict2["athenes"][2], recipe = item_test_dict2["athenes"][3])
        Item_Athenes = Items.objects.get(item_name = "athenes")
        self.assertEqual(Item_Athenes.stats, ["ap", "mr", "cdr", "bmr"])
        self.assertEqual(Item_Athenes.recfor, "mage")
        self.assertEqual(Item_Athenes.cost, "2700")
        self.assertEqual(Item_Athenes.recipe, ["codex", "chalice"])

    def test_item_model3(self):
        #Dictionary Key: Item name
        #Dictionary Value: [stats, recfor, cost, recipe]

        item_test_dict3 = { "athenes" : [ ["ap", "mr", "cdr", "bmr"], "mage", "2700", ["codex", "chalice"]], "rabadons": [["ap"], "mage", "3300", ["blasting_wand", "needlessly_large_rod"]]}

        Item.objects.create(item_name = "athenes", stats = item_test_dict3["athenes"][0], recfor = item_test_dict3["athenes"][1], cost = item_test_dict3["athenes"][2], recipe = item_test_dict3["athenes"][3])
        Item_Athenes = Items.objects.get(item_name = "athenes")
        self.assertEqual(Item_Athenes.stats, ["ap", "mr", "cdr", "bmr"])
        self.assertEqual(Item_Athenes.recfor, "mage")
        self.assertEqual(Item_Athenes.cost, "2700")
        self.assertEqual(Item_Athenes.recipe, ["codex", "chalice"])

        Item_Rabadons = Items.objects.get(item_name = "rabadons")
        self.assertEqual(Item_Rabadons.stats, ["ap"])
        self.assertEqual(Item_Rabadons.recfor, "mage")
        self.assertEqual(Item_Rabadons.cost, "3300")
        self.assertEqual(Item_Rabadons.recipe, ["blasting_wand", "needlessly_large_rod"])
# ----
# main
# ----

if __name__ == "__main__":
    main()

