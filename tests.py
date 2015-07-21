import os
import sys
import json
from io import StringIO
#from django.test.utils import setup_test_environment
#from django.core.urlresolvers import reverse
#from django.core.management import call_command

from urllib.request import urlopen
import urllib
import re
import requests


#New Imports
#from django.utils import unittest
#from django.test import TestCase
#from django.http import HttpResponse
from unittest import main, TestCase, TestLoader, TextTestRunner

from json import dumps, loads

#from django.test import TestCase
#from app.models import *


try:
    from urllib.request import urlopen, Request
except:
    from urllib2 import *

#from tastypie.test import ResourceTestCase

import json
#import watson
#end New Imports

def unittests():
    suite = TestLoader().loadTestsFromTestCase(ModelTestCase)
    stream = StringIO()
    status = TextTestRunner(stream = stream, verbosity = 1).run(suite)
    result = stream.getvalue()
    return result

# -----------
# TestModels
# -----------

class ModelTestCase (TestCase):

# ---------
# Champion
# ---------

    def test_champion_model1(self):
        champtest = {"Nidalee": {"role": "Assassin", "name": "Nidalee"}}
        self.assertEqual(champtest['Nidalee']['name'], "Nidalee")
        self.assertEqual(champtest['Nidalee']['role'], "Assassin")

    def test_champion_model2(self):
        cs = open("app/database/champions")
        champion_test_dict = json.load(cs)
        cs.close()
        champtest1 = champion_test_dict
        self.assertEqual(champtest1['Nidalee']['name'], "Nidalee")
        self.assertEqual(champtest1['Nidalee']['role'], "Assassin")

    def test_champion_model3(self):
        champurl = 'http://leagueofdowning.link/api/champions/76'
        champinfo = urlopen(champurl).info()
        raw_champ = urlopen(champurl).read().decode(champinfo.get_content_charset('utf8'))
        champ = json.loads(raw_champ) 
        self.assertEqual(champ['name'], "Nidalee")
        self.assertEqual(champ['role'], "Assassin")

    def test_champion_model4(self):
        champtest = {"Rammus": {"r_name": "Tremors", "title": "the Armordillo"}}
        self.assertEqual(champtest['Rammus']['r_name'], "Tremors")
        self.assertEqual(champtest['Rammus']['title'], "the Armordillo")

    def test_champion_model5(self):
        cs1 = open("app/database/champions")
        champion_test_dict1 = json.load(cs1)
        cs1.close()
        champtest2 = champion_test_dict1
        self.assertEqual(champtest2['Rammus']['r_name'], "Tremors")
        self.assertEqual(champtest2['Rammus']['title'], "the Armordillo")

    def test_champion_model6(self):
        champurl = 'http://leagueofdowning.link/api/champions/33'
        champinfo = urlopen(champurl).info()
        raw_champ = urlopen(champurl).read().decode(champinfo.get_content_charset('utf8'))
        champ = json.loads(raw_champ) 
        self.assertEqual(champ['r_name'], "Tremors")
        self.assertEqual(champ['title'], "the Armordillo")

# -------
# Player
# -------

    def test_player_model1(self):
        playertest = {"4347": {"role": "Support", "name": "viviD"}}
        self.assertEqual(playertest['4347']['name'], "viviD")
        self.assertEqual(playertest['4347']['role'], "Support")

    def test_player_model2(self):
        ps = open("app/database/players")
        player_test_dict = json.load(ps)
        ps.close()
        playertest1 = player_test_dict
        self.assertEqual(playertest1['4347']['name'], "viviD")
        self.assertEqual(playertest1['4347']['role'], "Support")

    def test_player_model3(self):
        playerurl = 'http://leagueofdowning.link/api/players/4347'
        playerinfo = urlopen(playerurl).info()
        raw_player = urlopen(playerurl).read().decode(playerinfo.get_content_charset('utf8'))
        player1 = json.loads(raw_player) 
        self.assertEqual(player1['ign'], "viviD")
        self.assertEqual(player1['role'], "Support")

    def test_player_model4(self):
        playertest = {"2125": {"id": 2125, "teamName": "Longzhu Incredible Miracle"}}
        self.assertEqual(playertest['2125']['id'], 2125)
        self.assertEqual(playertest['2125']['teamName'], "Longzhu Incredible Miracle")

    def test_player_model5(self):
        ps = open("app/database/players")
        player_test_dict = json.load(ps)
        ps.close()
        playertest1 = player_test_dict
        self.assertEqual(playertest1['2125']['id'], '2125')
        self.assertEqual(playertest1['2125']['teamName'], "Longzhu Incredible Miracle")

    def test_player_model6(self):
        playerurl = 'http://leagueofdowning.link/api/players/2125'
        playerinfo = urlopen(playerurl).info()
        raw_player = urlopen(playerurl).read().decode(playerinfo.get_content_charset('utf8'))
        player1 = json.loads(raw_player) 
        self.assertEqual(player1['player_id'], 2125)
        self.assertEqual(player1['team_name'], "Longzhu Incredible Miracle")

# -----
# Item
# -----

    def test_item_model1(self):
        itemtest = {"3266": {"image": "http://ddragon.leagueoflegends.com/cdn/5.13.1/img/item/3266.png", "name": "Enchantment: Captain"}}
        self.assertEqual(itemtest['3266']['name'], "Enchantment: Captain")
        self.assertEqual(itemtest['3266']['image'], "http://ddragon.leagueoflegends.com/cdn/5.13.1/img/item/3266.png")

    def test_item_model2(self):
        ts = open("app/database/items")
        item_test_dict = json.load(ts)
        ts.close()
        itemtest = item_test_dict
        self.assertEqual(itemtest['3266']['name'], "Enchantment: Captain")
        self.assertEqual(itemtest['3266']['image'], "http://ddragon.leagueoflegends.com/cdn/5.13.1/img/item/3266.png")


    def test_item_model3(self):
        itemurl = 'http://leagueofdowning.link/api/items/3266'
        iteminfo = urlopen(itemurl).info()
        raw_item = urlopen(itemurl).read().decode(iteminfo.get_content_charset('utf8'))
        item1 = json.loads(raw_item) 
        self.assertEqual(item1['name'], "Enchantment: Captain")
        self.assertEqual(item1['image'], "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/3266.png")

    def test_item_model4(self):
        itemtest = {"3135": {"base": 1000, "total_gold": 2295}}
        self.assertEqual(itemtest['3135']['base'], 1000)
        self.assertEqual(itemtest['3135']['total_gold'], 2295)

    def test_item_model5(self):
        ts = open("app/database/items")
        item_test_dict = json.load(ts)
        ts.close()
        itemtest = item_test_dict
        self.assertEqual(itemtest['3135']['gold']['base'], 1000)
        self.assertEqual(itemtest['3135']['gold']['total'], 2295)


    def test_item_model6(self):
        itemurl = 'http://leagueofdowning.link/api/items/3135'
        iteminfo = urlopen(itemurl).info()
        raw_item = urlopen(itemurl).read().decode(iteminfo.get_content_charset('utf8'))
        item1 = json.loads(raw_item) 
        self.assertEqual(item1['base_gold'], 1000)
        self.assertEqual(item1['total_gold'], 2295)

# ----
# API
# ----

    url = "http://leagueofdowning.link/"

# ---------
# Champion
# ---------

    def test_get_all_champions(self) :
        request = Request(self.url+"api/champions/")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        #response_objects = response_data["objects"]
        expected_response = {
  "1": {
    "lore": "In the time shortly before the League, there were those within the sinister city-state of Noxus who did not agree with the evils perpetrated by the Noxian High Command. The High Command had just put down a coup attempt from the self-proclaimed Crown Prince Raschallion, and a crack down on any form of dissent against the new government was underway. These political and social outcasts, known as the Gray Order, sought to leave their neighbors in peace as they pursued dark arcane knowledge. The leaders of this outcast society were a married couple: Gregori Hastur, the Gray Warlock, and his wife Amoline, the Shadow Witch. Together they led an exodus of magicians and other intelligentsia from Noxus, resettling their followers beyond the Great Barrier to the northern reaches of the unforgiving Voodoo Lands. Though survival was a challenge at times, the Gray Order's colony managed to thrive in a land where so many others would have failed.\n\nYears after the exodus, Gregori and Amoline had a child: Annie. Early on, Annie's parents knew there was something special about their daughter. At the age of two, Annie miraculously ensorcelled a shadow bear - a ferocious denizen of the petrified forests outside the colony - turning it into her pet. To this day she keeps her bear ''Tibbers'' by her side, often keeping him spellbound as a stuffed doll to be carried like a child's toy. The combination of Annie's lineage and the dark magic of her birthplace have given this little girl tremendous arcane power. It is this same girl who now finds herself as one of the most sought-after champions within the League of Legends - even by the city-state that would have exiled her parents had they not fled beforehand.\n\n''Annie may be one of the most powerful champions ever to have fought in a Field of Justice. I shudder to think of her capabilities when she becomes an adult.''\n-- High Councilor Kiersta Mandrake",
    "champion_id": 1,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MoltenShield.png",
    "q_name": "Disintegrate",
    "passive_name": "Pyromania",
    "e_description": "Increases Annie's Armor and Magic Resist and damages enemies who hit Annie with basic attacks.",
    "recommended_items": [
      1001,
      1056,
      3151,
      1028,
      3010
    ],
    "r_name": "Summon: Tibbers",
    "r_description": "Annie wills her bear Tibbers to life, dealing damage to units in the area. Tibbers can attack and also burns enemies that stand near him.",
    "name": "Annie",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Disintegrate.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Incinerate.png",
    "q_description": "Annie hurls a Mana infused fireball, dealing damage and refunding the Mana cost if it destroys the target.",
    "title": "the Dark Child",
    "e_name": "Molten Shield",
    "w_description": "Annie casts a blazing cone of fire, dealing damage to all enemies in the area.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Annie.png",
    "recommended_item_names": [
      "Boots of Speed",
      "Doran's Ring",
      "Liandry's Torment",
      "Ruby Crystal",
      "Catalyst the Protector"
    ],
    "w_name": "Incinerate",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/InfernalGuardian.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Annie_Passive.png",
    "passive_description": "After casting 4 spells, Annie's next offensive spell will stun the target for a short duration."
  },
  "2": {
    "lore": "Most men would say that death is a thing to be feared; none of those men would be Olaf. The Berserker lives only for the roar of a battle cry and the clash of steel. Spurred on by his hunger for glory and the looming curse of a forgettable death, Olaf throws himself into every fight with reckless abandon. Surrendering to the bloodlust deep within his being, Olaf is only truly alive when grappling with the jaws of death.\n\nThe coastal peninsula of Lokfar is among the most brutal places in the Freljord. There, rage is the only fire to warm frozen bones, blood is the only liquid that flows freely, and there is no worse fate than to grow old, frail, and forgotten. Olaf was a warrior of Lokfar with no shortage of glories and no hesitation to share them. While boasting one evening with his clansmen over the burning embers of a razed village, one of the elder warriors grew tired of Olaf's bluster. The old fighter goaded Olaf to read the omens and see if Olaf's fortunes matched his gloating. Emboldened by the challenge, Olaf mocked the aged raider's envy and tossed the knuckle bones of a long-dead beast to predict the heights of glory he'd achieve in death. All mirth left the gathering as the clansmen read the portents: the bones spoke of a long life and a quiet passing.\n\nInfuriated, Olaf stormed into the night determined to prove the prediction false by finding and slaughtering Lokfar's feared frost serpent. The monster had consumed thousands, man and ship alike, in its long lifetime and to die in battle with it would be a fitting end for any warrior. As Olaf hurled himself into the blackness of its maw, he fell deeper into the blackness of his mind. When the shock of freezing water roused him from the dark, there was only the butchered carcass of the beast afloat beside him. Thwarted but not defeated, Olaf set out to hunt down every legendary creature with claws and fangs, hoping that the next battle would be his last. Each time he charged headlong toward his coveted death, only to be spared by the frenzy that washed over him while on its brink.\n\nOlaf concluded that no mere beast could grant him a warrior's death. His solution was to take on the most fearsome tribe in the Freljord: the Winter's Claw. Sejuani appeared amused by Olaf's challenge to her warband, but his audacity would earn him no mercy. She ordered the charge and sent scores of her warriors to overwhelm Olaf. One by one, they fell until he lost himself in the bloodlust once again, effortlessly cutting a path to the leader of the Winter's Claw. The clash between Olaf and Sejuani rocked the glaciers with its force, and though he seemed unstoppable, Sejuani battled the berserker to a standstill. As they stood deadlocked, Sejuani's glare penetrated Olaf's berserker haze in a way no weapon ever could. His frenzy abated long enough for her to make him an offer: Sejuani swore that she would find Olaf his glorious death if he would lend his axe to her campaign of conquest. In that moment, Olaf vowed he would carve his legacy into the Freljord itself.\n\n''When you meet your ancestors, tell them Olaf sent you.'' \n-- Olaf",
    "champion_id": 2,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/OlafRecklessStrike.png",
    "q_name": "Undertow",
    "passive_name": "Berserker Rage",
    "e_description": "Olaf attacks with such force that it deals true damage to his target and himself, refunding the Health cost if he destroys the target.",
    "recommended_items": [
      3047,
      2003,
      1039,
      3156,
      1054,
      3153
    ],
    "r_name": "Ragnarok",
    "r_description": "Olaf temporarily becomes immune to disables.",
    "name": "Olaf",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/OlafAxeThrowCast.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/OlafFrenziedStrikes.png",
    "q_description": "Olaf throws an axe into the ground at a target location, dealing damage to units it passes through and slowing their Movement Speed. If Olaf picks up the axe, the ability's cooldown is reduced by 4.5 seconds.",
    "title": "the Berserker",
    "e_name": "Reckless Swing",
    "w_description": "Olaf's Attack Speed is increased, he gains Life Steal and has increased healing from all sources based on how much Health he is missing.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Olaf.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Maw of Malmortius",
      "Doran's Shield",
      "Blade of the Ruined King"
    ],
    "w_name": "Vicious Strikes",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/OlafRagnarok.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Olaf_Passive.png",
    "passive_description": "For each 1% of Health missing, Olaf's Attack Speed is increased by 1%."
  },
  "3": {
    "lore": "Long before the League's regulation of such magic, mages experimented with the creation of artificial life. Now forbidden, instilling golems with reason was once not so uncommon a practice amongst the more expert of craftsmen. One such visionary was the Demacian artificer, Durand. Peerless at crafting sentient beings, Durand's constructs served as tireless guardians for the border towns of his beloved city-state, affording them protection from their Noxian neighbors. For his own defense, however, Durand kept his magnum opus: Galio. This mighty construct - forged in the image of a gargoyle - kept him safe on his journeys, allowing him to perform his important work without fear of reprisal from those hostile to his homeland. That is, until dealing with his taxing sentinels finally roused the ire of the Noxian High Command.\n\nAs Durand crossed the Howling Marsh with his masterwork in tow, he was set upon by Noxian assassins in force. Outnumbered and overwhelmed, Galio looked on in horror as the murderers cut down his charge, executing him swiftly before vanishing back into the mists. Stripped of his reason for being, Galio despaired. For years he remained in solitude, standing vigil over the bones of the master he had failed to protect... a literal monument to his own everlasting shame. Then, one nondescript day, a sad but determined yordle girl carrying a mighty Demacian crown stopped in the shadow of a great statue to rest. Hidden in plain sight from his unsuspecting visitor, Galio studied the forlorn yordle. She looked as though she too shouldered a tremendous burden. As quietly and as stoically as she had arrived, she departed in the direction of Demacia. This encounter lit a spark in Galio's eye. Remembering the cause that his master had died defending, Galio arose from his silent purgatory and followed in the wake of this brave creature. He had a new reason to live: to join the League of Legends and fight for the will of Demacia.\n\n''There is no such thing as redemption. Only penance.''\n-- Galio",
    "champion_id": 3,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GalioRighteousGust.png",
    "q_name": "Resolute Smite",
    "passive_name": "Runic Skin",
    "e_description": "Galio claps his wings, unleashing a gust of concussive wind that damages enemies and leaves a directional draft in its wake that increases ally Movement Speed.",
    "recommended_items": [
      2003,
      3089,
      3111,
      3065,
      1056
    ],
    "r_name": "Idol of Durand",
    "r_description": "Galio assumes the form of a statue, taunting nearby enemies and storing concussive energy as they attack him. Galio then bursts from his statue shell, releasing the stored energy to damage surrounding foes.",
    "name": "Galio",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GalioResoluteSmite.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GalioBulwark.png",
    "q_description": "Galio fires a concussive blast from his eyes, slowing and dealing damage to enemies caught near the impact point.",
    "title": "the Sentinel's Sorrow",
    "e_name": "Righteous Gust",
    "w_description": "Galio shields an ally Champion, increasing their Armor and Magic Resistance, and restoring Galio's Health each time that Champion suffers damage.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Galio.png",
    "recommended_item_names": [
      "Health Potion",
      "Rabadon's Deathcap",
      "Mercury's Treads",
      "Spirit Visage",
      "Doran's Ring"
    ],
    "w_name": "Bulwark",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GalioIdolOfDurand.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Galio_RunicSkin.png",
    "passive_description": "Galio converts 50% of his total Magic Resistance into Ability Power."
  },
  "4": {
    "lore": "Although born to poor gypsy parents, the champion known as Twisted Fate was able to gamble his way to prosperity as a card shark in the seedy underground gambling circuits of Demacia and Noxus. No matter how close the authorities came to catching him, the rogue always found a way to slip through their fingers. Despite his good fortune, he was never able to win that which he truly desired - the ability to control magic. When Twisted Fate learned of an experiment being conducted in Zaun that might help him with his wish, he did the only thing a gambler of his worth could do - he went all in and volunteered for the experiment.\n\nConducted by the infamous Dr. Xavier Rath, Twisted Fate was told that the wager for such participation might be steep. He might change forever, or nothing might happen, or he might die horribly.  Pain, however, was likely a part of the deal no matter the outcome. These were hardly the worst odds the gambler had faced; his hopes raised, Twisted Fate underwent the experiment, enduring what he must for a chance at his dream. Then, it ended - with seemingly no effect whatsoever. The gypsy rogue flew into a murderous rage, but, before he could strike down the team, he suddenly teleported himself miles away.  With a sly grin, he realized his luck had won out yet again. He now brings his luck and rakish charm to the Institute of War, where he is the Champion of choice for many - especially the gambling kind. To this day, Twisted Fate has avoided his inevitable reunion with Dr. Rath. The Card Master knows, however, that a confrontation is coming.\n\nWhile the future may be mysterious and unknown to most, Twisted Fate is certain that his future lies within the cards.",
    "champion_id": 4,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CardmasterStack.png",
    "q_name": "Wild Cards",
    "passive_name": "Loaded Dice",
    "e_description": "Every 4 attacks, Twisted Fate deals bonus damage. In addition, his Attack Speed is increased.",
    "recommended_items": [
      2003,
      3174,
      3089,
      1056,
      3020
    ],
    "r_name": "Destiny",
    "r_description": "Twisted Fate predicts the fortunes of his foes, revealing all enemy champions and enabling the use of Gate, which teleports Twisted Fate to any target location in 1.5 seconds.",
    "name": "Twisted Fate",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/WildCards.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PickACard.png",
    "q_description": "Twisted Fate throws three cards, dealing damage to each enemy unit they pass through.",
    "title": "the Card Master",
    "e_name": "Stacked Deck",
    "w_description": "Twisted Fate chooses a magic card from his deck, and uses that for his next attack, causing bonus effects.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/TwistedFate.png",
    "recommended_item_names": [
      "Health Potion",
      "Athene's Unholy Grail",
      "Rabadon's Deathcap",
      "Doran's Ring",
      "Sorcerer's Shoes"
    ],
    "w_name": "Pick A Card",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Destiny.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Cardmaster_SealFate.png",
    "passive_description": "Upon killing a unit, Twisted Fate rolls his 'lucky' dice receiving anywhere between 1 and 6 bonus gold."
  },
  "5": {
    "lore": "Whenever Jarvan III, the king of Demacia, delivers one of his rallying speeches from the glinting marble balcony atop the Royal Palace, Xin Zhao is at his side. Coined the Seneschal of Demacia, Xin Zhao is the personal steward of the Lightshield Dynasty. His enigmatic, silent vigil has led to an abundance of conjecture concerning his ''secret life'' and origins. Whether it's ''Zaun double-agent'' tendered at the dinner table or ''indebted rune mage'' mused in the editorials of the ''Demacian Constant'', Xin Zhao betrays no hints to sate the curiosity of the masses... for good reason.\n\nPrior to the formation of the League, Noxus was renowned for a spectacle called The Fleshing. It was a gladiatorial event with a cruel twist: as a fighter won matches, his number of opponents (generally prisoners of war) fought simultaneously would increase. This meant eventual death for every contender, but with unparalleled glory. Xin Zhao, known then as Viscero, was slated to face 300 soldiers, nearly six times the previous record. This was clearly meant to be his final match. Jarvan II, hearing of this unprecedented feat, infiltrated the arena to offer him an alternative: serve Demacia and punish those who ultimately sentence him to death in exchange for his freedom. Xin Zhao accepted, astonished that a king would risk his own life on his behalf. Under the cover of a prearranged Demacian assault on Noxus, Jarvan liberated Xin Zhao and his 300 opponents. During their retreat, Xin Zhao took a poisoned dart meant for Jarvan. This act of loyalty, from a man who vowed no allegiance, earned Xin Zhao a spot at his side until the day the king died. Now in the service of his son, Jarvan III, Xin Zhao is stepping into a new ring - the Fields of Justice - to fight for his adopted country and to honor the legacy of the man who gave purpose to his life.\n\n''Death is inevitable, one can only avoid defeat.''\n      -  Demacian Manual of Arms",
    "champion_id": 5,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/XenZhaoSweep.png",
    "q_name": "Three Talon Strike",
    "passive_name": "Challenge",
    "e_description": "Xin Zhao charges an enemy, dealing damage and slowing all enemies in the area.",
    "recommended_items": [
      2003,
      1039,
      3111,
      3117,
      1054,
      3142,
      3143
    ],
    "r_name": "Crescent Sweep",
    "r_description": "Xin Zhao deals damage to nearby enemies based on their current Health and knocks non-challenged targets back. Xin Zhao gains bonus Armor and Magic Resist based on number of champions hit.",
    "name": "Xin Zhao",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/XenZhaoComboTarget.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/XenZhaoBattleCry.png",
    "q_description": "Xin Zhao's next 3 standard attacks deal increased damage that reduce his other ability cooldowns, with the third attack knocking an opponent into the air.",
    "title": "the Seneschal of Demacia",
    "e_name": "Audacious Charge",
    "w_description": "Xin Zhao passively heals every 3 attacks and can activate this ability to attack faster.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/XinZhao.png",
    "recommended_item_names": [
      "Health Potion",
      "Hunter's Machete",
      "Mercury's Treads",
      "Boots of Mobility",
      "Doran's Shield",
      "Youmuu's Ghostblade",
      "Randuin's Omen"
    ],
    "w_name": "Battle Cry",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/XenZhaoParry.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/XinZhao_TirelessWarrior.png",
    "passive_description": "Xin Zhao challenges his target with his basic attacks and Audacious Charge, reducing its Armor by 15% for 3 seconds."
  },
  "6": {
    "lore": "There are warriors who become great for their strength, cunning, or skill with arms. Others simply refuse to die. Urgot, once a great soldier of Noxus, may constitute a case in support of the latter. Prone to diving headlong into enemy battle lines, Urgot sowed chaos throughout the enemy ranks, often sustaining grievous injuries in the process. When his body was unable to weather further abuse, the crippled Urgot was delegated the position of High Executioner of Noxus. By this time, his hands had been ruined and he could barely walk. Scythe-like grafts affixed to his maimed limbs served to carry out his bloody work.\n\nUrgot finally met his end at what should have been his finest hour. Because of his military background, he often accompanied detachments into foreign territory to carry out judgment. After ambushing an enemy force, Jarvan IV, Crown Prince of Demacia, fell into the clutches of Urgot's division. Too far from Noxus to risk transporting their prize for ransom, Urgot prepared to dispose of their captive. At the final moment, however, the Dauntless Vanguard, led by Garen, the Might of Demacia, intervened, and Urgot was cut in two by the zealous warrior as he scrambled to free his Prince. In recognition of his service, the executioner's remains were remanded to the Bleak Academy for reanimation. A lifetime of abuse, however, had left his body in a catastrophic state; proving problematic to the necromancers' craft. Professor Stanwick Pididly, the prevailing scholar of Zaun, offered a solution. Within Pididly's laboratories, a nightmarish new body was forged for Urgot. Now as much machine as man, Urgot arrived at the League of Legends in search of the man who ended his life; necromantic energies coursing through his metal veins.\n\n''We can rebuild him. We have the techmaturgy.''\n-- Professor Stanwick Pididly",
    "champion_id": 6,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/UrgotPlasmaGrenade.png",
    "q_name": "Acid Hunter",
    "passive_name": "Zaun-Touched Bolt Augmenter",
    "e_description": "Urgot launches a corrosive charge that damages enemies in an area and reduces their Armor.",
    "recommended_items": [
      3047,
      2003,
      3035,
      1055,
      3110
    ],
    "r_name": "Hyper-Kinetic Position Reverser",
    "r_description": "Urgot charges up his Hyper-Kinetic Position Reverser, swapping positions with the target. His target is suppressed for the duration of the channel. He gains increased Armor and Magic Resist after the swap.",
    "name": "Urgot",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/UrgotHeatseekingMissile.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/UrgotTerrorCapacitorActive2.png",
    "q_description": "Urgot fires an Acid Hunter missile that collides with the first enemy it hits, slowing the target if he has his Terror Capacitor up. Acid Hunter missile-locks on enemies affected by Noxian Corrosive Charge.",
    "title": "the Headsman's Pride",
    "e_name": "Noxian Corrosive Charge",
    "w_description": "Urgot charges up his capacitor to gain a shield. While the shield is active, Urgot gains slowing attacks.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Urgot.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Last Whisper",
      "Doran's Blade",
      "Frozen Heart"
    ],
    "w_name": "Terror Capacitor",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/UrgotSwap2.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Urgot_Passive.png",
    "passive_description": "Urgot's basic attacks and Acid Hunters reduce his targets' damage by 15% for 2.5 seconds."
  },
  "7": {
    "lore": "Every city has its dark side, even one whose reputation is already of a questionable hue. Noxus - though its name is already invoked with a mixture of reverence and revulsion - is no exception to this simple truth. Deep within the winding dungeons that honeycomb the earth beneath its dark, meandering streets lies the real underbelly of this sprawling metropolis, a haven for all manner of malevolence. Amongst the cults, covens, and secret societies that call this labyrinth their home, LeBlanc, the Deceiver, presides over the Black Rose, a remnant from a lost, yet similarly unscrupulous time in Noxian history. Ruthless and seemingly ageless, LeBlanc and her ilk were a mainstay in Noxian political affairs during the era before the militarization of the Noxian government. In those days, this guild of powerful magicians met in secret to further their hidden agenda, and to hone a craft more subtle than that preferred by those currently in power.\n\nWhile their exact motives have always remained mysterious, it was widely believed that the Black Rose was the true power behind the throne while the aristocracy still reigned in Noxus. When raw martial prowess became the ultimate determination of whose will held sway in the Empire, the Black Rose seemed to vanish overnight. Many believed that perhaps their time had simply passed, and that its members had put aside their quests for social and political dominance. When LeBlanc reemerged at the gates of the Institute of War, however, it became clear that these masters of shadow and flame had simply been biding their time, waiting for a new global authority to emerge: the League of Legends.\n\n''The world is very different for those who cannot see beyond what is placed before their very eyes.''\n-- LeBlanc, the Deceiver",
    "champion_id": 7,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LeblancSoulShackle.png",
    "q_name": "Sigil of Malice",
    "passive_name": "Mirror Image",
    "e_description": "LeBlanc flings illusionary chains towards a target location. If it hits an enemy unit, it will deal initial magic damage and slow their Movement Speed by 25%. If the target remains shackled for 2 seconds, the target takes additional magic damage and is unable to move.",
    "recommended_items": [
      3135,
      2003,
      1056,
      3157,
      3020
    ],
    "r_name": "Mimic",
    "r_description": "LeBlanc can cast a mimicked version of the previous spell she cast.",
    "name": "LeBlanc",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LeblancChaosOrb.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LeblancSlide.png",
    "q_description": "LeBlanc projects an orb towards her target, dealing magic damage and marking the target for 3.5 seconds. If the target takes damage from one of LeBlanc's abilities, the sigil will trigger, dealing damage.",
    "title": "the Deceiver",
    "e_name": "Ethereal Chains",
    "w_description": "LeBlanc rapidly dashes to a target location, dealing magic damage to nearby units. In the following 4 seconds, she can activate Distortion again to return to her starting location.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Leblanc.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Doran's Ring",
      "Zhonya's Hourglass",
      "Sorcerer's Shoes"
    ],
    "w_name": "Distortion",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LeblancMimic.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/LeblancMirrorImage.png",
    "passive_description": "When LeBlanc drops below 40% Health, she becomes invisible for 1 second and creates a Mirror Image that deals no damage and lasts for up to 8 seconds.<br><br>Mirror Image has a 1 minute cooldown.<br><br><span class=\"color99FF99\">Mirror Image can be controlled by holding the Alt key and using the right mouse button.<\/span>"
  },
  "8": {
    "lore": "There is a temple hidden in the mountains between Noxus and the Tempest Flats, where the secrets of an ancient and terrifying sorcery are kept. The area surrounding the temple is littered with the exsanguinated corpses of those who have mistakenly wandered too close. These served only to pique the curiosity of Vladimir, when - in his youth - he trekked through these mountains during his flight from Noxus. A day earlier, the teenaged Vladimir had brutally murdered two boys his age, for no better reason than to enjoy the intoxicating scarlet bloom that surged forth. He realized immediately that he would never be able to suppress his murderous desires, and if he remained in Noxus, his foul deeds were sure to catch up with him. Without hesitation, he abandoned the city-state, and journeyed south.\n\nThe trail of bodies led him to a crumbling stone temple. Inside he found an aging monk who appraised him with eyes of pure crimson. Vladimir surprised the monk by returning the wicked gaze with zeal. Recognizing the boy's sinister craving, the monk taught Vladimir how to manipulate and control the fluid of life, often practicing on passing travelers. When it came time for Vladimir to learn the final lesson, the monk warned that failure would result in death. Vladimir did not fail, but success bore a grisly surprise. During the ritual, every drop of the monk's blood was drawn from his body and fused with Vladimir's, imbuing him with his master's magical essence, and that of every hemomancer before him. Left alone and suddenly without purpose, Vladimir resolved to return to Noxus, demanding enrollment in the League to prove the supremacy of his craft. When the Noxian High Command observed the gruesome fates which befell the palace guards, they elected to avail themselves of Vladimir's unsavory talents.\n\n''That which runs through you will run you through.''\n-- Vladimir",
    "champion_id": 8,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VladimirTidesofBlood.png",
    "q_name": "Transfusion",
    "passive_name": "Crimson Pact",
    "e_description": "Vladimir unleashes a torrent of blood, damaging surrounding enemies. Additionally, multiple Tides of Blood in a short period of time cause them to cost additional Health and deal additional damage, and increases his healing and regeneration.",
    "recommended_items": [
      2003,
      3089,
      3001,
      1054,
      3020
    ],
    "r_name": "Hemoplague",
    "r_description": "Vladimir infects an area with a virulent plague. Affected enemies take increased damage for the duration. Hemoplague deals additional magic damage after a few seconds to infected enemies.",
    "name": "Vladimir",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VladimirTransfusion.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VladimirSanguinePool.png",
    "q_description": "Vladimir drains life from his target.",
    "title": "the Crimson Reaper",
    "e_name": "Tides of Blood",
    "w_description": "Vladimir sinks into a pool of blood, becoming untargetable for 2 seconds. Additionally, enemies on the pool are slowed and Vladimir siphons life from them.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Vladimir.png",
    "recommended_item_names": [
      "Health Potion",
      "Rabadon's Deathcap",
      "Abyssal Scepter",
      "Doran's Shield",
      "Sorcerer's Shoes"
    ],
    "w_name": "Sanguine Pool",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VladimirHemoplague.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Vladimir_BloodGorged.png",
    "passive_description": "Every 40 points of bonus Health gives Vladimir 1 Ability Power and every 1 point of Ability Power gives Vladimir 1.4 bonus Health (does not stack with itself)."
  },
  "9": {
    "lore": "For nearly twenty years, Fiddlesticks has stood alone in the easternmost summoning chamber of the Institute of War. Only the burning emerald light of his unearthly gaze pierces the musty darkness of his dust-covered home. It is here that the Harbinger of Doom keeps a silent vigil. His is a cautionary tale of power run amok, taught to all summoners within the League. Decades ago, there existed a powerful rune mage from Zaun - Istvaan. At the end of the fifth Rune War, he became one of the League's first summoners. Too much a prisoner to the old ways of magic, Istvaan stepped further and further outside the rules of conduct in the League. In what was ultimately his last match, his reach finally exceeded his grasp. Sealing himself inside the easternmost summoning chamber, he began incanting the most forbidden of rituals - an extra-planar summoning.\n\nWhat exactly happened inside that chamber remains unknown. No champion came to represent Zaun that day in Summoner's Rift. Only silence echoed back from repeated knocks on the chamber door. The first apprentice who entered was cut down immediately by an unearthly scythe. What few who followed and survived were driven mad by fear, mere husks of men gibbering about crows and death. Afraid of the evil even Istvaan could not control, the League sealed all exits to the chamber, hoping they could contain what they could not destroy. Years went by, but the wooden figure within never moved save to slay any foolish enough to enter. Seeing no recourse to reclaim the chamber, the Council instead devised a use for Fiddlesticks: executioner. While he comes to life and seemingly abides by the rules of summoning in the Fields of Justice, what he awaits inside his chamber is unknown. His unmoving face yields no clues, and his scythe stands ready to strike down any who stand before him.\n\nThose who say 'you have nothing to fear but fear itself' have not yet felt the crows.",
    "champion_id": 9,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FiddlesticksDarkWind.png",
    "q_name": "Terrify",
    "passive_name": "Dread",
    "e_description": "A wisp of wind strikes an enemy unit and then bounces to nearby enemy units, dealing damage and silencing the victims.",
    "recommended_items": [
      2003,
      1039,
      3089,
      3001,
      1056,
      3020
    ],
    "r_name": "Crowstorm",
    "r_description": "A murder of crows flock wildly around Fiddlesticks, dealing damage each second to all enemy units in the area.",
    "name": "Fiddlesticks",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Terrify.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Drain.png",
    "q_description": "Strikes a target unit with fear, causing it to flee in terror for a duration.",
    "title": "the Harbinger of Doom",
    "e_name": "Dark Wind",
    "w_description": "Fiddlesticks saps the life force of an enemy, dealing damage to a target over time and healing himself.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/FiddleSticks.png",
    "recommended_item_names": [
      "Health Potion",
      "Hunter's Machete",
      "Rabadon's Deathcap",
      "Abyssal Scepter",
      "Doran's Ring",
      "Sorcerer's Shoes"
    ],
    "w_name": "Drain",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Crowstorm.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Fiddlesticks_Paranoia.png",
    "passive_description": "Fiddlesticks' spells reduce the Magic Resistance of his targets."
  },
  "266": {
    "lore": "Aatrox is a legendary warrior, one of only five that remain of an ancient race known as the Darkin. He wields his massive blade with grace and poise, slicing through legions in a style that is hypnotic to behold. With each foe felled, Aatrox's seemingly living blade drinks in their blood, empowering him and fueling his brutal, elegant campaign of slaughter.\n\nThe earliest tale of Aatrox is as old as recorded history. It tells of a war between two great factions remembered only as the Protectorate and the Magelords. Over time, the Magelords won a series of crushing victories, leaving them on the brink of obliterating their sworn enemy forever. On the day of their final confrontation, the Protectorate army found themselves outnumbered, exhausted, and poorly equipped. They braced for inevitable defeat.\n\nJust when all hope seemed lost, Aatrox appeared among the ranks of the Protectorate. With but a few words, he urged the soldiers to fight to the last before throwing himself into battle. His presence inspired the desperate warriors. At first, they could only watch in awe as this unknown hero cleaved through their enemies, his body and blade moving in unison as if one being. Soon, the warriors found themselves imbued with a potent thirst for battle. They followed Aatrox into the fray, each fighting with the furious strength of ten until they had won a most unlikely victory.\n\nAatrox vanished after that battle, but the Protectorate army's newfound fury did not. Their surprising triumph led to many more until they were able to finally return home victorious. Their countrymen hailed them as heroes, but though they had saved their entire civilization from destruction, darkness lingered in the mind of each warrior. Something within them had changed. Over time, their memories of battle faded, only to be replaced with a grim revelation: their acts of heroism were, in fact, brutal atrocities committed by their own hands.\n\nTales like these appear among the myths of many cultures. If they are all to be believed, Aatrox's presence has changed the course of some of the most important wars in history. Though these stories remember him as a savior in dark times, Aatrox's true legacy may be a world filled with conflict and strife.\n\n''Some fight for honor, some fight for glory. It matters only that you fight.''\n-- Aatrox",
    "champion_id": 266,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AatroxE.png",
    "q_name": "Dark Flight",
    "passive_name": "Blood Well",
    "e_description": "Aatrox unleashes the power of his blade, dealing damage to all enemies hit and slowing them.",
    "recommended_items": [
      1001,
      3065,
      1036,
      1054,
      1053
    ],
    "r_name": "Massacre",
    "r_description": "Aatrox draws in the blood of his foes, damaging all nearby enemy champions around him and gaining increased Attack Speed and bonus Attack Range for a short duration.",
    "name": "Aatrox",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AatroxQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AatroxW.png",
    "q_description": "Aatrox takes flight and slams down at a targeted location, dealing damage and knocking up enemies at the center of impact.",
    "title": "the Darkin Blade",
    "e_name": "Blades of Torment",
    "w_description": "While toggled on Aatrox deals bonus damage every third subsequent attack at the expense of his own Health. While toggled off Aatrox restores Health every third subsequent attack.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Aatrox.png",
    "recommended_item_names": [
      "Boots of Speed",
      "Spirit Visage",
      "Long Sword",
      "Doran's Shield",
      "Vampiric Scepter"
    ],
    "w_name": "Blood Thirst \/ Blood Price",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AatroxR.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Aatrox_Passive.png",
    "passive_description": "When using an ability that costs Health, Aatrox stores the self-inflicted damage into the Blood Well. Upon taking fatal damage, Aatrox extracts the blood from the well and recovers it as Health over a brief duration. Additionally, Aatrox gains 1% Attack Speed for every 2% blood that is in the well."
  },
  "267": {
    "lore": "Nami channels the primal energies of the ocean, harnessing its mystical restorative properties and commanding the raw power of the tides themselves. Though many doubted her, Nami had the bravery and determination to take on a dangerous quest when no one else would. Now her people believe she is the Tidecaller, a chosen one destined to complete a quest essential to the survival of her entire race.\n\nThe Tidecaller's sacred duty is to acquire a moonstone, a powerful object found only in the towering reaches of the surface world. Her people, the Marai, rely on the moonstone's light to ward off the terrors of the depths. However, the stone's power lasts only one hundred years. Before its light fades, the Tidecaller must journey into the Great Deep, retrieve an abyssal pearl, and carry it to the surface. There, on the night of the winter solstice of the hundredth year, the Tidecaller makes a ceremonial exchange with a landwalker bearing a moonstone. By trading the pearl for the moonstone, the Tidecaller ensures the survival of the Marai for another century.\n\nHowever, in Nami's time, as the hundred years drew to a close, no Tidecaller had been found. Without a chosen one to complete the quest, her people would face disaster, but the Marai waited in faith that the Tidecaller would appear. Nami refused to sit idle, insisting that without a Tidecaller to save them, someone had to act. Bravely, she decided to begin the quest herself and ventured alone into the dangerous depths. None expected her to survive, but after six days of battles with untold horrors, Nami returned with the pearl in hand. The Marai hailed her as the new Tidecaller. All that remained was for Nami to journey to the surface and complete the exchange.\n\nWhen Nami arrived at the surface, however, she found only an empty shore. She waited for days in a mystic cove, unsure of what to do. In all the legends of the Tidecallers, the bearer of the moonstone had never failed to arrive. Nami faced a choice. She knew the surface world only through tale and rumor, but the survival of the Marai depended upon her. Summoning the tide to bear her ashore, Nami began her search for the moonstone and became the first of her kind to explore the world above the ocean. She left her home behind, and vowed not to return until she had completed the Tidecaller's quest.\n\n''I am the tide, and I cannot be turned.''\n-- Nami",
    "champion_id": 267,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NamiE.png",
    "q_name": "Aqua Prison",
    "passive_name": "Surging Tides",
    "e_description": "Empowers an allied champion for a short duration. The ally's basic attacks deal bonus magic damage and slow the target.",
    "recommended_items": [
      2003,
      3303,
      3190,
      3174,
      3117
    ],
    "r_name": "Tidal Wave",
    "r_description": "Summons a massive Tidal Wave that knocks up, slows, and damages enemies.",
    "name": "Nami",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NamiQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NamiW.png",
    "q_description": "Sends a bubble towards a targeted area, dealing damage and stunning all enemies on impact.",
    "title": "the Tidecaller",
    "e_name": "Tidecaller's Blessing",
    "w_description": "Unleashes a stream of water that bounces back and forth between allies and enemies, healing allies and damaging enemies.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Nami.png",
    "recommended_item_names": [
      "Health Potion",
      "Spellthief's Edge",
      "Locket of the Iron Solari",
      "Athene's Unholy Grail",
      "Boots of Mobility"
    ],
    "w_name": "Ebb and Flow",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NamiR.png",
    "role": "Support",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/NamiPassive.png",
    "passive_description": "When Nami's abilities hit allied champions they gain Movement Speed for a short duration."
  },
  "12": {
    "lore": "As the mightiest warrior to ever emerge from the Minotaur tribes of the Great Barrier, Alistar defended his tribe from Valoran's many dangers; that is, until the coming of the Noxian army. Alistar was lured from his village by the machinations of Keiran Darkwill, General Boram Darkwill's youngest son and commander of the Noxian expeditionary force. When Alistar returned, he found his village burning and his family slain. Bellowing with rage, he charged an entire regiment of Noxus' elite, slaughtering them by the hundreds. Only the intervention of some of Noxus' most skilled summoners checked Alistar's rage. Brought in chains to Noxus, Alistar spent the intervening years as a gladiator in the Fleshing, pitted in endless battle for the entertainment of Noxus' wealthy leaders.\n\nAlistar's once noble soul slowly became twisted, and he would have been driven to insanity if not for Ayelia, a young servant girl who befriended him and eventually arranged for his escape. Suddenly free, Alistar joined the newly formed League of Legends to fight as a champion, hoping to one day exact his final vengeance upon Noxus and find the girl who had renewed his hope. Initially unwilling to cater to his celebrity status as a champion, Alistar has since discovered that there is power in fame, and he has become a vocal advocate for those whom the Noxian government treads upon. He also calls to light things that the Noxian military would prefer remain hidden -- something that has made him very unpopular with Noxus' nobles. His charitable work has earned him several philanthropic awards, which serve as an interesting contrast to the rage and destruction he brings to the League of Legends.\n\nIf you intend to grab the bull by the horns as a summoner, Alistar might have something to say about that.",
    "champion_id": 12,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TriumphantRoar.png",
    "q_name": "Pulverize",
    "passive_name": "Trample",
    "e_description": "Alistar lets out a commanding war cry, restoring Health to himself and nearby friendly units for half the amount. Can be cast more often if nearby enemies are dying.",
    "recommended_items": [
      1001,
      3065,
      1056,
      1028,
      3010
    ],
    "r_name": "Unbreakable Will",
    "r_description": "Alistar lets out a wild roar, gaining bonus damage, removing all crowd control effects on himself, and reducing incoming physical and magical damage for the duration.",
    "name": "Alistar",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Pulverize.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Headbutt.png",
    "q_description": "Alistar smashes the ground, dealing damage to all nearby enemies and tossing them into the air for 1.5 seconds. On landing, enemies are stunned.",
    "title": "the Minotaur",
    "e_name": "Triumphant Roar",
    "w_description": "Alistar rams a target with his head, dealing damage and knocking the target back.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Alistar.png",
    "recommended_item_names": [
      "Boots of Speed",
      "Spirit Visage",
      "Doran's Ring",
      "Ruby Crystal",
      "Catalyst the Protector"
    ],
    "w_name": "Headbutt",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FerociousHowl.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Alistar_Passive.png",
    "passive_description": "Each time Alistar casts a spell, he tramples nearby units and turrets for a few seconds, dealing damage to units he walks over."
  },
  "13": {
    "lore": "There are many on Runeterra who are attracted to the study of magic or, in recent times, the emerging field of techmaturgy. For most, pursuit of such knowledge is formalized in a college or university. The halls of traditional study were never for Ryze, however, who felt a more raw and primal connection to the magic of Runeterra than those who tried to teach him. He struck out on his own as a young man to discover what already called to him. Ryze traveled the world, seeking the wisdom of powerful hermits, witches, and shamans - anyone who had something to share beyond what was taught in the city-states of Valoran. When he had learned all he could from these fonts of wisdom, Ryze turned to seek the lost, forgotten, and forbidden knowledge in the world, delving into mystical worlds where others feared to tread.\n\nRyze's tireless searching for magical knowledge led him to an ancient form of spellcraft known as thorn magic. This art required Ryze to tattoo spells on his body, permanently infusing his being with vast arcane power and finally fulfilling his need to bond with the mystical energies of Runeterra. His travels also led him to uncover the giant indestructible scroll he now carries on his back - the purpose of the inscribed spell remains a secret only Ryze knows. He claims it is an abomination - something that he must safeguard from the world. This has piqued the curiosity of many, though no one is sure how to separate the scroll from Ryze, or if it is possible to overcome the rogue mage to do so. Since then, Ryze has joined the League of Legends to study the magical creatures and powerful will-workers that fight there, in order to complete his exploration of mystical Runeterra.\n\n''Ryze is no longer just a mage - he has become a creature of magic itself.''\n-- High Councilor Heywan Relivash",
    "champion_id": 13,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SpellFlux.png",
    "q_name": "Overload",
    "passive_name": "Arcane Mastery",
    "e_description": "Ryze releases an orb of pure magical power that deals damage and bounces from the initial target up to 5 times. Also gains bonus damage based on Ryze's maximum Mana. Targets hit have their Magic Resistance reduced.",
    "recommended_items": [
      2003,
      3110,
      3003,
      1027,
      3020
    ],
    "r_name": "Desperate Power",
    "r_description": "Ryze channels immense arcane power, he gains Spell Vamp and all of his spells deal area of effect damage.",
    "name": "Ryze",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Overload.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RunePrison.png",
    "q_description": "Ryze throws a charge of pure energy at an enemy for heavy damage and additional damage based upon Ryze's maximum Mana. Ryze also gains passive cooldown reduction.",
    "title": "the Rogue Mage",
    "e_name": "Spell Flux",
    "w_description": "Ryze traps target enemy unit in a cage of runes, damaging them and preventing them from moving. Also gains bonus damage based on Ryze's maximum Mana.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Ryze.png",
    "recommended_item_names": [
      "Health Potion",
      "Frozen Heart",
      "Archangel's Staff",
      "Sapphire Crystal",
      "Sorcerer's Shoes"
    ],
    "w_name": "Rune Prison",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DesperatePower.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Ryze_SpellStrike.png",
    "passive_description": "When Ryze casts a spell, all other spells have their cooldown reduced by 1 second."
  },
  "14": {
    "lore": "BLOOD.\n\nSMELL IT.\n\nWANT. ACHING. NEED!\n\nCLOSE NOW. THEY COME.\n\nNO CHAINS? FREE! KILL!\n\nIN REACH. YES! DIE! DIE!\n\nGone. Too quick. No fight. More. I want... more.\n\nA voice? Unfamiliar. I see him. The Grand General. My general.\n\nHe leads. I follow. Marching. To where? I should know. I can't remember.\n\nIt all bleeds together. Does it matter? Noxus conquers. The rest? Trivial. So long...  since I've tasted victory.\n\nThe war wagon rocks. Rattles. A cramped cage. Pointless ceremony. The waiting. Maddening. Faster, dogs!\n\nThere. Banners. Demacians and their walls. Cowards. Their gates will shatter. Thoughts of the massacre come easily.\n\nWho gave the order to halt? The underlings don't answer. No familiar faces. If I do not remember, neither will history.\n\nThe cage is opened. Finally! No more waiting. WE CHARGE!\n\nSlings and arrows? The weapons of children! Their walls will not save them!\n\nI can taste their fear. They shrink at every blow as their barricades splinter. SOON!\n\nNoxian drums. Demacian screams. Glory isn't accolades; glory is hot blood on your hands! This is life!\n\nA thousand shattered corpses lie at my feet, and Demacian homes burn all around me. It's over too quickly! Just one more...\n\nThe men stare. There's fear in their eyes. If they're afraid to look upon victory, I should pluck those craven eyes out. There is no fear in the Grand General's eyes, only approval. He is pleased with this conquest.\n\nWalking the field with the Grand General, surveying the carnage, I ache for another foe. He is hobbled, a leg wound from the battle? If it pains him, he does not show it. A true Noxian. I do not like his pet, though; it picks over the dead, having earned nothing. His war hounds were more fitting company.\n\nDemacia will be within our grasp soon. I can feel it. I am ready to march. The Grand General insists that I rest. How can I rest when my enemies still live?\n\nWhy do we mill about? The waiting eats at me. I'm left to my own devices. The bird watches. It's unsettling. Were it anyone else's, I would crush it.\n\nFatigue sets in. I've never felt so... tired.\n\nBoram? Is that you? What are you whispering?\n\nWhere am I?\n\nCaptured? Kenneled like some dog. How?\n\nThere was... the battle, the razing of the fortress, the quiet of the aftermath. Were we ambushed? I can't remember.\n\nI was wounded. I can feel the ragged gash... but no pain. They thought me dead. Now, I am their prize. Fate is laughing. I will not be caged! They will regret sparing me.\n\nDemacian worms! They parrot kind words, but they are ruthless all the same. This place is a dank pit. They bring no food. There is no torture. They do not make a show of me. I am left to rot.\n\nI remember my finest hour. I held a king by his throat and felt the final beat of his heart through my tightening grasp. I don't remember letting go. Is this your vengeance, Jarvan?\n\nI hear the triumphal march. Boots on stone. Faint, through the dungeon walls. The cadence of Noxian drums. I shall be free. Demacian blood will run in the streets!\n\nNo one came. I heard no struggle. No retreat. Did I imagine it?\n\nThere is no aching in this stump. I barely noticed the iron boot. It's caked in rust.\n\nWhen did I lose my leg?\n\nI still smell the blood. Battle. It brings comfort.\n\nThe hunger gnaws. I have not slept. Time crawls. So tired.\n\nHow long?\n\nSo dark. This pit. I remember. Grand General. His whispering. What was it?\n\nNot who I think.\n\nFading. Mustn't forget.\n\nMessage. Cut. Remember.\n\n''SION \u2013 Beware ravens.''\n\nFREE ME!\n\nBLOOD.",
    "champion_id": 14,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SionE.png",
    "q_name": "Decimating Smash",
    "passive_name": "Glory in Death",
    "e_description": "Sion fires a short range shockwave that damages and slows and reduces the Armor of the first enemy hit. If the shockwave hits a minion or monster, it will be knocked back, damaging and slowing all enemies that it passes through.",
    "recommended_items": [
      3047,
      3102,
      2003,
      3074,
      1039,
      3117,
      1054
    ],
    "r_name": "Unstoppable Onslaught",
    "r_description": "Sion charges in a direction, ramping up speed over time. He can steer his charge slightly with the mouse cursor location. When he collides with an enemy he deals damage and knocks them up based on the distance he has charged.",
    "name": "Sion",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SionQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SionW.png",
    "q_description": "Sion charges a powerful swing in an area in front of himself that will deal damage to enemies when released. If he charges for enough time, enemies hit by the swing will also be knocked up and stunned.<\/span>",
    "title": "The Undead Juggernaut",
    "e_name": "Roar of the Slayer",
    "w_description": "Sion shields himself and can reactivate after 2 seconds to deal Magic Damage to enemies nearby.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Sion.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Banshee's Veil",
      "Health Potion",
      "Ravenous Hydra (Melee Only)",
      "Hunter's Machete",
      "Boots of Mobility",
      "Doran's Shield"
    ],
    "w_name": "Soul Furnace",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SionR.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Sion_Passive1.png",
    "passive_description": "After being killed, Sion will reanimate himself with rapidly decaying Health.<br><br>He can move and attack during this time. He gains 100% Lifesteal, attacks extremely fast and will deal an additional 10% of his target's maximum Health as physical damage on hit. Max 75 bonus damage against monsters.<br><br>All of his abilities are replaced with Death Surge, which grants him a burst of Movement Speed."
  },
  "15": {
    "lore": "Known as the Battle Mistress, Sivir is a mercenary with a ruthless reputation. Combining unflinching bravery with endless ambition, she has garnered great fame and fortune. Faced with the revelation of her mysterious heritage, Sivir must weigh her desire to continue on her own path, or accept the burden of a greater legacy.",
    "champion_id": 15,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SivirE.png",
    "q_name": "Boomerang Blade",
    "passive_name": "Fleet of Foot",
    "e_description": "Creates a magical barrier that blocks a single enemy ability cast on Sivir. She receives Mana back if a spell is blocked.",
    "recommended_items": [
      2003,
      3035,
      3026,
      1055,
      3006
    ],
    "r_name": "On The Hunt",
    "r_description": "Sivir leads her allies in battle, granting them a surge Movement Speed for a period of time. Additionally passively grants Sivir bonus Attack Speed while Ricochet is active.",
    "name": "Sivir",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SivirQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SivirW.png",
    "q_description": "Sivir hurls her crossblade like a boomerang, dealing damage each way.",
    "title": "the Battle Mistress",
    "e_name": "Spell Shield",
    "w_description": "Sivir's next few basic attacks will bounce to nearby targets, dealing reduced damage to secondary targets.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Sivir.png",
    "recommended_item_names": [
      "Health Potion",
      "Last Whisper",
      "Guardian Angel",
      "Doran's Blade",
      "Berserker's Greaves"
    ],
    "w_name": "Ricochet",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SivirR.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Sivir_Passive.png",
    "passive_description": "Sivir gains a short burst of Movement Speed when she attacks an enemy champion."
  },
  "16": {
    "lore": "A healer gifted with the magic of the stars, Soraka holds all living creatures close to her heart. She was once a celestial being, but she sacrificed her immortality and entered the world of mortals. So long as evil threatens life in Valoran, Soraka will not allow herself peace.\n\nSoraka lived for centuries in an enchanted grove. A being of the stars, she healed the wounded and sick that sought her out. One man called Warwick came to her grove and begged her to heal his wife, who lay lifeless in his arms. His despair touched Soraka's heart. Though it was too late to save his wife, she offered to help heal the pain of his loss. Unwilling to let go of his grief Warwick ran from the grove, but returned over the following days to hear Soraka's guidance. She began to grow attached to the grieving man. One day Warwick told her he had found the men who killed his wife. He believed revenge would heal his pain - and if he died fighting, he would at least find peace. Though she pleaded with him, Warwick ignored her and left the grove. The voices of the stars warned her not to follow him, but Soraka had to intervene.\n\nShe stepped into the mortal world for the first time, and soon found Warwick desperately fighting a group of men. She tried to heal him, but for every wound she closed, the men inflicted two more. Soraka realized that she would have to fight to save her friend. The stars screamed in her mind, telling her not to use her powers for harm. Ignoring their warning, she struck the attackers with a flash of brilliant light. Crying out in terror and shielding their eyes from her divine radiance, they fled. Soraka's celestial form faded and the stars fell silent - for her transgression, she became mortal. She still felt the power of the stars within her, but they no longer offered her guidance. She took comfort in Warwick's safety, gently healing his wounds, but the man she had called her friend slipped a dagger between her ribs. As her blood spilled, Soraka realized he had fooled her, and everything he had done was a complicated ruse. Feeling humiliated and betrayed she called once more on the power of the stars, searing his flesh and cursing his cruelty. He retreated with an agonized howl, leaving Soraka to reflect upon her fate. Though her life had changed, she felt empowered and renewed with a singular purpose. No longer bound to the grove, Soraka set out into the mortal world, vowing to heal the wounded and protect the helpless.\n\n''The cruelty of one will not blind me to the suffering of many.''\n-- Soraka",
    "champion_id": 16,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SorakaE.png",
    "q_name": "Starcall",
    "passive_name": "Salvation",
    "e_description": "Creates a zone at a location that silences all enemies inside. When the zone expires, all enemies still inside are rooted.",
    "recommended_items": [
      1001,
      1056,
      3151,
      1028,
      3010
    ],
    "r_name": "Wish",
    "r_description": "Soraka fills her allies with hope, instantly restoring health to herself and all friendly champions.",
    "name": "Soraka",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SorakaQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SorakaW.png",
    "q_description": "A star falls from the sky at the target location dealing magic damage and slowing enemies in the center of effect.",
    "title": "the Starchild",
    "e_name": "Equinox",
    "w_description": "Soraka sacrifices a portion of her own Health to heal another friendly unit. Passively heals Soraka when she lands Starcall on an enemy Champion.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Soraka.png",
    "recommended_item_names": [
      "Boots of Speed",
      "Doran's Ring",
      "Liandry's Torment",
      "Ruby Crystal",
      "Catalyst the Protector"
    ],
    "w_name": "Astral Infusion",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SorakaR.png",
    "role": "Support",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Soraka_Passive.png",
    "passive_description": "Soraka runs faster towards nearby low health allies."
  },
  "17": {
    "lore": "Teemo is a legend among his yordle brothers and sisters in Bandle City. As far as yordles are concerned, there is something just slightly off about him. While Teemo enjoys the companionship of other yordles, he also insists on frequent solo missions in the ongoing defense of Bandle City. Despite his genuinely warm personality, something switches off inside Teemo's mind during combat so that the lives he must end while on patrol do not burden him. Even as a young recruit, the drill instructors and other trainees found it a little disconcerting that, while Teemo was normally charming and kind, he turned deadly serious and highly efficient the minute combat exercises began. Teemo's superiors quickly steered him toward the Scouts of the Mothership, which is one of Bandle City's most distinguished Special Forces unit alongside the Megling Commandos.\n\nWhile most yordles do not handle solo scouting missions with a great deal of finesse, Teemo is remarkably efficient at them. His record of success in defending Bandle City from infiltrators easily makes him one of the most dangerous yordles alive, though you'd never know it by having a cup of honey mead with him at his favorite inn. Bandle City chose Teemo as their first champion for the League, and he has taken to it like a duck to water. His signature weapon - a blowgun - uses a rare ajunta poison he personally gathers from the jungles of Kumungu. To help cope with his lengthy periods of isolation, Teemo recently struck up a friendship with Tristana, a fellow League champion and fellow member of Bandle City's Special Forces. This connection is healthy for both yordles, though now Valoran's voracious media outlets circulate rumors that the friendship is turning into a romantic relationship. Regardless, Teemo is a crowd favorite in the League of Legends, and a pint-sized foe that many have come to fear.\n\n''Teemo rides a thin line between chipper compatriot and unrepentant killer, but there's no one else I'd rather have as a friend.''\n-- Tristana",
    "champion_id": 17,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ToxicShot.png",
    "q_name": "Blinding Dart",
    "passive_name": "Camouflage",
    "e_description": "Each of Teemo's attacks will poison the target, dealing damage on impact and each second after for 4 seconds.",
    "recommended_items": [
      2003,
      3089,
      1056,
      3157,
      3020
    ],
    "r_name": "Noxious Trap",
    "r_description": "Teemo places an explosive poisonous trap using one of the mushrooms stored in his pack. If an enemy steps on the trap, it will release a poisonous cloud, slowing enemies and damaging them over time.",
    "name": "Teemo",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BlindingDart.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MoveQuick.png",
    "q_description": "Obscures an enemy's vision with a powerful venom, dealing damage to the target unit and blinding it for the duration.",
    "title": "the Swift Scout",
    "e_name": "Toxic Shot",
    "w_description": "Teemo scampers around, passively increasing his Movement Speed until he is struck by an enemy champion or turret. Teemo can sprint to gain bonus Movement Speed that isn't stopped by being struck for a short time.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Teemo.png",
    "recommended_item_names": [
      "Health Potion",
      "Rabadon's Deathcap",
      "Doran's Ring",
      "Zhonya's Hourglass",
      "Sorcerer's Shoes"
    ],
    "w_name": "Move Quick",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BantamTrap.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Teemo_Camouflage.png",
    "passive_description": "If Teemo stands still and takes no actions for a short duration, he becomes stealthed indefinitely. After leaving stealth, Teemo gains the Element of Surprise, increasing his Attack Speed by 40% for 3 seconds."
  },
  "18": {
    "lore": "Greatness comes in all shapes and sizes, as proven by this diminutive, cannon-wielding\u00a0yordle. In a world fraught with turmoil, Tristana refuses to back down from any challenge. She represents the pinnacle of martial proficiency, unwavering courage, and boundless optimism. For Trist and her gun, Boomer, every mission is a chance to prove that heroes do exist.",
    "champion_id": 18,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TristanaE.png",
    "q_name": "Rapid Fire",
    "passive_name": "Draw a Bead",
    "e_description": "When Tristana kills a unit, her cannonballs burst into shrapnel, dealing damage to surrounding enemies. Can be activated to place a bomb on a target enemy that explodes after a short duration dealing damage to surrounding units.",
    "recommended_items": [
      2003,
      3035,
      3026,
      1055
    ],
    "r_name": "Buster Shot",
    "r_description": "Tristana loads a massive cannonball into her weapon and fires it at an enemy unit. This deals Magic Damage and knocks the target back.",
    "name": "Tristana",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TristanaQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TristanaW.png",
    "q_description": "Tristana fires her weapon rapidly, increasing her Attack Speed for a short time.",
    "title": "the Yordle Gunner",
    "e_name": "Explosive Charge",
    "w_description": "Tristana fires at the ground to propel her to a distant location, dealing damage and slowing surrounding units for 3 seconds where she lands.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Tristana.png",
    "recommended_item_names": [
      "Health Potion",
      "Last Whisper",
      "Guardian Angel",
      "Doran's Blade"
    ],
    "w_name": "Rocket Jump",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TristanaR.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Tristana_Passive.png",
    "passive_description": "Increases Tristana's Attack Range as she levels."
  },
  "19": {
    "lore": "Warwick was once a man revered for his ability to track down human specimens for the darkest types of scientific research. When his ambitions exceeded his physical limits, he drank a dangerous elixir to transform himself into an unstoppable manhunter.  His newfound strength bore a heavy price.\n\nBefore his transformation, Warwick found his calling in Zaun as a ''procurer'' of human test subjects. Known for his crafty methods and ruthless determination, people regarded him with a cautious mixture of fear and respect. As his reputation grew, so did the demands placed upon him. His clients wanted more rare and dangerous specimens, and they wanted them sooner. To meet their demands, Warwick needed strength that transcended his limited human form. His longtime friend, Singed, devised a powerful formula. The recipe called for three critical components: silver from the Shadow Isles, the fang of a Balefire dire wolf, and the heart of a celestial being. Warwick tracked down the first two in short order, but the third proved a much greater challenge. He traveled to Ionia to trap Soraka, a creature believed to be a child of the stars, but she discovered his ploy and drove him away with powerful magic. Unable to tolerate his failure, Warwick returned to Singed disfigured and furious. He demanded the chemist's incomplete potion, but Singed warned him that the results would be unpredictable. Ignoring his friend's warning, Warwick drank the concoction. The brew transformed him into a creature both man and wolf, infusing him with raw strength and heightened senses. Exhilarated, he immediately began testing his newfound power. Each day his instincts became sharper, but his human half slipped further away. He could feel himself losing control: though he always got his prey, he often failed to bring them back alive. Now he seeks the heart of Soraka to stabilize his transformation before his mind gives way to the feral urges of the beast.\n\n''Eventually the beast catches up with all of us.''\n-- Warwick",
    "champion_id": 19,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BloodScent.png",
    "q_name": "Hungering Strike",
    "passive_name": "Eternal Thirst",
    "e_description": "Warwick passively senses weakened enemy champions around him. The scent of blood sends him into a fury, causing him to move at incredible speeds.",
    "recommended_items": [
      2003,
      3091,
      1039,
      3111,
      3117,
      1054,
      3110
    ],
    "r_name": "Infinite Duress",
    "r_description": "Warwick lunges at an enemy champion, suppressing his target and dealing magic damage for a few seconds.",
    "name": "Warwick",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HungeringStrike.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HuntersCall.png",
    "q_description": "Takes a bite out of an enemy unit and heals Warwick.",
    "title": "the Blood Hunter",
    "e_name": "Blood Scent",
    "w_description": "Warwick lets out a howl, increasing all nearby friendly champions' Attack Speed for a short time.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Warwick.png",
    "recommended_item_names": [
      "Health Potion",
      "Wit's End",
      "Hunter's Machete",
      "Mercury's Treads",
      "Boots of Mobility",
      "Doran's Shield",
      "Frozen Heart"
    ],
    "w_name": "Hunters Call",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/InfiniteDuress.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Warwick_InnerHunger.png",
    "passive_description": "Each of Warwick's attacks will heal him. Each successive attack against the same target will steal more and more Health."
  },
  "20": {
    "lore": "Sometimes bonds of friendship become stronger than even bonds of blood. When those bonds link a fearless boy to a fearsome Yeti, the bond becomes a force to be reckoned with. Given the responsibility of taming a terrifying beast, Nunu forged a friendship where others would have forged chains. Now Nunu and his burly pal Willump are an inseparable pair who combine youthful exuberance and brute strength with the mythical powers of the Yeti to overcome obstacles insurmountable to any ordinary duo. \n\n Nunu had only the vaguest memories of his parents or the time before he was part of the reclusive Frostguard tribe. Never welcome among his caretakers, Nunu's wanderlust and compassion often put him at odds with the tribe's elders and the boy frequently dreamt of places far beyond the shadow of the Frostguard citadel. Sometimes he would do more than just dream, much to the frustration of his minders. This was never more apparent than when Nunu was apprenticed to the tribe's beastmaster and charged with the care of the creatures under his yoke. \n\n The Frostguard held a menagerie of the Freljord's wildlife at their beck and call, but unique among their collection was the Yeti: an uncommon creature with mystical qualities and raw physical strength. The beastmaster taught Nunu that it was only a lean diet of plants and regular whippings that kept the vicious beast tame, but the more time Nunu spent caring for the creature, the more he learned that the Yeti was no feral monster.\n\n As he saw his new friend Willump growing weaker and sicker, Nunu began to sneak the Yeti scraps of meat, hoping to restore his health. Day by day, Willump grew stronger and not the slightest bit savage - contrary to the beastmaster's claims. Nunu had hopes of convincing him that the Yeti posed no danger, but it wasn't meant to be. The next time Nunu came to deliver Willump a meal, he found the Yeti\ufffds cage shattered, with only a crude drawing inside signaling the Yeti's farewell. Without hesitation, Nunu rushed into the wilderness in search of his friend.\n\n When Nunu finally caught up to Willump, he found the Yeti cornered by the beastmaster alongside a group of Frostguard warriors. Afraid that the men would hurt his friend, Nunu threw himself between the Yeti and the beastmaster's lash, but the brutal man would not stay his hand. As the furious beastmaster raised his whip once more, the Yeti swelled up with uncharacteristic fury. Even after so much mistreatment, it wasn't concern for himself but for the boy who'd shown him kindness that finally pushed Willump too far. The Yeti raged and left the man bloodied in the snow. \n\nTerrified by Willump's fury, the remaining Frostguard warriors fled. Nunu realized there was no going back. He yelled at Willump to run before the men returned to kill him, but the Yeti refused to leave the young boy. Nunu was faced with a hard choice: abandon his sole friend and lead a life of captivity with the Frostguard, or strike out into the harsh wilds and leave behind the only home he knew. Nunu chose the only path that made sense. Leaping onto the back of the mighty Yeti, Nunu joined Willump in his great escape. The pair took their first steps into the wide world from which they had been kept for so long. \n\n''Willump and I have a whole world to explore. Don't get in our way!'' \n-- Nunu",
    "champion_id": 20,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/IceBlast.png",
    "q_name": "Consume",
    "passive_name": "Visionary",
    "e_description": "Nunu launches a ball of ice at an enemy unit, dealing damage and temporarily slowing their Movement and Attack Speeds.",
    "recommended_items": [
      2003,
      1039,
      3111,
      3117,
      1056,
      3068,
      3110
    ],
    "r_name": "Absolute Zero",
    "r_description": "Nunu begins to sap the area of heat, slowing all nearby enemies. When the spell ends, he deals massive damage to all enemies caught in the area.",
    "name": "Nunu",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Consume.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BloodBoil.png",
    "q_description": "Nunu commands the yeti to take a bite out of a target minion or monster, dealing heavy damage to it and healing himself.",
    "title": "the Yeti Rider",
    "e_name": "Ice Blast",
    "w_description": "Nunu invigorates himself and an allied unit by heating their blood, increasing their Movement and Attack Speeds.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Nunu.png",
    "recommended_item_names": [
      "Health Potion",
      "Hunter's Machete",
      "Mercury's Treads",
      "Boots of Mobility",
      "Doran's Ring",
      "Sunfire Cape",
      "Frozen Heart"
    ],
    "w_name": "Blood Boil",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AbsoluteZero.png",
    "role": "Support",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Yeti_FrostNova.png",
    "passive_description": "Nunu can cast a spell for free after 5 attacks."
  },
  "21": {
    "lore": "For those who brave the harsh seas of Runeterra, attaining one's own ship and crew is the pinnacle of success. Sarah Fortune, a well-respected (some would say legendary) bounty hunter from Bilgewater, was able to achieve this feat just after her sixteenth birthday, etching out her name as the go-to gal for resolving special troubles. No bounty was too difficult or too dangerous for her feminine charm and her renowned use of her twin pistols, ''Shock and Awe''. Her success gave her the means to legitimately purchase her own ship... with a little flirtatious haggling, of course. Things weren't always so fortunate for Miss Fortune, though. When she was young, trade ships began to dot the horizon of her quiet home in the northern shores of Blue Flame Island's largest chunk. Trade routes brought piracy, and the inhabitants soon found themselves caught in a frenzy of pillage.\n\nOne day, young Sarah returned home to hear gunshots and screaming. Her front door was smashed open; inside, she saw her mother lying in a pool of blood. A sudden blow to her head made her collapse next to her slain mother. The last thing she could remember were her attacker's red eyes, as his face was blocked by a rogue's bandana. Miss Fortune has a strong distrust for pirates and she finds herself constantly bickering with the infamous Gangplank (the only captain to resist her charms) over the direction of Bilgewater politics. Her two goals: to unite the people of Bilgewater, making them into a strong and independent society, and to find the pirate who killed her mother. To that end, she has entered the League of Legends as a champion, trading her skills for the wealth and influence that will help her accomplish both.",
    "champion_id": 21,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MissFortuneScattershot.png",
    "q_name": "Double Up",
    "passive_name": "Strut",
    "e_description": "Miss Fortune unleashes a flurry of bullets at a location, dealing waves of damage to opponents and slowing them.",
    "recommended_items": [
      2003,
      3035,
      3026,
      1055,
      3006
    ],
    "r_name": "Bullet Time",
    "r_description": "Miss Fortune channels a flurry of bullets into a cone in front of her, dealing large amounts of damage to enemies.",
    "name": "Miss Fortune",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MissFortuneRicochetShot.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MissFortuneViciousStrikes.png",
    "q_description": "Miss Fortune fires a bullet at an enemy, damaging them and a target behind them.",
    "title": "the Bounty Hunter",
    "e_name": "Make It Rain",
    "w_description": "Miss Fortune passively increases damage dealt to a target with each strike. This ability can be activated to increase Miss Fortune's Attack Speed and cause her attacks to lower healing received by the target.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/MissFortune.png",
    "recommended_item_names": [
      "Health Potion",
      "Last Whisper",
      "Guardian Angel",
      "Doran's Blade",
      "Berserker's Greaves"
    ],
    "w_name": "Impure Shots",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MissFortuneBulletTime.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/MissFortune_Strut.png",
    "passive_description": "After 5 seconds of not being attacked, Miss Fortune gains an additional 25 Movement Speed. This bonus increases by 8 each second up to a maximum bonus of 70."
  },
  "22": {
    "lore": "With each arrow she fires from her ancient ice-enchanted bow, Ashe proves she is a master archer. She chooses each target carefully, waits for the right moment, and then strikes with power and precision. It is with this same vision and focus that she pursues her goal of uniting the tribes of the Freljord and forging them into a mighty nation.\n\nAs a child, Ashe was always a dreamer. She marveled at the colossal, abandoned fortresses of her ancestors, and spent hours by the fire listening to tales of the Freljord's fabled champions. Most of all she loved the legend of Avarosa, the renowned Queen of the once magnificent and united Freljord. Though her mother chided her foolishness, Ashe swore one day she would join the scattered and warlike tribes of the tundra. She knew in her heart that if her people would stand together once more, they would reach greatness again.\n\nWhen Ashe was only fifteen, her mother was killed while commanding the tribe on a brash raid. Suddenly thrust into the role of leader, Ashe made the difficult decision to follow her childhood vision instead of seeking the revenge she craved. She spoke passionately against her tribe's demand for retribution, declaring the time had come to put blood feuds aside and broker a lasting peace. Some of her warriors questioned her fitness to rule and soon hatched a treasonous plot to kill the young leader.\n\nThe assassins struck while Ashe was on a routine hunt, but their plan was interrupted by the warning cry of a great hawk. Ashe looked back to see her tribesmen approaching with swords drawn. Outnumbered and overwhelmed, Ashe ran for hours. She found herself deep in uncharted territory, her weapon lost in the chase. When she heard another cry from the hawk, Ashe put her faith in the strange creature and followed it to a clearing. There she found the bird perched on a pile of stones - an ancient Freljord burial cairn. With a last glance at her, the hawk screeched and flew away. Approaching the mound, Ashe felt her breath turn to frost and an unnatural cold chill her to the bone. The stone at the top of the cairn was marked with a single rune: Avarosa.\n\nThe assassins burst into the clearing. Ashe lifted the runestone from the cairn to defend herself, revealing something hidden underneath: an ornate bow carved from ice. She grasped it, crying out in pain as frost formed on her fingers, and tore the bow from its resting place. Cold flowed from the enchanted weapon into Ashe, awakening a tremendous power that had always lived within her. \n\nAshe turned to face the assassins. She drew the bow, and by sheer instinct, willed arrows of pure ice to form from the cold, crisp air. With a single frozen volley, she ended the insurrection. Carefully replacing the cairn stone, she gave thanks to Avarosa for her gift, and returned home. Ashe's tribe immediately recognized the legendary weapon in the archer's hand as a blessing from the ancient Freljord queen herself.\n\nWith Avarosa's bow and her vision of peaceful unification, Ashe's tribe soon swelled, becoming the largest in the Freljord. Now known as the Avarosan, they stand together with the belief that a united Freljord will once again become a great nation.\n\n''One tribe, one people, one Freljord.''\n -- Ashe",
    "champion_id": 22,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AsheSpiritOfTheHawk.png",
    "q_name": "Frost Shot",
    "passive_name": "Focus",
    "e_description": "Ashe gains bonus Gold when killing enemy units or structures. Ashe can activate to send her Hawk Spirit on a scouting mission.",
    "recommended_items": [
      1001,
      3087,
      1055,
      1036,
      1053
    ],
    "r_name": "Enchanted Crystal Arrow",
    "r_description": "Ashe fires a missile of ice in a straight line. If the arrow collides with an enemy Champion, it deals damage and stuns the Champion for up to 3.5 seconds, based on how far the arrow has traveled. In addition, surrounding enemy units take damage and are slowed.",
    "name": "Ashe",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FrostShot.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Volley.png",
    "q_description": "While active, each of Ashe's basic attacks slow her targets. This drains Mana with each attack.",
    "title": "the Frost Archer",
    "e_name": "Hawkshot",
    "w_description": "Ashe fires 7 arrows in a cone for increased damage. Volley also applies Ashe's current level of Frost Shot.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Ashe.png",
    "recommended_item_names": [
      "Boots of Speed",
      "Statikk Shiv",
      "Doran's Blade",
      "Long Sword",
      "Vampiric Scepter"
    ],
    "w_name": "Volley",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EnchantedCrystalArrow.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Ashe_Passive.png",
    "passive_description": "While out of combat, Ashe gains stacks of Focus. When Ashe has 100 stacks of Focus her next basic attack will critically strike."
  },
  "23": {
    "lore": "Fueled by his unbridled fury and rage, Tryndamere cuts his way through the tundra, mastering the art of battle by challenging the Freljord's greatest warriors. The wrathful barbarian seeks revenge on the one who decimated his clan and strikes down all those who stand between him and his final retribution.\n\nStruggling to survive in the harsh, frostbitten Freljord, the young Tryndamere and his people warred with other tribes over the scarce resources of the land. One such battle changed his life forever. Raiders ambushed Tryndamere's clan in the dead of night, and though his warriors were able to push the first wave of attackers back, they weren't prepared for the dark figure that next stepped forth. He wielded a cruel, living sword, and inspired an unhinged bloodlust in the invaders with his unearthly magic. Tryndamere's tribe was overrun within moments. With no hope of defeating the enigmatic being, Tryndamere threw himself at certain death. The dark figure swatted him aside, mortally wounding the young barbarian.\n\nTryndamere saw death and destruction engulf his home as his life slipped away. No one was left standing - only the screams of the dying remained. Unable to surrender to death, Tryndamere gave in fully to his wrath. His blood boiled and his anger consumed him, banishing his mortality. He staggered to his feet - barely able to take hold of his sword - steeling himself for the decisive confrontation with the shadowy being. But the dark figure did not even lift his blade, and instead gave Tryndamere a knowing smile as he withdrew into the shadows. That was the last time the barbarian ever saw his nemesis.\n\nA man robbed of his home and his people, Tryndamere wandered across the Freljord for years, vowing to forge himself into a brutal instrument of revenge. He visited all the tribes in the frozen wastes, besting each of their warriors until there were none left to challenge. In doing so, he mastered the barbarian ways of war and harnessed his anger as a force to be reckoned with. With sword in hand and rage in his heart, he is now on an undying quest for vengeance against the one who destroyed the life he once knew. \n\n''Rage is my weapon.''\n -- Tryndamere",
    "champion_id": 23,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/slashCast.png",
    "q_name": "Bloodlust",
    "passive_name": "Battle Fury",
    "e_description": "Tryndamere slices toward a target unit, dealing damage to enemies in his path.",
    "recommended_items": [
      2003,
      3026,
      1039,
      1055,
      3006,
      3031
    ],
    "r_name": "Undying Rage",
    "r_description": "Tryndamere's lust for battle becomes so strong that he is unable to die, no matter how wounded he becomes.",
    "name": "Tryndamere",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Bloodlust.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MockingShout.png",
    "q_description": "Tryndamere thrives on the thrills of combat, increasing his Attack Damage as he is more and more wounded. He can cast Bloodlust to consume his Fury and heal himself.",
    "title": "the Barbarian King",
    "e_name": "Spinning Slash",
    "w_description": "Tryndamere lets out an insulting cry, decreasing surrounding champions' Attack Damage. Enemies with their backs turned to Tryndamere also have their Movement Speed reduced.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Tryndamere.png",
    "recommended_item_names": [
      "Health Potion",
      "Guardian Angel",
      "Hunter's Machete",
      "Doran's Blade",
      "Berserker's Greaves",
      "Infinity Edge"
    ],
    "w_name": "Mocking Shout",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/UndyingRage.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Tryndamere_Passive.png",
    "passive_description": "Tryndamere gains Fury for each attack, critical strike, and killing blow he makes. Fury passively increases his Critical Strike Chance and can be consumed with his Bloodlust spell."
  },
  "24": {
    "lore": "It is seldom the case where a champion is defined by his actions after joining the League of Legends rather than before. Such is the case with Jax, for whom the argument could be made that he is the most prolific tournament fighter currently at the Institute of War. Before joining the League, Jax was an unremarkable soldier-for-hire. For reasons known only to the former leader of the League, High Councilor Reginald Ashram, Jax was put on the top of the list of candidates to receive a League Judgment - the interview process that either accepts or rejects a prospective champion. His Judgment was the quickest in League history, where the Doors of Acceptance glowed and slowly swung open as soon as it began. Jax faced no recorded Observation or Reflection during his Judgment.\n\nJax proved himself to be an immediate terror in the Fields of Justice. The self-proclaimed ''Armsmaster of the League'' rattled off a streak of consecutive wins that to this day has not been matched. A number of summoners in the League grew concerned that the perceived objectivity of the League of Legends would be questioned by the presence of an unknown fighter who was unbeatable. For this reason, the new leader of the League (following Reginald Ashram's disappearance), High Councilor Heyward Relivash, created special restrictions for Jax to fight under. This was something the League had never done before, and something that has never been done since. The burly fighter responded by imposing his own special conditions; as a means of protest, he permitted himself to fight using only a brass lamppost. Neither the League's sanctions nor his own has affected his winning ways. The League has since rescinded its sanctions, but Jax has not; he fights and fights well with his trusty brass lamppost.\n\n''Be advised - there has been an outbreak of lamppost-shaped bruises in the League of Legends.''\n-- Gragas",
    "champion_id": 24,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JaxCounterStrike.png",
    "q_name": "Leap Strike",
    "passive_name": "Relentless Assault",
    "e_description": "Jax's combat prowess allows him to dodge all incoming attacks for a short duration and then quickly counterattack, stunning all surrounding enemies.",
    "recommended_items": [
      3047,
      2003,
      3074,
      1039,
      3111,
      2041,
      3143
    ],
    "r_name": "Grandmaster's Might",
    "r_description": "Every third consecutive attack deals additional Magic Damage. Additionally, Jax can activate this ability to strengthen his resolve, increasing his Armor and Magic Resist for a short duration.",
    "name": "Jax",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JaxLeapStrike.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JaxEmpowerTwo.png",
    "q_description": "Jax leaps toward a unit. If they are an enemy, he strikes them with his weapon.",
    "title": "Grandmaster at Arms",
    "e_name": "Counter Strike",
    "w_description": "Jax charges his weapon with energy, causing his next attack to deal additional damage.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Jax.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Ravenous Hydra (Melee Only)",
      "Hunter's Machete",
      "Mercury's Treads",
      "Crystalline Flask",
      "Randuin's Omen"
    ],
    "w_name": "Empower",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JaxRelentlessAssault.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Armsmaster_MasterOfArms.png",
    "passive_description": "Jax's consecutive basic attacks continuously increase his Attack Speed."
  },
  "25": {
    "lore": "There is a world far away populated by graceful and beautiful winged beings gifted with immortality, where an ancient conflict still rages. Like so many conflicts, this war split families. One side proclaimed themselves as beings of perfect order and justice, fighting to unite the world under their law and strong central governance. Those that fought against them saw their kin as tyrants, creatures incapable of seeing the larger view, who would sacrifice individuality and freedom for the illusion of efficiency and safety. Morgana was one who fought against what she perceived as the tyranny of her kind, and for that she was branded ''fallen.'' Morgana was not innocent, having plumbed forgotten ways to gather forbidden might to become a powerful mistress of the black arts. This goal was driven by her obsession to defeat the general of the opposition's army - her sister, Kayle.\n\nWhile the two were in fact birth-sisters, Kayle struck the first blow by disowning any filial connection when Morgana refused to join her cause. Eventually, Morgana grew in power enough to not only reach, but challenge Kayle. As the time approached when the two would meet in what could be their final conflict, Morgana was suddenly summoned to Valoran. At first, Morgana made a deal with the League's summoners to fight in exchange for greater power. With the advent of Kayle into the League, Morgana now willingly fights in the League of Legends for the privilege of being able to destroy her sister again, and again, and again. She lies in wait for the day the bonds of the Institute of War no longer hold her, and on that day she plans to destroy Kayle once and for all and return home a hero.\n\n''There is no rest while Kayle's brand of tyranny still exists.''\n-- Morgana",
    "champion_id": 25,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BlackShield.png",
    "q_name": "Dark Binding",
    "passive_name": "Soul Siphon",
    "e_description": "Places a protective barrier around an allied champion, absorbing magical damage and disables until penetrated or the shield dissipates.",
    "recommended_items": [
      3135,
      2003,
      3174,
      1056,
      3020
    ],
    "r_name": "Soul Shackles",
    "r_description": "Latches chains of energy onto nearby enemy champions, dealing initial damage to them and slowing their Movement Speed, and then echoing the pain a few seconds later and stunning them if they remain close to Morgana.",
    "name": "Morgana",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DarkBindingMissile.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TormentedSoil.png",
    "q_description": "Morgana releases a sphere of dark magic. Upon contact with an enemy unit, the sphere will deal magic damage and force the unit to the ground for a period of time.",
    "title": "Fallen Angel",
    "e_name": "Black Shield",
    "w_description": "Infects an area with desecrated soil, causing enemy units who stand on the location to take continual damage.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Morgana.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Athene's Unholy Grail",
      "Doran's Ring",
      "Sorcerer's Shoes"
    ],
    "w_name": "Tormented Soil",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SoulShackles.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/FallenAngel_Empathize.png",
    "passive_description": "Morgana has Spell Vamp, healing herself whenever she deals damage with her spells."
  },
  "26": {
    "lore": "In the wastelands of Urtistan, there was once a great city. It perished long ago in a terrible Rune War, like most of the lands below the Great Barrier. Nevertheless, one man survived: a sorcerer named Zilean. Being obsessed with time, it was only fitting that he dwelled in the city's Clock Tower. As the havoc of the war neared his home, Zilean experimented with powerful temporal magic to divine all possible futures, hoping to discover a peaceful solution. But Zilean's enchantments affected his perception of the passage of time, and he was in a contemplative stasis when Urtistan was set upon by an entire phalanx of dark summoner-knights of unknown affiliation. By the time he realized his error, Urtistan was nothing more than smoldering debris. The summoners who were responsible for its destruction had wisely left the Clock Tower unharmed, both to avoid drawing Zilean's attention and to torment him for his oversight.\n\nZilean barely had time to grieve the momentous loss before he learned that his dangerous research had a cruel side effect: chrono-displasia. This mystical disease granted him immortality, but detached his consciousness from its anchor in the present time. He now mentally drifts through time, from any point he has already lived to the present, unable to impact the events which unfold. The most torturous aspect of this curse is that Zilean sometimes experiences Urtistan as it once was and the rest of the time resides in its lonely ruins. Only the powerful summoning magic employed by members of the League of Legends has been able to treat this condition, and Zilean has joined in hopes of finding a cure, and thereafter a way to save his people.\n\n''There is no greater grief than for a loss that is yet to come.''\n-- Zilean",
    "champion_id": 26,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TimeWarp.png",
    "q_name": "Time Bomb",
    "passive_name": "Heightened Learning",
    "e_description": "Zilean bends time around any unit, decreasing an enemy's Movement Speed or increasing an ally's Movement Speed for a short time.",
    "recommended_items": [
      2003,
      3089,
      1056,
      3157,
      3020
    ],
    "r_name": "Chronoshift",
    "r_description": "Zilean places a protective time rune on an allied champion, teleporting the champion back in time if they take lethal damage.",
    "name": "Zilean",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TimeBomb.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Rewind.png",
    "q_description": "Places a bomb on any unit, allied or enemy, which detonates after 4 seconds, dealing area of effect damage.",
    "title": "the Chronokeeper",
    "e_name": "Time Warp",
    "w_description": "Zilean can prepare himself for future confrontations, reducing the cooldowns of all of his other abilities. ",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Zilean.png",
    "recommended_item_names": [
      "Health Potion",
      "Rabadon's Deathcap",
      "Doran's Ring",
      "Zhonya's Hourglass",
      "Sorcerer's Shoes"
    ],
    "w_name": "Rewind",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ChronoShift.png",
    "role": "Support",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Chronokeeper_Slow.png",
    "passive_description": "Zilean and his nearby allied champions receive 8% additional experience."
  },
  "27": {
    "lore": "Singed descended from a long line of Zaun's revered chemists. Even in his youth, his talent for concocting potions far outstripped that of his peers, and he quickly distinguished himself from his less extraordinary chemist compatriots. It came as no surprise to anyone when he was selected for apprenticeship by the infamous Warwick, master apothecary on a lucrative retainer with the Noxian military during their campaign against Ionia. Within Warwick's laboratories, Singed toiled without end, rapidly absorbing every detail of his predecessor's deadly craft. Singed had little concern for the death and destruction that was the fruit of his labors. By the time the curse of lycanthropy descended to claim his master, Singed was poised and eager to make the transition from workhorse to innovator; he was ready to share his genius by bringing a new brand of suffering to the Ionian front. His zeal for progress was unquenchable, and when suitable test subjects proved to be in short supply, the eager chemist was often thought to turn his volatile mixtures on his own flesh.\n\nWhen the uneasy peace created by the League of Legends settled on the world, Singed journeyed to the one place where he was still able to showcase his beloved craft: the Institute of War. By this time he was barely even a man, his body both ruined and sustained by his ingenious craft. A thousand burns - accidents of shadow and flame - mar his ravaged form, and exposure to such harsh conditions has deadened his nerves, hardened his body, and strengthened his physique, transforming him into a veritable juggernaut. This, combined with a formidable arsenal of deadly concoctions, makes Singed a force to be reckoned with on the Fields of Justice.\n\n''My deadliest dose shall bear my patron's name!''\n-- Singed, having just christened the Insanity Potion",
    "champion_id": 27,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Fling.png",
    "q_name": "Poison Trail",
    "passive_name": "Empowered Bulwark",
    "e_description": "Damages target enemy unit and flings them into the air behind Singed. If the target Singed flings lands in his Mega Adhesive, they are also rooted.",
    "recommended_items": [
      3075,
      2003,
      3111,
      2041,
      3003
    ],
    "r_name": "Insanity Potion",
    "r_description": "Singed drinks a potent brew of chemicals, granting him increased combat stats.",
    "name": "Singed",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PoisonTrail.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MegaAdhesive.png",
    "q_description": "Leaves a trail of poison behind Singed, dealing damage to enemies caught in the path.",
    "title": "the Mad Chemist",
    "e_name": "Fling",
    "w_description": "Throws a vial of mega adhesive on the ground, slowing enemies who walk on it.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Singed.png",
    "recommended_item_names": [
      "Thornmail",
      "Health Potion",
      "Mercury's Treads",
      "Crystalline Flask",
      "Archangel's Staff"
    ],
    "w_name": "Mega Adhesive",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/InsanityPotion.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Singed_Passive.png",
    "passive_description": "Increases Singed's Health by 25 for every 100 Mana he has."
  },
  "28": {
    "lore": "Swift and lethal, Evelynn is one of the most deadly - and expensive - assassins in all of Runeterra. Able to merge with the shadows at will, she patiently stalks her prey, waiting for the right moment to strike. While Evelynn is clearly not entirely human, and her heritage remains unclear, it is believed that she hails from the Shadow Isles - though her link with that tortured realm remains shrouded in mystery.",
    "champion_id": 28,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EvelynnE.png",
    "q_name": "Hate Spike",
    "passive_name": "Shadow Walk",
    "e_description": "Evelynn slashes her target twice, dealing damage with each hit. She then gains increased Attack Speed for a short duration.",
    "recommended_items": [
      2003,
      3723,
      1039,
      2041,
      3143,
      3153,
      3020
    ],
    "r_name": "Agony's Embrace",
    "r_description": "Evelynn summons spikes from the ground to deal damage and slow enemies in the area. She then gains a shield based on how many enemy champions were hit.",
    "name": "Evelynn",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EvelynnQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EvelynnW.png",
    "q_description": "Evelynn fires a line of spikes through an enemy, dealing damage to all enemies in its path.",
    "title": "the Widowmaker",
    "e_name": "Ravage",
    "w_description": "Evelynn passively increases her Movement Speed when hitting enemy champions with her spells. Upon activation, Evelynn breaks free from slows affecting her and gains a massive Movement Speed boost for a short duration.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Evelynn.png",
    "recommended_item_names": [
      "Health Potion",
      "Enchantment: Warrior",
      "Hunter's Machete",
      "Crystalline Flask",
      "Randuin's Omen",
      "Blade of the Ruined King",
      "Sorcerer's Shoes"
    ],
    "w_name": "Dark Frenzy",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EvelynnR.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Evelynn_ShadowWalk.png",
    "passive_description": "When out of combat, Evelynn enters stealth only being able to be seen by nearby enemy champions or true sight. While stealthed, she rapidly regenerates Mana."
  },
  "29": {
    "lore": "H.I.V.E. Incident Report\nCode Violation: Industrial Homicide\nCasefile Status: Unsolved\nInvestigating Agent: Rol, P.\n\nTeam responded to report of suspicious character, criminal activity; proceeded to Sump Works, Sector 90TZ. Sector 90TZ notably absent. In its place: sinkhole, smoke, noxious fumes. Interviews with private security indicate urgent need for better private security.\nResponse team entered sinkhole. Toxic runoff had melted away building wreckage. Two survivors located, one partially liquefied and dripping off catwalk. Six deceased bodies found among wreckage, three of them partial; two appear to predate incident. Causes of death include acute deceleration, caustic liquidation, and\/or fatal crossbow wounds. Unclear if lab's destruction was itself the perpetrator's motive or an attempt to cover tracks.\n\nSurvivor #1 (Ra Qintava, facility researcher) brought up for interview, but unable to provide statement due to 1) post-traumatic stress and 2) liquefaction of tongue and lower jaw. Awaiting toxin screen and prosthesis fitting.\n\nSearch-and-rescue discovered apparent shantytown constructed from refuse. Recovered items include:\n\n     57 waterlogged romance novels, illegible, with edits made in crayon\n     108 bottles, unlabeled (possible toxic runoff or discarded shampoo remnants)\n     200 pounds chewing gum (possible installation art project)\n     1 jar toenails, labeled by toe\/finger, date, and mood\nSurvivor #2 (Valori Olant, Sludge Analyst) in recovery; regained lucidity following prolonged therapeutic electrocution. Statement transcript excerpt follows:\n\n     V.O.: GOT TO DO SOMETHING - \n     NURSE: She's lost so much blood --\n     P.R.: Her co-workers lost a lot more than that --\n     V.O.: IT'S STILL OUT THERE!\n     P.R.: Ma'am, I need you to focus. Tell me what he looked like.\n     V.O.: LIKE A RAT! (pause)\n     NURSE: Like a what?\n     P.R.: You mean, small? Beady-eyed? Sorta rat-faced -- ?\n     V.O.: I MEAN IT LOOKED LIKE A GIANT GODSDAMNED RAT! (pause). WITH A CROSSBOW! (pause).\n     P.R.: (to nurse) Can we moderate her painkillers \ufffd?\n     V.O.: YOU'RE NOT LISTENING! IT'S A HOMICIDAL, PSYCHOPATHIC, GIANT FREAKING RAT! \n     IN A WAISTCOAT!\n     P.R.: Nurse?\n     NURSE: (injecting Olant's arm with sedative) On it.\n     [EDIT]\n     V.O.: We were just scientists, working on refining human waste into inexpensive baby formula... [EDIT] I saw \ufffd I don't know how else to \ufffd this crazed, enormous RAT \ufffd screaming at us! Kicking over vats! Spitting on our food! [EDIT] The lab was sealed. Industrial waste was spilling everywhere. Nowhere to run. [EDIT] I woke up in the dark. Well, the acid had melted my eyeballs. I could SMELL the twitchy bastard inches from my face. It said, 'NOBODY STEALS TWITCH'S JUICE!' cackled wildly, and skittered off... I can still smell it in my mind. OH MY GODS, I CAN STILL SMELL IT\ufffd\n\nEnd transcript. At this point victim began screaming; has yet to stop. \n\n[UPDATE: Qintava, Written Testimony]\nSuspect summary, as reported:\n     NAME\/KNOWN ALIASES: ''Twitch.''\n     SEX: Male (unconfirmed).\n     AGE: Unknown.\n     HEIGHT: 4'9'' (hunched) \n     WEIGHT: < 99 lbs. (wet). \n     DISTINGUISHING FEATURES: Is a giant rat. \n     STATUS: At large; armed, extremely dangerous; DO NOT ENGAGE.\n\nH.I.V.E - Enforcing Progress!",
    "champion_id": 29,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TwitchExpunge.png",
    "q_name": "Ambush",
    "passive_name": "Deadly Venom",
    "e_description": "Twitch wreaks further havoc on poisoned enemies with a blast of his vile diseases.",
    "recommended_items": [
      3072,
      2003,
      1055,
      3006,
      3031
    ],
    "r_name": "Rat-Ta-Tat-Tat",
    "r_description": "Twitch unleashes the full power of his crossbow, shooting bolts over a great distance that pierce all enemies caught in their path.",
    "name": "Twitch",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TwitchHideInShadows.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TwitchVenomCask.png",
    "q_description": "Twitch becomes invisible for a short duration and, while invisible, he gains Movement Speed. When leaving invisibility, Twitch gains Attack Speed for a short duration.",
    "title": "the Plague Rat",
    "e_name": "Contaminate",
    "w_description": "Twitch hurls a cask of venom that explodes in an area, slowing targets and applying deadly venom to the target.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Twitch.png",
    "recommended_item_names": [
      "The Bloodthirster",
      "Health Potion",
      "Doran's Blade",
      "Berserker's Greaves",
      "Infinity Edge"
    ],
    "w_name": "Venom Cask",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TwitchFullAutomatic.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Twitch_Passive.png",
    "passive_description": "Twitch's basic attacks infect the target, dealing true damage each second."
  },
  "30": {
    "lore": "Karthus is a harbinger of oblivion, zealously devoted to the beauty and clarity of death. Even in his youth, he was utterly obsessed with mortality, growing ever more relentless in the pursuit of his dark desires. Yearning to be one with death itself, Karthus journeyed to the Shadow Isles and willingly offered himself to undeath. Karthus transformed into the Deathsinger, a dread lich existing solely to deliver the blessed gift of annihilation.",
    "champion_id": 30,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KarthusDefile.png",
    "q_name": "Lay Waste",
    "passive_name": "Death Defied",
    "e_description": "Karthus passively steals energy from his victims, gaining Mana on each kill. Alternatively, Karthus can surround himself in the souls of his prey, dealing damage to nearby enemies, but quickly draining his own Mana.  ",
    "recommended_items": [
      2003,
      3089,
      3027,
      1056,
      3157
    ],
    "r_name": "Requiem",
    "r_description": "After channeling for 3 seconds, Karthus deals damage to all enemy champions.",
    "name": "Karthus",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KarthusLayWasteA1.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KarthusWallOfPain.png",
    "q_description": "Karthus unleashes a delayed blast at a location, dealing damage to nearby enemies.",
    "title": "the Deathsinger",
    "e_name": "Defile",
    "w_description": "Karthus creates a passable screen of leeching energy. Any enemy units that walk through the screen have their Movement Speed and Magic Resist reduced for a period.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Karthus.png",
    "recommended_item_names": [
      "Health Potion",
      "Rabadon's Deathcap",
      "Rod of Ages",
      "Doran's Ring",
      "Zhonya's Hourglass"
    ],
    "w_name": "Wall of Pain",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KarthusFallenOne.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Karthus_Passive.png",
    "passive_description": "Upon dying, Karthus enters a spirit form that allows him to continue casting spells while dead for 7 seconds."
  },
  "31": {
    "lore": "There is a place between dimensions, between worlds. To some it is known as the Outside, to others it is the Unknown. To those that truly know, however, it is called the Void. Despite its name, the Void is not an empty place, but rather the home of unspeakable things - horrors not meant for minds of men.  Cho'Gath is a creature born of the Void, a thing whose true nature is so awful most will not speak its name. Its fellows have been poking at the walls that divide dimensions for a crack, a way into Runeterra, where they can visit their own personal paradise of horror upon the world. They are called the Voidborn, creatures so ancient and terrible that they have been removed from history altogether. It is rumored that the Voidborn command vast armies of unspeakable creatures on other worlds, that they were once driven from Runeterra by powerful magic lost to antiquity.\n\nIf such tales are true, then the rumors that follow must be equally true - that one day, the Voidborn will return. Even now, something dark stirs in Icathia, perverting the summoning rituals of the League to allow the presence of Cho'Gath. It is an alien creature of malice and violence, a thing that causes all but the most stalwart to cringe in fear. Cho'Gath even appears to feed on its predations, growing and swelling as it gorges itself. Worse yet, the creature is intelligent, perhaps greatly so, making most wonder how such a monster could be contained. Fortunately, the power of the League's summoning has confined Cho'Gath's presence exclusively to the League of Legends. It is here that summoners use Cho'Gath's Voidborn abilities to help decide the fate of Runeterra. The Terror of the Void knows what fate it would choose for Runeterra, given half the chance.\n\nWoe betide the day when Cho'Gath grows weary of the League.",
    "champion_id": 31,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VorpalSpikes.png",
    "q_name": "Rupture",
    "passive_name": "Carnivore",
    "e_description": "Cho'Gath's attacks passively release deadly spikes, dealing damage to all enemy units in front of him.",
    "recommended_items": [
      2003,
      3091,
      1039,
      3111,
      3117,
      1056,
      3143
    ],
    "r_name": "Feast",
    "r_description": "Devours an enemy unit, dealing a high amount of true damage. If the target is killed, Cho'Gath grows, gaining maximum Health (maximum 6 stacks). Cho'Gath loses half of his stacks upon death. Half the cooldown and mana cost are refunded if a minion or monster is killed.",
    "name": "Cho'Gath",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Rupture.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FeralScream.png",
    "q_description": "Ruptures the ground at target location, popping enemy units into the air, dealing damage and slowing them.",
    "title": "the Terror of the Void",
    "e_name": "Vorpal Spikes",
    "w_description": "Cho'Gath unleashes a terrible scream at enemies in a cone, dealing magic damage and Silencing enemies for a few seconds.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Chogath.png",
    "recommended_item_names": [
      "Health Potion",
      "Wit's End",
      "Hunter's Machete",
      "Mercury's Treads",
      "Boots of Mobility",
      "Doran's Ring",
      "Randuin's Omen"
    ],
    "w_name": "Feral Scream",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Feast.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/GreenTerror_TailSpike.png",
    "passive_description": "Whenever Cho'Gath kills a unit, he recovers Health and Mana. The values restored increase with Cho'Gath's level."
  },
  "32": {
    "lore": "Amumu is a diminutive, animated cadaver who wanders the world, trying to discover his true identity. He rose from an ancient Shuriman tomb bound in corpse wrappings with no knowledge of his past, consumed with an uncontrollable sadness.",
    "champion_id": 32,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Tantrum.png",
    "q_name": "Bandage Toss",
    "passive_name": "Cursed Touch",
    "e_description": "Permanently reduces the physical damage Amumu would take. Amumu can unleash his rage, dealing damage to surrounding enemies. Each time Amumu is hit, the cooldown on Tantrum is reduced by 0.5 seconds.",
    "recommended_items": [
      1001,
      1054,
      3068,
      1028,
      3010
    ],
    "r_name": "Curse of the Sad Mummy",
    "r_description": "Amumu entangles surrounding enemy units in bandages, damaging them and rendering them unable to attack or move.",
    "name": "Amumu",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BandageToss.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AuraofDespair.png",
    "q_description": "Amumu tosses a sticky bandage at a target, stunning and damaging the target while he pulls himself to them.",
    "title": "the Sad Mummy",
    "e_name": "Tantrum",
    "w_description": "Overcome by anguish, nearby enemies lose a percentage of their maximum Health each second.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Amumu.png",
    "recommended_item_names": [
      "Boots of Speed",
      "Doran's Shield",
      "Sunfire Cape",
      "Ruby Crystal",
      "Catalyst the Protector"
    ],
    "w_name": "Despair",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CurseoftheSadMummy.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/SadMummy_CorpseExplosion.png",
    "passive_description": "Amumu's attacks reduce the target's Magic Resistance for a short duration."
  },
  "33": {
    "lore": "The mysteries that surround Rammus are numerous. How did a simple creature of the desert suddenly become able to reason? How did he craft his vaunted suit of armor? What is he searching for as he crosses the Shuriman desert? One thing is for certain: trying to stop the inexorable Rammus is a fool's mission.",
    "champion_id": 33,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PuncturingTaunt.png",
    "q_name": "Powerball",
    "passive_name": "Spiked Shell",
    "e_description": "Rammus taunts an enemy champion or monster into a reckless assault against Rammus' hard shell, reducing Armor temporarily.",
    "recommended_items": [
      3047,
      2003,
      3025,
      1039,
      2041,
      3117,
      3143
    ],
    "r_name": "Tremors",
    "r_description": "Rammus creates waves of destruction pulsing through the ground, causing damage to units and structures near him.",
    "name": "Rammus",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PowerBall.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DefensiveBallCurl.png",
    "q_description": "Rammus accelerates in a ball towards his enemies, dealing damage and slowing targets affected by the impact.",
    "title": "the Armordillo",
    "e_name": "Puncturing Taunt",
    "w_description": "Rammus goes into a defensive formation, vastly increasing his Armor and Magic Resist, while returning damage to attacks.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Rammus.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Iceborn Gauntlet",
      "Hunter's Machete",
      "Crystalline Flask",
      "Boots of Mobility",
      "Randuin's Omen"
    ],
    "w_name": "Defensive Ball Curl",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Tremors2.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Armordillo_ScavengeArmor.png",
    "passive_description": "Rammus gains additional damage as his shell becomes reinforced, converting 25% of his Armor into Attack Damage."
  },
  "34": {
    "lore": "Anivia is a being of the coldest winter, a mystical embodiment of ice magic, and an ancient protector of the Freljord. She commands all the power and fury of the land itself, calling the snow and bitter wind to defend her home from those who would harm it. A benevolent but mysterious creature, Anivia is eternally bound to keep vigil over the Freljord through life, death, and rebirth.\n\nAnivia is as much a part of the Freljord as the never-ending frost. Long before mortals had ever set foot on the land's frigid tundra, she had lived countless lifetimes and died as many deaths. The beginnings and ends of her eternal cycle always heralded great change, from the calming of raging storms to the ebb and flow of ice ages. It is said that when the cryophoenix dies, an era ends; and when she is reborn, a new era begins.\n\nThough Anivia's past lifetimes have faded from her memory, she knows her purpose: she must protect the Freljord at all costs.\n\nWhen she was last reborn, Anivia witnessed the rise of a mighty and united human tribe. She guarded their lands with pride as they prospered, but such unity could not last forever. The great tribe fractured into three, and after that upheaval, Anivia watched the people of the Freljord become embroiled in battle. As she strove to calm the turmoil tearing her home apart, Anivia began to sense a greater threat: an ancient evil growing deep within the earth. To her horror, she felt the pure magic of the ice itself become blackened and corrupt. Like blood in water, darkness crept into the Freljord. With her destiny so tied to the power of the land, Anivia knew if such evil took root in her home, that same darkness would find its way into her heart. She could no longer remain a mere guardian - the cryophoenix had to act.\n\nAnivia soon discovered an ally in Ashe, the Frost Archer. Ashe too believed in unification as an end to the Freljord's perpetual strife, and Anivia offered the tribal leader her aid. Now, with war on the horizon, Anivia prepares to fight for peace, but she knows the inevitable truth of her destiny. One day, evil will rise from the ice, and she must destroy it - no matter the cost.\n\n''I am the fury of the blizzard, the bite of the wind, and the cold of the ice. I am the Freljord.''\n-- Anivia",
    "champion_id": 34,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Frostbite.png",
    "q_name": "Flash Frost",
    "passive_name": "Rebirth",
    "e_description": "With a flap of her wings, Anivia blasts a freezing gust of wind at her target, dealing a medium amount of damage. If the target has been slowed by Flash Frost or Glacial Storm, the damage they take is doubled.",
    "recommended_items": [
      1001,
      1056,
      3028,
      3151,
      1004
    ],
    "r_name": "Glacial Storm",
    "r_description": "Anivia summons a driving rain of ice and hail to damage her enemies and slow their advance.",
    "name": "Anivia",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FlashFrost.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Crystallize.png",
    "q_description": "Anivia brings her wings together and summons a sphere of ice that flies towards her opponents, chilling and damaging anyone in its path. When the sphere explodes it does moderate damage in a radius, stunning anyone in the area.",
    "title": "the Cryophoenix",
    "e_name": "Frostbite",
    "w_description": "Anivia condenses the moisture in the air into an impassable wall of ice to block all movement. The wall only lasts a short duration before it melts.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Anivia.png",
    "recommended_item_names": [
      "Boots of Speed",
      "Doran's Ring",
      "Chalice of Harmony",
      "Liandry's Torment",
      "Faerie Charm"
    ],
    "w_name": "Crystallize",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GlacialStorm.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Cryophoenix_Rebirth.png",
    "passive_description": "Upon dying, Anivia will revert into an egg. If the egg can survive for six seconds, she is gloriously reborn."
  },
  "35": {
    "lore": "Most would say that death isn't funny. It isn't, unless you're Shaco - then it's hysterical. He is Valoran's first fully functioning homicidal comic; he jests until someone dies, and then he laughs. The figure that has come to be known as the Demon Jester is an enigma. No one fully agrees from whence he came, and Shaco never offers any details on his own. A popular belief is that Shaco is not of Runeterra - that he is a thing summoned from a dark and twisted world. Still others believe that he is the demonic manifestation of humanity's dark urges and therefore cannot be reasoned with. The most plausible belief is that Shaco is an assassin for hire, left to his own lunatic devices until his services are needed. Shaco certainly has proven himself to be a cunning individual, evading authorities at every turn who might seek him for questioning for some horrendous, law-breaking atrocity. While such scuttlebutt might reassure the native inhabitants of Valoran, it seems unimaginable that such a malfeasant figure is allowed to remain at large.\n\nWhatever the truth of his history might be, Shaco has joined the League of Legends for reasons only he knows. He is a terrifying figure, typically shunned by both his fellow champions and the media at large. Only the summoners in the Institute of War know why such a creature was allowed into the League, but most Runeterrans suspect it to be a means that allows the power that be to keep an eye on the ever-elusive Shaco. Unsurprisingly, this champion is popular in places where madness can openly reign, such as among the power-hungry summoners of Zaun and Noxus.\n\nWhatever you do, don't tell him you missed the punch line.",
    "champion_id": 35,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TwoShivPoison.png",
    "q_name": "Deceive",
    "passive_name": "Backstab",
    "e_description": "Shaco's Shivs passively poison targets on hit, slowing them and applying a miss chance to minions and monsters. He can throw his Shivs to deal damage and poison the target.",
    "recommended_items": [
      2003,
      3026,
      1039,
      1055,
      3006,
      3031
    ],
    "r_name": "Hallucinate",
    "r_description": "Shaco creates an illusion of himself near him, which can attack nearby enemies. (Deals half damage to turrets.)  Upon death, it explodes, dealing damage to nearby enemies. ",
    "name": "Shaco",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Deceive.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JackInTheBox.png",
    "q_description": "Shaco becomes invisible and teleports to target location. His next attack is guaranteed to critically strike.",
    "title": "the Demon Jester",
    "e_name": "Two-Shiv Poison",
    "w_description": "Shaco creates an invisible, animated Jack-in-the-Box, which will fear, and then attack, nearby enemies.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Shaco.png",
    "recommended_item_names": [
      "Health Potion",
      "Guardian Angel",
      "Hunter's Machete",
      "Doran's Blade",
      "Berserker's Greaves",
      "Infinity Edge"
    ],
    "w_name": "Jack In The Box",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HallucinateFull.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Jester_CarefulStrikes.png",
    "passive_description": "Shaco deals 20% bonus damage when striking a unit from behind."
  },
  "36": {
    "lore": "It is said that the man now known as Dr. Mundo was born without any sort of conscience.  Instead, he had an unquenchable desire to inflict pain through experimentation. By the time he was five, most of the pets in the Zaun neighborhood where Mundo grew up had gone missing. By his teenage years, his parents were nowhere to be found. By the time he had legally acquired his license to practice medicine, he had been acquitted of thirty-eight separate charges of murder by the Zaun authorities; the lack of evidence made prosecution impossible.\n\nDr. Mundo has become equal parts serial killer and mad scientist, though no one is entirely sure how his butchery qualifies as science. However, he has made tremendous strides in mapping the pain response in the human brain and body, going so far as being able to suppress it, even in the most excruciating of circumstances. He has also tapped into the primal parts of the brain through chemistry, learning how to enhance aggression and adrenaline, as well as dulling conscience and the survival instinct. In short, Dr. Mundo's life's work has been how to create the perfect science-enhanced killer.  Unfortunately, the city-state of Noxus regards such behavior as a sign of initiative and ambition, rather than inhumanity. Originally fighting for Zaun, Dr. Mundo was recruited to also fight for Noxus in the League of Legends; the Madman dual faction status represents the fruits of a blossoming relationship between Zaun and Noxus. He continues his experiments to this day, even using himself as an experimental subject, as evidenced by his disfigured appearance and his... unique manner of speaking. There are rumors that the High Command in Noxus has given him free reign to pursue his life's work in his spare time.\n\nBeware the Madman of Zaun. In his eyes, you are already dead.",
    "champion_id": 36,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Masochism.png",
    "q_name": "Infected Cleaver",
    "passive_name": "Adrenaline Rush",
    "e_description": "Masochism increases Dr. Mundo's Attack Damage by a flat amount for 5 seconds. In addition, Dr. Mundo also gains an additional amount of Attack Damage for each percentage of Health he is missing.",
    "recommended_items": [
      3047,
      2003,
      1039,
      1054,
      3143,
      3151
    ],
    "r_name": "Sadism",
    "r_description": "Dr. Mundo sacrifices a portion of his Health for increased Movement Speed and drastically increased Health Regeneration.",
    "name": "Dr. Mundo",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/InfectedCleaverMissileCast.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BurningAgony.png",
    "q_description": "Dr. Mundo hurls his cleaver, dealing damage equal to a portion of his target's current Health and slowing them for a short time. Dr. Mundo delights in the suffering of others, so he is returned half of the Health cost when he successfully lands a cleaver.",
    "title": "the Madman of Zaun",
    "e_name": "Masochism",
    "w_description": "Dr. Mundo drains his Health to reduce the duration of disables and deal continual damage to nearby enemies.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/DrMundo.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Doran's Shield",
      "Randuin's Omen",
      "Liandry's Torment"
    ],
    "w_name": "Burning Agony",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Sadism.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/DrMundo_AdrenalineRush2.png",
    "passive_description": "Dr. Mundo regenerates 0.3% of his maximum Health each second."
  },
  "37": {
    "lore": "Sona has no memories of her true parents. As an infant, she was found abandoned on the doorstep of an Ionian adoption house, nestled atop an ancient instrument in an exquisite case of unknown origins. She was an unusually well-behaved child, always quiet and content. Her caretakers were sure she would find a home quickly, but it soon became apparent that what they mistook for uncommon geniality was actually an inability to speak or to produce any sound whatsoever. Sona remained at the adoption house until her teens, watching in hopeless silence as prospective adopters passed her by. During this time, the caretakers sold her unusual instrument to anxious collectors, hoping to build her a trust. For a myriad of bizarre and unexpected reasons, however, it would be returned, or simply appear again outside the house.\n\nWhen a wealthy Demacian woman named Lestara Buvelle learned of the instrument, she immediately embarked to Ionia. When the caretakers showcased the instrument for her, she rose wordlessly and explored the house, stopping outside Sona's room. Without hesitation, Lestara adopted her and left a generous donation for the instrument. With Lestara's guidance, Sona discovered a deep connection with the instrument which Lestara called an 'etwahl'. In her hands, it played tones which stilled or quivered the hearts of those around her. Within months, she was headlining with the mysterious etwahl for sold-out audiences. She played as though plucking heartstrings, effortlessly manipulating the emotions of her listeners - all without a single written note. In secret, she discovered a potent and deadly use for her etwahl, using its vibrations to slice objects from a distance. She honed this discipline in private, mastering her gift. When she felt prepared, she went to the only place which could offer her a fitting recital: the League of Legends.\n\n''Her melody moves the soul, her silence sunders the body.''\n-- Jericho Swain, after attending her concert",
    "champion_id": 37,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SonaE.png",
    "q_name": "Hymn of Valor",
    "passive_name": "Power Chord",
    "e_description": "Sona plays the Song of Celerity, granting herself bonus Movement Speed that decays over time. Sona gains a temporary aura that grants nearby allied champions bonus Movement Speed and extends the duration of her aura for each ally she aids.",
    "recommended_items": [
      1001,
      1056,
      3151,
      1028,
      3010
    ],
    "r_name": "Crescendo",
    "r_description": "Sona plays her ultimate chord, stunning enemy champions and forcing them to dance and dealing magic damage to them. Each rank increases the power of all aura effects.",
    "name": "Sona",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SonaQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SonaW.png",
    "q_description": "Sona plays the Hymn of Valor, sends out bolts of sound, dealing magic damage to two nearby enemies, prioritizing champions and monsters. Sona gains a temporary aura that grants allies tagged by the zone bonus damage on their next attack against enemies and extends the duration of her aura for each ally she aids.",
    "title": "Maven of the Strings",
    "e_name": "Song of Celerity",
    "w_description": "Sona plays the Aria of Perseverance, sending out protective melodies, healing Sona and a nearby wounded ally. Sona gains a temporary aura that grants allies tagged by the zone a temporary shield and extends the duration of her aura for each ally she aids.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Sona.png",
    "recommended_item_names": [
      "Boots of Speed",
      "Doran's Ring",
      "Liandry's Torment",
      "Ruby Crystal",
      "Catalyst the Protector"
    ],
    "w_name": "Aria of Perseverance",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SonaR.png",
    "role": "Support",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Sona_Passive_Charged.png",
    "passive_description": "After casting 3 spells, Sona's next attack deals bonus magic damage in addition to a bonus effect depending on what song Sona last activated."
  },
  "38": {
    "lore": "There is a place between dimensions and between worlds. To some it is known as the Outside, to others it is the Unknown. To most, however, it is called the Void. Despite its name, the Void is not an empty place, but rather the home of unspeakable things, horrors not meant for minds of men. Though such knowledge is lost in modern times, there are those who have unwittingly discovered what lies beyond, and they have been unable to turn away. Kassadin is such a creature. He was once a man forced to look upon the face of the Void and forever changed by what he saw. Once a seeker of forbidden knowledge, he discovered that what he sought was something else entirely. He is one of the few that has found his way to forgotten Icathia and lived to tell the tale, following the scant breadcrumbs hidden in ancient texts.\n\nWithin a decaying cyclopean city, Kassadin found secrets of the kind that he will never share - secrets that made him quake with fear at the visions of things to come that were thrust upon him. The power of the place threatened to consume him forever, but Kassadin took the only route available to him in order to survive - he let the Void inside him. Miraculously, he was able to overcome the alien urges that went with it, and he emerged as something more than human. Though a part of him died that day, he knows that he must protect Valoran from the things scratching at the door, waiting to get in and visit their torments upon the world. They are only one step away... something to which the appearance of the abomination known as Cho'Gath attests.\n\nIf you look upon the Void, you can't put it behind you. If you look upon Kassadin, he is probably already there.",
    "champion_id": 38,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ForcePulse.png",
    "q_name": "Null Sphere",
    "passive_name": "Void Stone",
    "e_description": "Kassadin draws energy from spells cast in his vicinity. Upon charging up, Kassadin can use Force Pulse to damage and slow enemies in a cone in front of him.",
    "recommended_items": [
      3070,
      2003,
      2041,
      3110,
      3003
    ],
    "r_name": "Riftwalk",
    "r_description": "Kassadin teleports to a nearby location dealing damage to nearby enemy units. Multiple Riftwalks in a short period of time cost additional Mana but also deal additional damage.",
    "name": "Kassadin",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NullLance.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NetherBlade.png",
    "q_description": "Kassadin fires an orb of void energy at a target, dealing damage and interrupting channels. The excess energy forms around himself, granting a temporary shield that absorbs magic damage.",
    "title": "the Void Walker",
    "e_name": "Force Pulse",
    "w_description": "Passive: Kassadin's basic attacks deal bonus magic damage. Active: Kassadin's next basic attack deals significant bonus magic damage and restores Mana.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Kassadin.png",
    "recommended_item_names": [
      "Tear of the Goddess",
      "Health Potion",
      "Crystalline Flask",
      "Frozen Heart",
      "Archangel's Staff"
    ],
    "w_name": "Nether Blade",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RiftWalk.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Voidwalker_Netherburn.png",
    "passive_description": "Kassadin takes 15% reduced magic damage and ignores unit collision."
  },
  "39": {
    "lore": "The Ionians have developed some of the most breathtaking and deadly martial arts on all of Runeterra - just one manifestation of their pursuit of enlightenment. The most remarkable blade style to emerge, however, was the unusual byproduct of foreign intervention. Master Lito was a swordsman whose teachings were sought by ruling classes from nearly every city-state. His art was a highly-guarded secret, but it was said that swords would breathe in his grasp. He withered unexpectedly from a mysterious disease which baffled the brightest of Runeterran physicians. When he died, he left behind Zelos and Irelia, his son and daughter, and a truly unique weapon. Zelos became a sergeant in the Ionian military and left to seek assistance from Demacia immediately prior to Noxus' invasion of Ionia. Irelia, charged with the protection of their home until Zelos returned, was alone when the Noxian forces struck.\n\nThe Ionians fought admirably, but soon Ionian blood stained the land beneath the prints of foreign boots. At the Great Stand of the Placidium, Ionians prepared for surrender, but were inspired to maintain their resistance when the young Irelia lifted her father's enormous blade and pledged to hold until her brother returned. In the chaos of the ensuing fight, Irelia was cursed with dark Noxian Necromancy. As her life ebbed, Soraka, the Starchild, made a final attempt to anchor her fading soul. Unwilling to relinquish her home, Irelia rose at the brink of death, and her father's sword lifted in the air alongside her. Irelia rushed back to the fore, unfazed by the blade's sudden animation. The weapon danced around her effortlessly, cutting down Noxians as they gaped in horror. The decimated invaders were forced to retreat from the Placidium. Irelia was appointed Ionia's Captain of the Guard, and when the defense of her homeland moved to the Fields of Justice, so did she.\n\n'The sword flourishes, as though painting with blood.'\n-- Taken from a Noxian Field Report",
    "champion_id": 39,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/IreliaEquilibriumStrike.png",
    "q_name": "Bladesurge",
    "passive_name": "Ionian Fervor",
    "e_description": "Irelia's attack balances the scales, dealing damage and slowing the target. However, if the target has a higher Health % than Irelia, then the blow stuns the target instead of slowing.",
    "recommended_items": [
      3047,
      2003,
      1039,
      2041,
      3143,
      3153
    ],
    "r_name": "Transcendent Blades",
    "r_description": "Irelia summons 4 spirit blades that she can fling to deal physical damage and siphon life from enemies they pass through.",
    "name": "Irelia",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/IreliaGatotsu.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/IreliaHitenStyle.png",
    "q_description": "Irelia dashes forward to strike her target. If it kills the target, Bladesurge's cooldown refreshes and refunds 35 Mana.",
    "title": "the Will of the Blades",
    "e_name": "Equilibrium Strike",
    "w_description": "Irelia is skilled in the art of Hiten, passively giving her physical attacks Health restoration. Activating Hiten Style doubles her Health restoration and gives her basic attacks true damage.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Irelia.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Crystalline Flask",
      "Randuin's Omen",
      "Blade of the Ruined King"
    ],
    "w_name": "Hiten Style",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/IreliaTranscendentBlades.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Irelia_IonianFervor.png",
    "passive_description": "Reduces the duration of all disables for each nearby enemy champion.<br><br>1 Champion: 10%<br>2 Champions: 25%<br>3 Champions: 40%"
  },
  "40": {
    "lore": "There are those sorcerers who give themselves over to the primal powers of nature, forgoing the learned practice of magic. Such a sorceress is Janna, who first learned magic as an orphan growing up amidst the chaos that is the city-state of Zaun. Janna eked out what living she could on the streets. Life was tough and dangerous for the beautiful young girl, and she survived by her wits, and by stealing when wits weren't enough. The rampant magic that characterizes Zaun was the first and most alluring tool which Janna realized could both protect and elevate her. Janna discovered that she had an affinity for a particular type of magic - the elemental magic of air. She mastered her studies of air magic in a matter of months, almost as if she was born of it. Janna went from a street vagrant to an avatar of the air virtually overnight, stunning and surpassing those who taught her. Such a rapid ascension also changed her physical appearance, giving her an otherworldly look.\n\nSeeking to right the injustice in the world (particularly the insanity that has become the city of Zaun), Janna has brought her talents to the League. She is a voice for the regulation of magical experimentation and a supporter of the development of techmaturgy, making her an indirect ally of the city-state of Piltover and the amazing techmaturgical minds that live there. Janna is also a new favorite of the League's many fans. She is often the center of attention at functions, fan appreciation days, and other celebratory events. There is something untouchable about Janna, however, and her affections can change as quickly as the wind.\n\nDo not be captivated by Janna's beauty. Like the wind, she is one gust away from terrible destruction.",
    "champion_id": 40,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EyeOfTheStorm.png",
    "q_name": "Howling Gale",
    "passive_name": "Tailwind",
    "e_description": "Janna conjures a defensive gale that shields an ally champion or turret from incoming damage and increases their Attack Damage.",
    "recommended_items": [
      2003,
      3301,
      3190,
      3117,
      3041
    ],
    "r_name": "Monsoon",
    "r_description": "Janna surrounds herself in a magical storm, throwing enemies back. After the storm has settled, soothing winds heal nearby allies while the ability is active.",
    "name": "Janna",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HowlingGale.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SowTheWind.png",
    "q_description": "By creating a localized change in pressure and temperature, Janna is able to create a small storm that grows in size with time. She can activate the spell again to release the storm. On release this storm will fly towards the direction it was cast in, dealing damage and knocking away any enemies in its path.",
    "title": "the Storm's Fury",
    "e_name": "Eye Of The Storm",
    "w_description": "Janna summons an air elemental that passively increases her Movement Speed and enables her to pass through units. She may also activate this ability to deal damage and slow an enemy's Movement Speed. The passive is lost while this ability is on cooldown.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Janna.png",
    "recommended_item_names": [
      "Health Potion",
      "Ancient Coin",
      "Locket of the Iron Solari",
      "Boots of Mobility",
      "Mejai's Soulstealer"
    ],
    "w_name": "Zephyr",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ReapTheWhirlwind.png",
    "role": "Support",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Janna_Tailwind.png",
    "passive_description": "Increases the Movement Speed of all allied champions by 5%."
  },
  "41": {
    "lore": "Gangplank was born the son of the dread pirate captain Vincent the Shadow - one of the most wealthy and feared pirates in all of Blue Flame Island. One might think this would have spoiled the boy with a cushioned life of privilege, but the truth is quite the opposite. Growing up in the city of Bilgewater isn't easy; pirates are not known for their compassion, and that most certainly extends to their families. Vincent wanted his son to grow up tough and strong, so he was extremely hard on the young Gangplank. Even as a child, Gangplank was as mean as a snake and is said to have slept with his eyes open. As he grew, the young man rapidly became the most ruthless and feared pirate in all of Bilgewater, and his daddy was never more proud than on the day of his son's eighteenth birthday - when Gangplank stabbed his old man in the back and claimed the famed pirate ship, the Dead Pool, for his own.\n\nThe continent of Valoran, however, is a dangerous place for pirates; Gangplank could read the writing on the wall. The den of pirates known as Bilgewater would soon be pulled down by the undertow of Valoranian politics and the Institute of War. It was time for Bilgewater to have their own champion to represent them in the League of Legends, and who better than the fiercest pirate of them all? It is said that Gangplank has enough power and favor to claim the title of the Pirate King back home, but that he is simply biding his time and building his reputation as a champion before he returns to a life of piracy.\n\nYo ho, blow the man down. Or at least shoot him when his back is turned and steal all his booty.",
    "champion_id": 41,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RaiseMorale.png",
    "q_name": "Parrrley",
    "passive_name": "Grog-Soaked Blade",
    "e_description": "Gangplank fires a shot into the air, increasing nearby allied champions' Attack Damage and Movement Speed.",
    "recommended_items": [
      3078,
      3047,
      2003,
      3025,
      2041
    ],
    "r_name": "Cannon Barrage",
    "r_description": "Gangplank signals his ship to fire upon an area, slowing enemies and dealing damage within the area.",
    "name": "Gangplank",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Parley.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RemoveScurvy.png",
    "q_description": "Gangplank takes aim and shoots an enemy unit with his pistol. If Parrrley deals a killing blow, he gains extra gold and half the Mana cost is refunded.",
    "title": "the Saltwater Scourge",
    "e_name": "Raise Morale",
    "w_description": "Consumes a large quantity of citrus fruit which clears any crowd control effects on him and heals him.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Gangplank.png",
    "recommended_item_names": [
      "Trinity Force",
      "Ninja Tabi",
      "Health Potion",
      "Iceborn Gauntlet",
      "Crystalline Flask"
    ],
    "w_name": "Remove Scurvy",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CannonBarrage.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Pirate_GrogSoakedBlade.png",
    "passive_description": "Gangplank's basic attacks and Parrrley apply a poison that deals magic damage each second and slows Movement Speed. Lasts 3 seconds and stacks up to 3 times."
  },
  "42": {
    "lore": "When Heimerdinger and his yordle colleagues migrated to Piltover, they embraced science as a way of life, and they immediately made several groundbreaking contributions to the techmaturgical community. What yordles lack in stature, they make up for with industriousness. Corki, the Daring Bombardier, gained his title by test-piloting one of these contributions - the original design for the Reconnaissance Operations Front-Line Copter, an aerial assault vehicle which has become the backbone of the Bandle City Expeditionary Force (BCEF). Together with his squadron - the Screaming Yipsnakes - Corki soars over Valoran, surveying the landscape and conducting aerial acrobatics for the benefit of onlookers below.\n\nCorki is the most renowned of the Screaming Yipsnakes for remaining cool under fire and exhibiting bravery to the point of madness. Before the League, he served several tours of duty, often volunteering for missions that would take him behind enemy lines, either gathering intelligence or delivering messages through hot zones. He thrived on danger, and enjoyed nothing more than a good dogfight in the morning. More than just an ace pilot, Corki also made several modifications to his copter, outfitting it with an arsenal of weapons which some speculate were more for show than functionality. When open hostilities ceased as part of the agreement surrounding the formation of the League, Corki was forced into a retirement, which he felt ''cut the engines and clipped the wings''. He tried to make do with stunt flying and canyon running, but it was never the same without the refreshing smell of gunpowder streaking through the air around him. When Heimerdinger joined the League of Legends, it was no surprise to see Corki follow soon after, eager to test his mettle against the best the world has to offer.\n\nHe is Corki - death from above!",
    "champion_id": 42,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GGun.png",
    "q_name": "Phosphorus Bomb",
    "passive_name": "Hextech Shrapnel Shells",
    "e_description": "Corki's gatling gun rapidly fires in a cone in front of him, dealing damage and reducing enemy Armor.",
    "recommended_items": [
      2003,
      3035,
      3026,
      1055,
      3020
    ],
    "r_name": "Missile Barrage",
    "r_description": "Corki fires a missile toward his target location that explodes on impact, dealing damage to enemies in an area. Corki stores missiles over time, up to a maximum. Every 3rd missile fired will be a Big One, dealing extra damage.",
    "name": "Corki",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PhosphorusBomb.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CarpetBomb.png",
    "q_description": "Corki fires a flash bomb at a target location, dealing magic damage to enemies in the area. This attack additionally reveals units in the area for a duration.",
    "title": "the Daring Bombardier",
    "e_name": "Gatling Gun",
    "w_description": "Corki surges to target location, dropping bombs that create a trail of destruction for opponents who remain in the fire.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Corki.png",
    "recommended_item_names": [
      "Health Potion",
      "Last Whisper",
      "Guardian Angel",
      "Doran's Blade",
      "Sorcerer's Shoes"
    ],
    "w_name": "Valkyrie",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MissileBarrage.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Corki_RapidReload.png",
    "passive_description": "Corki's basic attacks deal bonus true damage to minions, monsters, and champions."
  },
  "43": {
    "lore": "Karma is a woman of indomitable will and unbound spiritual power. She is the soul of Ionia made manifest and an inspiring presence on the battlefield, shielding her allies and turning back her foes. A strong leader torn between tradition and revolution, Karma seeks to protect the peace of Ionia - by force if necessary.\n\nKarma once lived a tranquil life in a small Ionian village. Led by elder monks, the villagers practiced a tradition of benevolent magic and pacifism. Known for her powerful connection to the spiritual realm and beloved as a just mediator amongst her people, Karma embraced these traditions as an essential aspect of the enlightenment sought by all Ionians. \n\nHer inner peace was tested when the armies of Noxus invaded Ionia. While the village's elder monks insisted their peaceful ways would spare them from violence, Karma had heard enough tales of Noxian cruelty to openly question the elders' wisdom. Stern and unmoving, they told her to trust in tradition. When the invaders marched on the village, the elder monks rode out to negotiate a bloodless end to the battle. The Noxian general was offended by their show of weakness and slaughtered the monks himself as he ordered his soldiers to strike the village.\n\nAs the Noxians advanced, the villagers prepared to accept death, bound to their peaceful vows. But Karma would not accept death and instead saw another way: sacrificing a single life to spare many others. To save her people, she drew upon the power within and summoned the full force of her will. A burst of spirit fire emerged from her body and spiraled towards the Noxian general. The flame took the form of twin dragons, the symbol of Ionia itself. It was the first time Karma had ever used her powers to harm instead of protect, and neither she nor the villagers had ever seen anything like it. When the magic subsided, the general had fallen before her and his soldiers had scattered. The opposing forces surrendered to Karma's strength leaving her people, and their traditions, untouched. \n\nWhile the war raged on, Karma became a formidable leader of the Ionian resistance, but the conflict did not end when Noxus's armies fled the Ionian shores. Ionia became divided between the resistance fighters who craved vengeance and the monks who demanded a return to spiritual tradition. Karma saw a third path, one that combined the strength Ionia found in war with the peaceful traditions the nation still held dear. She now seeks to return her ravaged land to an enduring peace.\n\n''Your spirit is something no one can take from you. Use it wisely.'' \n-- Karma",
    "champion_id": 43,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KarmaSolKimShield.png",
    "q_name": "Inner Flame",
    "passive_name": "Gathering Fire",
    "e_description": "Karma summons a protective shield that absorbs incoming damage and increases the Movement Speed of the protected ally.\n\nMantra Bonus: In addition to casting the shield, energy radiates out from the shield, dealing damage to enemies and applying Inspire to allied champions.",
    "recommended_items": [
      2003,
      3303,
      3174,
      3151,
      3020
    ],
    "r_name": "Mantra",
    "r_description": "Karma empowers her next ability to do an additional effect. Mantra is available at level 1 and does not require a skill point.",
    "name": "Karma",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KarmaQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KarmaSpiritBind.png",
    "q_description": "Karma sends forth a ball of spirit energy that explodes and deals damage upon hitting an enemy unit.\n\nMantra Bonus: In addition to the explosion, Mantra increases the destructive power of her Inner Flame, creating a cataclysm which deals damage after a short delay.",
    "title": "the Enlightened One",
    "e_name": "Inspire",
    "w_description": "Karma creates a tether between herself and a targeted enemy, dealing damage over time and revealing them. If the tether is not broken, the enemy will be rooted.\n\nMantra Bonus: Karma strengthens the link, dealing bonus damage and healing.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Karma.png",
    "recommended_item_names": [
      "Health Potion",
      "Spellthief's Edge",
      "Athene's Unholy Grail",
      "Liandry's Torment",
      "Sorcerer's Shoes"
    ],
    "w_name": "Focused Resolve",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KarmaMantra.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Karma_Passive.png",
    "passive_description": "Reduces Mantra's cooldown each time Karma damages an enemy champion with one of her abilities (Half-effect for Karma's basic attacks)"
  },
  "44": {
    "lore": "There is a form of magic unknown to many Runeterrans and discredited by the few who are even aware of its existence. It is the magic of the earth, drawing power from the resonance of crystals and gems. Taric, the Gem Knight, is Runeterra's sole practitioner of this form of magic, having been erratically summoned to Runeterra from a faraway world. Back home, Taric's father was a distinguished healer in their home city. Taric was always interested in his father's pursuits, even from a young age. Despite his burgeoning understanding of herbs, plants, and animal medicines, it was the power of gems that most fascinated the growing boy. It wasn't long before Taric had exhausted his father's coveted library and set out on a path of his own. He wanted to help the people, but not by simply salving their wounds and curing their woes. He wasn't to be a healer, but a defender - one who used the power of earth to preserve and protect.\n\nTaric became a wandering knight, renowned across his homeland as a guardian of the just until the day a spell of summoning grabbed him from his home and deposited him on Runeterra. Though disoriented and confused at first, he now feels that the continent of Valoran is in need of someone like him. Despite missing his homeland, Taric is happy to fight in the League, serving as a protector for all who seek one. His neat and stylish appearance combined with his shiny bejeweled armor and weapons have rapidly made him a celebrity champion of the League of Legends. Valoran's media, for some reason, has taken a great interest in his personal life. While open about his life as a champion and gracious in all things, Taric is tight-lipped about his life outside the League and prefers his privacy.\n\nAs Taric's father taught him, every stone has its meaning. For Taric's enemies, they all mean trouble.",
    "champion_id": 44,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Dazzle.png",
    "q_name": "Imbue",
    "passive_name": "Gemcraft",
    "e_description": "Taric emits a brilliant ball of prismatic light from his gemmed shield, stunning his target and damaging them based on how close he is to them.",
    "recommended_items": [
      3047,
      2003,
      3025,
      3302,
      3110
    ],
    "r_name": "Radiance",
    "r_description": "Taric slams his hammer into the ground to deal damage to nearby enemies. For a time after, Taric's gems radiate energy, empowering Taric and his allies with bonus Attack Damage and Ability Power.",
    "name": "Taric",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Imbue.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Shatter.png",
    "q_description": "Taric brings forth earthen energy to heal an ally and himself. This heal is more potent when Taric heals only himself.",
    "title": "the Gem Knight",
    "e_name": "Dazzle",
    "w_description": "Taric is protected by a hardening aura, increasing the Armor of himself and nearby allied champions. He may choose to splinter the enchanted rocks surrounding him to deal damage and decrease the Armor of nearby enemies at the cost of some Armor for a short time.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Taric.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Iceborn Gauntlet",
      "Relic Shield",
      "Frozen Heart"
    ],
    "w_name": "Shatter",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TaricHammerSmash.png",
    "role": "Support",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/GemKnight_Gemcraft.png",
    "passive_description": "After casting a spell, Taric's next basic attack deals bonus magic damage based on his Armor and reduces his cooldowns."
  },
  "45": {
    "lore": "To most, thoughts of yordles do not conjure images to be feared. The easygoing half-pint race, though fierce, is often regarded with some degree of joviality. Their high-pitched voices and naturally cute forms inspire something of a protective instinct in the larger races, or at least bring to mind images of children playing at being adults. Every now and again, however, a yordle turns so bad that even at its small stature it strikes terror into the hearts of others. Veigar is one such twisted yordle. As a master of the magical black arts, as well as a corrupter of cosmic energy, he is one of the most powerful sorcerers on Valoran.\n\nAs a child, Veigar was a normal yordle with one small exception - he had a deep curiosity for the world beyond Bandle City. The young yordle spent much of his time studying the rest of Valoran, and he jumped at the chance to join a business that traded with other major city-states. Unfortunately for both him and the world, a deal with Noxian trader turned into shady business and went bad; Veigar and his companions were subsequently set up to take the fall. Arrested by the authorities, he was imprisoned within the walls of Noxus for years. Such isolation is very dangerous for yordles - undoubtedly why his cruel jailers did such a thing - and Veigar was slowly driven mad.\n\nHe eventually escaped, having become a twisted version of his former self. Instead of returning to his people and Bandle City, he sought tutelage from dark wizards across the land. With his demented will focused on one task, he quickly became a dangerous and powerful wizard in his own right. Now he seeks to end all conflict on Valoran by bringing all of the city-states to their knees, regardless of their affiliation. The League of Legends is the perfect tool to help him meet his ends - for now.\n\nWho says evil needs to come in a fearsome-looking package?",
    "champion_id": 45,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VeigarEventHorizon.png",
    "q_name": "Baleful Strike",
    "passive_name": "Equilibrium",
    "e_description": "Veigar twists the edges of space around the target location for 3 seconds, stunning enemies who pass through the perimeter.",
    "recommended_items": [
      2003,
      3174,
      1056,
      3003,
      3020
    ],
    "r_name": "Primordial Burst",
    "r_description": "Blasts target enemy champion, dealing a large base amount of Magic Damage plus 80% of his target's Ability Power.",
    "name": "Veigar",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VeigarBalefulStrike.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VeigarDarkMatter.png",
    "q_description": "Unleashes dark energy at target enemy, dealing Magic Damage. If a unit is killed, Veigar gains some Ability Power permanently.",
    "title": "the Tiny Master of Evil",
    "e_name": "Event Horizon",
    "w_description": "Veigar calls a great mass of dark matter to fall from the sky to the target location, dealing Magic Damage when it lands.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Veigar.png",
    "recommended_item_names": [
      "Health Potion",
      "Athene's Unholy Grail",
      "Doran's Ring",
      "Archangel's Staff",
      "Sorcerer's Shoes"
    ],
    "w_name": "Dark Matter",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VeigarPrimordialBurst.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Veigar_Entropy.png",
    "passive_description": "Veigar's Mana Regen is increased by 1% for each 1% of Mana missing."
  },
  "48": {
    "lore": "Trundle is a hulking and devious troll with a mischievous streak. There is nothing he can't beat into submission and bend to his will, not even the ice itself. With his massive, frozen club, he chills his enemies to the core and runs them through with jagged shards of ice. Fiercely territorial, Trundle chases down anyone foolish enough to enter his domain and laughs as they bleed onto the tundra.\n\nTrundle's warband once followed a foolish and cowardly chieftain. Under such a weak leader, Trundle feared he and his kin would fall prey to the other troll hordes scattered across the tundra. When his challenge to the chieftain ended in humiliation, Trundle did something that wasn't very troll-like: instead of his fists, he turned to his wits. Thinking on his hairy feet, he spun a tall tale about the troll leaders of old, claiming they wielded weapons of great power as symbols of their right to rule. Though he'd made up the story on the spot, Trundle wagered that if he could find or steal such a weapon, he would become the rightful leader of the warband. The trolls believed him, but none thought him capable of undertaking such a challenge. Knowing the boastful troll would die trying, the foolish chieftain agreed and Trundle departed to the familiar sound of laughter.\n\nAlone but undaunted, Trundle ventured into the foreboding realm of the dreaded Ice Witch. There, hidden among the many ancient and dangerous secrets, he hoped to find a weapon to prove his elaborate tale. He out-muscled the Ice Witch's guards and outsmarted her dark magic traps, but nothing he scavenged matched the power he'd described to his kin. Finally, he found an unexpected prize: a huge and magical club of never-melting True Ice. Grasping the weapon, he marveled at the cold power that ran through him. But then the wrathful Ice Witch herself appeared. As she summoned her dark magic, Trundle believed he had met his end, but another clever idea struck him. With a knowing grin, he offered the Ice Witch a devious proposition: a troll army, he told her, would be of much more use to her than one troll corpse....\n\nWhen Trundle returned to the warband, his fellow trolls bowed to his conquest. Calling his weapon ''Boneshiver,'' he took a moment to enjoy the look of numb shock on his chieftain's face before he caved it in. Seizing command, Trundle announced that there would no longer be chieftains - only a Troll King before whom all of his kind would kneel. The trolls rallied behind their brash, new leader and prepared for the coming war. With Trundle leading the charge, the time of the trolls had finally come.\n\n''Outsmart anyone you can't beat, and beat anyone you can't outsmart.'' \n-- Trundle",
    "champion_id": 48,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TrundleCircle.png",
    "q_name": "Chomp",
    "passive_name": "King's Tribute",
    "e_description": "Trundle creates an ice pillar at target location, becoming impassable terrain and slowing all nearby enemy units.",
    "recommended_items": [
      3047,
      2003,
      3074,
      1039,
      3111,
      1055,
      3143
    ],
    "r_name": "Subjugate",
    "r_description": "Trundle immediately steals a percent of his target's Health, Armor and Magic Resistance. Over the next 4 seconds the amount of Health, Armor, and Magic Resistance stolen is doubled.",
    "name": "Trundle",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TrundleTrollSmash.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/trundledesecrate.png",
    "q_description": "Trundle bites his opponent, dealing damage, briefly slowing and sapping some of their Attack Damage.",
    "title": "the Troll King",
    "e_name": "Pillar of Ice",
    "w_description": "Trundle turns target location into his domain, gaining Attack Speed, Movement Speed, and increased healing from all sources while on it.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Trundle.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Ravenous Hydra (Melee Only)",
      "Hunter's Machete",
      "Mercury's Treads",
      "Doran's Blade",
      "Randuin's Omen"
    ],
    "w_name": "Frozen Domain",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TrundlePain.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Trundle_Passive.png",
    "passive_description": "When an enemy unit dies near Trundle, he heals for a percent of its maximum Health."
  },
  "50": {
    "lore": "The earliest account of Swain's existence comes from a Noxian infirmary doctor's notes. According to them, Swain limped into the ward without cry or complaint; his right leg was snapped in half, with bone protruding from the skin. A small, scowling bird seemed affixed to his shoulder. The doctor gawked in horror as the young adolescent answered questions about his health and age with a calm, even stare. Even behind the echoing crack as the sand counterweights reset his tibia, Swain's measuring gaze never flickered, nor did his eyes twitch from the pop of his fibula. He refused the doctor's recommendation of magical treatment for the leg's inoperable damage, requesting only a spare crutch before shuffling away. He next surfaced in documents from the Noxian military, although it is evident that they are incomplete. Normally a crippled boy would be turned away in shame from Noxus' proud legion, but the records indicate his first designation was that of a ranking officer.\n\nThe men who've served under him (and survived) have remained in his charge with unshakable faith and loyalty. He leapt through the High Command's hierarchy, often ascending when superiors requested demotions to join his unit. A cunning strategist, Swain was decorated after every battle he fought, regularly hobbling in contemplation at the front of the assault. His rise to power seemed unceasing until he was suddenly relegated to inactive status prior to the Ionian Invasion - a bewildering decision which reeked of bureaucratic subversion. If Swain was upset by the events which unfolded, he never belied it. His face was so implacable that it was popularly rumored to be a mask, disguising something utterly inhuman beneath. More controversy surrounded the bird that never left his shoulder, whose name he whispered only to it. When Demacia escalated its presence in the League, Swain was immediately returned to active duty.\n\n''If you haven't yet lost the ability to ask, you may not yet ask for relief.''\n-Swain",
    "champion_id": 50,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SwainTorment.png",
    "q_name": "Decrepify",
    "passive_name": "Carrion Renewal",
    "e_description": "Swain afflicts his target, dealing damage to them over time and causing them to take increased damage from Swain.",
    "recommended_items": [
      2003,
      3089,
      3065,
      1056,
      3020
    ],
    "r_name": "Ravenous Flock",
    "r_description": "Swain inspires dread in his enemies by temporarily taking the form of a raven. During this time ravens strike out at up to 3 nearby enemies. Each raven deals damage and heals Swain for half of the damage dealt.",
    "name": "Swain",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SwainDecrepify.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SwainShadowGrasp.png",
    "q_description": "Swain sets his raven to cripple an enemy. Over the next 3 seconds, the target is damaged and slowed.",
    "title": "the Master Tactician",
    "e_name": "Torment",
    "w_description": "Swain marks a target area. After a short delay, mighty talons grab hold of enemy units, dealing damage and rooting them.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Swain.png",
    "recommended_item_names": [
      "Health Potion",
      "Rabadon's Deathcap",
      "Spirit Visage",
      "Doran's Ring",
      "Sorcerer's Shoes"
    ],
    "w_name": "Nevermove",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SwainMetamorphism.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/SwainCarrionRenewal.png",
    "passive_description": "Swain regenerates Mana each time he kills a unit. This amount increases each level."
  },
  "51": {
    "lore": "One of the reasons Piltover is known as the City of Progress is because it has an extraordinarily low crime rate. This hasn't always been the case; brigands and thieves of all sorts used to find the city-state an ideal mark for plunder, primarily due to the valuable resources it imports to fuel its techmaturgical research. Some even theorize that it would have fallen long ago to the chaos of organized crime if not for Caitlyn, the Sheriff of Piltover. Born the daughter of a wealthy statesman and a pioneering hextech researcher, Caitlyn discovered her natural gift for investigation when, at age 14, her father was assaulted and robbed on his way home. She snuck out of her house that night with her father's rifle and tracked down the muggers from the crime scene. At first, her parents did their best to discourage her from such risky hobbies, but she was incorrigible. Wishing to protect her daughter in the only way she knew how, Caitlyn's mother began outfitting her with techmaturgical devices tailored to her sleuthing needs.\n\nCaitlyn quickly gained notoriety, both because she was single handedly defeating crime in Piltover and also because she soon developed into a ravishing beauty. She never backed down from a case or a challenge, and she was one of the sharpest shots in the city-state. Her services were soon requested by Demacia to help track down a mysterious outlaw who had begun committing high-profile heists. The bandit, who always left a card with an ornate 'C' at the scene of the crime, became Caitlyn's arch-nemesis. To this day, Caitlyn still searches for this cat burglar, and the chase has led her all across Valoran. She has joined the League to hone her skills and gain the influence necessary to track down the only quarry that has managed to evade her.\n\n''Go ahead, run. I'll give you a five minute head start.''\n- Caitlyn, from her book 'Willing Apprehension'.",
    "champion_id": 51,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CaitlynEntrapment.png",
    "q_name": "Piltover Peacemaker",
    "passive_name": "Headshot",
    "e_description": "Caitlyn fires a heavy net to slow her target. The recoil knocks Caitlyn back.",
    "recommended_items": [
      2003,
      3035,
      3026,
      1055,
      3006
    ],
    "r_name": "Ace in the Hole",
    "r_description": "Caitlyn takes time to line up the perfect shot, dealing massive damage to a single target at a huge range. Enemy champions can intercept the bullet for their ally.",
    "name": "Caitlyn",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CaitlynPiltoverPeacemaker.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CaitlynYordleTrap.png",
    "q_description": "Caitlyn revs up her rifle for 1 second to unleash a penetrating shot that deals physical damage (deals less damage to subsequent targets).",
    "title": "the Sheriff of Piltover",
    "e_name": "90 Caliber Net",
    "w_description": "Caitlyn sets a trap to find sneaky yordles. When sprung, the trap immobilizes the champion, reveals them for a short duration, and deals magic damage over 1.5 seconds.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Caitlyn.png",
    "recommended_item_names": [
      "Health Potion",
      "Last Whisper",
      "Guardian Angel",
      "Doran's Blade",
      "Berserker's Greaves"
    ],
    "w_name": "Yordle Snap Trap",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CaitlynAceintheHole.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Caitlyn_Headshot.png",
    "passive_description": "Every few basic attacks, Caitlyn will fire a headshot dealing 150% damage to a champion or 250% damage to a minion."
  },
  "53": {
    "lore": "The city of Zaun is a place where both magic and science have gone awry. The unchecked nature of experimentation has taken its toll on the city. However, Zaun's lenient restrictions allow their researchers and inventors the leeway to push the bounds of science at an accelerated rate, for better or worse. It was under these conditions that a team of doctoral students from Zaun's College of Techmaturgy made a breakthrough in the field of intelligent steam automation. Their creation, the steam golem Blitzcrank, was developed to exercise judgment on-the-fly in order to assist with Zaun's hazardous waste reclamation process, since so often the conditions did not allow for human supervision. However, he soon began exhibiting unforeseen behaviors.\n\nOver time, the scientists were able to identify a demonstrated learning process, and Blitzcrank fast became a celebrity. As is sadly often the case though, credit for the golem's creation was scooped up by another - Professor Stanwick Pididly - though most now know the truth. In the wake of the ensuing legal maelstrom, it became evident that neither party truly had the steam golem's best interests at heart, and Blitzcrank humbly petitioned for personal autonomy. Backed by overwhelming support from the public, it took the liberal Council of Zaun only a few weeks to declare Blitzcrank a fully-independent, sentient entity. A unique being, the golem left Zaun, distressed by the controversy and feeling there was no place he could fit in. His travels led him to the one location in Valoran where unique beings have a place - the League of Legends. Fortunately, he was easily able to adapt his design to suit the rigors he would face on the Fields of Justice.\n\nThough Blitzcrank may batter anything that stands in his way, he really has a heart of gold...encased in a framework of iron...in a carapace of steel.",
    "champion_id": 53,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PowerFist.png",
    "q_name": "Rocket Grab",
    "passive_name": "Mana Barrier",
    "e_description": "Blitzcrank charges up his fist to make his next attack deal double damage and pop his target up in the air.",
    "recommended_items": [
      2003,
      3301,
      3025,
      3117,
      3110
    ],
    "r_name": "Static Field",
    "r_description": "Passively causes lightning bolts to damage a nearby enemy. Additionally, Blitzcrank can activate this ability to damage nearby enemies and silence them for 0.5 seconds, but doing so removes the passive lightning until Static Field becomes available again.",
    "name": "Blitzcrank",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RocketGrab.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Overdrive.png",
    "q_description": "Blitzcrank fires his right hand to grab an opponent on its path, dealing damage and dragging it back to him.",
    "title": "the Great Steam Golem",
    "e_name": "Power Fist",
    "w_description": "Blitzcrank super charges himself to get dramatically increased Movement and Attack Speed.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Blitzcrank.png",
    "recommended_item_names": [
      "Health Potion",
      "Ancient Coin",
      "Iceborn Gauntlet",
      "Boots of Mobility",
      "Frozen Heart"
    ],
    "w_name": "Overdrive",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/StaticField.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Blitzcrank_ManaBarrier.png",
    "passive_description": "When Blitzcrank's life is brought below 20% health, he activates Mana Barrier. This creates a mana shield equal to 50% of his mana for 10 seconds. Mana Barrier can only occur once every 90 seconds."
  },
  "54": {
    "lore": "There is a world of perfect harmony, where all are part of the whole. The Monolith is the essence of all creation, and its denizens are but singular pieces of it. It is beautiful in its symmetry, and in its almost complete lack of uncertainty. The rocky beings that live there know their place and work to fulfill their duties to the fullest extent, functioning almost as a superorganism or hive. Malphite has always strived to live up to his full potential, as his own personal part of the whole, serving the role of a distinguished creature questing to enforce his people's flawless vision of order.\n\nOne day, without warning, a dimensional rift opened, and he was summoned across the cosmos to the world of Runeterra. The transition was painful and terrifying for him, as he was cut off from the song of his people and the Monolith - things that had been ever-present in him since the day he was born. He raged, trapped in the Summoning Circle, as those who had called him made their plea. Runeterra was a world that had nearly been consumed by its disharmony. It was a world that needed champions to bring order out of chaos. It was to that end that the rock-creature was summoned, so that he could aid them in this quest. Looking past his own fear and apprehension, Malphite could see that this was a respectable goal, and one in which he could participate - perhaps uniquely so. Today, as part of the League of Legends, he hammers those who would seek to upset Valoran's movement toward order, especially turning his attention to those that wield chaotic magic. Unfortunately, Malphite has also begun to change, as he has been forced to face his own profound loneliness among the world's vibrant individuality.\n\nBeware, minions of chaos! The Shard of the Monolith has come.",
    "champion_id": 54,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Landslide.png",
    "q_name": "Seismic Shard",
    "passive_name": "Granite Shield",
    "e_description": "Malphite slams the ground, sending out a shockwave that deals magic damage based on his Armor as damage and reduces the Attack Speed of enemies for a short duration.",
    "recommended_items": [
      3047,
      2003,
      3025,
      1039,
      2041,
      3143
    ],
    "r_name": "Unstoppable Force",
    "r_description": "Malphite ferociously charges to a location, damaging enemies and knocking them into the air.",
    "name": "Malphite",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SeismicShard.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Obduracy.png",
    "q_description": "Using his primal elemental magic, Malphite sends a shard of the earth through the ground at his foe, dealing damage upon impact and stealing Movement Speed for 4 seconds.",
    "title": "Shard of the Monolith",
    "e_name": "Ground Slam",
    "w_description": "Malphite starts to hit with such force that his attacks deal damage to all units in front of him. Activating Brutal Strikes greatly increases his Armor and Attack Damage for a short amount of time.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Malphite.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Iceborn Gauntlet",
      "Hunter's Machete",
      "Crystalline Flask",
      "Randuin's Omen"
    ],
    "w_name": "Brutal Strikes",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/UFSlash.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Malphite_GraniteShield.png",
    "passive_description": "Malphite is shielded by a layer of rock which absorbs damage up to 10% of his maximum Health. If Malphite has not been hit for 10 seconds, this effect recharges."
  },
  "55": {
    "lore": "Driven by an intense killer instinct, Katarina uses her talents as an assassin for the glory of Noxus, and the continued elevation of her family. While her fervor drives her to ever-greater feats, it can sometimes lead her astray.\n\nFrom childhood, Katarina displayed a natural gift for combat. As the daughter of a prominent Noxian general many paths were open to her, but she rejected them all for the path of the blade. Rigorously trained by the finest assassins in Noxus, her father the best among them, it was not long before Katarina demanded her first assignment. The task they gave her was aggravatingly simple: assassinate a low-ranking Demacian officer. As she set to her work infiltrating the enemy camp, Katarina discovered an opportunity too tantalizing to pass by - the arrival of a Demacian General. Stalking him to his tent, she quietly dispatched his guards and slit his throat. Pleased with her impressive kill, she disappeared into the night. Katarina's elation faded the next day when her original objective, the Demacian officer, led his forces to ambush unprepared Noxian soldiers. Though the Noxians fought valiantly, they suffered heavy casualties. Furious at her mistake, Katarina set off to complete her original task. Returning to the camp, she spied her now heavily guarded target and realized a stealthy kill was no longer possible. Drawing her blades, Katarina swore the officer would die, no matter the cost. She leapt into battle, unleashing a whirlwind of steel. One by one blades flashed and guards fell, each strike bringing her one step closer to the officer. A final thrown dagger restored her honor. Bloody and bruised, Katarina barely escaped the Demacian forces, and returned to Noxus a changed woman. The scar she earned that night now serves as a constant reminder that she must never let passion interfere with duty.\n\n''Never question my loyalty. You will never know what I endure for it.''\n-- Katarina",
    "champion_id": 55,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KatarinaE.png",
    "q_name": "Bouncing Blades",
    "passive_name": "Voracity",
    "e_description": "Katarina instantly teleports to her target's location and takes reduced damage from enemies for a few seconds. If the target is an enemy, she deals damage.",
    "recommended_items": [
      2003,
      1001,
      3026,
      3089,
      3136
    ],
    "r_name": "Death Lotus",
    "r_description": "Katarina becomes a flurry of blades, throwing daggers with unrivaled speed at up to three nearby Champions. Daggers deal magic damage and reduce incoming healing on targets hit.",
    "name": "Katarina",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KatarinaQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KatarinaW.png",
    "q_description": "Katarina throws a dagger that bounces from enemy to enemy, dealing magic damage and marking them. Her next spell or basic attack against a marked target will consume the mark and deal additional magic damage.",
    "title": "the Sinister Blade",
    "e_name": "Shunpo",
    "w_description": "Katarina whirls her daggers around her, dealing magic damage to all enemies in the area. If she hits an enemy Champion, Katarina gains a burst of speed for a short duration.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Katarina.png",
    "recommended_item_names": [
      "Health Potion",
      "Boots of Speed",
      "Guardian Angel",
      "Rabadon's Deathcap",
      "Haunting Guise"
    ],
    "w_name": "Sinister Steel",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KatarinaR.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Katarina_Voracity.png",
    "passive_description": "Champion kills or assists reduce Katarina's cooldowns by 15 seconds."
  },
  "56": {
    "lore": "Before Nocturne, people believed that dreams were figments of their imagination, meaningless images that flashed through the mind when one slept. This belief was put to the test when a rash of sleep-related incidents started afflicting summoners of the League. Some would wake up screaming, terrified and beyond consolation. Some could not fall asleep, slowly going mad as the nights ticked by. Some simply never woke up. Physicians were baffled until a Field Architect happened to pass out next to a nexus on Twisted Treeline. Witnesses said he cried out once and then stopped breathing. Immediately after, magical energy arced out from the nexus, and Nocturne appeared.\n\nNocturne did not take his introduction to this world kindly. He slaughtered everything he could find before summoners were able to magically confine him. After a period of intense study, League experts divined that Nocturne hunted summoners in their sleep, attacking them in a place where their magic was useless. This seemed to be his only purpose. The families of the victims demanded justice, but League officials were concerned that death might only return Nocturne to the place from which he came. They bound him to a nexus fragment, trapping him in the physical world. As punishment for his crimes, they allowed summoners to call upon Nocturne in the League matches, bending his will to the summoners he hates and creating his own personal nightmare. League scholars don't know whether he truly came from the plane of dreams, or whether there are any more like him. Some theorize that the summoning act affected summoners' subconscious minds, luring Nocturne to them in their sleep. Perhaps the most disturbing theory is that Nocturne is a person's nightmare come to life. If this is true, they wonder, who is the dreamer?\n\n''The darkness is closing in...it's pitch black now...but I can still see him...''\n- Kelvin Ma, patient #4236",
    "champion_id": 56,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NocturneUnspeakableHorror.png",
    "q_name": "Duskbringer",
    "passive_name": "Umbra Blades",
    "e_description": "Nocturne plants a nightmare into his target's mind, dealing damage each second and fearing the target if they do not get out of range by the end of the duration.",
    "recommended_items": [
      3047,
      2003,
      1039,
      3117,
      1055,
      3142,
      3143
    ],
    "r_name": "Paranoia",
    "r_description": "Nocturne reduces the sight radius of all enemy champions and removes their ally vision in the process. He can then launch himself at a nearby enemy champion.",
    "name": "Nocturne",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NocturneDuskbringer.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NocturneShroudofDarkness.png",
    "q_description": "Nocturne throws a shadow blade that deals damage, leaves a Dusk Trail, and causes champions to leave a Dusk Trail. While on the trail, Nocturne can move through units and has increased Movement Speed and Attack Damage.",
    "title": "the Eternal Nightmare",
    "e_name": "Unspeakable Horror",
    "w_description": "Nocturne empowers his blades, passively gaining Attack Speed. Activating Shroud of Darkness allows Nocturne to fade into the shadows, creating a magical barrier which blocks a single enemy ability and doubles his passive Attack Speed if successful.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Nocturne.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Boots of Mobility",
      "Doran's Blade",
      "Youmuu's Ghostblade",
      "Randuin's Omen"
    ],
    "w_name": "Shroud of Darkness",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NocturneParanoia.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Nocturne_UmbraBlades.png",
    "passive_description": "Every 10 seconds, Nocturne's next attack strikes surrounding enemies for 120% physical damage and heals himself. <br><br>Nocturne's basic attacks reduce this cooldown by 1 second."
  },
  "57": {
    "lore": "Maokai was once a peaceful nature spirit dwelling in an idyllic forest, but the arrogance of humans brought an end to that life. Now he is a gnarled shadow of his former self, twisted by dark magics that defied the natural order of life and death. Infused with power he never asked for, the mighty treant has become a vengeful force of nature, sundering his enemies with wild magic and iron-hard limbs as he searches Valoran for the means to restore the Shadow Isles to its former glory.\n\nBefore the Shadow Isles became a land of death, the islands teemed with natural life and beauty. This was never truer than in the isles' sacred forest: a paradise of thriving trees and countless species, both animal and spirit alike. When the king of the Shadow Isles ordered his sorcerers to crack open the barrier separating life and death, the forest served as a well of power the magi drank deeply from. \n\nThe sorcerers' ritual succeeded in corrupting the cycle of life and unleashing forces they could not hope to contain. Vitality seeped from every living thing in the Shadow Isles: great trees withered into gnarled husks, people warped into twisted shades, and forest spirits became hollow wisps. Maokai, the strongest spirit of the sacred forest, watched in horror as his world crumbled and died around him. He fought to mend the wound in the world, but could not halt the destruction wrought by human folly. As the ghastly energies sought to overwhelm the great spirit, he made one last desperate attempt to preserve the life of the land. Maokai inhabited the ancient oak at the heart of the forest's spiritual power. There he gathered the essence of the isles into the tree as the corruption of undeath clawed hungrily at anything within reach. Fortified by boundless magic, Maokai could not be consumed entirely, though the spirit was not left unscathed.\n\nMaokai, now saturated with the essences of life and death, became fused with the ancient oak and contorted into an abomination. For ages, pain and grief were the only companions the spirit had. His boughs grew heavy as he wept at the desolation of everything he had known and loved, and his roots tore from the earth as he raged at the reckless sorcerers that had ruined his home. But all was not lost. Maokai had preserved the last vital spark remaining in the Shadow Isles, and with it, the hope of returning life to the land.\n\nLike moths to a flame, the tormented shades of the Shadow Isles were drawn to the living essence within Maokai. The spirit guarded the seed of life from the relentless undead, but Maokai knew he could not fend them off forever. He needed to escape the land of death his home had become, so he cast himself into the sea and trusted in nature to guide him towards a living land. There he hoped to find the means to cast out the forces of undeath and restore life to the Shadow Isles.\n\n Maokai -- \n ''To defy the natural order has consequences.''",
    "champion_id": 57,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MaokaiSapling2.png",
    "q_name": "Arcane Smash",
    "passive_name": "Sap Magic",
    "e_description": "Maokai flings a sapling that deals area damage on impact. The sapling then wards the nearby area. When enemies approach, the sapling attacks enemies with an arcane blast.",
    "recommended_items": [
      3047,
      2003,
      3025,
      1039,
      3117,
      1056,
      3143
    ],
    "r_name": "Vengeful Maelstrom",
    "r_description": "Maokai shields his allies by drawing power from hostile spells and attacks, reducing non-tower damage done to allied champions in the area. When Maokai ends the effect, he unleashes the absorbed energy to deal damage to enemies within the vortex.",
    "name": "Maokai",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MaokaiTrunkLine.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MaokaiUnstableGrowth.png",
    "q_description": "Maokai knocks back nearby enemies with a shockwave, dealing magic damage and slowing them.",
    "title": "the Twisted Treant",
    "e_name": "Sapling Toss",
    "w_description": "Maokai dissolves into a cloud of arcane energies. He regrows near a target enemy, dealing damage and rooting it in place.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Maokai.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Iceborn Gauntlet",
      "Hunter's Machete",
      "Boots of Mobility",
      "Doran's Ring",
      "Randuin's Omen"
    ],
    "w_name": "Twisted Advance",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MaokaiDrain3.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Maokai_Passive.png",
    "passive_description": "Each time a spell is cast near Maokai he draws energy from it, gaining a charge of Magical Sap. When Maokai has 5 charges his next basic attack heals him for 7% of his max Health."
  },
  "58": {
    "lore": "Renekton was once a staunch gatekeeper of ancient Shurima, but in the centuries since the fall of that once-glorious empire, he has been consumed by madness. Now, he is little more than a rage-fueled beast who seeks to kill his brother Nasus, who he believes is to blame for his current state of mind.",
    "champion_id": 58,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RenektonSliceAndDice.png",
    "q_name": "Cull the Meek",
    "passive_name": "Reign of Anger",
    "e_description": "Renekton dashes, dealing damage to units along the way. Empowered, Renekton deals bonus damage and reduces the Armor of units hit.",
    "recommended_items": [
      2003,
      3074,
      3111,
      1054,
      3143
    ],
    "r_name": "Dominus",
    "r_description": "Renekton transforms into the Tyrant form, gaining bonus Health and dealing damage to enemies around him. While in this form, Renekton gains Fury periodically.",
    "name": "Renekton",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RenektonCleave.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RenektonPreExecute.png",
    "q_description": "Renekton swings his blade, dealing moderate physical damage to all targets around him, and heals for a small portion of the damage dealt. If he has more than 50 Fury, his damage and heal are increased.",
    "title": "the Butcher of the Sands",
    "e_name": "Slice and Dice",
    "w_description": "Renekton slashes his target twice, dealing moderate physical damage and stuns them for 0.75 seconds. If Renekton has more than 50 Fury, he slashes his target three times, dealing high physical damage and stuns them for 1.5 seconds.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Renekton.png",
    "recommended_item_names": [
      "Health Potion",
      "Ravenous Hydra (Melee Only)",
      "Mercury's Treads",
      "Doran's Shield",
      "Randuin's Omen"
    ],
    "w_name": "Ruthless Predator",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RenektonReignOfTheTyrant.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Renekton_Predator.png",
    "passive_description": "Renekton gains Fury for every autoattack he makes. This Fury can empower his abilities with bonus effects. Additionally, Renekton gains bonus Fury when he is low on life."
  },
  "59": {
    "lore": "As the royal family of Demacia for centuries, members of the Lightshield line have spent their lives waging war against any who opposed Demacian ethics. It is said that every Lightshield is born with anti-Noxian sentiment in his blood. Jarvan IV is no exception, even though he is the first Lightshield born to the age of the League of Legends. As his forefathers had before him, he led Demacian troops into bloody engagements with Noxian forces, and on many occasions he has bled alongside wounded allies and fallen comrades. In his most crushing defeat, he was outmaneuvered and captured by a Noxian battalion under the command of Jericho Swain. This mistake nearly cost him his life at the hands of Urgot, but he was rescued by the Dauntless Vanguard, an elite Demacian strike force led by Jarvan's childhood companion, Garen.\n\nThose close to him believed that his capture changed him. Xin Zhao was quoted as saying: ''His eyes never seemed to look at you, only through you to something he could not look away from.'' One day, without warning, Jarvan IV handpicked a squad of Demacian soldiers and left Demacia, vowing to find ''atonement''. He began by tracking and hunting the most dangerous beasts and bandits he could find in northern Valoran, but he soon tired of such prey. Seeking something that only he understood, he ventured south of the Great Barrier. He wasn't heard from again for nearly two years. After many had assumed the worst, he returned to glorious fanfare on the streets of Demacia. His Demacian plates were adorned with the bones and scales of creatures unknown. His eyes bore the wisdom of someone twice his age. Of the twelve soldiers who had departed with him, only two returned. In a tone as cold and steady as steel, he swore to bring the enemies of Demacia to their knees.\n\n''There is only one truth, and you will find it at the point of my lance.''\n-- the ''last words'' of Jarvan IV at his failed execution",
    "champion_id": 59,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JarvanIVDemacianStandard.png",
    "q_name": "Dragon Strike",
    "passive_name": "Martial Cadence",
    "e_description": "Jarvan IV carries the pride of Demacia, passively granting him bonus Attack Speed and Armor. Activating Demacian Standard allows Jarvan IV to place a Demacian flag that deals magic damage on impact and grants Attack Speed to nearby allied champions.",
    "recommended_items": [
      2003,
      1039,
      3111,
      2041,
      3071,
      3117,
      3143
    ],
    "r_name": "Cataclysm",
    "r_description": "Jarvan IV heroically leaps into battle at a target with such force that he terraforms the surrounding area to create an arena around them.",
    "name": "Jarvan IV",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JarvanIVDragonStrike.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JarvanIVGoldenAegis.png",
    "q_description": "Jarvan IV extends his lance, dealing physical damage and lowering the Armor of all enemies in its path. Additionally, this will pull Jarvan to his Demacian Standard, knocking up enemies in his path.",
    "title": "the Exemplar of Demacia",
    "e_name": "Demacian Standard",
    "w_description": "Jarvan IV calls upon the ancient kings of Demacia to shield him from harm and slow surrounding enemies.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/JarvanIV.png",
    "recommended_item_names": [
      "Health Potion",
      "Hunter's Machete",
      "Mercury's Treads",
      "Crystalline Flask",
      "The Black Cleaver",
      "Boots of Mobility",
      "Randuin's Omen"
    ],
    "w_name": "Golden Aegis",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JarvanIVCataclysm.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/JarvanIV_MartialCadence.png",
    "passive_description": "Jarvan IV's initial basic attack on a target deals bonus physical damage. This effect cannot occur again on the same target for a short duration."
  },
  "60": {
    "lore": "Elise's entrancing beauty and grace conceal the pitiless, black heart of a deadly predator. With ruthless cunning, she lures the unsuspecting with promises of favor from the spider god. Having exchanged her humanity to become something far more sinister, Elise sacrifices the innocent to maintain her power and seemingly eternal youth. No one can fathom how many have been caught in her web, slain to feed her insatiable hunger.",
    "champion_id": 60,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EliseHumanE.png",
    "q_name": "Neurotoxin \/ Venomous Bite",
    "passive_name": "Spider Swarm",
    "e_description": "Human Form: Stuns the first enemy unit hit and reveals them if they are not stealthed.\n\nSpider Form: Elise and her Spiderlings ascend into the air and then descend upon target enemy.",
    "recommended_items": [
      2003,
      1039,
      2041,
      3068,
      3151,
      3020
    ],
    "r_name": "Spider Form",
    "r_description": "Transforms into a menacing spider with new abilities. While in Spider Form, Elise deals bonus Magic Damage on attack and has increased Movement Speed.",
    "name": "Elise",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EliseHumanQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EliseHumanW.png",
    "q_description": "Human Form: Deals damage based upon how high the target's Health is.\n\nSpider Form: Lunges at an enemy and deals damage based upon how low their Health is.",
    "title": "The Spider Queen",
    "e_name": "Cocoon \/ Rappel",
    "w_description": "Human Form: Releases a venom-gorged Spiderling that explodes when it nears a target.\n\nSpider Form: Elise and her Spiderlings gain Attack Speed and heal Elise on each attack.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Elise.png",
    "recommended_item_names": [
      "Health Potion",
      "Hunter's Machete",
      "Crystalline Flask",
      "Sunfire Cape",
      "Liandry's Torment",
      "Sorcerer's Shoes"
    ],
    "w_name": "Volatile Spiderling \/ Skittering Frenzy",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EliseR.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/ElisePassive.png",
    "passive_description": "Human Form: When Elise's spells hit an enemy, she readies a Spiderling.<br><br>Spider Form: Elise summons her Spiderlings to attack nearby foes."
  },
  "61": {
    "lore": "There once was a Piltovian man named Corin Reveck who had a daughter named Orianna, whom he loved more than anything else in the world. Though Orianna had incredible talent for dancing, she was deeply fascinated by the champions of the League of Legends. This fascination compelled her to begin training to become such a champion. It is unfortunate that her sheltered, wide-eyed naivete led her to take unnecessary and dangerous chances which ultimately led to her tragic demise. Orianna's death shattered Corin, driving him into deep depression and an obsession with techmaturgy. He could not stand the void his daughter's death left in his life, so he decided to build a replacement - one that would complete Orianna's dream of joining the League. What was created is the clockwork killing machine that Corin named after his daughter. Knowing that she was destined to be a champion and seeing the way the times were changing, he created The Ball as her pet and protector. This nearly symbiotic creation uses a different type of techmaturgy, relying more heavily on electricity than clockwork.\n\nOrianna and The Ball now fight as Champions in the League of Legends, using her sometimes misguided morality as a compass. She tries in earnest to fit in with those around her. However, no matter how hard she tries, Orianna can never be human and there is always something unnerving and alien about her. Though she attempts social interaction with other champions in the League of Legends, there are few who can get past her exotic nature. To many, it's as if there's nothing inside, that Orianna is just a soulless clockwork shell - a dangerous and deadly one at that. However, all along she remains the perfect daughter in her father's eyes.\n\n''Dance with me, my pet. Dance with me into oblivion.''",
    "champion_id": 61,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/OrianaRedactCommand.png",
    "q_name": "Command: Attack",
    "passive_name": "Clockwork Windup",
    "e_description": "Orianna commands her ball to attach to an allied champion, shielding them and dealing magic damage to any enemies it passes through on the way. Additionally, the ball grants additional Armor and Magic Resist to the champion it is attached to.",
    "recommended_items": [
      2003,
      3089,
      1056,
      3116,
      3020
    ],
    "r_name": "Command: Shockwave",
    "r_description": "Orianna commands her ball to unleash a shockwave, dealing magic damage and launching nearby enemies towards the ball after a short delay.",
    "name": "Orianna",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/OrianaIzunaCommand.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/OrianaDissonanceCommand.png",
    "q_description": "Orianna commands her ball to fire toward a target location, dealing magic damage to targets along the way (deals less damage to subsequent targets). Her ball remains at the target location after.",
    "title": "the Lady of Clockwork",
    "e_name": "Command: Protect",
    "w_description": "Orianna commands the ball to release a pulse of energy, dealing magic damage around it. This leaves a field behind that speeds up allies and slows enemies.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Orianna.png",
    "recommended_item_names": [
      "Health Potion",
      "Rabadon's Deathcap",
      "Doran's Ring",
      "Rylai's Crystal Scepter",
      "Sorcerer's Shoes"
    ],
    "w_name": "Command: Dissonance",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/OrianaDetonateCommand.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/OriannaPassive.png",
    "passive_description": "Orianna's autoattack deals additional magic damage. This damage increases the more Orianna attacks the same target."
  },
  "62": {
    "lore": "During the chaos of the Rune Wars, an enormous runestone was lost deep within the Plague Jungles. It remained there, untouched for centuries, emanating a potent magic which infused nearby wildlife with sentience and vitality. A group of monkeys who were particularly empowered by it came to worship the stone, and their leader - a wise sage - became convinced that he could harness its power to make the monkeys immortal. He performed an elaborate ritual, but things didn't go as he expected. The runestone was destroyed, and instead of granting immortality, it produced Kong, a monkey who carried in his heart the strength and power it had contained. Kong was driven by an unquenchable desire for greatness. He sought out every beast and monster the Plague Jungles could offer, eager to find a worthy opponent, but none offered the challenge he craved. He asked the sage for advice, and learned about a legend of hairless monkeys to the north who, with wits and might, had bent the world to their will.\n\nKong left, journeying north, determined to discover if the legend was true. He crossed the Southern Wastes and then the Great Barrier. On his way, he happened upon Master Yi, who was deep in meditation. Kong asked him who the strongest warrior in the north was, and Yi told him about the League of Legends. The tale intoxicated Kong, a place where he could battle the strongest fighters in the world was, to him, paradise. Kong asked Yi to introduce him to this League, and to teach him the ways of humans, so that he could be a fitting champion. In return, he would honor Yi by using Yi's Wuju style to become the greatest warrior Runeterra had ever seen. Admiring his passion, Yi agreed, but under the condition that Kong would one day teach the lessons of Wuju to a pupil of his own. In the spirit of this agreement, he renamed Kong ''Wukong,'' and gave him a weapon suited to his unusual nature - an enchanted staff that the young Doran had crafted. The weapon was an unrivalled masterpiece. Guided by Yi, Wukong joined the League of Legends to prove himself as the best, and to show the world the true power of Wuju.\n\n''Only in combat do you learn who you truly are.''\n-- Wukong",
    "champion_id": 62,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MonkeyKingNimbus.png",
    "q_name": "Crushing Blow",
    "passive_name": "Stone Skin",
    "e_description": "Wukong dashes toward a target enemy and sends out images to attack up to 2 additional enemies near his target, dealing physical damage to each enemy struck.",
    "recommended_items": [
      3078,
      2003,
      1039,
      3111,
      2041,
      3117,
      3143
    ],
    "r_name": "Cyclone",
    "r_description": "Wukong's staff grows outward and he spins it around, dealing damage and knocking up enemies. Wukong gains Movement Speed over the duration of the spell.",
    "name": "Wukong",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MonkeyKingDoubleAttack.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MonkeyKingDecoy.png",
    "q_description": "Wukong's next attack deals additional physical damage, gains range, and reduces the enemy's Armor for a short duration.",
    "title": "the Monkey King",
    "e_name": "Nimbus Strike",
    "w_description": "Wukong becomes invisible for 1.5 seconds. An uncontrollable decoy is left behind that will deal Magic Damage to enemies near it after 1.5 seconds.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/MonkeyKing.png",
    "recommended_item_names": [
      "Trinity Force",
      "Health Potion",
      "Hunter's Machete",
      "Mercury's Treads",
      "Crystalline Flask",
      "Boots of Mobility",
      "Randuin's Omen"
    ],
    "w_name": "Decoy",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MonkeyKingSpinToWin.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/MonkeyKingStoneSkin.png",
    "passive_description": "Increases Wukong's Armor and Magic Resistance for each nearby enemy champion."
  },
  "63": {
    "lore": "In a faraway place known as Lokfar there was a seafaring marauder called Kegan Rodhe. As was his people's way, Kegan sailed far and wide with his fellows, stealing treasures from those unlucky enough to catch their attention. To some, he was a monster; to others, just a man. One night, as they sailed through the arctic waters, strange lights danced over the frozen wastes. There was something hypnotic about them; it was something that drew them to it like moths to a flame. Trekking across the frozen waste, they came to a cave covered in ancient runes. The meaning of the runes long lost to them, Kegan led the way inside. There, inside a perfect cage of ice floated a dancing column of flame. There was no way such a thing should be burning, especially not in this place. However, its movement was as hypnotic as a siren's song, captivating and seductive. While the others stayed back, Kegan could not help but approach it while holding out his hand...\n\nThat is the last thing Kegan Rodhe remembers, for now his body belongs to Brand. It is a creature of olden times, perhaps even a casualty of the Rune Wars. It is known in ancient texts as the Burning Vengeance. It is a creature of pure fiery hate that exists for no other reason than to lay waste the world of men and yordles. No one is quite sure how Brand found his way to Valoran, but he began his predations at once. Overcome by Demacian forces, he was given a choice: fight within the confines of the League or die. Naturally, he chose to use his destructive powers in the League, for now...\n\n''This place will burn, not by cinder flying or breath of wind, but by the vengeance of my hand.''\n-- Brand",
    "champion_id": 63,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BrandConflagration.png",
    "q_name": "Sear",
    "passive_name": "Blaze",
    "e_description": "Brand conjures a powerful blast at his target, dealing magic damage to them. If the target is ablaze, Conflagration spreads to nearby enemies.",
    "recommended_items": [
      3135,
      2003,
      1056,
      3157,
      3020
    ],
    "r_name": "Pyroclasm",
    "r_description": "Brand unleashes a devastating torrent of fire, dealing magic damage each time it bounces. If a target is ablaze, Pyroclasm will priotize champions for the next bounce.",
    "name": "Brand",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BrandBlaze.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BrandFissure.png",
    "q_description": "Brand launches a ball of fire forward that deals magic damage. If the target is ablaze, Sear will stun the target for 2 seconds.",
    "title": "the Burning Vengeance",
    "e_name": "Conflagration",
    "w_description": "After a short delay, Brand creates a pillar of flame at a target area, dealing magic damage to enemy units within the area. Units that are ablaze take an additional 25% damage.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Brand.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Doran's Ring",
      "Zhonya's Hourglass",
      "Sorcerer's Shoes"
    ],
    "w_name": "Pillar of Flame",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BrandWildfire.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/BrandBlaze.png",
    "passive_description": "Brand's spells light his targets ablaze, dealing 8% of their maximum Health in magic damage over 4 seconds."
  },
  "64": {
    "lore": "As a young teen, Lee Sin was intent on becoming a summoner. His will and dedication were unmatched by any of his peers, and his skill drew the attention of Reginald Ashram, the League's High Councilor at the time. While studying at the Arcanum Majoris, Lee Sin became frustrated with instruction paced for the other students. He spent his free time researching the nuances of summoning in hopes of graduating sooner. He made amazing advances in his arcane studies, surpassing all other students. By all indications, he would have become one of the League's greatest summoners were it not for one terrible mistake. Too impatient, he attempted to test his ability by summoning a beast from the Plague Jungles. What he summoned instead was a young boy, but not in one piece. He barely had time to look the boy in what was once his face before the jumbled human mass fell lifeless to the floor. A League investigation later revealed that the boy's entire village was obliterated by feedback from the ritual.\n\nLee Sin's talents were so promising that the League was willing to overlook the incident, but he could never forgive himself. He left the Institute and journeyed to the Shojin Monastery for eternal repentance, swearing never to practice magic again. Years later, hoping to atone for his crime with martyrdom, he set himself ablaze as a protest of the Noxian occupation of Ionia. He remained alive in this state, enduring searing agony for weeks. His actions paved the way for a League match wherein Ionia prevailed, but by the time he was doused, his eyes had been burned completely from their sockets. Hailed as a savior, he was reborn, and his will to act invigorated. He joined the League of Legends to continue his atonement with sweat and blood, a true monk's only possessions.\n\n''The actions of one may sunder the world, but the efforts of many may rebuild it.''\n- Lee Sin",
    "champion_id": 64,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BlindMonkEOne.png",
    "q_name": "Sonic Wave \/ Resonating Strike",
    "passive_name": "Flurry",
    "e_description": "Tempest: Lee Sin smashes the ground, sending out a shockwave that deals magic damage and reveals enemy units hit. If Tempest hits an enemy, Lee Sin can cast cripple for the next 3 seconds.\nCripple: Lee Sin cripples nearby enemies revealed by Tempest, reducing their Movement Speed for 4 seconds. Movement Speed recovers gradually over the duration.",
    "recommended_items": [
      3047,
      2003,
      1039,
      3071,
      3117,
      1055,
      3143
    ],
    "r_name": "Dragon's Rage",
    "r_description": "Lee Sin performs a powerful roundhouse kick launching his target back, dealing physical damage to the target and any enemies they collide with. Enemies the target collides with are knocked into the air for a short duration. This technique was taught to him by Jesse Perring, although Lee Sin does not kick players off the map.",
    "name": "Lee Sin",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BlindMonkQOne.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BlindMonkWOne.png",
    "q_description": "Sonic Wave: Lee Sin projects a discordant wave of sound to locate his enemies, dealing physical damage to the first enemy it encounters. If Sonic Wave hits, Lee Sin can cast Resonating Strike for the next 3 seconds.\nResonating Strike: Lee Sin dashes to the enemy hit by Sonic Wave, dealing physical damage plus 8% of their missing Health.",
    "title": "the Blind Monk",
    "e_name": "Tempest \/ Cripple",
    "w_description": "Safeguard: Lee Sin rushes towards a target ally, shielding himself from damage. If the ally is a champion, they are also shielded. After using Safeguard, Lee Sin can cast Iron Will for the next 3 seconds.\nIron Will: Lee Sin's intense training allows him to thrive in battle. For 5 seconds, Lee Sin gains Life Steal and Spell Vamp.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/LeeSin.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "The Black Cleaver",
      "Boots of Mobility",
      "Doran's Blade",
      "Randuin's Omen"
    ],
    "w_name": "Safeguard \/ Iron Will",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BlindMonkRKick.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/LeeSinPassive.png",
    "passive_description": "After Lee Sin uses an ability, his next 2 basic attacks gain 40% Attack Speed and return 15 Energy each."
  },
  "67": {
    "lore": "The world is not always as civilized as people might think. There are still those who would follow the blackest paths of magic and become corrupted by the darker powers that flow through Runeterra. Shauna Vayne knows this fact well. As a young privileged girl in the heart of Demacia's elite, her father tried to convince her of the constabulary's ever-vigilant eye. Young and naive, she truly believed that her world was one of perfect safety, until one night, when a twisted witch took interest in her father. The malevolent woman overcame her father's conciliar guard, then tortured her family before murdering them. The young Shauna escaped only by hiding herself and then fleeing once the hag had departed, plagued by the screams of her loved ones as she ran. A burning hatred was born in her that day, one that could never be denied.\n\nVayne was able to take care of herself using her father's money, and she began to train as soon as an instructor would have her as a student. By the time she was a fully grown woman, she had become a grim warrior. However, the fields of battle were not to be her home. Demacia needed a protector, one who hunted those lost to the darkness. Shauna used her family's contacts to become the first Night Hunter, and now her prowess is the stuff of legends. It is said that those who practice the black arts quake when they hear that the Night Hunter is on the prowl. Despite her crusade, Shauna has looked at the League of Legends in horror. There are champions who have clearly lost themselves to the blackest of magics, and who have been embraced within the League even though they should be put down for the safety of all. The time has come for the Night Hunter to execute her secret mission - to purge the League of Legends.\n\nNot all shadows are to be feared. At least, if Vayne has her way.",
    "champion_id": 67,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VayneCondemn.png",
    "q_name": "Tumble",
    "passive_name": "Night Hunter",
    "e_description": "Vayne draws a heavy crossbow from her back, and fires a huge bolt at her target, knocking them back and dealing damage. If they collide with terrain, they are impaled, dealing bonus damage and stunning them.",
    "recommended_items": [
      2003,
      3026,
      1055,
      3006,
      3031
    ],
    "r_name": "Final Hour",
    "r_description": "Readying herself for an epic confrontation, Vayne gains increased Attack Damage, invisibility during Tumble, and triple the bonus Movement Speed from Night Hunter.",
    "name": "Vayne",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VayneTumble.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VayneSilveredBolts.png",
    "q_description": "Vayne tumbles, maneuvering to carefully place her next shot. Her next attack deals bonus damage.",
    "title": "the Night Hunter",
    "e_name": "Condemn",
    "w_description": "Vayne tips her bolts with a rare metal, toxic to evil things. The third consecutive attack or ability against the same target deals a percentage of the target's maximum Health as bonus true damage. (Max: 200 damage vs. Monsters)",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Vayne.png",
    "recommended_item_names": [
      "Health Potion",
      "Guardian Angel",
      "Doran's Blade",
      "Berserker's Greaves",
      "Infinity Edge"
    ],
    "w_name": "Silver Bolts",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VayneInquisition.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Vayne_NightHunter.png",
    "passive_description": "Vayne ruthlessly hunts evil-doers. She gains 30 Movement Speed when moving toward nearby enemy champions."
  },
  "68": {
    "lore": "Even amongst yordles, Rumble was always the runt of the litter. As such, he was used to being bullied. In order to survive, he had to be scrappier and more resourceful than his peers. He developed a quick temper and a reputation for getting even, no matter who crossed him. This made him something of a loner, but he didn't mind. He liked to tinker, preferring the company of gadgets, and he could usually be found rummaging through the junkyard. He showed great potential as a mechanic. His teachers recommended him for enrollment at the Yordle Academy of Science and Progress in Piltover, where he may very well have become one of Heimerdinger's esteemed proteges, but Rumble refused to go. He believed that Heimerdinger and his associates were ''sellouts,'' trading superior yordle technology to humans for nothing more than a pat on the head while yordles remained the butt of their jokes. When a group of human graduates from the Yordle Academy sailed to Bandle City to visit the place where their mentor was born and raised, Rumble couldn't resist the temptation to see them face-to-face (so to speak). He only intended to get a good look at the humans, but four hours and several choice words later, he returned home bruised and bloodied with an earful about how he was an embarrassment to ''enlightened'' yordles like Heimerdinger. The next morning he left Bandle City without a word, and wasn't seen again for months. When he returned, he was at the helm of a clanking, mechanized monstrosity. He marched it to the center of town amidst dumbfounded onlookers and there announced that he would join the League of Legends to show the world what yordle-tech was really capable of, without hiding behind a foreign banner.\n\n''Ugh, it's gonna take forever to scrape your face off my suit!''\n-- Rumble",
    "champion_id": 68,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RumbleGrenade.png",
    "q_name": "Flamespitter",
    "passive_name": "Junkyard Titan",
    "e_description": "Rumble launches a taser, electrocuting his target with magic damage and slowing their Movement Speed. A second shot can be fired within 3 seconds. While in Danger Zone the damage and slow percentage is increased.  ",
    "recommended_items": [
      3135,
      2003,
      1054,
      3116,
      3020
    ],
    "r_name": "The Equalizer",
    "r_description": "Rumble fires off a group of rockets, creating a wall of flames that damages and slows enemies. ",
    "name": "Rumble",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RumbleFlameThrower.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RumbleShield.png",
    "q_description": "Rumble torches opponents in front of him, dealing magic damage in a cone for 3 seconds. While in Danger Zone this damage is increased. ",
    "title": "the Mechanized Menace",
    "e_name": "Electro Harpoon",
    "w_description": "Rumble pulls up a shield, protecting him from damage and granting him a quick burst of speed. While in Danger Zone, the shield strength and speed bonus is increased. ",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Rumble.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Doran's Shield",
      "Rylai's Crystal Scepter",
      "Sorcerer's Shoes"
    ],
    "w_name": "Scrap Shield",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RumbleCarpetBomb.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Rumble_Junkyard Titan1.png",
    "passive_description": "Every spell Rumble casts gives him Heat. When he reaches 50% Heat he reaches Danger Zone, granting all his basic abilities bonus effects. When he reaches 100% Heat, he starts Overheating, granting his basic attacks bonus damage, but making him unable to cast spells for a few seconds. "
  },
  "69": {
    "lore": "Cassiopeia is a terrifying creature - half woman, half snake - whose slightest glance brings death. The youngest daughter of one of Noxus' most influential families, she was once a beautiful and cunning temptress capable of manipulating the hardest heart. Transformed by the venom of an ancient Shuriman tomb guardian, she continues to serve Noxian interests as she always has, just in a more... visceral way.",
    "champion_id": 69,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CassiopeiaTwinFang.png",
    "q_name": "Noxious Blast",
    "passive_name": "Aspect of the Serpent",
    "e_description": "Cassiopeia lets loose a damaging attack at her target, increasing further Poison damage delt to the target. If the target dies, Cassiopeia regains Mana. If the target is poisoned, the cooldown of this spell is refreshed.",
    "recommended_items": [
      2003,
      3089,
      1056,
      3116
    ],
    "r_name": "Petrifying Gaze",
    "r_description": "Cassiopeia releases a swirl of magical energy from her eyes, stunning any enemies in front of her that are facing her and slowing any others with their back turned.",
    "name": "Cassiopeia",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CassiopeiaNoxiousBlast.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CassiopeiaMiasma.png",
    "q_description": "Cassiopeia blasts an area with poison after a brief delay, granting her increased Movement Speed if she hits an enemy champion.",
    "title": "the Serpent's Embrace",
    "e_name": "Twin Fang",
    "w_description": "Cassiopeia releases a cloud of poison, lightly damaging and slowing any enemy that happens to pass through it.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Cassiopeia.png",
    "recommended_item_names": [
      "Health Potion",
      "Rabadon's Deathcap",
      "Doran's Ring",
      "Rylai's Crystal Scepter"
    ],
    "w_name": "Miasma",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/CassiopeiaPetrifyingGaze.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Cassiopeia_DeadlyCadence.png",
    "passive_description": "Cassiopeia gains stacks of Aspect of the Serpent over time and by poisoning enemy champions."
  },
  "72": {
    "lore": "Skarner, the crystalline guardian, defends the entrance to a realm deep beneath the Shuriman wastes. The few who survive trespassing his domain describe a creature of terrifying intelligence, anger, and precision. What this merciless creature protects, no one knows.",
    "champion_id": 72,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SkarnerFracture.png",
    "q_name": "Crystal Slash",
    "passive_name": "Crystallizing Sting",
    "e_description": "Skarner summons a blast of crystalline energy which deals damage to enemies struck and slows them.",
    "recommended_items": [
      3078,
      2003,
      3025,
      1039,
      3111,
      2041,
      3117
    ],
    "r_name": "Impale",
    "r_description": "Skarner suppresses an enemy champion and deals magic damage to it. During this time, Skarner can move freely and will drag his helpless victim around with him. When the effect ends, Skarner's target will be dealt additional damage.",
    "name": "Skarner",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SkarnerVirulentSlash.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SkarnerExoskeleton.png",
    "q_description": "Skarner lashes out with his claws, dealing physical damage to all nearby enemies and charging himself with Crystal Energy for several seconds if a unit is struck. If he casts Crystal Slash again while powered by Crystal Energy, he deals bonus magic damage. Whenever he hits a target with Crystal Slash he gains a stacking buff that increases his Attack Speed for a few seconds. Basic attack reduce this ability's cooldown.",
    "title": "the Crystal Vanguard",
    "e_name": "Fracture",
    "w_description": "Skarner gains a shield, and while the shield persists his Movement Speed is increased.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Skarner.png",
    "recommended_item_names": [
      "Trinity Force",
      "Health Potion",
      "Iceborn Gauntlet",
      "Hunter's Machete",
      "Mercury's Treads",
      "Crystalline Flask",
      "Boots of Mobility"
    ],
    "w_name": "Crystalline Exoskeleton",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SkarnerImpale.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Skarner_Passive.png",
    "passive_description": "Skarner's damaging spells apply Crystal Venom to enemies for 5 seconds that stacks up to 3 times. <br><br>If an enemy has 3 stacks of Crystal Venom, Skarner's next attack will deal additional magic damage and stun the target. Skarner cannot apply Crystal Venom to this target for 6 seconds after he stuns them."
  },
  "74": {
    "lore": "From the Journal of Professor Cecil B. Heimerdinger\n\n10.14\n\n09:15\n\nCurrent meteorological conditions in Bandle City seem optimal. Atmospheric pressure is ideal for today's experiments!\n\nRunning a fifth trial for my Tridyminiumobulator this afternoon. Some fine tuning is required; singed my mustache. Need to adjust the energy throughput.\n\n16:00\n\nTridyminiumobulator is still not maintaining intended proper energy efficiency! Necessary to run more numbers. In the meantime, I have found something else that's very intriguing.\n\nWhile returning home after today's tests, I passed a gaggle of young yordles throwing a spherical projectile at each other. It's a simple enough concept: throw the object at someone, catch it, throw it at another yordle, repeat. But yordle miscalculations result in several errors! They throw with inconsistent accuracy and force, and the ''ball'' (as they refer to it) is frequently dropped... There are many ways for this process to be improved. According to my calculations, and after collecting data from the participants, if the pitching was consistent in both speed and arc there would be a 44.57% increase to fun! I need to ponder this for the evening.\n\n10.15\n\n05:20\n\nEureka! I've devised a solution.\n\nI've invented an automated ball pitcher. Current name: H-28G. It employs a consistent speed and trajectory, ensuring that the recipient will always be able to catch the ball. It redirects itself to the nearest yordle (if there is more than one in the vicinity) ensuring everyone has a turn. I'll take it to the young yordles today and demonstrate my invention.\n\nAlso: spilled toxic acid on my shoes this morning. Bothersome.\n\n10:30\n\nTested the automated pitcher today. It did not go as planned. The young ones were excited enough about my invention, but, when the machine was turned on, it was far too powerful! Even at its lowest setting it completely knocked a yordle off his feet. Clearly, I overestimated the velocity behind their throws... I'll return soon to make adjustments.\n\nBut my priority, for now, is the Tridyminiumobulator; I must fix its complications before lunch. Once it's in good shape, I'll need to test it somewhere else. Bandle City is proving insufficient for field research.\n\n10.16\n\n15:55\n\nApparently, there's a giant in town. A highly annoying anomaly. The noise outside is disturbing my research!\n\nMust check fish tank today. They've been strangely quiet...\n\n10.17\n\n10:40\n\nI have heard that many yordles have been injured due to the giant-related disturbance. If this doesn't stop soon, intervention will be necessary! I hope H-28G is still intact. I would lose a lot of time if it has to be rebuilt.\n\n16:30\n\nEverything is quiet again. It seems that the giant came to his senses and ran off. I need to gather H-28G tomorrow, once I've finished with more pressing matters. I've almost perfected the Tridyminiumobulator!\n\n10.18\n\n08:30\n\nToday has been quite eventful already. I was surprised by a knock at my door. It seemed like the entire city was standing in front of my house. Normally, when a crowd has gathered, it's because they have some petty grievance about my work. But this time, they were celebrating!\n\nAstonishingly, it seems one of the young yordles took advantage of the H-28G prototype I had left behind amidst the giant tomfoolery. He proved to be innovative, and repurposed the invention into a makeshift turret. It's powerful enough to scare off a giant - imagine that! What an ingenious little fellow.\n\nI wish I could employ his like-minded encephalon in the near future - I have big plans and his assistance could be valuable - but he'd have to leave Bandle City. The scope of my plans necessitates a more expansive testing ground.\n\nRuneterra should suffice!",
    "champion_id": 74,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HeimerdingerE.png",
    "q_name": "H-28G Evolution Turret",
    "passive_name": "Techmaturgical Repair Bots",
    "e_description": "Heimerdinger lobs a grenade at a location, dealing damage to enemy units, as well as stunning anyone directly hit and slowing surrounding units.",
    "recommended_items": [
      2003,
      3174,
      3089,
      1056,
      3020
    ],
    "r_name": "UPGRADE!!!",
    "r_description": "Heimerdinger invents an upgrade, causing his next spell to have increased effects. ",
    "name": "Heimerdinger",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HeimerdingerQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HeimerdingerW.png",
    "q_description": "Heimerdinger lays down a rapid-fire cannon turret equipped with a secondary pass-through beam attack (turrets deal half damage to towers).",
    "title": "the Revered Inventor",
    "e_name": "CH-2 Electron Storm Grenade",
    "w_description": "Heimerdinger fires long-range rockets that converge on his cursor. ",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Heimerdinger.png",
    "recommended_item_names": [
      "Health Potion",
      "Athene's Unholy Grail",
      "Rabadon's Deathcap",
      "Doran's Ring",
      "Sorcerer's Shoes"
    ],
    "w_name": "Hextech Micro-Rockets",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HeimerdingerR.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Heimerdinger_Passive.png",
    "passive_description": "Heimerdinger gives nearby allied H-28G Turrets and Champions increased Health Regeneration. "
  },
  "75": {
    "lore": "To some, Nasus is a demigod who walks among the ruins of an ancient civilization; to others, he is nothing more than a myth. Legend speaks of his dominion over death and time. Millennia ago, he stood at the apex of Shuriman society as curator and guardian. He now roams the arid wastes, seeking to release his brother Renekton from the grip of madness.",
    "champion_id": 75,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NasusE.png",
    "q_name": "Siphoning Strike",
    "passive_name": "Soul Eater",
    "e_description": "Nasus unleashes a spirit flame at a location, dealing damage and reducing the Armor of enemies who stand on it.",
    "recommended_items": [
      3078,
      3047,
      2003,
      3025,
      1039,
      3111,
      2041
    ],
    "r_name": "Fury of the Sands",
    "r_description": "Nasus unleashes a mighty sandstorm that batters nearby enemies. While the storm rages, he gains increased Health, Attack Range, and drains nearby enemies' max Health converting into bonus damage for the duration.",
    "name": "Nasus",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NasusQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NasusW.png",
    "q_description": "Nasus strikes his foe, dealing damage and increasing the power of his future Siphoning Strikes if he slays his target.",
    "title": "the Curator of the Sands",
    "e_name": "Spirit Fire",
    "w_description": "Nasus ages an enemy champion, decelerating their Movement and Attack Speeds over time.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Nasus.png",
    "recommended_item_names": [
      "Trinity Force",
      "Ninja Tabi",
      "Health Potion",
      "Iceborn Gauntlet",
      "Hunter's Machete",
      "Mercury's Treads",
      "Crystalline Flask"
    ],
    "w_name": "Wither",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NasusR.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Nasus_Passive.png",
    "passive_description": "Nasus drains his foe's spiritual energy, giving him bonus Life Steal."
  },
  "76": {
    "lore": "There are few dwellers, let alone champions, residing in the blasted and dangerous lands that lie south of the Great Barrier. Much of that world still bears the scars of past Runes Wars, especially the mysterious Kumungu Jungle. There are long-forgotten treasures in these strange places which many risk life and limb to acquire. The champion known as Nidalee was only a young girl travelling with her treasure-seeking parents when they lost their way in the dense, rainy jungles. The jungle was unforgiving, and she watched her parents suffer agonizing final days as they fell victim to a mysterious and vicious disease.\n\nAs improbable as it was for a child to survive in the inhospitable jungle by herself, she did just that. Her youthful innocence and a fortunate naivete caused her to appeal to the beasts of that place and she was taken in by a family of cougars and raised as one of their own. She grew and somehow absorbed the raw magic of the dense wilds, evolving beyond both her human physiology and her feline affectation. On one pivotal day in her life, standing over the torn remnants of a Noxian squad of woodcutters, Nidalee chose to rejoin the so-called civilized world, to fight in the League of Legends so as to protect the vast woods from both Demacia and Noxus.\n\nNidalee was taught to fight by her feline family, battling viciously with tooth and nail. Something in her feline ways may draw you to her, but remember that she is no pussycat.",
    "champion_id": 76,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PrimalSurge.png",
    "q_name": "Javelin Toss \/ Takedown",
    "passive_name": "Prowl",
    "e_description": "In human form, Nidalee channels the spirit of the cougar to heal her allies and imbue them with Attack Speed for a short duration. As a cougar, she claws in a direction, dealing damage to enemies in front of her.",
    "recommended_items": [
      3158,
      2003,
      1056,
      3157,
      3100
    ],
    "r_name": "Aspect Of The Cougar",
    "r_description": "Nidalee transforms into a cougar, gaining new abilities.",
    "name": "Nidalee",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JavelinToss.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Bushwhack.png",
    "q_description": "In human form, Nidalee throws a spiked javelin at her target that gains damage as it flies.  As a cougar, her next attack will attempt to fatally wound her target, dealing more damage the less life they have.",
    "title": "the Bestial Huntress",
    "e_name": "Primal Surge \/ Swipe",
    "w_description": "In human form, Nidalee lays a trap for unwary opponents that, when sprung, damages and reveals its target. As a cougar, she jumps in a direction, dealing damage in an area where she lands.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Nidalee.png",
    "recommended_item_names": [
      "Ionian Boots of Lucidity",
      "Health Potion",
      "Doran's Ring",
      "Zhonya's Hourglass",
      "Lich Bane"
    ],
    "w_name": "Bushwhack \/ Pounce",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AspectOfTheCougar.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Nidalee_Passive.png",
    "passive_description": "Moving through brush increases Nidalee's Movement Speed by 10% for 2 seconds, increased to 30% toward visible enemy champions within 5500 range.<br><br>Hitting champions or monsters with Javelin Toss and Bushwhack triggers a <span class=\"colorFFF673\">Hunt<\/span>, revealing them for 4 seconds. During this time, Nidalee gains 10% Movement Speed (increased to 30% toward the <span class=\"colorFFF673\">Hunted<\/span> target) and her first Takedown and Pounce are enhanced against them."
  },
  "77": {
    "lore": "Udyr is more than a man; he is a vessel for the untamed power of four primal animal spirits. When tapping into the spirits' bestial natures, Udyr can harness their unique strengths: the tiger grants him speed and ferocity, the turtle resilience, the bear might, and the phoenix its eternal flame. With their combined power, Udyr can turn back all those who would attempt to harm the natural order.\n\nIn the Freljord, there is a unique caste that lives outside the society of those savage lands. They are the custodians of the natural world: the Spirit Walkers. Once a generation, a child is born under a blood red moon, a child said to live between the two worlds of spirit and man. This child is brought to the Spirit Walker to continue the shamanic line. Udyr was such a child, and knew the howl of the tundra wolves even before he learned the language of his ancestors. Through the Spirit Walker, Udyr would one day learn the meaning of the spirits' calls and tend to the balance of nature. The Spirit Walker often told Udyr he would be tested more than those who had come before him, for the spirits of the Freljord were growing ever more restless, though the reason remained clouded. \n\nThe answer arrived in the dead of winter, as Udyr and the Spirit Walker were descended upon by a fearsome figure known only through frightened whispers: the Ice Witch. Knowing the boy would fall easy prey to her vile magic, the Spirit Walker shielded the child from her assault at the cost of his own life. Wracked by grief, Udyr howled with fury, and he felt the Freljord itself howl with him. In that moment, the child embraced the spirits' primal nature and became a beast himself. Coursing with their untamed power, Udyr's angry roar shook the mountaintops and brought down a torrential avalanche. Once Udyr had finally clawed his way out of the frost, the Ice Witch was nowhere to be found.\n\nFor years, the tribes of the north learned to avoid the wildman and his domain. Then one day, Udyr caught the scent of a fearless trespasser. Determined to chase the intruder from his territory, he attacked, only to be deflected with ease. The wildman launched himself at the stranger again and again, only to be effortlessly cast aside each time. Exhausted and defeated, Udyr felt his animosity ebb and croaked a clumsy ''who'' to the stranger. Lee Sin had come seeking the Spirit Walker's guidance and instead found a man who had also lost his way. The monk promised he would right Udyr's path and guided him to a monastery said to be protected by four eternal spirits of great power and wisdom. There, Udyr would find harmony.\n\nLee Sin brought Udyr to a land that was a stark contrast to his birthplace. Survival was not the only law that governed the lives of Ionians or creatures of the land. For the first time, Udyr felt at peace with the spirits surrounding him and found comfort in human companionship. His time among the monks taught him to temper his instincts, while his meditations with the ancient temple spirits taught him wisdom. Through them both, Udyr learned to truly embrace his life as the next Spirit Walker.\n\nUdyr owed much to the Ionians. It was a debt he was never asked to honor, but one he would ultimately repay many times over. When the armies of Noxus invaded, Udyr did not stand idle as the brutal soldiers oppressed the peaceful Ionians - he had not forgotten how to bare his teeth. Udyr leapt at their armies with all the ferocity of a cornered beast and gave the invaders good reason to fear the wilderness. From the trees, his claws tore the Noxians down in scores; on the river banks, he threw them back like a flood, and in the fields, he consumed them with searing wildfire. Only when the Noxians fled with their tails between their legs did Udyr quell his rage. \n\nPeace returned to Ionia, but still Udyr felt something stirring him from his rest. The spirits of the Freljord called out to him, warning of an unnatural evil emerging from the ice. Udyr understood the true threat that the Ice Witch posed to his homeland: she was the herald of a greater darkness that would soon envelop the land. Armed with the potent spirits of the temple, Udyr returned to the Freljord, seeking to defend the natural world from all who would threaten its balance. \n\n''Through us, nature's will is done.''\n -- Udyr",
    "champion_id": 77,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/UdyrBearStance.png",
    "q_name": "Tiger Stance",
    "passive_name": "Monkey's Agility",
    "e_description": "Bear Stance: Activation - Udyr increases Movement Speed for a short duration. Persistent Effect - Udyr's basic attacks stun his target for 1 second. This effect cannot occur on the same target for several seconds.",
    "recommended_items": [
      3047,
      2003,
      1039,
      3111,
      1055,
      3143,
      3153
    ],
    "r_name": "Phoenix Stance",
    "r_description": "Phoenix Stance: Activation - Udyr unleashes pulsing waves of fire, dealing damage to nearby enemies for 5 seconds. Persistent Effect - With the first basic attack and every third attack after, Udyr engulfs enemies in front of him with flames.",
    "name": "Udyr",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/UdyrTigerStance.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/UdyrTurtleStance.png",
    "q_description": "Tiger Stance: Activation - Udyr's Attack Speed is increased for a few seconds, and his first basic attack will deal a high amount of damage over 2 seconds. Persistent Effect - Udyr's basic attacks deal extra damage.",
    "title": "the Spirit Walker",
    "e_name": "Bear Stance",
    "w_description": "Turtle Stance: Activation - Udyr gains a temporary shield that absorbs damage. Persistent Effect - Udyr gains Life Steal.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Udyr.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Mercury's Treads",
      "Doran's Blade",
      "Randuin's Omen",
      "Blade of the Ruined King"
    ],
    "w_name": "Turtle Stance",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/UdyrPhoenixStance.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Udyr_MonkeysAgility.png",
    "passive_description": "Entering a stance grants Udyr 10% Attack Speed and 5 Movement Speed for a short duration. This effect can stack up to 3 times."
  },
  "78": {
    "lore": "While other young yordle girls played skip-step and braided wreathes out of posies, Poppy spent her youth earning calluses and grease stains in her father's armor shop. Blomgrun, her father, was Bandle City's finest smith. The only thing he loved as much as his work was his young daughter, Poppy - named for the sprightly sounds of the sparks that leapt from his ever-burning forge. He welled with pride the day she was first able to lift his trusty hammer, Whomper. Poppy immediately took to his art, demonstrating a natural gift for smithing, which Blomgrun honed with devoted instruction.\n\nOne day, a Demacian general named Florin Berell commissioned Blomgrun to craft a helm, glorious beyond comparison. Blomgrun toiled away on this project, determined to present Florin with his finest work. He let Poppy set the center jewel, entrusting her with the most important piece. When the pair finished, they departed for Demacia to deliver it in person. Word of the general's order, however, was leaked to the Noxian High Command, and two Noxian assassins were dispatched to intercept the delivery. Blomgrun was able to occupy the assassins long enough for Poppy to escape with the prized helm. She watched helplessly from the brush as her father was slain. Instead of fleeing home, she carried the helm the rest of the way to Demacia alone. She refused payment for it, saying that no amount would compensate for her father's life. Instead, she offered it as a gift, honoring her father's final intentions. Florin saw the grim determination behind the tears in her eyes, and requested that the leadership of Bandle City appoint Poppy as the yordle ambassador to Demacia. Soon after, seeking to crush Noxus with her father's hammer, Poppy volunteered for the League of Legends.\n\nPoppy may be small, but Whomper - or her will - is not.",
    "champion_id": 78,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PoppyHeroicCharge.png",
    "q_name": "Devastating Blow",
    "passive_name": "Valiant Fighter",
    "e_description": "Poppy charges at an enemy and carries them further. The initial impact deals a small amount of damage, and if they collide with terrain, her target will take a high amount of damage and be stunned.",
    "recommended_items": [
      3047,
      2003,
      1039,
      2041,
      3117,
      3143,
      3153
    ],
    "r_name": "Diplomatic Immunity",
    "r_description": "Poppy focuses intently on a single enemy champion, dealing increased damage to them. Poppy is immune to any damage and abilities from enemies other than her target.",
    "name": "Poppy",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PoppyDevastatingBlow.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PoppyParagonOfDemacia.png",
    "q_description": "Poppy crushes her opponent, dealing attack damage plus a flat amount and 8% of her target's max Health as bonus damage. The bonus damage cannot exceed a threshold based on rank.",
    "title": "the Iron Ambassador",
    "e_name": "Heroic Charge",
    "w_description": "Passive: Upon receiving damage from or dealing damage with a basic attack, Poppy's Armor and damage are increased for 5 seconds. This effect can stack 10 times. Active: Poppy gains max stacks of Paragon of Demacia and her Movement Speed is increased for 5 seconds.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Poppy.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Crystalline Flask",
      "Boots of Mobility",
      "Randuin's Omen",
      "Blade of the Ruined King"
    ],
    "w_name": "Paragon of Demacia",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PoppyDiplomaticImmunity.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Poppy_ValiantFighter.png",
    "passive_description": "All physical and Magic Damage dealt to Poppy that exceeds 10% of her current Health is reduced by 50%. This does not reduce damage from structures."
  },
  "79": {
    "lore": "The only thing more important to Gragas than fighting is drinking. His unquenchable thirst for stronger ale has led him in search of the most potent and unconventional ingredients to toss in his still. Impulsive and unpredictable, this rowdy carouser loves cracking kegs as much as cracking heads. Thanks to his strange brews and temperamental nature, drinking with Gragas is always a risky proposition.\n\nGragas has an eternal love of good drink, but his massive constitution prevented him from reaching a divine state of intoxication. One night, when he had drained all the kegs and was left wanting, Gragas was struck by a thought rather than the usual barstool: why couldn't he brew himself something that would finally get him truly drunk? It was then that he vowed to create the ultimate ale.\n\nGragas' quest eventually brought him to the Freljord, where the promise of acquiring the purest arctic water for his recipe led him into uncharted glacial wastes. While lost in an unyielding blizzard, Gragas stumbled upon a great howling abyss. There he found it: a flawless shard of ice unlike anything he had ever seen. Not only did this unmelting shard imbue his lager with incredible properties, but it also had a handy side effect - it kept the mixture chilled at the perfect serving temperature.\n\nUnder the spell of his new concoction, Gragas headed for civilization, eager to share the fermented fruits of his labor. As fate would have it, the first gathering to catch Gragas' bleary eyes would shape the future of the Freljord. He blundered into a deteriorating negotiation between two tribes discussing an alliance with Ashe. Though Ashe welcomed a break in the tension, the other warriors bristled at the intrusion and hurled insults at the drunken oaf. True to his nature, Gragas replied with a diplomatic headbutt, setting off a brawl matched only in the legends of the Freljord.\n\nWhen the fallen from that great melee finally awoke, Ashe proposed a friendly drink as an alternative to fighting. With their tempers doused in suds, the two tribes, formerly on the brink of war, bonded over a common love of Gragas' brew. Although strife was averted and Gragas hailed a hero, he still had not achieved his dream of drunken blissfulness. So once more, he set off to wander the tundra in search of ingredients for Runeterra's perfect pint.\n\n''Now this'll put hair on your chest!''\n -- Gragas",
    "champion_id": 79,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GragasE.png",
    "q_name": "Barrel Roll",
    "passive_name": "Happy Hour",
    "e_description": "Gragas charges to a location and collides with the first enemy unit he comes across, dealing damage to all nearby enemy units and stunning them.",
    "recommended_items": [
      3135,
      2003,
      1039,
      1056,
      3068,
      3020
    ],
    "r_name": "Explosive Cask",
    "r_description": "Gragas hurls his cask to a location, dealing damage and knocking back enemies caught in the blast radius.",
    "name": "Gragas",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GragasQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GragasW.png",
    "q_description": "Gragas rolls his cask to a location, which can be activated to explode or will explode on its own after 4 seconds. Enemies struck by the blast have their Movement Speed slowed.",
    "title": "the Rabble Rouser",
    "e_name": "Body Slam",
    "w_description": "Gragas guzzles down brew from his cask for 1 second. After finishing, he becomes drunkenly empowered, dealing more damage on his next basic attack and reducing damage received.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Gragas.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Hunter's Machete",
      "Doran's Ring",
      "Sunfire Cape",
      "Sorcerer's Shoes"
    ],
    "w_name": "Drunken Rage",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GragasR.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/GragasPassiveHeal.png",
    "passive_description": "On ability use, Gragas takes a drink restoring 4% of his max Health. This effect can only happen every 8 seconds."
  },
  "80": {
    "lore": "Far above the clouds on Mount Targon resides a stalwart tribe of people known as the Rakkor who still revere combat and war as ultimate artforms. They remember the Rune Wars of Runeterra and know that the League of Legends can only repress the rising tides of violence for so long. Each member of the tribe is bred to be a disciplined and vicious warrior, preferring to battle soldiers of either the Noxian or Demacian armies only when outnumbered at least ten to one. Rakkor warriors are trained not only to be as lethal with their bare hands as the most capable martial artists, but also to fiercely wield the many relic-weapons of the tribe. Such treasures have been handed down from generation to generation, and have harnessed the mystical nature of Runeterra in their very cores. These relic-weapons are among the most dangerous in existence - and it comes as no surprise that they have found their way to the League of Legends in the hands of Pantheon.\n\nThis stone-faced warrior is a paragon of his people, his very existence an anthem of exultation to the art of combat. Pantheon found it insulting that the people of Valoran would install an organization to replace war, complete with so-called champions, without including the Rakkor. Gathering the blessings of his tribe and armed with the relics of his ancestors, he has descended on the League to show the world a true warrior. He cares not who he fights, and cares nothing for the pageantry or prestige of a League champion, but lives only for the austere glory of battle. As long as Pantheon breathes, he thirsts for another foe to vanquish.\n\n''I was hoping they had more reinforcements.''\n-- Pantheon, standing amidst the pieces of a brutalized Noxian battalion.",
    "champion_id": 80,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PantheonE.png",
    "q_name": "Spear Shot",
    "passive_name": "Aegis Protection",
    "e_description": "Pantheon focuses and unleashes 3 swift strikes to the area in front of him, dealing double damage to champions. Pantheon also becomes more aware of his enemy's vital spots, allowing him to always crit enemies below 15% Health.",
    "recommended_items": [
      3047,
      3102,
      2003,
      1039,
      2041,
      3071,
      3117
    ],
    "r_name": "Grand Skyfall",
    "r_description": "Pantheon composes himself then leaps into the air to a target, striking all enemy units in an area. Enemies closer to the impact point take more damage.",
    "name": "Pantheon",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PantheonQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PantheonW.png",
    "q_description": "Pantheon hurls his spear at an opponent, dealing damage.",
    "title": "the Artisan of War",
    "e_name": "Heartseeker Strike",
    "w_description": "Pantheon leaps at an enemy and bashes the enemy with his shield, stunning them. After finishing the attack, Pantheon readies himself to block the next attack.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Pantheon.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Banshee's Veil",
      "Health Potion",
      "Hunter's Machete",
      "Crystalline Flask",
      "The Black Cleaver",
      "Boots of Mobility"
    ],
    "w_name": "Aegis of Zeonia",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/PantheonRJump.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Pantheon_AOZ.png",
    "passive_description": "After attacking or casting spells 4 times, Pantheon will block the next incoming basic attack or turret attack."
  },
  "81": {
    "lore": "The intrepid young adventurer Ezreal has explored some of the most remote and abandoned locations on Runeterra. During an expedition to the buried ruins of ancient Shurima, he recovered an amulet of incredible mystical power. Likely constructed to be worn by one of the Ascended, the enormous talisman nonetheless fit snugly upon his arm, amplifying his raw sorcerous skill to such an extent that he's gained the reputation of a hero, much to his embarrassment.",
    "champion_id": 81,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EzrealArcaneShift.png",
    "q_name": "Mystic Shot",
    "passive_name": "Rising Spell Force",
    "e_description": "Ezreal teleports to a target nearby location and fires a homing bolt which strikes the nearest enemy unit.",
    "recommended_items": [
      3158,
      2003,
      3035,
      3025,
      1055
    ],
    "r_name": "Trueshot Barrage",
    "r_description": "Ezreal channels for 1 second to fire a powerful barrage of energy missiles which do massive damage to each unit they pass through (deals 10% less damage to each unit it passes through).",
    "name": "Ezreal",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EzrealMysticShot.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EzrealEssenceFlux.png",
    "q_description": "Ezreal fires a damaging bolt of energy which reduces all of his cooldowns by 1 second if it strikes an enemy unit.",
    "title": "the Prodigal Explorer",
    "e_name": "Arcane Shift",
    "w_description": "Ezreal fires a fluctuating wave of energy, dealing magic damage to enemy champions, while increasing the Attack Speed of allied champions.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Ezreal.png",
    "recommended_item_names": [
      "Ionian Boots of Lucidity",
      "Health Potion",
      "Last Whisper",
      "Iceborn Gauntlet",
      "Doran's Blade"
    ],
    "w_name": "Essence Flux",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/EzrealTrueshotBarrage.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Ezreal_RisingSpellForce.png",
    "passive_description": "Hitting a target with any of Ezreal's abilities increases his Attack Speed by 10% for 6 seconds (effect stacks up to 5 times)."
  },
  "82": {
    "lore": "The vicious wraith Mordekaiser is among the most terrifying and hateful of spirits that haunt the Shadow Isles. Entombed in ancient armor, the Master of Metal is said to be the first of the unliving, a revenant who existed even before the Shadow Isles were wrought. His twisted soul thrives on his own suffering, as well as the anguish he inflicts upon others. Those who dare face Mordekaiser in battle risk a horrific curse: he enslaves his victims' souls to become instruments of destruction.",
    "champion_id": 82,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MordekaiserSyphonOfDestruction.png",
    "q_name": "Mace of Spades",
    "passive_name": "Iron Man",
    "e_description": "Mordekaiser deals damage to enemies in a cone in front of him. For each unit hit, Mordekaiser's shield absorbs energy.",
    "recommended_items": [
      3135,
      2003,
      1054,
      3116,
      3020
    ],
    "r_name": "Children of the Grave",
    "r_description": "Mordekaiser curses an enemy, stealing a percent of their life initially and each second. If the target dies while the spell is active, their soul is enslaved and will follow Mordekaiser as a ghost for 30 seconds.",
    "name": "Mordekaiser",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MordekaiserMaceOfSpades.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MordekaiserCreepingDeathCast.png",
    "q_description": "On next hit, Mordekaiser swings his mace with such force that it echoes out, striking up to 3 additional nearby targets, dealing damage plus bonus damage. If the target is alone, the attack deals extra damage.",
    "title": "the Master of Metal",
    "e_name": "Siphon of Destruction",
    "w_description": "Unleashes a protective cloud of metal shards to surround an ally, increasing their Armor and Magic Resistance and dealing damage per second to enemies in the cloud.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Mordekaiser.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Doran's Shield",
      "Rylai's Crystal Scepter",
      "Sorcerer's Shoes"
    ],
    "w_name": "Creeping Death",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/MordekaiserChildrenOfTheGrave.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Mordekaiser_IronMan.png",
    "passive_description": "A percent of the damage dealt from abilities is converted into a temporary shield, absorbing incoming damage."
  },
  "83": {
    "lore": "A terrifying and tragic figure, Yorick is a ghoulish being that exists on the edge of mortality. Some say he was the last of his family line, dying without an heir to continue its legacy, and that he is cursed to continue to his family's duty even after death. Wielding the twisted shovel he bore in life, he continues his macabre work, endlessly digging and filling graves upon the haunted Shadow Isles.",
    "champion_id": 83,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/YorickRavenous.png",
    "q_name": "Omen of War",
    "passive_name": "Unholy Covenant",
    "e_description": "Yorick steals life from his target and summons a Ravenous Ghoul that heals Yorick for the damage it deals.",
    "recommended_items": [
      3078,
      2003,
      3025,
      3111,
      2041
    ],
    "r_name": "Omen of Death",
    "r_description": "Yorick conjures a revenant in the image of one of his allies. If his ally dies while its revenant is alive, the revenant sacrifices itself to reanimate them and give them time to enact vengeance.",
    "name": "Yorick",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/YorickSpectral.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/YorickDecayed.png",
    "q_description": "Yorick's next attack will deal bonus physical damage and summon a Spectral Ghoul that deals additional damage and moves faster than Yorick's other ghouls. While the Spectral Ghoul is alive, Yorick moves faster as well.",
    "title": "the Gravedigger",
    "e_name": "Omen of Famine",
    "w_description": "Yorick summons a Decaying Ghoul that arrives with a violent explosion, dealing damage and slowing nearby enemies. While the Decaying Ghoul remains alive, nearby enemies continue to be slowed.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Yorick.png",
    "recommended_item_names": [
      "Trinity Force",
      "Health Potion",
      "Iceborn Gauntlet",
      "Mercury's Treads",
      "Crystalline Flask"
    ],
    "w_name": "Omen of Pestilence",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/YorickReviveAlly.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/YorickUnholyCovenant.png",
    "passive_description": "Yorick takes 5% reduced damage and his basic attacks deal 5% more damage for each summon that is active. Meanwhile, Yorick's ghouls have 35% of Yorick's Attack Damage and Health."
  },
  "84": {
    "lore": "There exists an ancient order originating in the Ionian Isles dedicated to the preservation of balance. Order, chaos, light, darkness -- all things must exist in perfect harmony for such is the way of the universe. This order is known as the Kinkou and it employs a triumvirate of shadow warriors to uphold its causes in the world. Akali is one of these shadow warriors, entrusted with the sacred duty of Pruning the Tree - eliminating those who threaten the equilibrium of Valoran. \n\nA prodigal martial artist, Akali began training with her mother as soon as she could make a fist. Her mother's discipline was relentless and unforgiving, but predicated on the fundamental principle: ''We do that which must be done.'' When the Kinkou inducted her into the order at the age of fourteen, she could slice a dangling chain with a chop of her hand. There was no question - she would succeed her mother as the Fist of Shadow. She has had to do much in this role which others might find morally questionable, but to her it is in service of her mother's inviolable doctrine. She now works with her fellows Shen and Kennen to enforce the balance of Valoran. This hallowed pursuit has unsurprisingly led the triumvirate to the Fields of Justice.\n\n''The Fist of Shadow strikes from the cover of death itself. Do not impede the balance.''",
    "champion_id": 84,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AkaliShadowSwipe.png",
    "q_name": "Mark of the Assassin",
    "passive_name": "Twin Disciplines",
    "e_description": "Akali flourishes her kamas, dealing damage based on her Attack Damage and Ability Power.",
    "recommended_items": [
      1001,
      1054,
      3116,
      3136,
      1028
    ],
    "r_name": "Shadow Dance",
    "r_description": "Akali moves through shadows to quickly strike her target, dealing damage and consuming an Essence of Shadow charge. Akali recharges Essence of Shadow charges both periodically and upon kills and assists, max 3 stacks.",
    "name": "Akali",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AkaliMota.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AkaliSmokeBomb.png",
    "q_description": "Akali spins her kama at a target enemy to deal Magic Damage and mark the target for 6 seconds. Akali's melee attacks against a marked target will trigger and consume the mark to cause additional damage and restore Energy.",
    "title": "the Fist of Shadow",
    "e_name": "Crescent Slash",
    "w_description": "Akali throws down a cover of smoke. While inside the area, Akali becomes invisible and gains a short burst of Movement Speed. Attacking or using abilities will briefly reveal her. Enemies inside the smoke have their Movement Speed reduced.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Akali.png",
    "recommended_item_names": [
      "Boots of Speed",
      "Doran's Shield",
      "Rylai's Crystal Scepter",
      "Haunting Guise",
      "Ruby Crystal"
    ],
    "w_name": "Twilight Shroud",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AkaliShadowDance.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/AkaliTwinDisciplines.png",
    "passive_description": "Discipline of Force: Akali's basic attacks deal an additional 6% bonus Magic Damage, increasing by 1% for every 6 Ability Power.<br><br>Discipline of Might: Akali gains 6% Spell Vamp, increasing by 1% for every 6 Bonus Attack Damage."
  },
  "85": {
    "lore": "There exists an ancient order originating in the Ionian Isles dedicated to the preservation of balance. Order, chaos, light, darkness -- all things must exist in perfect harmony for such is the way of the universe. This order is known as the Kinkou and it employs a triumvirate of shadow warriors to uphold its causes in the world. Kennen is one of these shadow warriors, entrusted with the sacred duty of Coursing the Sun - tirelessly conveying the justice of the Kinkou.\n\nKennen was born in Bandle City and it was said that in his first living moments he bolted first from the womb and second from the midwife who delivered him. His parents had thought that he would outgrow his boundless energy, but as he matured his energy found no limits and was matched only by his unnerving speed. Despite his astonishing gifts, he remained unnoticed (or at least uncaught, as he was quite the prankster) until, on a dare, he ran straight up the great outer wall of the Placidium. When word of this feat reached Kinkou ears, Kennen was quickly and quietly brought in for an audience. He found that the role of the Heart of the Tempest suited him, frenetically delivering both the word and the punishments of the Kinkou across the realm. He now works with his fellows Akali and Shen to enforce the balance of Valoran. This hallowed pursuit has unsurprisingly led the triumvirate to the Fields of Justice.\n\n''The Heart of the Tempest beats eternal...and those beaten remember eternally.''",
    "champion_id": 85,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KennenLightningRush.png",
    "q_name": "Thundering Shuriken",
    "passive_name": "Mark of the Storm",
    "e_description": "Kennen morphs into a lightning form, enabling him to pass through units. Any enemy unit he runs through takes damage and gets a Mark of the Storm.",
    "recommended_items": [
      2003,
      3089,
      3152,
      1055,
      3020
    ],
    "r_name": "Slicing Maelstrom",
    "r_description": "Kennen summons a storm that strikes at random nearby enemy champions for magical damage.",
    "name": "Kennen",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KennenShurikenHurlMissile1.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KennenBringTheLight.png",
    "q_description": "Kennen throws a fast moving shuriken towards a location, causing damage and adding a Mark of the Storm to any opponent that it hits.",
    "title": "the Heart of the Tempest",
    "e_name": "Lightning Rush",
    "w_description": "Kennen passively deals extra damage and adds a Mark of the Storm to his target every few attacks, and he can activate this ability to damage and add another Mark of the Storm to targets who are already marked.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Kennen.png",
    "recommended_item_names": [
      "Health Potion",
      "Rabadon's Deathcap",
      "Will of the Ancients",
      "Doran's Blade",
      "Sorcerer's Shoes"
    ],
    "w_name": "Electrical Surge",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KennenShurikenStorm.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Kennen_MarkOfStorm.png",
    "passive_description": "Kennen's abilities add a Mark of the Storm to its target for 6.25 seconds. Upon receiving 3 Marks of the Storm, an opponent is stunned for 1 second and Kennen gains 25 Energy. <br><br><span class=\"color99FF99\">The stun has a diminished effect if it occurs again within 7 seconds.<\/span>"
  },
  "86": {
    "lore": "Throughout Valoran, the resolve of Demacia's military is alternately celebrated or despised, but always respected. Their ''zero tolerance'' moral code is strictly upheld by civilians and soldiers alike. In combat, this means Demacian troops may not make excuses, flee, or surrender under any circumstance. These principles are espoused to their forces by unrivaled demagogues who lead by example. Garen, the valiant warrior who bears the title ''the Might of Demacia'', is the paradigm to which these leaders are compared. Thousands of great heroes have risen and fallen on the bloody battlefields between Demacia and its preeminent rival, Noxus. It was beneath their mighty banners of war that Garen first met steel with Katarina, the Sinister Blade. The infantrymen who beheld this event (and survived) commented that it seemed as though the two were locked in a mortal waltz against a symphony of clashing blades.\n\nGaren, the pride of the Demacian military and leader of the Dauntless Vanguard, returned from this battle breathless for the first time in his career, though some speculate that this was due to reasons other than exhaustion. The plausibility of these rumors was bolstered when, in every instance thereafter, Garen seized the opportunity to encounter the Sinister Blade again. A paragon of Demacian ethic, Garen never entertained such allegations, for he knew others couldn't understand. Even simply the pursuit of a worthy opponent on the battlefield is, to a true warrior, the reason to rise each morning. The promise of one, particularly so beautifully and diametrically opposed, is the validation of his existence. \n\n''The most effective way to kill an opponent is to slice through the man next to him.''\n-- Garen, on front line strategy",
    "champion_id": 86,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GarenE.png",
    "q_name": "Decisive Strike",
    "passive_name": "Perseverance",
    "e_description": "Garen performs a dance of death with his sword, dealing damage around him for the duration.",
    "recommended_items": [
      2003,
      1054,
      3142,
      3009,
      3083
    ],
    "r_name": "Demacian Justice",
    "r_description": "Garen calls upon the might of Demacia to deal a finishing blow to an enemy champion that deals damage based upon how much Health his target has missing.",
    "name": "Garen",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GarenQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GarenW.png",
    "q_description": "Garen gains a burst of Movement Speed, breaking free of all slows affecting him and his next attack strikes a vital area of his foe, dealing bonus damage and silencing them.",
    "title": "The Might of Demacia",
    "e_name": "Judgment",
    "w_description": "Garen passively increases his Armor and Magic Resist. He may also activate this ability to grant himself a shield that reduces incoming damage and crowd control durations for a short time.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Garen.png",
    "recommended_item_names": [
      "Health Potion",
      "Doran's Shield",
      "Youmuu's Ghostblade",
      "Boots of Swiftness",
      "Warmog's Armor"
    ],
    "w_name": "Courage",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GarenR.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Garen_Passive.png",
    "passive_description": "If Garen has not been struck by damage or enemy abilities for the last 10 seconds, Garen regenerates 0.4% of his maximum Health each second. Minion damage does not stop Perseverance. "
  },
  "89": {
    "lore": "On the upper slopes of Mount Targon, the warriors of Rakkor live and breathe only for war. However, Targon's peak is reserved for a special group of Rakkoran who answer to a ''higher'' calling. Members of this group, called the Solari, retire their mantles of war, choosing instead to devote their lives to reverence of the sun. According to legend, the Solari were formed by a warrior who could call the raw might of the sun down upon his enemies in combat. He claimed Mount Targon's summit, the point on Valoran closest to the sun, for his solar devotion, a tradition which generations of Solari have preserved to this day.\n\nLeona's parents were traditional Rakkorans, both bred for the heat of battle. To them, Leona was a problem child. She was capable of fighting as fiercely as any other - including her childhood friend, Pantheon - but she did not share their zeal for killing. She believed that the true worth of a soldier lay in her ability to defend and protect. When it came time for her Rite of Kor, a ceremony in which two Rakkoran teens battle to the death for the right to bear a relic-weapon, Leona refused to fight. For this, the Rakkoran leaders ordered her execution, but when they tried to strike the fatal blow, sunlight burst forth, bathing Mount Targon in light. As it faded, Leona stood unharmed and her executioners lay unconscious around her. The Solari immediately claimed Leona, demanding that her sentence be repealed. She donned the golden armor of the Solari and they bestowed upon her the sword and shield passed down from the ancient sun-warriors of legend. The Solari helped Leona focus her abilities, and when she was ready she left to join the League of Legends.\n\n''The sun's rays reach all of Runeterra, so too must the image of its champion.''\n-- Leona",
    "champion_id": 89,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LeonaZenithBlade.png",
    "q_name": "Shield of Daybreak",
    "passive_name": "Sunlight",
    "e_description": "Leona projects a solar image of her sword, dealing magic damage to all enemies in a line. When the image fades, the last enemy champion struck will be briefly immobilized and Leona will dash to them.",
    "recommended_items": [
      2003,
      3111,
      3302,
      3143,
      3068
    ],
    "r_name": "Solar Flare",
    "r_description": "Leona calls down a beam of solar energy, dealing damage to enemies in an area. Enemies in the center of the area are stunned, while enemies on the outside are slowed.",
    "name": "Leona",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LeonaShieldOfDaybreak.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LeonaSolarBarrier.png",
    "q_description": "Leona uses her shield to perform her next basic attack, dealing bonus magic damage and stunning the target.",
    "title": "the Radiant Dawn",
    "e_name": "Zenith Blade",
    "w_description": "Leona raises her shield to gain Armor and Magic Resistance. When the duration first ends, if there are nearby enemies, she will deal magic damage to them and prolong the duration of the effect.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Leona.png",
    "recommended_item_names": [
      "Health Potion",
      "Mercury's Treads",
      "Relic Shield",
      "Randuin's Omen",
      "Sunfire Cape"
    ],
    "w_name": "Eclipse",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LeonaSolarFlare.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/LeonaSunlight.png",
    "passive_description": "Damaging spells afflict enemies with Sunlight for 3.5 seconds. When allied Champions deal damage to those targets, they consume the Sunlight debuff to deal additional magic damage."
  },
  "90": {
    "lore": "Many men have gone mad beneath the glare of the Shurima sun, but it was during the night's chilling embrace that Malzahar relinquished his sanity. Malzahar was born a seer, blessed with the gift of prophecy. His talent, though unrefined, promised to be one of Runeterra's greatest boons, but destiny plotted him another course; his sensitivity to the roiling tides of fate allowed other, unwelcome things to tug at his subconscious mind. In his dreams, where the veil of separation is thinnest, a sinister thing beckoned.  For some time, Malzahar was able to resist its prodding solicitation, but with each passing night the voice grew louder, or perhaps deeper, until he could withstand the call no more.\n\nHe ventured into the desert without supplies, drawn by the lure of a specious charm. His destination: a lost civilization to the east, known to ancient texts as Icathia. Few believed such a place ever existed, and those who did were certain that the sands had long since devoured whatever remained. When Malzahar's cracked feet finally failed him, he found himself kneeling at the base of a bizarre crumbling obelisk. Beyond it lay the alien geometry of a ruined city and the giant decaying idols of dark and horrific gods.  His eyes, seeing what others cannot, and what none should, were filled with the essence of the Void. His once shifting visions of the future were replaced with the immutable promise of Valoran beset by creatures of the Void. Standing alone, but not alone, amidst the echoing dunes, he noticed the familiar voice escape his own lips in a parched rasp, bearing three words whose weight trembled his knees: League of Legends. Now infused with the power of the Void itself, Malzahar set off to the north to seek his fate.\n\n''The land may melt, the sea may swell, the sky may fall... but They will come.''\n-- Malzahar",
    "champion_id": 90,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AlZaharMaleficVisions.png",
    "q_name": "Call of the Void",
    "passive_name": "Summon Voidling",
    "e_description": "Malzahar infects his target's mind with cruel visions of their demise, dealing damage each second. If the target dies while afflicted by the visions, they pass on to a nearby enemy unit and Malzahar gains Mana. Malzahar's Voidlings are attracted to affected units.",
    "recommended_items": [
      3135,
      2003,
      1056,
      3116,
      3020
    ],
    "r_name": "Nether Grasp",
    "r_description": "Malzahar channels the essence of the Void to suppress an enemy champion and deal damage each second.",
    "name": "Malzahar",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AlZaharCalloftheVoid.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AlZaharNullZone.png",
    "q_description": "Malzahar opens up two portals to the Void. After a short delay, they fire projectiles that deal Magic Damage and silence enemy champions.",
    "title": "the Prophet of the Void",
    "e_name": "Malefic Visions",
    "w_description": "Malzahar creates a zone of negative energy which damages enemies that stand in it.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Malzahar.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Doran's Ring",
      "Rylai's Crystal Scepter",
      "Sorcerer's Shoes"
    ],
    "w_name": "Null Zone",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AlZaharNetherGrasp.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/AlZahar_SummonVoidling.png",
    "passive_description": "After casting 4 spells, Malzahar summons an uncontrollable Voidling to engage enemy units for 21 seconds. Voidlings have 200 + 50 x lvl Health and 20 + 5 x lvl Attack Damage.<br><br>Voidlings Grow after 7 seconds (+50% Attack Damage\/Armor), and Frenzy after 14 seconds (+100% Attack Speed)."
  },
  "91": {
    "lore": "Talon's earliest memories are the darkness of Noxus' underground passages and the reassuring steel of a blade. He remembers no family, warmth, or kindness. Instead, the clink of stolen gold and the security of a wall at his back are all the kinship he has ever craved. Kept alive only by his quick wits and deft thievery, Talon scraped out a living in the seedy underbelly of Noxus. His mastery of the blade quickly marked him as a threat, and Noxian guilds sent assassins to him with a demand: join their ranks or be killed. He left the bodies of his pursuers dumped in Noxus' moat as his response.\n\nThe assassination attempts grew increasingly dangerous until one assailant met Talon blade-for-blade in a match of strength. To his surprise, Talon was disarmed and facing down his executioner's sword when the assassin revealed himself to be General Du Couteau. The General offered Talon the choice between death at his hand, or life as an agent of the Noxian High Command. Talon chose life, on the condition that his service was to Du Couteau alone, for the only type of orders he could respect were from one he could not defeat. Talon remained in the shadows, carrying out secret missions on Du Couteau's orders that took him from the frigid lands of Freljord to the inner sanctums of Bandle City. When the general vanished, Talon considered reclaiming his freedom, but he had gained immense respect for Du Couteau after years in his service. He became obsessed with tracking down the general's whereabouts. Talon's suspicions led him to the doors of the Institute of War, where he joined the League of Legends in order to find those responsible for Du Couteau's disappearance.\n\n''The three deadliest blademasters in all of Valoran are bound to the house of Du Couteau: my father, myself, and Talon. Challenge us, if you dare.''\n-- Katarina Du Couteau",
    "champion_id": 91,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TalonCutthroat.png",
    "q_name": "Noxian Diplomacy",
    "passive_name": "Mercy",
    "e_description": "Talon instantly appears behind his target, briefly slowing them and amplifying his damage against that target.",
    "recommended_items": [
      2003,
      3035,
      3026,
      2041,
      3117
    ],
    "r_name": "Shadow Assault",
    "r_description": "Talon disperses a ring of blades and becomes invisible while gaining additional Movement Speed. When Talon emerges from invisibility, the blades converge on his location. Each time the blades move, Shadow Assault deals physical damage to enemies hit by at least one blade.  ",
    "name": "Talon",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TalonNoxianDiplomacy.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TalonRake.png",
    "q_description": "Talon's next basic attack deals bonus physical damage. If the target is a champion, they will bleed, taking additional physical damage over a period of time and revealing their location for the duration.",
    "title": "the Blade's Shadow",
    "e_name": "Cutthroat",
    "w_description": "Talon sends out a volley of daggers that then return back to him, dealing physical damage every time it passes through an enemy. Additionally the enemy is slowed for a short duration.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Talon.png",
    "recommended_item_names": [
      "Health Potion",
      "Last Whisper",
      "Guardian Angel",
      "Crystalline Flask",
      "Boots of Mobility"
    ],
    "w_name": "Rake",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/TalonShadowAssault.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/TalonMercy.png",
    "passive_description": "Talon deals 10% more damage with his basic attacks to any target that is slowed, stunned, immobilized, or suppressed."
  },
  "92": {
    "lore": "In Noxus, any citizen may rise to power regardless of race, gender, or social standing - strength is all that matters. It was with committed faith in this ideal that Riven strove to greatness. She showed early potential as a soldier, forcing herself to master the weight of a long sword when she was barely its height. She was ruthless and efficient as a warrior, but her true strength lay in her conviction. She entered battles without any trace of doubt in her mind: no ethical pause, no fear of death. Riven became a leader amongst her peers, poster child of the Noxian spirit. So exceptional was her passion that the High Command recognized her with a black stone rune sword forged and enchanted with Noxian sorcery. The weapon was heavier than a kite shield and nearly as broad - perfectly suited to her tastes. Soon after, she was deployed to Ionia as part of the Noxian invasion.\n\nWhat began as war quickly became extermination. Noxian soldiers followed the terrifying Zaunite war machines across fields of death. It wasn't the glorious combat for which Riven trained. She carried out the orders of her superiors, terminating the remnants of a beaten and fractured enemy with extreme prejudice. As the invasion continued, it became clear that the Ionian society would not be reformed, merely eliminated. During one bitter engagement, Riven's unit became surrounded by Ionian forces. They called for support as the enemy closed in around them. What they received instead was a barrage of biochemical terror launched by Singed. Riven watched as around her Ionian and Noxian alike fell victim to an unspeakably gruesome fate. She managed to escape the bombardment, though she could not erase the memory. Counted dead by Noxus, she saw an opportunity to start anew. She shattered her sword, severing ties with the past, and wandered in self-imposed exile - on a quest to seek atonement and a way to save the pure Noxian vision in which she believed.\n\n''There is a place between war and murder in which our demons lurk.''",
    "champion_id": 92,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RivenFeint.png",
    "q_name": "Broken Wings",
    "passive_name": "Runic Blade",
    "e_description": "Riven steps forward a short distance and blocks incoming damage.",
    "recommended_items": [
      3047,
      2003,
      1039,
      3071,
      3117,
      1054,
      3143
    ],
    "r_name": "Blade of the Exile",
    "r_description": "Riven empowers her keepsake weapon with energy, and gains Attack Damage and Range. During this time, she also gains the ability to use Wind Slash, a powerful ranged attack, once. ",
    "name": "Riven",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RivenTriCleave.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RivenMartyr.png",
    "q_description": "Riven lashes out in a series of strikes. This ability can be reactivated three times in a short time frame with the third hit knocking back nearby enemies.",
    "title": "the Exile",
    "e_name": "Valor",
    "w_description": "Riven emits a Ki Burst, damaging and stunning nearby enemies.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Riven.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "The Black Cleaver",
      "Boots of Mobility",
      "Doran's Shield",
      "Randuin's Omen"
    ],
    "w_name": "Ki Burst",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RivenFengShuiEngine.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/RivenRunicBlades.png",
    "passive_description": "Riven's abilities charge her blade, causing her basic attacks to deal bonus physical damage. Riven's blade may be charged up to three times and expends one charge per attack."
  },
  "96": {
    "lore": "When the prophet Malzahar was reborn in Icathia, he was led there by an ominous voice which thereafter anchored itself to his psyche. From within, this voice bestowed upon him terrible purpose, and though Malzahar was no longer tormented by its call, the voice did not cease its unrelenting summons. This baleful beacon's gentle flicker - now fastened to Runeterra - drew forth a putrid beast that ambled across a threshold it did not understand, widening a fissure between the spaces which were never meant to meet. There amongst the haunting ruins of Icathia, Kog'Maw manifested in Valoran with unsettling curiosity. The spark which led him to Runeterra teased him still, urging him gently towards Malzahar. It also encouraged him to familiarize himself with his new environment, to the stark horror of everything he encountered on his journey.\n\nThe enchanting colors and aromas of Runeterra intoxicated Kog'Maw, and he explored the fruits of the strange world the only way he knew how: by devouring them. At first he sampled only the wild flora and fauna he happened across. As he traversed the parched Tempest Flats, however, he came upon a tribe of nomads. Seemingly unhampered by conventional rules of physics, Kog'Maw consumed every nomad and any obstacles they put in his way, amounting to many times his own mass and volume. The most composed of his victims may have had time to wonder if this was due to the caustic enzymes which stung the ground as they dripped from his gaping mouth, although such musings were abruptly concluded. When his wake of catastrophe reached the Institute of War, an enthusiastic Malzahar greeted him with an enticing prospect: taste the best Runeterra could offer on the Fields of Justice.\n\n'If that's just hungry, I don't want to see angry.'\n-- Tryndamere, the Barbarian King",
    "champion_id": 96,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KogMawVoidOoze.png",
    "q_name": "Caustic Spittle",
    "passive_name": "Icathian Surprise",
    "e_description": "Kog'Maw launches a peculiar ooze which damages all enemies it passes through and leaves a trail which slows enemies who stand on it.",
    "recommended_items": [
      2003,
      3026,
      1055,
      3006,
      3031
    ],
    "r_name": "Living Artillery",
    "r_description": "Kog'Maw fires a living artillery shell at a great distance dealing damage and revealing non-stealthed targets. Additionally, multiple Living Artilleries in a short period of time cause them to cost additional Mana.",
    "name": "Kog'Maw",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KogMawQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KogMawBioArcaneBarrage.png",
    "q_description": "Passive: Increases Kog'Maw's Attack Speed. Active: Kog'Maw launches a corrosive projectile which deals Magic Damage and corrodes the target's Armor and Magic Resist for 4 seconds.",
    "title": "the Mouth of the Abyss",
    "e_name": "Void Ooze",
    "w_description": "Kog'Maw's attacks gain range and deal a percent of the target's maximum Health as Magic Damage.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/KogMaw.png",
    "recommended_item_names": [
      "Health Potion",
      "Guardian Angel",
      "Doran's Blade",
      "Berserker's Greaves",
      "Infinity Edge"
    ],
    "w_name": "Bio-Arcane Barrage",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KogMawLivingArtillery.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/KogMaw_IcathianSurprise.png",
    "passive_description": "Upon dying, Kog'Maw starts a chain reaction in his body which causes him to move faster and detonate after 4 seconds; dealing 100 + (25 x lvl) true damage to surrounding enemies."
  },
  "98": {
    "lore": "There exists an ancient order originating in the Ionian Isles dedicated to the preservation of balance. Order, chaos, light, darkness - all things must exist in perfect harmony for such is the way of the universe. This order is known as the Kinkou and it employs a triumvirate of shadow warriors to uphold its causes in the world. Shen is one of these shadow warriors, entrusted with the sacred duty of Watching the Stars - exercising judgment untainted by prejudice.\n\nBorn to a clan whose members have decorated the ranks of the Kinkou for generations, Shen was trained his entire life to become the Eye of Twilight, and thereupon to dispassionately determine what must be done in the interests of equilibrium. As his final trial to ascend to this position, he was made to attend the Takanu, a ceremony in which his father was tortured before his eyes to test his resolve. Any reaction whatsoever would have resulted in his immediate disqualification, but he never averted his gaze and never blinked, not once. As the Eye of Twilight, Shen must make decisions that would buckle the wills of ordinary men, removing all emotion from the equation. He now works with his fellows Akali and Kennen to enforce the balance of Valoran. This hallowed pursuit has unsurprisingly led the triumvirate to the Fields of Justice.\n\nThe Eye of Twilight sees not the despair of its victims, only the elegance of equilibrium.",
    "champion_id": 98,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ShenShadowDash.png",
    "q_name": "Vorpal Blade",
    "passive_name": "Ki Strike",
    "e_description": "Shen dashes rapidly toward a target location, taunting enemy champions he encounters and dealing minor damage.",
    "recommended_items": [
      3078,
      3047,
      2003,
      1039,
      1054,
      3143
    ],
    "r_name": "Stand United",
    "r_description": "Shen shields target allied champion from incoming damage, and soon after teleports to their location.",
    "name": "Shen",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ShenVorpalStar.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ShenFeint.png",
    "q_description": "Damages and life taps a target unit, healing allies that attack the target.",
    "title": "Eye of Twilight",
    "e_name": "Shadow Dash",
    "w_description": "Shen shields himself, absorbing incoming damage for a few seconds.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Shen.png",
    "recommended_item_names": [
      "Trinity Force",
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Doran's Shield",
      "Randuin's Omen"
    ],
    "w_name": "Feint",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ShenStandUnited.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Shen_KiStrike.png",
    "passive_description": "Every 8 seconds, Shen's next attack deals bonus damage."
  },
  "99": {
    "lore": "Born to the prestigious Crownguards, the paragon family of Demacian service, Luxanna was destined for greatness. She grew up as the family's only daughter, and she immediately took to the advanced education and lavish parties required of families as high profile as the Crownguards. As Lux matured, it became clear that she was extraordinarily gifted. She could play tricks that made people believe they had seen things that did not actually exist. She could also hide in plain sight. Somehow, she was able to reverse engineer arcane magical spells after seeing them cast only once. She was hailed as a prodigy, drawing the affections of the Demacian government, military, and citizens alike.\n\nAs one of the youngest women to be tested by the College of Magic, she was discovered to possess a unique command over the powers of light. The young Lux viewed this as a great gift, something for her to embrace and use in the name of good. Realizing her unique skills, the Demacian military recruited and trained her in covert operations. She quickly became renowned for her daring achievements; the most dangerous of which found her deep in the chambers of the Noxian High Command. She extracted valuable inside information about the Noxus-Ionian conflict, earning her great favor with Demacians and Ionians alike. However, reconnaissance and surveillance was not for her. A light of her people, Lux's true calling was the League of Legends, where she could follow in her brother's footsteps and unleash her gifts as an inspiration for all of Demacia.\n\n ''Her guiding light makes enemies wary, but they should worry most when the light fades.''\n - Garen, The Might of Demacia",
    "champion_id": 99,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LuxLightStrikeKugel.png",
    "q_name": "Light Binding",
    "passive_name": "Illumination",
    "e_description": "Fires an anomaly of twisted light to an area, which slows nearby enemies. Lux can detonate it to damage enemies in the area of effect.",
    "recommended_items": [
      3135,
      2003,
      3174,
      1056,
      3157
    ],
    "r_name": "Final Spark",
    "r_description": "After gathering energy, Lux fires a beam of light that deals damage to all targets in the area. In addition, triggers Lux's passive ability and refreshes the Illumination debuff duration.",
    "name": "Lux",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LuxLightBinding.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LuxPrismaticWave.png",
    "q_description": "Lux releases a sphere of light that binds and deals damage to up to two enemy units.",
    "title": "the Lady of Luminosity",
    "e_name": "Lucent Singularity",
    "w_description": "Lux throws her wand and bends the light around any friendly target it touches, protecting them from enemy damage.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Lux.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Athene's Unholy Grail",
      "Doran's Ring",
      "Zhonya's Hourglass"
    ],
    "w_name": "Prismatic Barrier",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LuxMaliceCannon.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/LuxIlluminatingFraulein.png",
    "passive_description": "Lux's damaging spells charge the target with energy for 6 seconds. Lux's next attack ignites the energy, dealing bonus magic damage (depending on Lux's level) to the target."
  },
  "101": {
    "lore": "Powerful beyond reckoning, the Ascended being known as Xerath was once a mortal of flesh and blood. He is now something vastly different - a being of writhing arcane energy. Having emerged from millennia-spanning imprisonment, he is now ready to unleash his power upon Runeterra, and utterly destroy any who oppose him.",
    "champion_id": 101,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/XerathMageSpear.png",
    "q_name": "Arcanopulse",
    "passive_name": "Mana Surge",
    "e_description": "Deals magic damage to an enemy and stuns them.",
    "recommended_items": [
      3135,
      2003,
      1056,
      3157,
      3020
    ],
    "r_name": "Rite of the Arcane",
    "r_description": "Xerath immobilizes himself and gains three shots of a long-range attack.",
    "name": "Xerath",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/XerathArcanopulseChargeUp.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/XerathArcaneBarrage2.png",
    "q_description": "Fires a long-range beam of energy, dealing magic damage to all targets hit.",
    "title": "the Magus Ascendant",
    "e_name": "Shocking Orb",
    "w_description": "Calls down a barrage of arcane energy, slowing and dealing magic damage to all enemies in an area. Targets in the middle receive additional damage and a stronger slow.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Xerath.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Doran's Ring",
      "Zhonya's Hourglass",
      "Sorcerer's Shoes"
    ],
    "w_name": "Eye of Destruction",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/XerathLocusOfPower2.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Xerath_Passive1.png",
    "passive_description": "Xerath's basic attacks periodically restore Mana."
  },
  "102": {
    "lore": "A half-breed born from the union between dragon and human, Shyvana searched all her life for belonging. Persecution forged her into a brutal warrior, and those who dare stand against Shyvana face the fiery beast lurking just beneath her skin.\n\nDragonkind considered Shyvana's impure blood an abomination, and she spent her youth pursued relentlessly by one cruel drake. Constantly on the run, she and her father, an outcast dragon, never knew a lasting home. A brutal reflection of countless battles, Shyvana grew hateful and savage. After years of strife, her father finally fell to the other dragon, but not before gravely wounding his foe. Furious with grief, Shyvana pursued her father's murderer as he fled north to recover. There she encountered a group of humans on the trail of the same drake. Though the men looked upon her in fear, their leader approached Shyvana peacefully. He introduced himself as Jarvan IV, the Prince of Demacia, and offered to aid Shyvana in her quest for vengeance. Together they hunted down and confronted the vicious dragon that had slain her father. Shyvana did not expect the men to survive, but in the clash of fire and steel, Jarvan and his men fought with strength she had never believed humans to possess. The ironclad warriors drove their foe into submission, and Shyvana struck the final blow, tearing the beast's heart from its body. Inspired by her ferocity, Jarvan offered her a place in the ranks of his elite guard. Shyvana could still see fear in the eyes of his men, but she longed for a true home. Trusting Jarvan's word, she accepted his offer and now serves as a Demacian warrior. Though her human allies admire her power, they keep their distance. Shyvana strives to repay the prince's kindness with the power of the dragon within, but she cannot help but wonder if the humans are right to fear her.\n\n''I have proven my might to dragonkind - what challenge shall humans pose?''\n-- Shyvana",
    "champion_id": 102,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ShyvanaFireball.png",
    "q_name": "Twin Bite",
    "passive_name": "Dragonborn",
    "e_description": "Shyvana unleashes a fireball that deals damage to all enemies it encounters and leaves cinders on the target, marking them for 4 seconds. Shyvana's basic attacks on marked targets deal a percentage of their maximum Health as damage on-hit.\n\n<span class=\"colorFF3300\">Dragon Form: <\/span>Flame Breath engulfs all units in a cone in front of her.",
    "recommended_items": [
      3047,
      2003,
      1039,
      1055,
      3143,
      3153
    ],
    "r_name": "Dragon's Descent",
    "r_description": "Shyvana transforms into a dragon and takes flight to a target location. Enemies along her path take damage and are knocked toward her target location.\n\nShyvana passively gains Fury per second and gains 2 Fury on basic attack.",
    "name": "Shyvana",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ShyvanaDoubleAttack.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ShyvanaImmolationAura.png",
    "q_description": "Shyvana strikes twice on her next attack. Basic attacks reduce the cooldown of Twin Bite by 0.5 seconds.\n\n<span class=\"colorFF3300\">Dragon Form: <\/span>Twin Bite cleaves all units in front Shyvana. ",
    "title": "the Half-Dragon",
    "e_name": "Flame Breath",
    "w_description": "Shyvana surrounds herself in fire, dealing magic damage per second to nearby enemies and moving faster for 3 seconds. The Movement Speed reduces over the duration of the spell. Basic attacks extend the duration of Burnout. \n\n<span class=\"colorFF3300\">Dragon Form: <\/span>Burnout scorches the ground beneath it, enemies on the scorched earth continue to take damage.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Shyvana.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Doran's Blade",
      "Randuin's Omen",
      "Blade of the Ruined King"
    ],
    "w_name": "Burnout",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ShyvanaTransformCast.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/ShyvanaReinforcedScales.png",
    "passive_description": "<mainText>Shyvana gains bonus Armor and Magic Resistance. These bonuses are doubled while Shyvana is in Dragon Form.<\/mainText>"
  },
  "103": {
    "lore": "Unlike other foxes that roamed the woods of southern Ionia, Ahri had always felt a strange connection to the magical world around her; a connection that was somehow incomplete. Deep inside, she felt the skin she had been born into was an ill fit for her and dreamt of one day becoming human. Her goal seemed forever out of reach, until she happened upon the wake of a human battle. It was a grisly scene, the land obscured by the forms of wounded and dying soldiers. She felt drawn to one: a robed man encircled by a waning field of magic, his life quickly slipping away. She approached him and something deep inside of her triggered, reaching out to the man in a way she couldn't understand. His life essence poured into her, carried on invisible strands of magic. The sensation was intoxicating and overwhelming. As her reverie faded, she was delighted to discover that she had changed. Her sleek white fur had receded and her body was long and lithe - the shape of the humans who lay scattered about her.\n\nHowever, though she appeared human, she knew that in truth the transformation was incomplete. A cunning creature, she adapted herself to the customs of human society and used her profound gift of beauty to attract unsuspecting men. She could consume their life essences when they were under the spell of her seductive charms. Feeding on their desires brought her closer to her dream, but as she took more lives, a strange sense of regret began to well within her. She had reservations about actions which never troubled her as a fox. She realized that she could not overcome the pangs of her evolving morality. In search of a solution, Ahri found the Institute of War, home of the most gifted mages on Runeterra. They offered her a chance to attain her humanity without further harm through service in the League of Legends.\n\n''Mercy is a human luxury... and responsibility.''\n-- Ahri",
    "champion_id": 103,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AhriSeduce.png",
    "q_name": "Orb of Deception",
    "passive_name": "Essence Theft",
    "e_description": "Ahri blows a kiss that damages and charms an enemy it encounters, causing them to walk harmlessly towards her.",
    "recommended_items": [
      1001,
      1056,
      3151,
      1028,
      3010
    ],
    "r_name": "Spirit Rush",
    "r_description": "Ahri dashes forward and fires essence bolts, damaging 3 nearby enemies (prioritizes Champions). Spirit Rush can be cast up to three times before going on cooldown.",
    "name": "Ahri",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AhriOrbofDeception.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AhriFoxFire.png",
    "q_description": "Ahri sends out and pulls back her orb, dealing magic damage on the way out and true damage on the way back. Ahri gains movement speed that decays while her orb is traveling.",
    "title": "the Nine-Tailed Fox",
    "e_name": "Charm",
    "w_description": "Ahri releases three fox-fires, that lock onto and attack nearby enemies.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Ahri.png",
    "recommended_item_names": [
      "Boots of Speed",
      "Doran's Ring",
      "Liandry's Torment",
      "Ruby Crystal",
      "Catalyst the Protector"
    ],
    "w_name": "Fox-Fire",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AhriTumble.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Ahri_SoulEater.png",
    "passive_description": "Gains a charge of Essence Theft whenever a spell hits an enemy (max: 3 charges per spell). Upon reaching 9 charges, Ahri's next spell heals her whenever it hits an enemy."
  },
  "104": {
    "lore": "Malcolm Graves was born in the back of a Bilgewater tavern and left there with a bottle of spiked milk. He survived a childhood in the pirate-run slums using every dirty trick in the book. Intent on building a new life for himself, he stowed away on the first ship to the mainland he could sneak aboard. However, the grim realities of the world forced him to eke out an unsavory living in the underground of various city-states, jumping the border whenever things got too hot. At a particularly high-stakes game of cards, he found himself seated opposite Twisted Fate. They both flipped four aces on the final hand.  It was the first time either conman had met his equal. The two formed an alliance, swindling marks at the tables and scrapping back-to-back in the alleys afterward. Together, they ran the streets - stacking chips, decks, and charges.\n\nUnfortunately Graves made the mistake of hustling a hefty sum from Dr. Aregor Priggs, a high-ranking Zaunite official and businessman. When Priggs discovered how he'd been played, he became obsessed with revenge. He learned about Twisted Fate's all-consuming desire to control magic and he promptly offered him a trade: serve Graves up in exchange for enrollment in a procedure which would grant his wish. Twisted Fate took the deal - both he and Graves knew the stakes of their arrangement, but the offer was too good. Once acquired, Priggs had Graves taken to a special location built to hold men whose crimes - or more precisely their punishments - were meant to stay off the books. Graves endured years of captivity at the hands of Zaun's most unscrupulous wardens before he managed to escape. One of his fellow detainees introduced him to an eccentric gunsmith who modified a shotgun exactly to his specifications. After he paid a visit to Priggs, Graves joined the League of Legends with two targets in his sights: Twisted Fate and payback.\n\n''They got a saying in the locker: ain't got nothin' but time to plan.''\n-Graves",
    "champion_id": 104,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GravesMove.png",
    "q_name": "Buckshot",
    "passive_name": "True Grit",
    "e_description": "Graves dashes forward gaining an Attack Speed boost for several seconds. Hitting enemies with basic attacks lowers the cooldown of this skill. ",
    "recommended_items": [
      3102,
      2003,
      3035,
      1055,
      3006
    ],
    "r_name": "Collateral Damage",
    "r_description": "Graves fires an explosive shell dealing heavy damage to the first champion it hits. After hitting a champion or reaching the end of its range, the shell explodes dealing damage in a cone. ",
    "name": "Graves",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GravesClusterShot.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GravesSmokeGrenade.png",
    "q_description": "Graves fires three bullets in a cone, damaging all enemies in their paths.",
    "title": "the Outlaw",
    "e_name": "Quickdraw",
    "w_description": "Graves fires a smoke canister at the target area creating a cloud of smoke. Enemies inside the smoke cloud have reduced sight range and Movement Speed. ",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Graves.png",
    "recommended_item_names": [
      "Banshee's Veil",
      "Health Potion",
      "Last Whisper",
      "Doran's Blade",
      "Berserker's Greaves"
    ],
    "w_name": "Smoke Screen",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/GravesChargeShot.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/GravesTrueGrit.png",
    "passive_description": "Graves gains increasing Armor and Magic Resistance the longer he remains in combat. "
  },
  "105": {
    "lore": "Centuries ago, an ancient water-dwelling race built a hidden city beneath a mountain in the sea. Though these creatures had their enemies, the city was an impenetrable fortress, and, in the safety it provided, they grew complacent. Fizz, however, harbored a curious spirit that could not be satisfied living so cushioned a life. Unable to resist the allure of danger, Fizz had a habit of sneaking out of the city to look for trouble. In his many adventures he grew to be a powerful fighter with a keen resourcefulness that let him skirt danger with clever ease. One day, Fizz returned to find the city abandoned: his people had vanished, leaving Fizz without a clue to explain their disappearance. With nothing left in the city to keep him, Fizz salvaged an enchanted trident from the ruins and set out alone.\n\nFor years, Fizz wandered the ocean, using the skills he'd learned during his adventures as a young boy to survive. Finally, Fizz discovered the port of Bilgewater. He was fascinated with the existence of life above the water and could not resist exploring the island. In his endless curiosity, Fizz inadverently meddled in the affairs of the humans who lived there and his presence did not go unnoticed. His mischief angered many residents who eventually sought to capture or kill him. Fizz found himself cornered, and he prepared to return to the sea despite the fondness he'd come to hold for Bilgewater. As he stood at the docks, a massive dragon-shark attacked the port. Fizz defeated the beast, using his resourcefulness and knowledge of the creatures' weaknesses to his advantage. Having earned the gratitude and respect of the humans, Fizz decided to stay in Bilgewater. He joined the League of Legends to further serve his new home.\n\n''Fizz makes even the saltiest sailors of Bilgewater look like drunken landlubbers in a fight. Good thing he's on our side.''\n-- Miss Fortune, the Bounty Hunter",
    "champion_id": 105,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FizzJump.png",
    "q_name": "Urchin Strike",
    "passive_name": "Nimble Fighter",
    "e_description": "Fizz hops into the air, landing gracefully upon his spear and becoming untargetable. From this position, Fizz can either slam the ground or choose to jump again before smashing back down.",
    "recommended_items": [
      3135,
      2003,
      3026,
      1056,
      3020
    ],
    "r_name": "Chum the Waters",
    "r_description": "Fizz unleashes a magical fish that latches onto enemies or hovers over terrain, slowing champions if it is latched on to them. After a brief delay, a shark erupts from beneath the earth, dealing damage to enemies around the fish and knocking them aside.",
    "name": "Fizz",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FizzPiercingStrike.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FizzSeastonePassive.png",
    "q_description": "Fizz strikes his target and runs them through, dealing magic damage and applying on hit effects.",
    "title": "the Tidal Trickster",
    "e_name": "Playful \/ Trickster",
    "w_description": "Fizz's Trident causes rending wounds in his opponents, dealing Magic Damage to the target based on their missing Health and reducing their healing and regeneration.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Fizz.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Guardian Angel",
      "Doran's Ring",
      "Sorcerer's Shoes"
    ],
    "w_name": "Seastone Trident",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FizzMarinerDoom.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/FizzPassive.png",
    "passive_description": "Fizz's dexterity allows him to move through units and take less physical damage from basic attacks."
  },
  "106": {
    "lore": "The unforgiving northern reaches of the Freljord are home to the Ursine, a fierce and warlike race that has endured the barren tundra for thousands of years. Their leader is a furious adversary who commands the force of lightning to strike fear within his foes: Volibear. Both a warrior and a mystic, Volibear seeks to defend the ancient ways and the warrior spirit of his tribe.\n\nThough history recorded their once legendary feats in battle, the Ursine now lived in tranquil seclusion. The warriors were headed by a triumvirate of leaders who maintained a long-lived isolation, avoiding the petty affairs and conflicts of others. As shaman to the three, Volibear was a respected sage known for his insight. It was an era of unprecedented peace, but Volibear felt dread stirring within him. Prosperity was turning the tribe soft and weak, and many had long forgotten the sacred art of war. In time, Volibear felt the fire of their souls would be extinguished. When he revealed his misgivings to the triumvirate, they refused to listen and warned him to know his place.\n\nSeeking wisdom, Volibear undertook a perilous climb to the peak of the Ursine's sacred mountain, a place forever shrouded in a thundering maelstrom. The eye of the storm was said to bestow portents, and legend held that the tempest would mark the next great chieftain of the tribe. As Volibear ascended the peak, he was struck by an unnatural bolt of lightning. When the shaman awoke, he was possessed by a horrific vision of the Freljord utterly consumed by darkness. Volibear saw an unprepared and complacent Ursine force slaughtered by terrible creatures of ice. In an instant, he knew his race would perish if they did not prepare for war.\n\nVolibear rushed down the mountainside to recount what he had seen, but found the path blocked by three Ursine - the triumvirate. Knowing he would end the lasting peace, they refused to heed Volibear's warning and demanded his silence, by his word - or his death. Resolute and adamant, Volibear swore that the Ursine's very survival depended on his message, and launched into ferocious combat against the three. A terrible clash ensued, and just as Volibear succumbed to his opponents, he called upon the power of the maelstrom. Unleashing raw lightning, he struck the trio down with a thunderous blow. Stunned and astonished, the triumvirate beheld the sign of Ursine leadership: the force of the sacred storm.\n\nRecognizing his foretold ascendance, the triumvirate appointed Volibear as the Ursine's new leader. His influence was swift and decisive: he roused his tribe from complacency, revived their battle-hardened traditions, and allied with Sejuani, the warrior who would fight with them against the coming evil. With time, the tribe grew lean and fierce, becoming known again as fearsome warriors of legend. Volibear and the Ursine now stand ready for the dark day that looms on the icy horizon.\n\n''The Ursine cannot know peace without war.''\n\n-- Volibear",
    "champion_id": 106,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VolibearE.png",
    "q_name": "Rolling Thunder",
    "passive_name": "Chosen of the Storm",
    "e_description": "Volibear lets out a powerful roar that damages and slows enemies. Minions and monsters are feared as well.",
    "recommended_items": [
      3078,
      2003,
      1039,
      3111,
      3117,
      1054,
      3143
    ],
    "r_name": "Thunder Claws",
    "r_description": "Volibear channels the power of the storm causing his attacks to blast his targets with lightning that bounces to other nearby enemies.",
    "name": "Volibear",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VolibearQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VolibearW.png",
    "q_description": "Volibear drops to all fours and runs faster. This bonus speed increases when chasing enemy champions. The first enemy he attacks is thrown backwards over Volibear.",
    "title": "the Thunder's Roar",
    "e_name": "Majestic Roar",
    "w_description": "Volibear's repeated attacks grant him additional Attack Speed. Once Volibear has repeatedly attacked three times, he can perform a vicious bite on his target which deals increased damage based on the target's missing Health.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Volibear.png",
    "recommended_item_names": [
      "Trinity Force",
      "Health Potion",
      "Hunter's Machete",
      "Mercury's Treads",
      "Boots of Mobility",
      "Doran's Shield",
      "Randuin's Omen"
    ],
    "w_name": "Frenzy",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VolibearR.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/VolibearPassive.png",
    "passive_description": "Volibear heals rapidly for a few seconds when his Health drops to a critical level."
  },
  "107": {
    "lore": "On every wall of his den, the trophy hunter Rengar mounts the heads, horns, claws, and fangs of the most lethal creatures in Valoran. Though his collection is extensive, he remains unsatisfied, tirelessly seeking greater game. He takes time with every kill, studying his prey, learning, and preparing himself for the next encounter with the one monster he never managed to defeat.\n\nRengar never knew his real parents, but was raised by a human who was revered as a legendary hunter. He was an ideal pupil, intently absorbing the lessons of his father, and improving them with his uncanny feral instincts. Before his mane had fully grown, Rengar set off on his own and claimed a wide territory for himself. Along its perimeter, he mounted the skulls of his slain prey - a warning to would-be aggressors. He thought undisputed reign of a region would fulfill him, but instead, he grew restless. No beasts in his domain proved challenging prey, and without formidable adversaries to push his limits, Rengar's spirit waned. He feared that no worthwhile game remained, that he would never again feel the thrill of the hunt. Just when things seemed their bleakest, he encountered the monster. It was a disturbing, alien thing, distinctly out of place in his world. It bore huge scything claws and devoured any animal that strayed across its path. Overzealous at the prospect of a challenge, Rengar ambushed the monster in haste. It far outclassed anything he'd hunted before. Their fight was savage, and each suffered crippling wounds. Rengar lost an eye, but the most grievous blow was to his pride. He had never before failed to make the kill. Worse yet, the severity of his injuries forced him to retreat. Over the following days, he hovered on the threshold between life and death. He was wracked with pain, but beneath it, he felt a glimmer of joy. The hunt was on. If such powerful beings existed in the world, he would find them, and stack their heads high. The monster, however, was a kill he wanted to savor. On his den's largest wall, he reserves a space for the beast's head, a trophy he swears will one day be the centerpiece of his collection.\n\n''Prey on the weak and you will survive, prey on the strong and you will live.''\n-- Rengar",
    "champion_id": 107,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RengarE.png",
    "q_name": "Savagery",
    "passive_name": "Unseen Predator",
    "e_description": "Rengar throws a bola, slowing the first target hit for a short duration.\nFerocity effect: Roots the target.",
    "recommended_items": [
      3047,
      2003,
      1039,
      3117,
      1054,
      3143,
      3153
    ],
    "r_name": "Thrill of the Hunt",
    "r_description": "Rengar activates his predatory instincts, stealthing himself and revealing all enemy Champions in a large radius around him. While stealthed, he gains Movement Speed when he moves towards enemies and his next attack will cause him to leap. He gains Movement Speed and rapidly generates Ferocity after he breaks stealth.",
    "name": "Rengar",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RengarQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RengarW.png",
    "q_description": "Rengar's next basic attack deals bonus damage.\nFerocity effect: Rengar deals enhanced damage and grants him Attack Speed and Attack Damage.",
    "title": "the Pridestalker",
    "e_name": "Bola Strike",
    "w_description": "Rengar lets out a battle roar, damaging enemies and gaining bonus Armor and Magic Resist for a short duration.\nFerocity effect: Rengar heals for a large amount.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Rengar.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Boots of Mobility",
      "Doran's Shield",
      "Randuin's Omen",
      "Blade of the Ruined King"
    ],
    "w_name": "Battle Roar",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/RengarR.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Rengar_Passive.png",
    "passive_description": "While in brush or stealth Rengar will leap at the target when using his basic attack.<br><br><span class=\"colorEDDA74\">Rengar builds 1 point of Ferocity with each ability he uses on enemies. When reaching 5 points of Ferocity, Rengar's next ability becomes empowered, granting it a bonus effect.<\/span>"
  },
  "110": {
    "lore": "For his incomparable skill with the bow and his unquestioned sense of honor, Varus was chosen to be the warden of a sacred Ionian temple. The temple was built to contain an ancient pit of corruption so vile that Ionian Elders feared it could envelop the island in darkness. Varus prided himself on his position, as only the most exceptional Ionian warriors were selected for the role. He lived with his family in a nearby village and led a quiet life of disciplined routine until the day the forces of Noxus invaded Ionia. Their shock troops left nothing but death and desolation in their wake, and the temple lay in their path. Varus was forced to make a decision. He was bound by honor to stay and defend the temple, but without him the village's few inhabitants could offer little resistance against the oncoming war machine. Gravely, he chose to fulfill his duty as a warden. The corruption could not be allowed to escape.\n\nHis arrows sundered the troops who tried to wrest the temple from him that day. However, when he returned to the village, he found that it had been reduced to a smoldering graveyard. Remorse at the sight of his slain family gave way to overwhelming regret and then to seething hatred. He swore to slaughter every Noxian invader, but first he needed to become stronger. He turned to that which he had sacrificed everything to protect. The pit of corruption would consume him wholly, as a flame devours a wick, but its abominable power would burn within him until he was lost. This was a path from which there could be no return. With grim resolve, he condemned himself to the black flames, feeling malevolent energy bond to his skin...and with it, the promise of ruin. He left, seeking the blood of all Noxians involved with the invasion, a grisly task that eventually led him to the invasion's most infamous perpetrators in the League of Legends.\n\n''The life of an arrow is fleeting, built of nothing but direction and intent.''\n-- Varus",
    "champion_id": 110,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VarusE.png",
    "q_name": "Piercing Arrow",
    "passive_name": "Living Vengeance",
    "e_description": "Varus fires a hail of arrows that deal physical damage and desecrate the ground. Desecrated ground slows enemies' Movement Speed and reduces their healing and regeneration. ",
    "recommended_items": [
      3072,
      3102,
      2003,
      1055,
      3006
    ],
    "r_name": "Chain of Corruption",
    "r_description": "Varus flings out a damaging tendril of corruption that immobilizes the first enemy champion hit and then spreads towards nearby uninfected champions, immobilizing them too on contact. ",
    "name": "Varus",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VarusQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VarusW.png",
    "q_description": "Varus readies and then fires a powerful shot that gains extra range and damage the longer he spends preparing to fire.",
    "title": "the Arrow of Retribution",
    "e_name": "Hail of Arrows",
    "w_description": "Varus' basic attacks deal bonus magic damage and apply Blight. Varus' other abilities detonate Blight, dealing magic damage based on the target's maximum Health.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Varus.png",
    "recommended_item_names": [
      "The Bloodthirster",
      "Banshee's Veil",
      "Health Potion",
      "Doran's Blade",
      "Berserker's Greaves"
    ],
    "w_name": "Blighted Quiver",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VarusR.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/VarusPassive.png",
    "passive_description": "On kill or assist, Varus temporarily gains Attack Speed. This bonus is larger if the enemy is a champion."
  },
  "111": {
    "lore": "Once, Nautilus was a sailor commissioned by the Institute of War to explore the uncharted reaches of the Guardian's Sea. This expedition took him deep into unknown waters where he and his crew found a vast section of black oozing liquid that none of the crew could identify. Though their job was to investigate anything new that they found, no man aboard was willing to brave the murk except Nautilus. Only moments after he donned the hulking diver's suit and climbed over the ship's rail, something lurking in the muck grabbed hold of him. He clung to the side of the ship, but the thing below pulled him fiercely, rocking the entire ship. The other sailors grew afraid and made a terrible decision. As he stared and pled for help, they wrenched his grip free of the rail. He tumbled into the ink, grabbing the anchor in futile desperation. Dark tendrils enveloped him and he could do nothing but watch as the dimming outline of his ship faded away. Then everything went black.\n\nWhen Nautilus awoke, he was something... different. The great iron suit had become a seamless shell around him, concealing whatever awful truth lay inside. All the details of his memory seemed fuzzy and indistinct but one fact remained clear: he was left here, alone in the sunless depths, to die. In his hands he still clutched the anchor that belonged to the men who had condemned him. Having no other purpose, he took this clue and trudged - too heavy to swim or run - in search of answers. He wandered without direction or sense of passing time in what felt like an eternal dream. By the time he stumbled upon the shores of Bilgewater, he could find no traces of the man he was. No house, no family, no life to which he could return. Terrified sailors who'd heard his tale directed Nautilus back to the Institute, but the summoners refused to relinquish the names of the others they commissioned. By then Nautilus had learned about the League of Legends and there he saw an opportunity to discover and punish those responsible for the time and life he lost.\n\n''When consumed by utter darkness, there is nothing left but forward.''\n-- Nautilus",
    "champion_id": 111,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NautilusSplashZone.png",
    "q_name": "Dredge Line",
    "passive_name": "Staggering Blow",
    "e_description": "Nautilus slams the ground, causing the earth to explode around him in a set of three explosions. Each explosion damages and slows enemies.",
    "recommended_items": [
      2003,
      1039,
      3111,
      3117,
      1054,
      3143,
      3068
    ],
    "r_name": "Depth Charge",
    "r_description": "Nautilus fires a shockwave into the earth that chases an opponent. This shockwave rips up the earth above it, knocking enemies into the air. When it reaches the opponent, the shockwave erupts, knocking his target into the air and stunning them.",
    "name": "Nautilus",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NautilusAnchorDrag.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NautilusPiercingGaze.png",
    "q_description": "Nautilus hurls his anchor forward. If it hits a champion, he drags both himself and the opponent close together. If it hits terrain, Nautilus instead pulls himself to the anchor and the cooldown of Dredge Line is reduced by half.",
    "title": "the Titan of the Depths",
    "e_name": "Riptide",
    "w_description": "Nautilus surrounds himself with dark energies, gaining a shield that blocks incoming damage. While the shield persists, his attacks apply a damage over time effect to enemies around his target.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Nautilus.png",
    "recommended_item_names": [
      "Health Potion",
      "Hunter's Machete",
      "Mercury's Treads",
      "Boots of Mobility",
      "Doran's Shield",
      "Randuin's Omen",
      "Sunfire Cape"
    ],
    "w_name": "Titan's Wrath",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/NautilusGrandLine.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Nautilus_StaggeringBlow.png",
    "passive_description": "Nautilus' basic attacks deal bonus physical damage and immobilize his targets. This effect cannot happen more than once every few seconds on the same target."
  },
  "112": {
    "lore": "Early in life, Viktor discovered his passion for science and invention, particularly in the field of mechanical automation. He attended Zaun's prestigious College of Techmaturgy and led the team that constructed Blitzcrank - a scientific breakthrough that he expected to vault him to the top of his profession. Unfortunately his triumph was usurped by Professor Stanwick, who stole credit for developing Blitzcrank's sentience and later used Viktor's research to revive Urgot. Viktor's appeals for justice fell on deaf ears, and he sank into a deep depression. He withdrew from the College and barricaded himself in his private laboratory, cutting all human ties.  There, in secret, he conceived a project for which nobody else could claim credit. Desiring both to revolutionize his field and to eliminate the jealous human emotions which festered inside him, he engineered parts to replace and improve his own body.\n\nWhen Viktor re-emerged, almost no trace of the original man remained. Not only had he supplanted the majority of his anatomy, but his personality had changed. His previous hope to better society was replaced by an obsession with what he called ''the glorious evolution.'' He saw himself as the patron and pioneer of Valoran's future - a future in which man would renounce his flesh in favor of superior hextech augmentations. Though Viktor's initial appeals were met with heavy skepticism, scientists were confounded by the sophistication of his machinery. By integrating his mind with techmaturgical devices, he had been able to drastically accelerate the progress of his research.  His transformation had stripped him of what he perceived as his emotional weaknesses, but there was some lingering residue of resentment against the Professor. Viktor joined the League of Legends to pit his inventions against the greatest opponents Valoran could offer, and to correct any weaknesses or inefficiencies that remained.\n\n''In one's hand, techmaturgy is a tool. As one's hand, it is liberation.''\n-- Viktor",
    "champion_id": 112,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ViktorDeathRay.png",
    "q_name": "Siphon Power",
    "passive_name": "Glorious Evolution",
    "e_description": "Viktor uses his robotic arm to fire a chaos beam that cuts across the field in a line, dealing damage to all enemies in its path.\n\nAugment: An explosion follows the Death Ray's wake, dealing magic damage.",
    "recommended_items": [
      3135,
      2003,
      1056,
      3116,
      3020
    ],
    "r_name": "Chaos Storm",
    "r_description": "Viktor conjures a singularity on the field which deals magic damage and interrupts enemy channels. The singularity then does magic damage to all nearby enemies every second. Viktor can redirect the singularity.\n\nAugment: The Chaos Storm moves faster.",
    "name": "Viktor",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ViktorPowerTransfer.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ViktorGravitonField.png",
    "q_description": "Viktor blasts an enemy unit dealing magic damage, gaining a shield and empowering his next basic attack.\n\nAugment: Viktor gains bonus Movement Speed after casting.",
    "title": "the Machine Herald",
    "e_name": "Death Ray",
    "w_description": "Viktor conjures a heavy gravitational field that slows enemies in its radius. Enemies who stay within the device for too long are stunned.\n\nAugment: Enemies stunned by Gravity Field are dragged to the center.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Viktor.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Doran's Ring",
      "Rylai's Crystal Scepter",
      "Sorcerer's Shoes"
    ],
    "w_name": "Gravity Field",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ViktorChaosStorm.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Viktor_Passive.png",
    "passive_description": "Viktor starts with the Prototype Hex Core that can be upgraded three times in the store to augment his abilities."
  },
  "113": {
    "lore": "Sejuani was weaned on hardship and reared on barbarity. Where others succumbed to the harshness of the Freljord, she was tempered by it until pain became power, hunger an encouragement, and frost an ally in culling the weak. Through her ordeals, she learned that to thrive in the endless winter, one must become just as cold and unforgiving. In Sejuani's eyes, her followers either have the mettle to endure or the right to die. Once she has conquered the Freljord, she knows that those who survive will form a nation to be feared.\n\nAs a child, the leader of the Winter's Claw watched her tribe's numbers slowly dwindle. Cold and starvation took all but the most resilient. She was the only one of her siblings to survive to her tenth year, leaving Sejuani sure that she too would die in misery. In desperation, she sought spiritual counsel from her tribe's mystic. But the seer did not foretell Sejuani's death. Instead, she prophesized that Sejuani would one day conquer and unite the divided tribes of the Freljord.\n\nArmored with absolute faith in her destiny, Sejuani pushed herself to extremes that would have killed anyone without her will to endure. She walked into blizzards without food or furs and trained while frigid winds raked her flesh. She clashed with the strongest warriors of her tribe, one after another, until her legs gave out beneath her. When she assumed leadership of her tribe, Sejuani commanded her warriors to follow her example. Under her rule, the tribe grew stronger than they had ever been.\n\nIn the end, it was an offer of peace - rather than an act of war - that began Sejuani's campaign of conquest. On the first day of winter, envoys from Ashe's tribe approached Sejuani's camp bearing a gift of Avarosan grain. Ashe's intent was clear: if Sejuani united with her tribe, the Winter's Claw would never go hungry again. To Sejuani, the gift was an insult. In Ashe's tribe, she saw men and women, slight and soft, who preferred to farm instead of fight. Her contempt for them was absolute.\n\nSejuani gathered her people and set the grain alight. She proclaimed that Ashe's offer of charity would bring only weakness. Stripping the envoys of their supplies, Sejuani sent them back with a message: the Winter's Claw would prove to the Avarosan that only the strong deserve to survive in the Freljord. As the grain burned behind them, Sejuani rode out with her warband to inflict the first of many painful lessons to come.\n\n''I was cut from the ice, shaped in the storms, hardened in the cold.''\n-- Sejuani",
    "champion_id": 113,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SejuaniWintersClaw.png",
    "q_name": "Arctic Assault",
    "passive_name": "Frost",
    "e_description": "Abilities and basic attacks apply Frost to enemies. Activating Permafrost damages and slows all nearby enemies with Frost.",
    "recommended_items": [
      3047,
      2003,
      1039,
      2041,
      3117,
      3143,
      3068
    ],
    "r_name": "Glacial Prison",
    "r_description": "Sejuani throws her True Ice bola in a line. If the bola hits an enemy champion, it shatters, stunning the target and nearby enemies. If the bola reaches its maximum range, it shatters and slows nearby enemies. ",
    "name": "Sejuani",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SejuaniArcticAssault.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SejuaniNorthernWinds.png",
    "q_description": "Charges forward, dealing magic damage and knocking enemies into the air. The charge stops after knocking an enemy champion into the air.",
    "title": "the Winter's Wrath",
    "e_name": "Permafrost",
    "w_description": "Sejuani's next basic attack deals bonus magic damage to the target and enemies near it. She then spins her flail, dealing magic damage to nearby enemies.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Sejuani.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Crystalline Flask",
      "Boots of Mobility",
      "Randuin's Omen",
      "Sunfire Cape"
    ],
    "w_name": "Flail of the Northern Winds",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SejuaniGlacialPrisonStart.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Sejuani_Passive.png",
    "passive_description": "Damaging an enemy with an ability or basic attack grants Sejuani bonus Armor and reduces movement-slowing effects on her."
  },
  "114": {
    "lore": "Fiora, Demacia's most notorious duelist, earned her fame with her sharp blade and sharper tongue. She boasts the refinement of an aristocratic upbringing, and a fierce devotion to the perfection of her craft. Having surpassed her peers at home, Fiora now seeks greater foes. She will settle for nothing less than the world's acknowledgement of her mastery.\n\nAs the youngest child of House Laurent, a family known for its long line of elite duelists, Fiora considered herself destined for greatness. She longed to match the skill of her father, a legendary swordsman, and her talent quickly surpassed that of her siblings. Fiora's peers perceived her confidence as arrogance, but she dismissed them, striving even harder to become a worthy successor to her father. Her devotion turned out to be misplaced. On the eve of an arranged duel, authorities caught Fiora's father slipping a paralysis poison into his opponent's drink. His treachery destroyed the family's reputation, and Fiora's own honor fell under question. Outraged and desperate to clear her name, she challenged her father to a duel. Though he fought with power and style, Fiora realized the man had long forgotten the discipline that defined a true duelist. She disarmed him, and with her blade to his chest, she demanded control of House Laurent. Her father surrendered, but even in victory, Fiora knew the shadow of doubt still tainted her reputation. Intent to seize her destiny, Fiora vows to surpass her father's false legacy and prove that she is not only the greatest duelist in Demacia - but all of Valoran.\n\n''I came here seeking a challenge - is this the best these fools can offer me?''\n-- Fiora",
    "champion_id": 114,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FioraFlurry.png",
    "q_name": "Lunge",
    "passive_name": "Duelist",
    "e_description": "Fiora temporarily gains additional Attack Speed. Each basic attack or Lunge she lands during this time increases her Movement Speed. Killing a champion refreshes the cooldown on Burst of Speed.",
    "recommended_items": [
      2003,
      3026,
      1055,
      3006,
      3142
    ],
    "r_name": "Blade Waltz",
    "r_description": "Fiora dashes around the battlefield to deal physical damage to enemy champions. Successive strikes against the same target deal less damage.",
    "name": "Fiora",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FioraQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FioraRiposte.png",
    "q_description": "Fiora dashes forward to strike her target, dealing physical damage. Fiora can perform the dash a second time within a couple seconds at no Mana cost.",
    "title": "the Grand Duelist",
    "e_name": "Burst of Speed",
    "w_description": "Fiora's Attack Damage is increased. When activated, Fiora parries the next basic attack and reflects magic damage back to the attacker. Works against champions, large monsters and large minions.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Fiora.png",
    "recommended_item_names": [
      "Health Potion",
      "Guardian Angel",
      "Doran's Blade",
      "Berserker's Greaves",
      "Youmuu's Ghostblade"
    ],
    "w_name": "Riposte",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/FioraDance.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Fiora_Duelist.png",
    "passive_description": "Fiora regenerates Health over 6 seconds each time she deals damage. Striking champions will cause this effect to stack up to 4 times."
  },
  "115": {
    "lore": "Ziggs was born with a talent for tinkering, but his chaotic, hyperactive nature was unusual among yordle scientists. Aspiring to be a revered inventor like Heimerdinger, he rattled through ambitious projects with manic zeal, emboldened by both his explosive failures and his unprecedented discoveries. Word of Ziggs' volatile experimentation reached the famed Yordle Academy in Piltover and its esteemed professors invited him to demonstrate his craft. His characteristic disregard for safety brought the presentation to an early conclusion, however, when the hextech engine Ziggs was demonstrating overheated and exploded, blowing a huge hole in the wall of the Academy. The professors dusted themselves off and sternly motioned for him to leave. Devastated, Ziggs prepared to return to Bandle City in shame. However, before he could leave, a group of Zaunite agents infiltrated the Academy and kidnapped the professors. The Piltover military tracked the captives to a Zaunite prison, but their weapons were incapable of destroying the fortified walls. Determined to outdo them, Ziggs began experimenting on a new kind of armament, and quickly realized that he could harness his accidental gift for demolition to save the captured yordles.\n\nBefore long, Ziggs had created a line of powerful bombs he lovingly dubbed ''hexplosives.'' With his new creations ready for their first trial, Ziggs traveled to Zaun and sneaked into the prison compound. He launched a gigantic bomb at the prison and watched with glee as the explosion tore through the reinforced wall. Once the smoke had cleared, Ziggs scuttled into the facility, sending guards running with a hail of bombs. He rushed to the cell, blew the door off its hinges, and led the captive yordles to freedom. Upon returning to the Academy, the humbled professors recognized Ziggs with an honorary title - Dean of Demolitions - and proposed that he demonstrate this new form of yordle ingenuity in the League of Legends. Vindicated at last, Ziggs accepted the proposal, eager to bring his ever-expanding range of hexplosives to the greatest testing grounds in the world: the Fields of Justice.\n\n''Ziggs? Unpredictable, dangerous, yes yes. But quite brilliant!''\n-- Heimerdinger",
    "champion_id": 115,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZiggsE.png",
    "q_name": "Bouncing Bomb",
    "passive_name": "Short Fuse",
    "e_description": "Ziggs scatters proximity mines that detonate on enemy contact, dealing magic damage and slowing.",
    "recommended_items": [
      3135,
      2003,
      1056,
      3157,
      3020
    ],
    "r_name": "Mega Inferno Bomb",
    "r_description": "Ziggs deploys his ultimate creation, the Mega Inferno Bomb, hurling it an enormous distance. Enemies in the primary blast zone take more damage than those farther away. ",
    "name": "Ziggs",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZiggsQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZiggsW.png",
    "q_description": "Ziggs throws a bouncing bomb that deals magic damage.",
    "title": "the Hexplosives Expert",
    "e_name": "Hexplosive Minefield",
    "w_description": "Ziggs flings an explosive charge that detonates after 4 seconds, or when this ability is activated again. The explosion deals magic damage to enemies, knocking them away. Ziggs is also knocked away, but takes no damage.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Ziggs.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Doran's Ring",
      "Zhonya's Hourglass",
      "Sorcerer's Shoes"
    ],
    "w_name": "Satchel Charge",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZiggsR.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/ZiggsPassiveReady.png",
    "passive_description": "Every 12 seconds, Ziggs' next basic attack deals bonus magic damage. This cooldown is reduced whenever Ziggs uses an ability."
  },
  "117": {
    "lore": "Perhaps more than any other champion in the League, Lulu marches to the beat of her own drum. During her youth in Bandle City, she spent most of her time wandering alone in the forest or lost in a daydream. It wasn't that she was antisocial; the day-to-day bustle of Bandle City just couldn't compete with the vibrant world of her imagination. She saw wonder in places most people overlooked. This was how she found Pix, a fae spirit, pretending to be stuck in a birdhouse. Lulu's imagination distinguished her to Pix and he seized the opportunity to lure her into his world. He brought her to the Glade, the enchanted home of the fae, which lay nestled in a clearing in the woods. There the rigid properties of the outside world - things like size and color - changed as frequently and whimsically as the direction of the wind. Lulu felt at home in the Glade and she lingered there with Pix, fascinated by this secret place.\n\nShe quickly lost track of time. Her life in the Glade was comfortable and natural. She and Pix played fae games together, the sorts of games that she had been told were ''make believe''... and she got exceedingly good at them. It caught her by surprise when she suddenly remembered that she had left a life behind in Bandle City. The Glade had a way of making everything outside seem distant and surreal. Lulu decided to revisit her former home, to share some of the lovely things she'd learned, but when she and Pix returned the world had changed. Time, she discovered, was another property that behaved differently in the Glade, and centuries had passed while she was away. Lulu sought to reconnect to the residents of the outside world but her attempts had unfortunate results. She led all the children off to play hide and seek, temporarily changing them into flowers and animals to spice up the game, but their parents didn't appreciate her efforts. When the yordles insisted that she leave their land, she turned to a vibrant magical place where those with unusual gifts were not just accepted but adored: the League of Legends.\n\n''The best path between two points is upside-down, between, then inside-out and round again.''\n-- Lulu",
    "champion_id": 117,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LuluE.png",
    "q_name": "Glitterlance",
    "passive_name": "Pix, Faerie Companion",
    "e_description": "If cast on an ally, commands Pix to jump to an ally and shield them. He then follows them and aids their attacks. If cast on an enemy, commands Pix to jump to an enemy and damage them. He then follows them and grants you vision of that enemy.",
    "recommended_items": [
      2003,
      3303,
      3190,
      3117,
      3165
    ],
    "r_name": "Wild Growth",
    "r_description": "Lulu enlarges an ally, knocking nearby enemies into the air and granting the ally a large amount of bonus Health. For the next few seconds, that ally gains an aura that slows nearby enemies.",
    "name": "Lulu",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LuluQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LuluW.png",
    "q_description": "Pix and Lulu each fire a bolt of magical energy that heavily slows all enemies it hits. An enemy can only be damaged by one bolt.",
    "title": "the Fae Sorceress",
    "e_name": "Help, Pix!",
    "w_description": "If cast on an ally, grants them Movement Speed for a short time. If cast on an enemy, turns them into an adorable critter that can't attack or cast spells.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Lulu.png",
    "recommended_item_names": [
      "Health Potion",
      "Spellthief's Edge",
      "Locket of the Iron Solari",
      "Boots of Mobility",
      "Morellonomicon"
    ],
    "w_name": "Whimsy",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LuluR.png",
    "role": "Support",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Lulu_PixFaerieCompanion.png",
    "passive_description": "Pix is a wild Faerie that accompanies Lulu. Pix will fire a barrage of magical energy at targets that Lulu attacks."
  },
  "119": {
    "lore": "Unlike his brother Darius, victory in battle was never enough for Draven. He craved recognition, acclaim, and glory. He first sought greatness in the Noxian military, but his flair for the dramatic went severely underappreciated. Thirsting for a method to share ''Draven'' with the world, he turned his attention to the prison system. There he carved out the celebrity he desired by turning the tedious affair of executions into a premiere spectacle.\n\nAt Draven's first execution, he shocked onlookers when he ordered the doomed prisoner to run for dear life. Just before the man managed to flee from sight, Draven brought him down with a flawless throw of his axe. Soon, all Draven's executions became a gauntlet through which Noxian prisoners raced for a final chance at life. He used this trial as his own personal stage, and turned executions into a leading form of entertainment. He rallied onlookers into a frenzy, while desperate prisoners scrambled to evade him. They never succeeded. Rejecting the solemn, black uniforms of Noxian executioners Draven donned bright outfits and developed flashy signature moves to distinguish himself. Crowds flocked to see Draven in action, and tales of his performances spread quickly. As his popularity grew, so did his already-inflated ego. He belonged at the center of attention. Before long, the scope of his ambitions outgrew the population of Noxus. He decided that the glorious exploits of Draven should be put on display for the entire world.\n\n'' 'The best' is wherever I decide to set the bar each day.''\n-- Draven",
    "champion_id": 119,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DravenDoubleShot.png",
    "q_name": "Spinning Axe",
    "passive_name": "League of Draven",
    "e_description": "Draven throws his axes, dealing physical damage to targets hit and knocking them aside. Targets hit are slowed.",
    "recommended_items": [
      3102,
      2003,
      3035,
      1055,
      3006
    ],
    "r_name": "Whirling Death",
    "r_description": "Draven hurls two massive axes to deal physical damage to each unit struck. Whirling Death slowly reverses direction and returns to Draven after striking an enemy champion. Draven may also activate this ability while the axes are in flight to cause it to return early. Deals less damage for each unit hit and resets when the axes reverse direction.",
    "name": "Draven",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DravenSpinning.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DravenFury.png",
    "q_description": "Draven's next attack will deal bonus physical damage. This axe will ricochet off the target high up into the air. If Draven catches it, he automatically readies another Spinning Axe. Draven can have two Spinning Axes at once.",
    "title": "the Glorious Executioner",
    "e_name": "Stand Aside",
    "w_description": "Draven gains increased Movement Speed and Attack Speed. The Movement Speed bonus decreases rapidly over its duration. Catching a Spinning Axe will refresh the cooldown of Blood Rush.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Draven.png",
    "recommended_item_names": [
      "Banshee's Veil",
      "Health Potion",
      "Last Whisper",
      "Doran's Blade",
      "Berserker's Greaves"
    ],
    "w_name": "Blood Rush",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DravenRCast.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Draven_passive.png",
    "passive_description": "Draven gains his fans' Adoration when he catches a Spinning Axe or kills a minion, monster, or tower. Killing enemy champions grants Draven bonus gold based on how much Adoration he has."
  },
  "120": {
    "lore": "Hecarim is a towering, armored specter whose name is whispered fearfully across the length and breadth of Runeterra. He patrols the Shadow Isles, running down anyone foolish enough to set foot upon its cursed soil. As the vanguard of undeath, Hecarim rides forth from the Black Mist, laughing mockingly as he tramples the living beneath his iron-shod hooves.",
    "champion_id": 120,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HecarimRamp.png",
    "q_name": "Rampage",
    "passive_name": "Warpath",
    "e_description": "Hecarim gains increasing Movement Speed for a short duration. His next attack knocks the target back and deals additional physical damage based on the distance he has traveled since activating the ability. ",
    "recommended_items": [
      2003,
      1039,
      3111,
      2041,
      3117,
      3142,
      3143
    ],
    "r_name": "Onslaught of Shadows",
    "r_description": "Hecarim summons spectral riders and charges forward, dealing magic damage in a line. Hecarim creates a shockwave when he finishes his charge, causing nearby enemies to flee in terror.",
    "name": "Hecarim",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HecarimRapidSlash.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HecarimW.png",
    "q_description": "Hecarim cleaves nearby enemies dealing physical damage. ",
    "title": "the Shadow of War",
    "e_name": "Devastating Charge",
    "w_description": "Hecarim deals magic damage to nearby enemies for a short duration. Hecarim gains Health equal to a percentage of any damage those enemies suffer.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Hecarim.png",
    "recommended_item_names": [
      "Health Potion",
      "Hunter's Machete",
      "Mercury's Treads",
      "Crystalline Flask",
      "Boots of Mobility",
      "Youmuu's Ghostblade",
      "Randuin's Omen"
    ],
    "w_name": "Spirit of Dread",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/HecarimUlt.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Hecarim_Passive.png",
    "passive_description": "Hecarim gains Attack Damage equal to a percentage of his bonus Movement Speed."
  },
  "121": {
    "lore": "A vicious Void predator, Kha'Zix infiltrated Valoran to devour the land's most promising creatures. With each kill he absorbs his prey's strength, evolving to grow more powerful. Kha'Zix hungers most to conquer and consume Rengar, the one beast he considers his equal.\n\nWhen Kha'Zix crossed over into this world, he was fragile and ravenous. The animals he first encountered were too small to fuel the rapid evolution he craved. Kha'Zix focused his hunger on the most dangerous creatures he could find, risking his life to satisfy his need. With each kill he feasted and changed, becoming a stronger, faster predator. Kha'Zix soon chased his prey with unrestrained aggression, believing he was unstoppable. One day, while savoring a fresh kill, the predator became the prey. From cover a creature pounced in a blur of fangs and steel, tackling him to the ground. It roared in his face slashing and clawing, and Kha'Zix felt his blood spill for the first time. Screeching in fury, he sliced at the brute's eye driving it back. They fought from sunset to sunrise. Finally, near death, they reluctantly separated. As his wounds closed, Kha'Zix burned with anticipation at the idea of devouring one who could match the Void's strength. He resumed his search for powerful prey with renewed vigor. Someday, Kha'Zix will feast on Rengar.\n\n''Kill. Consume. Adapt.''\n-- Kha'Zix",
    "champion_id": 121,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KhazixE.png",
    "q_name": "Taste Their Fear",
    "passive_name": "Unseen Threat",
    "e_description": "Kha'Zix leaps to an area, dealing physical damage upon landing. If he chooses to <span class=\"color00DD33\">Evolve Wings<\/span>, Leap's range increases dramatically. Also, on champion kill or assist, Leap's cooldown resets.",
    "recommended_items": [
      3047,
      2003,
      1039,
      2041,
      3071,
      3117,
      3143
    ],
    "r_name": "Void Assault",
    "r_description": "Each rank allows Kha'Zix to evolve one of his abilities, giving it a unique additional effect. When activated, Void Assault stealths Kha'Zix, triggers Unseen Threat, and increases Movement Speed. If he chooses to <span class=\"color00DD33\">Evolve Active Camouflage<\/span>, Void Assault can be cast three times and stealth duration increased.",
    "name": "Kha'Zix",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KhazixQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KhazixW.png",
    "q_description": "Kha'Zix passively marks enemies that are isolated from nearby allies. Taste Their Fear deals physical damage to a single target. Damage increased on isolated targets. If he chooses to <span class=\"color00DD33\">Evolve Enlarged Claws<\/span>, this deals extra bonus damage against isolated targets. Kha'Zix also gains increased range on his basic attacks and Taste Their Fear.",
    "title": "the Voidreaver",
    "e_name": "Leap",
    "w_description": "Kha'Zix fires exploding spikes that slow and deal physical damage to all nearby enemies. Kha'Zix is healed if he is also within the explosion radius. If he chooses to <span class=\"color00DD33\">Evolve Spike Racks<\/span>, Void Spike fires three spikes in a cone and Void Spike's slow effect is increased.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Khazix.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Crystalline Flask",
      "The Black Cleaver",
      "Boots of Mobility",
      "Randuin's Omen"
    ],
    "w_name": "Void Spike",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/KhazixR.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Khazix_P.png",
    "passive_description": "When Kha'Zix is not visible to the enemy team, he gains Unseen Threat, causing his next basic attack against an enemy Champion to deal bonus magic damage and slow."
  },
  "122": {
    "lore": "There is no greater symbol of Noxian might than Darius, the nation's most feared and battle-hardened warrior. Orphaned at a young age, Darius had to fight to keep himself and his younger brother alive. By the time he joined the military, he had already developed the strength and discipline of a veteran soldier. The first true test of Darius's resolve occurred in a crucial battle against Demacia, where the Noxian forces were exhausted and outnumbered. Darius's captain called for his troops to retreat, but Darius refused to accept such an act of cowardice. Breaking formation, Darius strode towards the captain and decapitated him with one sweep of his gigantic axe. Both terrified and inspired, the soldiers followed Darius into battle and fought with incredible strength and fervor. After a long and grueling battle, they ultimately emerged victorious.\n\nSeizing momentum from this victory, Darius led his now fiercely loyal troops in a devastating campaign against Demacia. After proving his power on the battlefield, Darius turned his gaze homeward. He saw a Noxus riddled with weakness, where greedy, complacent nobles drained the nation's strength. Seeking to restore his country to greatness, Darius took it upon himself to reshape the Noxian leadership. He identified weak figureheads and violently removed them from their positions of power. Many in Noxus saw Darius's cull as an attempt to seize power, but he had a different plan for the throne. He had been watching the rise of Jericho Swain with keen interest. In Swain, Darius saw a leader with the mind and determination to bring Noxus to glory. Now allied with the Master Tactician, Darius works to unite the nation behind his vision of true Noxian strength.\n\n''A united Noxus could control the world - and would deserve to.''\n-- Darius",
    "champion_id": 122,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DariusAxeGrabCone.png",
    "q_name": "Decimate",
    "passive_name": "Hemorrhage",
    "e_description": "Darius hones his axe, passively causing his physical damage to ignore a percentage of his target's Armor. When activated, Darius sweeps up his enemies with his axe's hook and pulls them to him.",
    "recommended_items": [
      3078,
      3047,
      2003,
      1039,
      3111,
      1054,
      3143
    ],
    "r_name": "Noxian Guillotine",
    "r_description": "Darius leaps to an enemy champion and strikes a lethal blow, dealing true damage. This damage is increased for each stack of Hemorrhage on the target. If Noxian Guillotine is a killing blow, its cooldown is refreshed for a brief duration.",
    "name": "Darius",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DariusCleave.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DariusNoxianTacticsONH.png",
    "q_description": "Darius swings his axe in a wide circle. Enemies struck by the blade take more damage than those struck by the handle.",
    "title": "the Hand of Noxus",
    "e_name": "Apprehend",
    "w_description": "Darius's next attack strikes an enemy's crucial artery. As they bleed out, their Movement and Attack Speed is slowed. Crippling Strike's cooldown is lower the more bloodied its target.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Darius.png",
    "recommended_item_names": [
      "Trinity Force",
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Mercury's Treads",
      "Doran's Shield",
      "Randuin's Omen"
    ],
    "w_name": "Crippling Strike",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DariusExecute.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Darius_Icon_Hemorrhage.png",
    "passive_description": "Darius aims his attacks strategically, causing his target to bleed. This effect stacks up to five times."
  },
  "126": {
    "lore": "Armed with wit, charm, and his signature transforming hammer, Jayce lives to protect his native Piltover. Long before his nation called him a hero, however, he was a promising young inventor. When Piltover commissioned him to study a rare arcane crystal, Jayce discovered it could be used as a vast energy source. Eager to make a name for himself, he began developing a device to harness its power. Word of the crystal's potential reached beyond the borders of Piltover. Viktor, the machine-augmented scientist from Zaun, brought Jayce an offer - together, they could use the crystal to advance his ''glorious evolution,'' a vision of humanity fused with technology. Jayce refused, but the Zaunite had no intention of leaving empty handed. He effortlessly blasted Jayce aside and seized the crystal, incinerating the lab's meager security force as he left for Zaun. Jayce implored the Piltover government to respond, but the officials refused to support an act of aggression. He decided to act alone, realizing that if no one struck back, Piltover would never be safe.\n\nJayce returned to the lab to prepare for his attack. After intense research, development, and hands-on testing, he emerged with his crowning achievement - the Mercury Hammer. Weapon in hand, Jayce marched to Zaun and began his one-man assault. Viktor's acolytes rushed to stop him, but Jayce smashed them aside, fighting his way into the heart of the lab. Inside, Jayce saw the horrifying brilliance of Viktor's creations, all powered by the energy of the arcane crystal. He realized that his only option was to destroy the power source, but Viktor stood in his way. Though their clash left both scientists heavily wounded, Jayce managed a desperate strike at the crystal. He shattered it and escaped as Viktor's machines erupted in flames. When he returned home, exhausted but victorious, the citizens of Piltover hailed Jayce as a hero. He reveled in the adoration, but knew that his actions had drawn the attention of dangerous enemies. Now devoted to the defense of his people, Jayce is Piltover's best hope for a bright future.\n\n''Trust me: if we're smart, Piltover can stand strong against any threat. Hey, I'm living proof.''\n-- Jayce",
    "champion_id": 126,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JayceThunderingBlow.png",
    "q_name": "To the Skies! \/ Shock Blast",
    "passive_name": "Hextech Capacitor",
    "e_description": "Hammer Stance: Deals magic damage to an enemy and knocks them back a short distance.\n\nCannon Stance: Deploys an Acceleration Gate increasing the Movement Speed of all allied champions who pass through it. If Shock Blast is fired through the gate the missile speed, range, and damage will increase.",
    "recommended_items": [
      3158,
      2003,
      3035,
      3026,
      1055
    ],
    "r_name": "Mercury Cannon \/ Mercury Hammer",
    "r_description": "Hammer Stance: Transforms the Mercury Hammer into the Mercury Cannon gaining new abilities and increased range. The first attack in this form reduces the target's Armor and Magic Resist.\n\nCannon Stance: Transforms the Mercury Cannon into the Mercury Hammer gaining new abilities and increasing Armor and Magic Resist. The first attack in this form deals additional magic damage.",
    "name": "Jayce",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JayceToTheSkies.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JayceStaticField.png",
    "q_description": "Hammer Stance: Leaps to an enemy dealing physical damage and slowing enemies.\n\nCannon Stance: Fires an orb of electricity that detonates upon hitting an enemy (or reaching the end of its path) dealing physical damage to all enemies in the area of the explosion.",
    "title": "the Defender of Tomorrow",
    "e_name": "Thundering Blow \/ Acceleration Gate",
    "w_description": "Hammer Stance: Passive: Restores Mana per strike. Active: Creates a field of lightning damaging nearby enemies for several seconds.\n\nCannon Stance: Gains a burst of energy, increasing Attack Speed to maximum for several attacks.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Jayce.png",
    "recommended_item_names": [
      "Ionian Boots of Lucidity",
      "Health Potion",
      "Last Whisper",
      "Guardian Angel",
      "Doran's Blade"
    ],
    "w_name": "Lightning Field \/ Hyper Charge",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JayceStanceHtG.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Jayce_Passive.png",
    "passive_description": "Gains 40 Movement Speed for 1.25 seconds and can move through units each time Transform is cast."
  },
  "127": {
    "lore": "Lissandra's magic twists the pure power of ice into something dark and terrible. With the force of her black ice, she does more than freeze - she impales and crushes those who oppose her. To the terrified denizens of the north, she is known only as ''The Ice Witch.'' The truth is much more sinister: Lissandra is a corruptor of nature who plots to unleash an ice age on the world.\n\nCenturies ago, Lissandra betrayed her tribe to evil creatures, known as the Frozen Watchers, in return for power. That was the last day that warm blood ran through her veins. With her corrupted tribesmen and the strength of the Watchers, she swept across the land like a terrible blizzard. As her empire spread, the world grew colder and ice choked the land. When the Watchers were defeated by ancient heroes, Lissandra did not lose faith and swore to prepare the world for their return.\n\nLissandra worked to purge all knowledge of the Watchers from the world. Using magic to take human form, she masqueraded as numerous seers and elders. Over the course of generations, she rewrote the stories of the Freljord, and so the history of its people changed. Today the fragmented retellings of the Watchers are seen as children's tales. But this deception wasn't enough - Lissandra also needed an army.\n\nShe set her sights on the noble Frostguard tribe. Lissandra knew corrupting the Frostguard would take centuries, and so she launched her greatest deception. She murdered and stole the identity of the Frostguard leader. Then she slowly began to warp the tribe's proud traditions. When her human form grew old, she faked her own death and then murdered her successor to steal her identity. With each generation, the Frostguard grew more insular, cruel and twisted. Today, the world still sees them as a noble and peaceful tribe that guards against evil creatures like the Ice Witch. In truth, they now serve the witch and long for the glorious return of the Watchers.\n\nLissandra knows that on that day nations will fall and the world will be reborn in ice.\n\n''Close your eyes and let the cold take you.'' \n-- Lissandra",
    "champion_id": 127,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LissandraE.png",
    "q_name": "Ice Shard",
    "passive_name": "Iceborn",
    "e_description": "Lissandra creates an ice claw that deals magic damage. Reactivating this ability transports Lissandra to the claw's current location.",
    "recommended_items": [
      2003,
      3174,
      3027,
      1056,
      3165
    ],
    "r_name": "Frozen Tomb",
    "r_description": "If cast on an enemy champion, the target is frozen solid, stunning it. If cast on Lissandra, she encases herself in dark ice, becoming untargetable and invulnerable. Dark ice then emanates from the target dealing magic damage to enemies and slowing Movement Speed.",
    "name": "Lissandra",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LissandraQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LissandraW.png",
    "q_description": "Throws a spear of ice that shatters when it hits an enemy, dealing magic damage and slowing Movement Speed. Shards pass through the target, dealing the same damage to other enemies hit.",
    "title": "the Ice Witch",
    "e_name": "Glacial Path",
    "w_description": "Freezes nearby enemies in ice, dealing magic damage and rooting them. ",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Lissandra.png",
    "recommended_item_names": [
      "Health Potion",
      "Athene's Unholy Grail",
      "Rod of Ages",
      "Doran's Ring",
      "Morellonomicon"
    ],
    "w_name": "Ring of Frost",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LissandraR.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Lissandra_Passive.png",
    "passive_description": "Every 18 seconds Lissandra's next ability costs no Mana. This cooldown is reduced by 1 second whenever Lissandra impairs an enemy's movement with an ability (does not apply to movement-impairing effects from items)."
  },
  "131": {
    "lore": "An unyielding avatar of the moon's power, Diana wages a dark crusade against the sun-worshipping Solari. Though she once sought the acceptance of her people, years of futile struggle shaped her into a bitter, resentful warrior. She now presents her foes with a terrible ultimatum: revere the moon's light, or die by her crescent blade.\n\nThough she was born to the Solari, Diana's inquisitive nature set her apart from her brethren. She had always found solace and guidance in the night sky, and questioned the dominance of the sun in her society. The Solari elders responded to her challenges with only derision and punishment. Diana remained convinced, however, that if she could find evidence of the moon's power, the elders would listen to reason. For years, she studied Solari archives in solitude until she discovered an encoded message hidden in an old tome. This clue led her to a secluded valley on Mount Targon where she unearthed the hidden entrance to an ancient, sealed temple. Inside, among aging relics and faded murals, she found an ornate suit of armor and a beautiful crescent blade, both inscribed with sigils of the moon. Diana donned the armaments and returned to the Solari elders that night. She declared that the artifacts proved others had once worshipped the moon as she did. Her discovery of evidence challenging Solari dominion shocked the elders. To Diana's horror, they pronounced her a heretic and condemned her to death. As the elders prepared her for execution, Diana's anger and sorrow overwhelmed her desire for acceptance. She lifted her gaze to the sky, calling upon the moon for strength. Lunar power surged within her and she shattered her bindings. Raising her relic blade, she turned and slaughtered the elders. With the temple in ruins behind her, Diana resolved to destroy all those who would deny the power of the moon.\n\n''The sun does not reveal truth. Its light only burns and blinds.''\n-- Diana",
    "champion_id": 131,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DianaVortex.png",
    "q_name": "Crescent Strike",
    "passive_name": "Moonsilver Blade",
    "e_description": "Diana draws in and slows all nearby enemies.",
    "recommended_items": [
      3135,
      2003,
      1039,
      1056,
      3157,
      3020
    ],
    "r_name": "Lunar Rush",
    "r_description": "Diana dashes to an enemy and deals magic damage. Lunar Rush has no cooldown when used to teleport to a target afflicted with Moonlight.",
    "name": "Diana",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DianaArc.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DianaOrbs.png",
    "q_description": "Diana swings her blade to unleash a bolt of lunar energy that deals damage in an arc before exploding. Afflicts enemies struck with the Moonlight debuff, revealing them if they are not stealthed. ",
    "title": "Scorn of the Moon",
    "e_name": "Moonfall",
    "w_description": "Diana creates three orbiting spheres that detonate on contact with enemies to deal damage in an area. She also gains a temporary shield that absorbs damage. If her third sphere detonates, the shield gains additional strength.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Diana.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Hunter's Machete",
      "Doran's Ring",
      "Zhonya's Hourglass",
      "Sorcerer's Shoes"
    ],
    "w_name": "Pale Cascade",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/DianaTeleport.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Diana_Passive_LunarBlade.png",
    "passive_description": "Gains Attack Speed. Every third strike cleaves nearby enemies for additional magic damage."
  },
  "133": {
    "lore": "Quinn and Valor are an elite ranger team. With crossbow and claw, they undertake their nation's most dangerous missions deep within enemy territory, from swift reconnaissance to lethal strikes. The pair's unbreakable bond is deadly on the battlefield, leaving opponents blind and riddled with arrows long before they realize who they're fighting: not one, but two Demacian legends.\n\nAs a young girl, Quinn shared a hunger for adventure with her twin brother. They dreamed of becoming knights, but lived a quiet, humble life in the rural borderlands of Demacia. Together they imagined triumphant battles in faraway lands, seizing glory for their king and slaying foes in the name of Demacian justice. When daydreams alone could no longer satisfy their warriors souls, they embarked on daring wilderness adventures in search of true danger. One such quest turned to tragedy when a terrible accident claimed her brother's life. Overcome with grief, Quinn abandoned her dreams of knighthood. \n\nOn the anniversary of her loss, Quinn gathered the courage to return to the scene of the tragedy. To her surprise, she found a wounded Demacian eagle at the site of her brother's death - a rare and beautiful bird long believed extinct. Quinn nursed the fledgling back to health, and as they grew up together, a deep bond formed between the two. She saw the same quality in her newfound friend that had lived within her brother, and so she gave him the name ''Valor.'' The pair found strength in each other, and together they pursued the dream she had once abandoned. \n\nThe Demacian army had never seen heroes like Quinn and Valor. Their deadly skills quickly set them apart from their rank-and-file peers, but many still had their doubts. How could a common-born girl, even with such a powerful creature at her side, forego years of military training? Quinn and Valor proved themselves on one critical mission, tracking down a Noxian assassin who had evaded an entire Demacian battalion. When they brought him to justice, they finally earned the admiration and respect of their nation. The two now serve as living, fighting icons of Demacian strength and perseverance. Together, Quinn and Valor will stand against any threat to their beloved home.\n\n''Most soldiers only rely on their weapons. Few truly rely on each other.''\n -- Quinn",
    "champion_id": 133,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/QuinnE.png",
    "q_name": "Blinding Assault",
    "passive_name": "Harrier",
    "e_description": "Quinn dashes to an enemy, dealing physical damage and slowing the target's Movement Speed. Upon reaching the target, she leaps off the target, briefly interrupting it, and lands near her maximum Attack Range away from the target. Valor will immediately mark this enemy as Vulnerable.",
    "recommended_items": [
      2003,
      3035,
      3026,
      1055,
      3006
    ],
    "r_name": "Tag Team",
    "r_description": "Valor replaces Quinn on the battlefield as a mobile melee attacker. When ready, Quinn returns in a hail of arrows, dealing physical damage to all nearby enemies.",
    "name": "Quinn",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/QuinnQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/QuinnW.png",
    "q_description": "Quinn calls Valor to blind and damage targets in an area.",
    "title": "Demacia's Wings",
    "e_name": "Vault",
    "w_description": "Passively grants Quinn Attack Speed and Movement Speed after she attacks a Vulnerable target. Valor's Attack Speed is permanently increased. Activate to have Valor reveal a large area nearby (does not reveal stealthed units).",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Quinn.png",
    "recommended_item_names": [
      "Health Potion",
      "Last Whisper",
      "Guardian Angel",
      "Doran's Blade",
      "Berserker's Greaves"
    ],
    "w_name": "Heightened Senses",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/QuinnR.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Quinn_Passive.png",
    "passive_description": "Valor periodically marks enemies as Vulnerable. Quinn's first basic attack against Vulnerable targets will deal bonus physical damage."
  },
  "134": {
    "lore": "Born with immense magical potential, Syndra loves nothing more than exercising the incredible power at her command. With each passing day, her mastery of magical force grows more potent and devastating. Refusing any notion of balance or restraint, Syndra wants only to retain control of her power, even if it means annihilating the authorities that seek to stop her.\n\nThroughout her youth in Ionia, Syndra's reckless use of magic terrified the elders of her village. They took her to a remote temple, leaving her in the care of an old mage. To Syndra's delight, the mage explained that the temple was a school - a place where she could develop her talents under his guidance. Though she learned much during her time there, Syndra no longer felt her power growing as it had in her youth. Her frustration grew, and she finally confronted her mentor, demanding an explanation. He revealed that he had dampened Syndra's magic, hoping to help her learn control and restraint. Accusing him of betrayal, she advanced on the mage, commanding him to lift the spell that was holding her back. He backed away, telling her that if she couldn't control herself, he would be forced to nullify Syndra's magic completely. Furious, she summoned her power and dashed the old man against the walls. With her mentor dead, Syndra felt the rush of her unbounded potential for the first time in years. Though she had won her freedom, she refused to return to the society that had tried to steal her gift. Instead, Syndra decided to claim her former prison as a stronghold. Pushing the boundaries of her magic, she tore the structure from its foundations and raised it into the sky. Free to delve further into her art, Syndra now aims to grow powerful enough to destroy the weak, foolish leaders of Ionia - and anyone else who would dare to shackle her greatness.\n\n''Power belongs to those who can wield it.''\n-- Syndra",
    "champion_id": 134,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SyndraE.png",
    "q_name": "Dark Sphere",
    "passive_name": "Transcendent",
    "e_description": "Syndra knocks enemies and Dark Spheres back dealing magic damage. Enemies hit by Dark Spheres become stunned.",
    "recommended_items": [
      3135,
      2003,
      1056,
      3157,
      3020
    ],
    "r_name": "Unleashed Power",
    "r_description": "Syndra bombards an enemy Champion with all of her Dark Spheres.",
    "name": "Syndra",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SyndraQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SyndraW.png",
    "q_description": "Syndra conjures a Dark Sphere dealing magic damage. The sphere remains and can be manipulated by her other powers.",
    "title": "the Dark Sovereign",
    "e_name": "Scatter the Weak",
    "w_description": "Syndra picks up and throws a Dark Sphere or enemy minion dealing magic damage and slowing the Movement Speed of enemies. ",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Syndra.png",
    "recommended_item_names": [
      "Void Staff",
      "Health Potion",
      "Doran's Ring",
      "Zhonya's Hourglass",
      "Sorcerer's Shoes"
    ],
    "w_name": "Force of Will",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/SyndraR.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/SyndraPassive.png",
    "passive_description": "Spells gain extra effects at max rank.<br><br><span class=\"colorFF9900\">Dark Sphere<\/span>: Deals 15% bonus damage to champions.<br><span class=\"colorFF9900\">Force of Will<\/span>: Increases the slowing duration by 33%.<br><span class=\"colorFF9900\">Scatter the Weak<\/span>: Spell width increased by 50%.<br><span class=\"colorFF9900\">Unleashed Power<\/span>: Range increased by 75."
  },
  "143": {
    "lore": "Longing to take control of her fate, the ancient, dying plant Zyra transferred her consciousness into a human body for a second chance at life. Centuries ago, she and her kind dominated the Kumungu Jungle, using thorns and vines to consume any animal that set foot in their territory. As the years passed, the animal population steadily died off. Food became increasingly scarce, and Zyra could only stand by helplessly as the last of her kin withered away. She thought she would perish alone, until the appearance of an unwary sorceress presented her with an opportunity for salvation.\n\nIt was the first time in years Zyra had sensed a creature wander so close. Hunger drew her to the sorceress, but some other, deeper instinct compelled her. She enveloped the woman in thorns with ease, but as she savored this final meal, foreign memories invaded her thoughts. She saw great jungles of metal and stone where humans and animals thrived. Potent magic surged through her vines, and she devised an elegant but risky plan to survive. Using the woman's memories, Zyra poured her newfound magic into the creation of a human-shaped vessel. She didn't know what sort of world awaited her, but she had nothing left to lose. When Zyra opened her eyes, she was overwhelmed by the raw power ready at her fingertips. It wasn't until she noticed the shriveled remains of the plant she once was that she realized how vulnerable she had become. If this body died, there would be no network of vines to retreat through, no roots to regrow her... but she felt truly alive. She beheld the world for the first time as animals did, and a dark smile crept across her lips. She was reborn, and there was so much now within her grasp.\n\n''Closer to the flower, closer to the thorns.''\n--Zyra",
    "champion_id": 143,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZyraGraspingRoots.png",
    "q_name": "Deadly Bloom",
    "passive_name": "Rise of the Thorns",
    "e_description": "Zyra sends forth vines through the ground to ensnare her target, dealing damage and rooting enemies they come across. If cast upon a seed, Grasping Roots grows a Vine Lasher, whose short range attacks reduce enemy Movement Speed.",
    "recommended_items": [
      2003,
      3303,
      3151,
      3157,
      3020
    ],
    "r_name": "Stranglethorns",
    "r_description": "Zyra summons a twisted thicket at her target location, dealing damage to enemies as it expands and knocking them airborne as it contracts.",
    "name": "Zyra",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZyraQFissure.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZyraSeed.png",
    "q_description": "Zyra grows a bud at target location. After a brief delay, it explodes, launching damaging thorns at all nearby enemies. If cast upon a seed, Deadly Bloom grows a Thorn Spitter plant, which fires at enemies from afar.",
    "title": "Rise of the Thorns",
    "e_name": "Grasping Roots",
    "w_description": "Zyra plants a seed, granting vision of an area for up to 30 seconds. Other spells cast on seeds will turn them into plants, who fight for Zyra. Additionally passively grants her Cooldown Reduction.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Zyra.png",
    "recommended_item_names": [
      "Health Potion",
      "Spellthief's Edge",
      "Liandry's Torment",
      "Zhonya's Hourglass",
      "Sorcerer's Shoes"
    ],
    "w_name": "Rampant Growth",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZyraBrambleZone.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/ZyraP.png",
    "passive_description": "When Zyra dies, she briefly returns to her plant form. After 2 seconds, she can press any ability to fire a thorn toward her cursor, dealing true damage to each enemy it strikes."
  },
  "11": {
    "lore": "Through the ancient martial art of Wuju, Master Yi has tempered his body and sharpened his mind until thought and action have become one. Though he chooses to enter into violence as a last resort, the grace and speed with which he wields his blade ensures resolution is always swift. As the last living practitioner of Wuju, Master Yi has devoted his life to finding able pupils to carry on the legacy of his lost people. \n\nEven before Yi mastered Wuju, he was considered one of the most skilled practitioners of the mystical martial art. He would soon prove his mastery when word of a massive Noxian invasion reached his remote village. Yi swept across the battlefields of Ionia, turning back the tide of Noxus's vast infantry with swift and deadly strikes, much to the embarrassment of Noxian High Command. Recognizing the threat the Wuju disciples posed to their invasion, the Noxians chose to unleash a nightmarish chemical attack on the home of the deadly art. Those who somehow survived the poisonous concoction had their minds twisted beyond repair. Yi's home was left in ruin.\n\nAt the war's conclusion, Yi returned to the grotesque remains of his village. There he became the attack's final casualty. Slain in spirit, if not in body, Yi clung to the only feeling left within his heart: vengeance. Driven only by his desire to punish those who'd destroyed his home, Yi spent years training in seclusion. He became a deadlier swordsman than he had ever been, but true mastery of Wuju still eluded him.\n\nAt the height of Yi's frustration, a monkey of unusually noble bearing interrupted his training. Standing as straight and tall as a man, the monkey watched and mimicked Yi's movements. Yi shooed the monkey away, but the agile creature took great amusement in turning Yi's own techniques against him. Gradually, Yi felt his anger subside as he sparred with the playful animal, and when the burden of his hatred had fully lifted, he found he had caught the monkey by his tail. Yi then understood that he would never master Wuju so long as he pursued it for vengeance, and as he let go of the monkey, he also released his desire to shed his enemy's blood.\n\n Yi thanked the monkey for showing him what he'd been blind to, and was surprised when the creature actually replied. He wished to learn Yi's art of fighting. It was an odd request, but through it Yi saw his new path: the way to honor the memory of his lost people was to pass their teachings on to a new generation.\n\n''The edge of the sharpest blade is no match for the calm of the peaceful mind.'' \n-- Master Yi",
    "champion_id": 11,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/WujuStyle.png",
    "q_name": "Alpha Strike",
    "passive_name": "Double Strike",
    "e_description": "Master Yi becomes skilled in the art of Wuju, passively increasing his Attack Damage. Activating Wuju Style grants bonus true damage on basic attacks, but the passive bonus is then lost while on cooldown.",
    "recommended_items": [
      2003,
      3026,
      1039,
      1055,
      3006,
      3031
    ],
    "r_name": "Highlander",
    "r_description": "Master Yi moves with unparalleled agility, temporarily increasing his Movement and Attack Speeds as well as making him immune to all slowing effects. While active, Champion kills or assists extends Highlander's duration. Passively reduces cooldown for his other abilities on a kill or assist.",
    "name": "Master Yi",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/AlphaStrike.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Meditate.png",
    "q_description": "Master Yi teleports across the battlefield with blinding speed, dealing physical damage to multiple units in his path, while simultaneously becoming untargetable. Alpha Strike can critically strike and deals bonus physical damage to minions and monsters. Basic attacks reduce Alpha Strike's cooldown.",
    "title": "the Wuju Bladesman",
    "e_name": "Wuju Style",
    "w_description": "Master Yi rejuvenates his body by focus of mind, restoring Health and taking reduced damage for a short time.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/MasterYi.png",
    "recommended_item_names": [
      "Health Potion",
      "Guardian Angel",
      "Hunter's Machete",
      "Doran's Blade",
      "Berserker's Greaves",
      "Infinity Edge"
    ],
    "w_name": "Meditate",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/Highlander.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/MasterYi_Passive1.png",
    "passive_description": "Every few strikes, Master Yi strikes twice."
  },
  "154": {
    "lore": "Zac is the product of a Zaun experiment to manufacture a hexchem-engineered supersoldier - the Zaun Amorphous Combatant. Combining brute strength with limitless flexibility, he is a versatile juggernaut: a creative fighter who bounces over obstacles and pounds his foes into submission. Though he was created inside a weapons laboratory, Zac was rescued and adopted by two loving parents who raised him to be a kind and friendly child. As the years passed, he grew up to be a fierce hero, sworn to protect the ordinary, everyday people of Zaun.\n\nLong ago, two Zaun scientists developed an organic substance that could withstand extreme conditions, spontaneously alter its biological structure, and generate tremendous amounts of kinetic force. As the scientists, husband and wife, watched the prototype grow from a spoon-sized droplet to a small blob, they noticed that their creation would respond to their presence. It sprung forward when they called and bounced when they sang. The couple began to see more than an experiment; they saw a small child, filled with affection and joy.\n\nAfter testing the prototype one evening, the scientists placed the blob back in its cage. It slouched and shuddered in the corner, inconsolably sad. At that moment, the couple realized that their beloved creation wished for a free life outside the lab. They were struck by their conscience and could not allow the prototype to be used as a weapon. The husband and wife fled with the young blob, replacing its weapon designation - Zaun Amorphous Combatant - with a proper name: Zac. In a quiet neighborhood far from the cities of Zaun, the scientists raised Zac as their own child.\n\nZac was always different from the other children. None had his powers of strength and flexibility, so the couple taught him to tell right from wrong and to use his gifts responsibly. Thanks to the care and affection of his loving parents, Zac lived a peaceful, happy childhood.\n\nThat childhood ended when the Zaun laboratory finally found Zac. Unable to replicate the formula used to create the amorphous prototype, the laboratory's staff never stopped searching for the scientists and their experiment. When they tracked down the family, they threatened to tear it apart. The staff abducted Zac's parents and demanded that the couple assist in his capture and return. Seized by the fear of losing his freedom and his parents, Zac unleashed every ounce of his raw energy and mass for the very first time. He subdued his parents' captors, sent the laboratory's workers fleeing, and brought his loved ones home. From then on, Zac vowed to defend all ordinary lives threatened by extraordinary treachery and wickedness. Originally built to destroy, he now protects the innocent and the helpless.\n\n''Even if you don't have a spine, you still have to stand up for yourself.''\n -- Zac",
    "champion_id": 154,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZacE.png",
    "q_name": "Stretching Strike",
    "passive_name": "Cell Division",
    "e_description": "Zac attaches his arms to the ground and stretches back, launching himself forward.",
    "recommended_items": [
      2003,
      1039,
      3111,
      3117,
      1054,
      3143,
      3068
    ],
    "r_name": "Let's Bounce!",
    "r_description": "Zac launches into the air, gaining Movement Speed, and slams down three times, each time damaging, slowing and knocking up nearby enemies.",
    "name": "Zac",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZacQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZacW.png",
    "q_description": "Zac extends his arms, slowing and dealing damage to nearby enemies.",
    "title": "the Secret Weapon",
    "e_name": "Elastic Slingshot",
    "w_description": "Zac's body erupts, damaging nearby enemies.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Zac.png",
    "recommended_item_names": [
      "Health Potion",
      "Hunter's Machete",
      "Mercury's Treads",
      "Boots of Mobility",
      "Doran's Shield",
      "Randuin's Omen",
      "Sunfire Cape"
    ],
    "w_name": "Unstable Matter",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZacR.png",
    "role": "Tank",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/ZacPassive.png",
    "passive_description": "Each time Zac hits an enemy with an ability, he sheds a chunk of himself that can be reabsorbed to restore Health. Upon taking fatal damage, Zac splits into 4 bloblets that attempt to recombine. If any bloblets remain after 8 seconds, he will revive with an amount of Health depending on the Health of the surviving bloblets. Each bloblet has a percentage of Zac's maximum Health, Armor and Magic Resistance. This ability has a 5 minute cooldown."
  },
  "412": {
    "lore": "Thresh is a sadistic, spectral reaper who relishes tormenting the living and the dead. Once a jailer who mercilessly brutalized all under his charge, Thresh was hanged from his own chains by the prisoners he had tortured. With his vicious essence unbound, the Chain Warden roams Runeterra in search of prey. He derives twisted joy from slowly breaking the minds of his most defiant victims, before trapping their souls within the sickly green light of his lantern.",
    "champion_id": 412,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ThreshE.png",
    "q_name": "Death Sentence",
    "passive_name": "Damnation",
    "e_description": "Thresh's attacks wind up, dealing more damage the longer he waits between attacks. When activated, Thresh sweeps his chain, knocking all enemies hit in the direction of the blow.",
    "recommended_items": [
      2003,
      3301,
      3190,
      3117,
      3068
    ],
    "r_name": "The Box",
    "r_description": "A prison of walls that slow and deal damage if broken.",
    "name": "Thresh",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ThreshQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ThreshW.png",
    "q_description": "Thresh binds an enemy in chains and pulls them toward him. Activating this ability a second time pulls Thresh to the enemy.",
    "title": "the Chain Warden",
    "e_name": "Flay",
    "w_description": "Thresh throws out a lantern that shields nearby allied Champions from damage. Allies can click the lantern to dash to Thresh.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Thresh.png",
    "recommended_item_names": [
      "Health Potion",
      "Ancient Coin",
      "Locket of the Iron Solari",
      "Boots of Mobility",
      "Sunfire Cape"
    ],
    "w_name": "Dark Passage",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ThreshRPenta.png",
    "role": "Support",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Thresh_Passive.png",
    "passive_description": "Thresh can harvest the souls of enemies that die near him, permanently granting him Armor and Ability Power."
  },
  "157": {
    "lore": "Yasuo is a man of resolve, an agile swordsman who wields the wind itself to cut down his foes. This once-proud warrior has been disgraced by a false accusation and forced into a desperate fight for survival. With the world turned against him, he will do everything in his power to bring the guilty to justice and restore his honor.\n\nFormerly a brilliant pupil at a renowned Ionian sword school, Yasuo was the only student in a generation to master the legendary wind technique. Many believed he was destined to become a great hero. However, his fate was changed forever when Noxus invaded. Yasuo was charged with guarding an Ionian Elder, but, foolishly believing his blade alone could make the difference, he left his post to join the fray. By the time he returned, the Elder had been slain.\n\nDisgraced, Yasuo willingly turned himself in, prepared to pay for his failure with his life. He was shocked, however, to find himself accused not just of dereliction, but of the murder itself. Though confused and racked with guilt, he knew the assassin would go unpunished if he did not act. Yasuo raised his sword against the school and fought his way free, knowing his treason would turn all of Ionia against him. Left truly alone for the first time in his life, he set out to find the Elder's real killer.\n\nYasuo spent the next several years wandering the land, seeking any clue that might lead him to the murderer. All the while, he was relentlessly hunted by his former allies, continually forced to fight or die. His mission drove him ever forward, until he was tracked down by the one foe he dreaded most - his own brother, Yone.\n\nBound by a common code of honor, the two warriors bowed and drew their swords. Silently they circled one another under the moonlight. When they finally charged forward, Yone was no match for Yasuo; with a single flash of steel he cut his brother down. Yasuo dropped his weapon and rushed to Yone's side.\n\nOvercome with emotion, he demanded to know how his own kin could think him guilty. Yone spoke: ''The Elder was killed by a wind technique. Who else could it be?'' Understanding swept over Yasuo as he suddenly realized why he had been accused. He professed his innocence once more and begged his brother's forgiveness. Tears streamed down Yasuo's face as his brother passed in his arms.\n\nYasuo buried Yone under the rising sun, but could take no time to mourn. Others would be after him before long. His brother's revelation had given Yasuo newfound purpose; he now had the clue that would lead to the true killer. Swearing an oath, he gathered his belongings and, with one last look at Yone's grave, set out with the wind at his back.\n\n''The story of a sword is inked in blood.''\n-- Yasuo",
    "champion_id": 157,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/YasuoDashWrapper.png",
    "q_name": "Steel Tempest",
    "passive_name": "Way of the Wanderer",
    "e_description": "Dashes through a unit, dealing escalating Magic Damage with each cast.",
    "recommended_items": [
      2003,
      3035,
      3026,
      1055,
      3006
    ],
    "r_name": "Last Breath",
    "r_description": "Moves to a unit and strikes them repeatedly for heavy damage. Can only be cast on Airborne targets.",
    "name": "Yasuo",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/YasuoQW.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/YasuoWMovingWall.png",
    "q_description": "A skillshot basic attack. After two successful Steel Tempests, the next fires a tornado that knocks enemies Airborne.",
    "title": "the Unforgiven",
    "e_name": "Sweeping Blade",
    "w_description": "Creates a moving wall that blocks enemy projectiles.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Yasuo.png",
    "recommended_item_names": [
      "Health Potion",
      "Last Whisper",
      "Guardian Angel",
      "Doran's Blade",
      "Berserker's Greaves"
    ],
    "w_name": "Wind Wall",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/YasuoRKnockUpComboW.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Yasuo_Passive.png",
    "passive_description": "Yasuo's Critical Strike Chance is doubled. Additionally, Yasuo builds toward a shield whenever he is moving. The shield triggers when he takes damage from a champion or monster."
  },
  "161": {
    "lore": "I pass into the sudden glare. Blink. Blink, blink, blink. My eyes adjust and evaluate the landscape before me.\n\nThere's a scurrying. I look down to find a small, white creature standing on its hind legs, sniffing at my body. It intrigues me.\n\nWhat use are you?\n\nI analyze the creature. A flash of hot magenta light, a dust pile where it was quivering.\n\nMammalian... Nocturnal... Impeccable hearing. Incredibly weak. Yet they breed so prodigiously.\n\n''Hm,'' I mutter to myself. Hopefully there will be more complex things to be found; those fascinate me.\n\nConsume and learn: this is my purpose. The others who travel with me are primitive: kill and eat, kill and eat. I need to gather all available information - harvest any valuable resources.\n\nEventually, we come upon a destroyed city, save for one pristine tower. It appears to be protected - or intentionally left standing. I deconstruct the composition of the ruins. My analysis suggests this habitat was a place of great magic; I'm not surprised it was a target of such destruction. There is something compelling about the tower. While the others are off scavenging, I enter the citadel.\n\nCryptic instruments are strewn about. I examine one. Another flash of hot magenta light, another dust pile.\n\nFascinating: a tool to alter their concept of time.\n\nStrange.\n\nUnprecedented.\n\nFrom the state of the tower, it seems the owner departed only recently. The artifacts left behind have existed in more than one time and place. Some are more complex than others; all are more impressive than anything I have seen on this plane. Clearly, the owner knows things I have not encountered in any of my travels.\n\nI require such knowledge.\n\nLeaving the tower, I find the others closing in on the entrance, ready to destroy it as they have destroyed everything else we have met. They will only get in the way of my goal. There are some things the Void should not consume indiscriminately.\n\nWithout warning, I lash out a tentacle, its tip glowing white hot. Lightning arcs through the first creature, knocking it back. Its screams fade as I extend all three limbs, energy crackling between them, scorching the air where the streams meet. The other two run; they know what's coming.\n\nMust they always flee?\n\nI open my eye wide and unleash a beam of energy, following the escaping creatures. They are instantly reduced to ash. ''Hmm. Void-native melting point is inconsistent,'' I note.\n\nBut that is of no consequence. The hunger inside me grows. I am ravenous. Insatiable, as never before.\n\nI have glimpsed the ultimate knowledge.\n\nAnd I will have it.",
    "champion_id": 161,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VelkozE.png",
    "q_name": "Plasma Fission",
    "passive_name": "Organic Deconstruction",
    "e_description": "Vel'Koz causes an area to explode, knocking up enemies, and knocking close enemies slightly away.",
    "recommended_items": [
      2003,
      1056,
      3151,
      3116,
      3020
    ],
    "r_name": "Life Form Disintegration Ray",
    "r_description": "Vel'Koz unleashes a channelled beam that follows the cursor for 2.5 seconds that deals damage and slows enemies.",
    "name": "Vel'Koz",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VelkozQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VelkozW.png",
    "q_description": "Vel'Koz shoots a bolt of plasma that splits in two on reactivation or upon hitting an enemy. The bolt slows and damages on hit.",
    "title": "the Eye of the Void",
    "e_name": "Tectonic Disruption",
    "w_description": "Vel'Koz opens a rift to the void that deals an initial burst of damage, then explodes for a second burst of damage after a delay.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Velkoz.png",
    "recommended_item_names": [
      "Health Potion",
      "Doran's Ring",
      "Liandry's Torment",
      "Rylai's Crystal Scepter",
      "Sorcerer's Shoes"
    ],
    "w_name": "Void Rift",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/VelkozR.png",
    "role": "Mage",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Velkoz_Passive.png",
    "passive_description": "Vel'Koz's spells build Organic Deconstruction stacks on enemies. The third spell hit consumes the stacks and deals bonus true damage."
  },
  "201": {
    "lore": "''Would you like a bedtime story?''\n\n''Grandma, I'm too old for that.''\n\n''You're never too old to be told a story.''\n\nThe girl reluctantly crawls into bed and waits, knowing she won't win this battle. A bitter wind howls outside, whipping falling snow into devil whirls.\n\n''What kind? A tale of the Ice Witch, perhaps?'' her grandmother asks.\n\n''No, not her.''\n\n''What about a story of Braum?'' She was met with silence. The old woman smiles. ''Oh, there are so many. My grandmother used to tell me of the time Braum protected our village from the great dragon! Or once - this was long ago - he raced down a river of lava! Or -'' She pauses; puts a finger to her lips. ''Have I told you how Braum got his shield?''\n\nThe girl shakes her head. The hearth fire snaps, holding off the wind.\n\n''Well. In the mountains above our village lived a man named Braum -''\n\n''I know that!'' \n\n''He mostly kept to his farm, tending his sheep and goats, but he was the kindest man anyone had ever met, and he always had a smile on his face and a laugh on his lips.\n\n''Now, one day something terrible happened: a young troll boy around your age - was climbing the mountain and happened on a vault, set into the mountainside, the entrance guarded by a huge stone door with a shard of True Ice at its center. When he opened the door, he couldn't believe his eyes: the vault was filled with gold, jewels - every kind of treasure you could imagine!\n\n''What he didn't know was that the vault was a trap. The Ice Witch had cursed it - and as the troll boy entered, the magical door CLANGED shut behind him and locked him inside! Try as he might, he couldn't get out.\n\n''A passing shepherd heard his cries. Everyone rushed to help, but even the strongest warriors couldn't open the door. The boy's parents were beside themselves; his mother's wails of grief echoed around the mountain. It seemed hopeless.\n\n''And then, to everyone's surprise, they heard a distant laugh.''\n\n''It was Braum, wasn't it?''\n\n''Aren't you clever! Braum had heard their cries and came striding down the mountainside. The villagers told him of the troll boy and the curse. Braum smiled, nodded, turned to the vault, and faced the door. He pushed it. Pulled it. Punched it; kicked it; tried to rip it from its hinges. But the door wouldn't budge.''\n\n''But he's the strongest man ever!''\n\n''It was perplexing,'' her grandmother agrees. ''For four days and nights, Braum sat on a boulder, trying to think of a solution. After all, a child's life was at stake.\n\n''Then, as the sun rose on the fifth day, his eyes widened and a broad grin lit up his face. If I can't go through the door,' he said, then I'll just have to go through -''\n\nThe girl thinks; her own eyes widen. ''- the mountain!''\n\n''The mountain. Braum headed to the summit and began punching his way straight down, pummeling into the stone, fist after fist, rocks flying in his wake, until he had vanished deep into the mountain. \n\n''As the villagers held their breath, the rock around the door crumbled - and when the dust cleared, they saw Braum standing amidst the treasure, the weak but happy troll boy in his arms.''\n\n''I knew he could do it!''\n\n''But before they could celebrate, everything began to rumble and shake: Braum's tunnel had weakened the mountaintop, and now it was caving in! Thinking quickly, Braum grabbed the enchanted door and held it above him like a shield, protecting them as the mountaintop collapsed all around them. When it was over, Braum was amazed: there wasn't a single scratch on the door! Braum knew it was something very special.\n\n''And from that moment on, that magical shield never left Braum's side.''\n\nThe girl is sitting upright, struggling to conceal her excitement. Her grandmother waits. She shrugs and gets up to leave.\n\n''Grandma,'' the girl stops her, ''can you tell me another?''\n\n''Tomorrow.'' Her grandmother smiles; kisses her forehead; blows out the candle. ''For you need to sleep, and there are many more stories to tell.''",
    "champion_id": 201,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BraumE.png",
    "q_name": "Winter's Bite",
    "passive_name": "Concussive Blows",
    "e_description": "Braum raises his shield in a direction for several seconds, intercepting all projectiles causing them to hit him and be destroyed. He negates the damage of the first attack completely and reduces the damage of all subsequent attacks from this direction.",
    "recommended_items": [
      2003,
      3117,
      3302,
      3143,
      3800
    ],
    "r_name": "Glacial Fissure",
    "r_description": "Braum slams the ground, knocking up enemies nearby and in a line in front of him. A fissure is left along the line that slows enemies.",
    "name": "Braum",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BraumQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BraumW.png",
    "q_description": "Braum propels freezing ice from his shield, slowing and dealing magic damage.\n\nApplies a stack of <span class=\"colorFFF673\">Concussive Blows<\/span>.",
    "title": "the Heart of the Freljord",
    "e_name": "Unbreakable",
    "w_description": "Braum leaps to a target allied champion or minion. On arrival, Braum and the ally gain Armor and Magic Resist for a few seconds.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Braum.png",
    "recommended_item_names": [
      "Health Potion",
      "Boots of Mobility",
      "Relic Shield",
      "Randuin's Omen",
      "Righteous Glory"
    ],
    "w_name": "Stand Behind Me",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/BraumRWrapper.png",
    "role": "Support",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Braum_Passive.png",
    "passive_description": "Braum adds stacks of Concussive Blows to enemies with basic attacks or Winter's Bite. He and his allies continue to add stacks with basic attacks, at 4 stacks their target will be stunned."
  },
  "222": {
    "lore": "Jinx lives to wreak havoc without a thought for the consequences, leaving a trail of mayhem and panic in her wake. A manic and impulsive criminal, she despises nothing more than boredom, and gleefully brings her own volatile brand of pandemonium to the one place she finds dullest: Piltover. With an arsenal of deadly toys, she unleashes the brightest explosions and loudest blasts - all the better to shock and surprise the hapless authorities. Always just out of the law's reach, Jinx's favorite game is to toy with Piltover's finest - especially Vi.\n\nPiltover had long been known as the City of Progress, a place where peace and order reigned. That serenity was challenged when a new kind of criminal arrived, the likes of whom had never been seen. This mysterious outlaw unleashed a series of warped and destructive capers that endangered the entire city, and left its people reeling from the worst crime spree in Piltover's history.\n\nAs the string of crimes without rhyme or reason hit the city, sightings of the lawbreaker emerged. Though the young woman's origins were a mystery, some saw traces of Piltover hextech in her firearms, while others described the street fashions of Zaun in her dress. Because her arrival always brought trouble with it, those who crossed her path soon gave her a name: Jinx.\n\nAs Jinx's rampage escalated, Caitlyn - the sheriff of Piltover - responded by declaring a state of emergency and organizing a city-wide manhunt. In typical Jinx fashion, the criminal marked the Piltover treasury, the city's most secure building, with a direct challenge to its most abrasive officer. With a caricature of Vi's face splashed across the treasury's facade, and a scribbled time and date of her supposed raid, Jinx was openly daring the enforcer to stop her from robbing it.\n\nDetermined to put the troublemaker behind bars, Vi watched and waited outside the treasury until Jinx's time had finally come. True to her scrawled promise, the smiling menace showed her face. Knowing this was her chance to capture the outlaw, Vi gave chase into the building's interior. She smashed through wall after wall to chase down Jinx, who giggled as she lit up the evacuated treasury with fiery explosions. Vi finally cornered the criminal inside the vault, but Jinx wasn't done just yet. With a maniacal laugh, she fired a barrage of rockets, bringing the entire building down upon them both.\n\nWhen Vi finally crawled out of the ruins, the battered enforcer found no trace of Jinx. Adding insult to injury, not a single ounce of gold had been taken from the ruined vault. Instead, the criminal left a parting message to her favorite officer of the law - a challenge only now visible through the gaping opening in Piltover's skyline. The lights of the city spelled out a simple taunt: you'll never catch me. As Vi read the message, she heard the distant laughter of her new nemesis, and the city plunged into utter darkness for the very first time.\n\n''Oh look - I'm opening my box of care! Oh wait - it's empty!''\n-- Jinx",
    "champion_id": 222,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JinxE.png",
    "q_name": "Switcheroo!",
    "passive_name": "Get Excited!",
    "e_description": "Jinx throws out a line of snare grenades that explode after 5 seconds, lighting enemies on fire. Flame Chompers will bite enemy champions who walk over them, rooting them in place.",
    "recommended_items": [
      3102,
      2003,
      3035,
      1055,
      3006
    ],
    "r_name": "Super Mega Death Rocket!",
    "r_description": "Jinx fires a super rocket across the map that gains damage as it travels. The rocket will explode upon colliding with an enemy champion, dealing damage to it and surrounding enemies based on their missing Health. ",
    "name": "Jinx",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JinxQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JinxW.png",
    "q_description": "Jinx modifies her basic attacks by swapping between Pow-Pow, her minigun and Fishbones, her rocket launcher. Attacks with Pow-Pow grant Attack Speed, while attacks with Fishbones deal area of effect damage, gain increased range, and drain Mana.",
    "title": "the Loose Cannon",
    "e_name": "Flame Chompers!",
    "w_description": "Jinx uses Zapper, her shock pistol, to fire a blast that deals damage to the first enemy hit, slowing and revealing it if it is not stealthed.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Jinx.png",
    "recommended_item_names": [
      "Banshee's Veil",
      "Health Potion",
      "Last Whisper",
      "Doran's Blade",
      "Berserker's Greaves"
    ],
    "w_name": "Zap!",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JinxR.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Jinx_Passive.png",
    "passive_description": "Jinx receives massively increased Movement Speed whenever she damages an enemy champion, tower, or inhibitor that is then killed or destroyed within 3 seconds."
  },
  "236": {
    "lore": "Lucian wields relic weapons imbued with ancient power and stands a stalwart guardian against the undead. His cold conviction never wavers, even in the face of the maddening horrors he destroys beneath his hail of purifying fire. Lucian walks alone on a grim mission: to purge the spirits of those ensnared in undeath, his eternal beloved among them.\n\nLike the twin relic weapons they wielded, Lucian and his wife Senna were carved from the same stone. Together they battled evil in Runeterra for years, bringing light to darkness and purging those taken by corruption. They were beacons of righteousness: Senna's dedication to their cause never faltered, while Lucian's kindness and warmth touched the hearts of the many lives they saved. Two parts of one whole, they were devoted and inseparable.\n\nThough Lucian and Senna witnessed terror that would break most warriors, nothing they had seen compared to the horrors wrought by the Shadow Isles. When the spectral denizens of that accursed place began to manifest across Runeterra, Lucian and Senna hunted them down wherever they appeared. It was grim work, but the fearless pair prevailed until one tragic encounter with the soul-collector Thresh. Lucian and Senna had faced such nightmarish undead before, but never one so deviously clever and cruel. As the terrible battle unfolded, Thresh sprung an unexpected ploy. To Lucian's horror, the creature tricked Senna and ensnared her soul, trapping her in a spectral prison. Nothing could bring her back. Senna was lost, and for the first time, Lucian faced his mission alone. \n\nThough the Warden had taken half of Lucian's heart, he had also created the Shadow Isles' most dangerous foe. Lucian became a man of dark determination, one who would stop at nothing to purge the undead from the face of Runeterra. In honor of Senna's memory, he took up her fallen weapon and vowed to see their mission through to the end. Now wielding both relic weapons, Lucian fights to slay the undead and cleanse the souls of the Shadow Isles. He knows that Senna's soul is lost, but never loses hope that one day he will bring her peace. \n\n''Be grateful. By slaying you now, I spare you an eternity of torment.'' \n -- Lucian",
    "champion_id": 236,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LucianE.png",
    "q_name": "Piercing Light",
    "passive_name": "Lightslinger",
    "e_description": "Lucian quickly dashes a short distance. Lightslinger attacks reduce Relentless Pursuit's cooldown.",
    "recommended_items": [
      2003,
      3035,
      3026,
      1055,
      3006
    ],
    "r_name": "The Culling",
    "r_description": "Lucian unleashes a torrent of shots from his weapons.",
    "name": "Lucian",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LucianQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LucianW.png",
    "q_description": "Lucian shoots a bolt of piercing light through a target.",
    "title": "the Purifier",
    "e_name": "Relentless Pursuit",
    "w_description": "Lucian shoots a missile that explodes in a star shape, marking enemies. Lucian gains Movement Speed for attacking marked enemies.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Lucian.png",
    "recommended_item_names": [
      "Health Potion",
      "Last Whisper",
      "Guardian Angel",
      "Doran's Blade",
      "Berserker's Greaves"
    ],
    "w_name": "Ardent Blaze",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/LucianR.png",
    "role": "Marksman",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Lucian_Passive.png",
    "passive_description": "Whenever Lucian uses an ability, his next attack becomes a double-shot."
  },
  "238": {
    "lore": "Zed is the first ninja in 200 years to unlock the ancient, forbidden ways. He defied his clan and master, casting off the balance and discipline that had shackled him all his life. Zed now offers power to those who embrace knowledge of the shadows, and slays those who cling to ignorance.\n\nAn orphan, Zed was taken in and trained by a great ninja master. Only one other student appeared to be Zed's equal - the master's son, Shen. It seemed Zed could never win the favor of the master, as every match between the rivals ended in a draw. Frustrated and jealous, he sought an advantage. The young ninja ventured into a sealed part of the clan's temple, where he found an ornate, foreboding box. Sensing the dark knowledge within, Zed knew he should not open it, but he peered inside nonetheless. In an instant, shadows touched his mind, revealing techniques that had long been hidden. Now armed with a secret edge, he challenged Shen, and this time he defeated the master's son. He expected praise and recognition in his moment of victory, but somehow the master knew Zed had used forbidden ways, and banished him.\n\nHumiliated, the young ninja wandered for years. His bitterness turned to ambition, and he began to train others in the style of the shadows. As his power grew, so did his circle of followers, but he knew that without the box, his technique would never be perfect. One day, Zed looked at his followers and saw that his students were now an army. He led them back to the temple to claim his prize. At the gates, he was surprised to find the old master waiting, receiving Zed and his disciples as if they were welcome guests. The old man laid his sword at Zed's feet, declaring that he had failed Zed as his master. By banishing his former student, the master had doomed Zed to the shadows, instead of leading him to the balanced path. The old man implored Zed to enter the temple, destroy the box, and lead his followers to balance. The dark ninja followed the master inside. Moments later, the assembled ninjas heard Zed cry out in pain. Mysteriously, he emerged unscathed, and threw the severed head of the master at Shen's feet. Screaming in rage, Zed commanded his followers to slaughter the master's students and seize the box.\n\nThat day, the old ninja order fell. Though many students died, some escaped thanks to Shen's heroic efforts. Now the temple is a dark training ground for the Order of the Shadow. Zed rules as the Order's master, and his edict is simple: perfect one's technique, and kill all ninjas who refuse to embrace the shadows.\n\n''Balance is a lie - we are the true ninjas.''\n\n-- Zed",
    "champion_id": 238,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZedPBAOEDummy.png",
    "q_name": "Razor Shuriken",
    "passive_name": "Contempt for the Weak",
    "e_description": "Zed and his shadow spin their blades, creating a burst of shadow energy.  The shadow's spin slows.",
    "recommended_items": [
      1001,
      3071,
      1055,
      3067,
      1028
    ],
    "r_name": "Death Mark",
    "r_description": "Zed leaves a shadow behind and dashes to target Champion, marking them for death. After 3 seconds, the mark will trigger, dealing a percentage of the damage Zed has dealt while the mark was active. ",
    "name": "Zed",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZedShuriken.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZedShadowDash.png",
    "q_description": "Zed and his shadow both throw their spinning blades forward, dealing damage to any targets they pass through.",
    "title": "the Master of Shadows",
    "e_name": "Shadow Slash",
    "w_description": "Zed's shadow dashes forward, remaining in place for 4 seconds, and mimicking his spell casts. Zed can reactivate to swap places with the shadow. Zed's Attack Damage is passively increased.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Zed.png",
    "recommended_item_names": [
      "Boots of Speed",
      "The Black Cleaver",
      "Doran's Blade",
      "Kindlegem",
      "Ruby Crystal"
    ],
    "w_name": "Living Shadow",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ZedUlt.png",
    "role": "Assassin",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/shadowninja_P.png",
    "passive_description": "Zed's basic attacks against targets below 50% Health deal 6-10% of the target's maximum Health as bonus Magic Damage. This effect can only occur once every 10 seconds on the same target."
  },
  "10": {
    "lore": "In a world far away where an ancient war still rages, Kayle was a great hero - the strongest of an immortal race committed to destroying evil wherever it could be found. For ten thousand years, Kayle fought tirelessly for her people, wielding her flaming sword forged before time itself. She shielded her delicate features beneath her enchanted armor, the sole remaining masterpiece of an extinct race of craftsmen. Though a beautiful, striking creature, Kayle, now as then, avoids showing her face; war has taken a terrible toll upon her spirit. In her quest for victory, she sometimes would try to lift the wicked up from their morass of evil, but more than often she instead purged those she herself deemed beyond redemption. To Kayle, justice can so often be an ugly thing.\n\nTen years ago, Kayle's war against evil was nearly won... until her rebellious sister Morgana, a pariah amongst their people, suddenly gained powerful new allies: magicians of a hitherto unknown world called Runeterra. Morgana traded servitude to a number of the summoners in Runeterra's League of Legends for powerful new abilities that, if mastered, threatened to bring Kayle and her people to their knees. To save her world, Kayle had no choice but to make a pact with the League herself. She approached the leader of the League, High Counselor Reginald Ashram, with a deal of her own. In exchange for a thousand years of Kayle's service, Ashram halted all League interference on Kayle's world. With Ashram's disappearance five years ago, Kayle has new causes on Valoran: find out who or what caused Ashram to disappear, defeat her sister Morgana upon the Fields of Justice, and bring her own brand of justice to the League of Legends.\n\n''In the League of Legends, Justice comes on swift wings.''",
    "champion_id": 10,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JudicatorRighteousFury.png",
    "q_name": "Reckoning",
    "passive_name": "Holy Fervor",
    "e_description": "Ignites Kayle's sword with a holy flame, granting Kayle a ranged splash attack and bonus magic damage.",
    "recommended_items": [
      2003,
      3085,
      1039,
      3006,
      1056,
      3157,
      3020
    ],
    "r_name": "Intervention",
    "r_description": "Shields Kayle or an ally for a short time, causing them to be immune to damage.",
    "name": "Kayle",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JudicatorReckoning.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JudicatorDivineBlessing.png",
    "q_description": "Blasts an enemy unit with angelic force, dealing damage, slowing Movement Speed, and applying Holy Fervor.",
    "title": "The Judicator",
    "e_name": "Righteous Fury",
    "w_description": "Blesses a target friendly champion, granting them increased Movement Speed and healing them.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Kayle.png",
    "recommended_item_names": [
      "Health Potion",
      "Runaan's Hurricane (Ranged Only)",
      "Hunter's Machete",
      "Berserker's Greaves",
      "Doran's Ring",
      "Zhonya's Hourglass",
      "Sorcerer's Shoes"
    ],
    "w_name": "Divine Blessing",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/JudicatorIntervention.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/Kayle_Passive.png",
    "passive_description": "When Kayle attacks a champion, the target loses 3% Armor and Magic Resistance for 5 seconds. This effect stacks up to 5 times."
  },
  "254": {
    "lore": "To Vi, every problem is just another brick wall to punch through with her gigantic hextech gauntlets. Though she grew up on the wrong side of the law, Vi now uses her criminal know-how to serve Piltover's police force. Vi's brash attitude, abrasive humor, and blatant refusal to follow orders can often infuriate her by-the-books partner, Caitlyn. But even the sheriff of Piltover cannot deny that Vi is an invaluable asset in the fight against crime.\n\nAs a child growing up in the lawless outskirts of Piltover, Vi learned to rob and cheat to get by. Stealing and stripping hextech hardware gave her the skills of a master mechanic, while life on the streets taught her self-reliance. When she was six, a ragtag group of criminals took a shine to the young delinquent and brought her into their fold. By the time Vi was eleven, she had become a seasoned accomplice, and she relished the thrill of every heist.\n\nVi's attitude changed when a raid on a mining facility went bad. She was forced to decide between fleeing with her crew and trying to save the innocent mine workers from a collapsed tunnel. Vi chose to play the hero. While searching for a way to free the mine workers from the rubble, she discovered a damaged robotic mining rig. Improvising, she wrenched off its huge fists and modified them into makeshift hextech gauntlets. Fitting the heavy weapons to her tiny hands, the young girl flexed her arm and threw a powered punch at the rubble. The force of the blow blasted away the rock. With the workers free to escape, Vi fled the scene.\n\nAfter that job gone wrong, Vi severed her connection to the crew. She returned to a life of solitary crime, but stole only from other criminals. As the years went by, Vi modified and improved her hextech fists, allowing her to bust up heists and snatch loot with ease. Eventually, word of her notoriety reached Caitlyn, the famed Sheriff of Piltover. Rather than seek Vi's arrest, Caitlyn offered the criminal a way to pay her debt to society: work for the law in Piltover. Vi laughed. To her, a job that let her beat up crooks without forcing her to run from the cops sounded perfect. She immediately accepted. Caitlyn now struggles to keep Vi in line, and Vi treats Caitlyn's orders as mere suggestions, but when they work together, they are feared by all lawbreakers in Piltover.\n\n''It's a shame. I've got two fists, but you've only got one face.''\n-- Vi",
    "champion_id": 254,
    "e_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ViE.png",
    "q_name": "Vault Breaker",
    "passive_name": "Blast Shield",
    "e_description": "Vi's next attack blasts through her target, dealing damage to enemies behind it.",
    "recommended_items": [
      3047,
      2003,
      1039,
      3111,
      3071,
      1054,
      3143
    ],
    "r_name": "Assault and Battery",
    "r_description": "Vi runs down an enemy, knocking aside anyone in the way. When she reaches her target she knocks it into the air, jumps after it, and slams it back into the ground.",
    "name": "Vi",
    "q_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ViQ.png",
    "w_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ViW.png",
    "q_description": "Vi charges her gauntlets and unleashes a vault shattering punch, carrying her forward. Enemies she hits are knocked back and receive a stack of Denting Blows.",
    "title": "the Piltover Enforcer",
    "e_name": "Excessive Force",
    "w_description": "Vi's punches break her opponent's Armor, dealing bonus damage and granting her Attack Speed.",
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/champion\/Vi.png",
    "recommended_item_names": [
      "Ninja Tabi",
      "Health Potion",
      "Hunter's Machete",
      "Mercury's Treads",
      "The Black Cleaver",
      "Doran's Shield",
      "Randuin's Omen"
    ],
    "w_name": "Denting Blows",
    "r_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/spell\/ViR.png",
    "role": "Fighter",
    "passive_image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/passive\/ViPassive.png",
    "passive_description": "Vi charges a shield over time. The shield can be activated by hitting an enemy with an ability."
  }
}
        """
        for obj in response_data:
            for key in obj:
                if type(obj[key]) == list:
                    obj[key] = sorted(obj[key])

        for obj in expected_response:
            for key in obj:
                if type(obj[key]) == list:
                    obj[key] = sorted(obj[key])
        """


        for obj in response_data:
            self.assertTrue(obj in expected_response)

    def test_get_champion(self) :
        self.maxDiff = None
        expected_response = {"w_image": "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/Incinerate.png", "e_name": "Molten Shield", "title": "the Dark Child", "r_description": "Annie wills her bear Tibbers to life, dealing damage to units in the area. Tibbers can attack and also burns enemies that stand near him.", "passive_image": "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/passive/Annie_Passive.png", "q_image": "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/Disintegrate.png", "role": "Mage", "passive_description": "After casting 4 spells, Annie's next offensive spell will stun the target for a short duration.", "e_image": "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/MoltenShield.png", "w_name": "Incinerate", "w_description": "Annie casts a blazing cone of fire, dealing damage to all enemies in the area.", "champion_id": 1, "q_name": "Disintegrate", "r_name": "Summon: Tibbers", "r_image": "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/InfernalGuardian.png", "e_description": "Increases Annie's Armor and Magic Resist and damages enemies who hit Annie with basic attacks.", "lore": "In the time shortly before the League, there were those within the sinister city-state of Noxus who did not agree with the evils perpetrated by the Noxian High Command. The High Command had just put down a coup attempt from the self-proclaimed Crown Prince Raschallion, and a crack down on any form of dissent against the new government was underway. These political and social outcasts, known as the Gray Order, sought to leave their neighbors in peace as they pursued dark arcane knowledge. The leaders of this outcast society were a married couple: Gregori Hastur, the Gray Warlock, and his wife Amoline, the Shadow Witch. Together they led an exodus of magicians and other intelligentsia from Noxus, resettling their followers beyond the Great Barrier to the northern reaches of the unforgiving Voodoo Lands. Though survival was a challenge at times, the Gray Order's colony managed to thrive in a land where so many others would have failed.\n\nYears after the exodus, Gregori and Amoline had a child: Annie. Early on, Annie's parents knew there was something special about their daughter. At the age of two, Annie miraculously ensorcelled a shadow bear - a ferocious denizen of the petrified forests outside the colony - turning it into her pet. To this day she keeps her bear ''Tibbers'' by her side, often keeping him spellbound as a stuffed doll to be carried like a child's toy. The combination of Annie's lineage and the dark magic of her birthplace have given this little girl tremendous arcane power. It is this same girl who now finds herself as one of the most sought-after champions within the League of Legends - even by the city-state that would have exiled her parents had they not fled beforehand.\n\n''Annie may be one of the most powerful champions ever to have fought in a Field of Justice. I shudder to think of her capabilities when she becomes an adult.''\n-- High Councilor Kiersta Mandrake", "image": "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/champion/Annie.png", "recommended_items": [1056, 1028, 1001, 3010, 3151], "q_description": "Annie hurls a Mana infused fireball, dealing damage and refunding the Mana cost if it destroys the target.", "passive_name": "Pyromania", "name": "Annie"}
        request = Request(self.url+"api/champions/1/")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        """
        for key in response_data:
            if type(response_data[key]) == list:
                response_data[key] = sorted(response_data[key])
        """
        self.assertEqual(expected_response, response_data)

# -------
# Player
# -------

    def test_get_all_players(self) :
        request = Request(self.url+"api/players/")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        #response_objects = response_data["objects"]
        expected_response = {
  "2178": {
    "last_name": "",
    "team_name": "Najin e-mFire",
    "most_played_champion_names": [
      "Sivir",
      "Vayne",
      "Lucian"
    ],
    "player_id": 2178,
    "games_played": 6,
    "total_gold": 72298,
    "first_name": "Gyumin",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/NJE-Ohq-2015lck.jpg",
    "ign": "Ohq",
    "kda": 3.4545454545455,
    "gpm": 339.05580740972,
    "role": "AD Carry",
    "most_played_champions": [
      15,
      67,
      236
    ],
    "bio": "Ohq is the AD Carry for Xenics Storm. As an important member of this new squad, Ohq\u2019s performance will be crucial to their debut in the OGN Champions Spring. "
  },
  "918": {
    "last_name": "",
    "team_name": "CJ ENTUS",
    "most_played_champion_names": [
      "Sivir",
      "Lucian",
      "Jinx"
    ],
    "player_id": 918,
    "games_played": 6,
    "total_gold": 86400,
    "first_name": "Hosan",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/CJ-Space-2015lck.png",
    "ign": "Space",
    "kda": 8.8888888888889,
    "gpm": 403.64400840925,
    "role": "AD Carry",
    "most_played_champions": [
      15,
      236,
      222
    ],
    "bio": ""
  },
  "2125": {
    "last_name": "",
    "team_name": "Longzhu Incredible Miracle",
    "most_played_champion_names": [
      "Lee Sin",
      "Shyvana",
      "Renekton"
    ],
    "player_id": 2125,
    "games_played": 6,
    "total_gold": 62452,
    "first_name": "Jung",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/IM-Apple-2015lck.jpg",
    "ign": "Apple",
    "kda": 2.6470588235294,
    "gpm": 313.43538268507,
    "role": "Top Lane",
    "most_played_champions": [
      64,
      102,
      58
    ],
    "bio": ""
  },
  "3722": {
    "last_name": "",
    "team_name": "Samsung Galaxy",
    "most_played_champion_names": [
      "Sivir",
      "Graves",
      "Corki"
    ],
    "player_id": 3722,
    "games_played": 32,
    "total_gold": 452677,
    "first_name": "Lee",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SSG-Fury-2015lck.jpg",
    "ign": "Fury",
    "kda": 2.7848101265823,
    "gpm": 358.67441399802,
    "role": "AD Carry",
    "most_played_champions": [
      15,
      104,
      42
    ],
    "bio": ""
  },
  "877": {
    "last_name": "",
    "team_name": "SKTelecom T1",
    "most_played_champion_names": [
      "Shyvana",
      "Renekton",
      "Ryze"
    ],
    "player_id": 877,
    "games_played": 7,
    "total_gold": 79722,
    "first_name": "Kyunghwan",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SKT-Marin-2015lck.jpg",
    "ign": "MaRin",
    "kda": 2,
    "gpm": 328.25418611035,
    "role": "Top Lane",
    "most_played_champions": [
      102,
      58,
      13
    ],
    "bio": "Kyunghwan \"Marin\" Jang dove directly into the deep end of Korea\u2019s esports ecosystem when he signed with SK Telecom T1 S in 2013. After the SK organization consolidated their dual teams into one squad, Marin was named the starting top laner for the remade SK Telecom T1, one of the strongest League of Legends teams in the world. With a penchant for disrupting enemy teams by playing tanky champions like Maokai and Gnar, Marin is a feared opponent on Summoner\u2019s Rift."
  },
  "2160": {
    "last_name": "",
    "team_name": "Jin Air Green Wings",
    "most_played_champion_names": [
      "Nidalee",
      "Heimerdinger",
      "Orianna"
    ],
    "player_id": 2160,
    "games_played": 6,
    "total_gold": 61926,
    "first_name": "Changseok",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/GBM-headshot.jpg",
    "ign": "GBM",
    "kda": 1.2916666666667,
    "gpm": 303.3853188536,
    "role": "Mid Lane",
    "most_played_champions": [
      76,
      74,
      61
    ],
    "bio": ""
  },
  "662": {
    "last_name": "",
    "team_name": "Longzhu Incredible Miracle",
    "most_played_champion_names": [
      
    ],
    "player_id": 662,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Koo",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/worlds_players_Najin_Expession.jpg",
    "ign": "Expession",
    "kda": 0,
    "gpm": 0,
    "role": "Top Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "663": {
    "last_name": "",
    "team_name": "Najin e-mFire",
    "most_played_champion_names": [
      "Elise",
      "Lee Sin",
      "Kha'Zix"
    ],
    "player_id": 663,
    "games_played": 7,
    "total_gold": 89702,
    "first_name": "Jae-geol",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/NJE-Watch-2015lck.jpg",
    "ign": "Watch",
    "kda": 3.8125,
    "gpm": 281.56526288255,
    "role": "Jungler",
    "most_played_champions": [
      60,
      64,
      121
    ],
    "bio": "Watch is Najin White Shield\u2019s aggressive jungler. Focusing on ganking quickly to avoid counterganks, Watch favors champions like Elise and Lee Sin, though he was first known for his Nocturne play while he was an amateur. Due to his \u2018babysitting\u2019 style, it goes without saying that he will be a player to watch at the 2014 World Championship."
  },
  "2801": {
    "last_name": "",
    "team_name": "Longzhu Incredible Miracle",
    "most_played_champion_names": [
      
    ],
    "player_id": 2801,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Taeil",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/IM-Frozen-2015lck.jpg",
    "ign": "Frozen",
    "kda": 0,
    "gpm": 0,
    "role": "Mid Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "880": {
    "last_name": "",
    "team_name": "SKTelecom T1",
    "most_played_champion_names": [
      
    ],
    "player_id": 880,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Jihoon",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SKT-EasyHoon-2015lck.jpg",
    "ign": "Easyhoon",
    "kda": 0,
    "gpm": 0,
    "role": "Mid Lane",
    "most_played_champions": [
      
    ],
    "bio": "Jihoon \u201cEasyHoon\u201d Lee has bumped heads in the mid lane with some of the best players in the world, including Faker, Ambition, Ryu, and more. After debuting as a pro player with MVP Blue in 2013, EasyHoon was quickly picked up by SKT T1 as a dynamic mid lane substitute. With a control-mage focused mid lane style EasyHoon compliments Faker\u2019s assassin play perfectly, allowing SKT to prepare a diverse set of strategies."
  },
  "4386": {
    "last_name": "",
    "team_name": "Jin Air Green Wings",
    "most_played_champion_names": [
      
    ],
    "player_id": 4386,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Seong-huyk",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/Kuzan.jpg",
    "ign": "Kuzan",
    "kda": 0,
    "gpm": 0,
    "role": "Mid Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4643": {
    "last_name": "",
    "team_name": "KT Rolster",
    "most_played_champion_names": [
      
    ],
    "player_id": 4643,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Ho-seong",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KT-Edge-2015-lck.png",
    "ign": "Edge",
    "kda": 0,
    "gpm": 0,
    "role": "Mid Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "2808": {
    "last_name": "",
    "team_name": "Jin Air Green Wings",
    "most_played_champion_names": [
      
    ],
    "player_id": 2808,
    "games_played": 6,
    "total_gold": 0,
    "first_name": "Seonho",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/chei-headshot.jpg",
    "ign": "Chei",
    "kda": 0,
    "gpm": 0,
    "role": "Support",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4389": {
    "last_name": "",
    "team_name": "Samsung Galaxy",
    "most_played_champion_names": [
      
    ],
    "player_id": 4389,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Min-ho",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SSG-Crown-2015lck.jpg",
    "ign": "Crown",
    "kda": 0,
    "gpm": 0,
    "role": "Mid Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "934": {
    "last_name": "",
    "team_name": "Jin Air Green Wings",
    "most_played_champion_names": [
      
    ],
    "player_id": 934,
    "games_played": 6,
    "total_gold": 0,
    "first_name": "Hyungwoo",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/cpt-jack-headshot.jpg",
    "ign": "Cpt Jack",
    "kda": 0,
    "gpm": 0,
    "role": "AD Carry",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4391": {
    "last_name": "",
    "team_name": "Jin Air Green Wings",
    "most_played_champion_names": [
      
    ],
    "player_id": 4391,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Eun-teak",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/sweet-headshot.jpg",
    "ign": "Sweet",
    "kda": 0,
    "gpm": 0,
    "role": "Support",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "2812": {
    "last_name": "",
    "team_name": "KOO Tigers",
    "most_played_champion_names": [
      "Jarvan IV",
      "Lee Sin"
    ],
    "player_id": 2812,
    "games_played": 31,
    "total_gold": 370324,
    "first_name": "Hojin",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KOO-Hojin-2015lck.jpg",
    "ign": "Hojin",
    "kda": 4.45,
    "gpm": 305.86330786702,
    "role": "Jungler",
    "most_played_champions": [
      59,
      64
    ],
    "bio": ""
  },
  "882": {
    "last_name": "",
    "team_name": "SKTelecom T1",
    "most_played_champion_names": [
      "Annie",
      "Thresh",
      "Zyra"
    ],
    "player_id": 882,
    "games_played": 7,
    "total_gold": 49113,
    "first_name": "Jaewan",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SKT-Wolf-2015lck.jpg",
    "ign": "Wolf",
    "kda": 1.5416666666667,
    "gpm": 202.22206972276,
    "role": "Support",
    "most_played_champions": [
      1,
      412,
      143
    ],
    "bio": "Jaewan \"Wolf\" Lee launched his esports career with NaJin Shield in 2012. After training his support skills with Locodoco at NaJin, Wolf eventually made his way to SK Telecom T1 S in 2013. Shortly after he joined, the organization was restructured, and Wolf suddenly found himself on SK Telecom T1. Now Wolf and Bang are beginning to cement their bond as a bot lane duo, with Wolf playing a crucial role in Bang's deadly Kalista and Sivir play."
  },
  "686": {
    "last_name": "",
    "team_name": "KT Rolster",
    "most_played_champion_names": [
      "Lulu",
      "Gragas",
      "Ziggs"
    ],
    "player_id": 686,
    "games_played": 6,
    "total_gold": 100172,
    "first_name": "Sangmoon",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KT-Nagne-2015lck.jpg",
    "ign": "Nagne",
    "kda": 3.7692307692308,
    "gpm": 396.35452387233,
    "role": "Mid Lane",
    "most_played_champions": [
      117,
      79,
      115
    ],
    "bio": ""
  },
  "2803": {
    "last_name": "",
    "team_name": "Longzhu Incredible Miracle",
    "most_played_champion_names": [
      
    ],
    "player_id": 2803,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Jongik",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/IM-Tusin-2015lck.jpg",
    "ign": "TuSin",
    "kda": 0,
    "gpm": 0,
    "role": "Support",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "692": {
    "last_name": "",
    "team_name": "SKTelecom T1",
    "most_played_champion_names": [
      "Ahri",
      "Riven",
      "Gragas"
    ],
    "player_id": 692,
    "games_played": 8,
    "total_gold": 99147,
    "first_name": "Sanghyuk",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SKT-Faker-2015lck.jpg",
    "ign": "Faker",
    "kda": 5.3125,
    "gpm": 392.42826043934,
    "role": "Mid Lane",
    "most_played_champions": [
      103,
      92,
      79
    ],
    "bio": "Considered one of the best mid laners in the world, Sanghyuk \"Faker\" Lee is an icon of modern esports. Faker was integral to SKT T1 K\u2019s 1st place finish in the 2013 League of Legends World Championship and the OGN Champions league. Mainly favoring assassins in the mid lane, Faker has dominated his competition over the years with Ahri, Zed, Riven, and especially LeBlanc. While Faker has already raised the bar for what a mid laner is expected to deliver, only time will tell if he is truly the best player ever to compete in League of Legends."
  },
  "693": {
    "last_name": "",
    "team_name": "SKTelecom T1",
    "most_played_champion_names": [
      "Lee Sin",
      "Jarvan IV",
      "Elise"
    ],
    "player_id": 693,
    "games_played": 8,
    "total_gold": 71808,
    "first_name": "Sungwoong",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SKT-Bengi-2015lck.jpg",
    "ign": "bengi",
    "kda": 6.7692307692308,
    "gpm": 284.21927567782,
    "role": "Jungler",
    "most_played_champions": [
      64,
      59,
      60
    ],
    "bio": "Seong-Woong \"Bengi\" Bae is a former League of Legends World Champion and star jungler for SKT T1. Known for his supportive jungling style that focuses more on feeding his solo lanes than getting himself ahead, Bengi is a core component in the Faker terror train. However, Bengi is more than just a support jungle. He is also known for his excellent Lee Sin and Vi mechanics, and is comfortable playing whichever role his team requires. After achieving 1st place in both OGN and the World Championships, Bengi doesn\u2019t have much to prove anymore. But that doesn\u2019t mean he has lost his competitive drive, as evidenced by his unstoppable 11W-2L record on Jarvan IV and a clean 100% win record with Sejuani in the LCK Spring Split."
  },
  "3644": {
    "last_name": "",
    "team_name": "CJ ENTUS",
    "most_played_champion_names": [
      
    ],
    "player_id": 3644,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Jong-bean",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/CJ-Max-2015lck.png",
    "ign": "Max",
    "kda": 0,
    "gpm": 0,
    "role": "Support",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "3645": {
    "last_name": "",
    "team_name": "Samsung Galaxy",
    "most_played_champion_names": [
      "Maokai",
      "Rumble",
      "Dr. Mundo"
    ],
    "player_id": 3645,
    "games_played": 32,
    "total_gold": 403789,
    "first_name": "Seong-jin",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SSG-CuVee-2015lck.jpg",
    "ign": "CuVee",
    "kda": 1.8347826086957,
    "gpm": 319.93846153846,
    "role": "Top Lane",
    "most_played_champions": [
      57,
      68,
      36
    ],
    "bio": ""
  },
  "3646": {
    "last_name": "",
    "team_name": "Samsung Galaxy",
    "most_played_champion_names": [
      "Lee Sin",
      "Nidalee"
    ],
    "player_id": 3646,
    "games_played": 32,
    "total_gold": 349301,
    "first_name": "Jun-cheol",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SSG-Eve-2015lck.jpg",
    "ign": "Eve",
    "kda": 2.3440860215054,
    "gpm": 276.76540112248,
    "role": "Jungler",
    "most_played_champions": [
      64,
      76
    ],
    "bio": ""
  },
  "2805": {
    "last_name": "",
    "team_name": "Jin Air Green Wings",
    "most_played_champion_names": [
      
    ],
    "player_id": 2805,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Woohyung",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/pilot-headshot.jpg",
    "ign": "Pilot",
    "kda": 0,
    "gpm": 0,
    "role": "AD Carry",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "3648": {
    "last_name": "",
    "team_name": "Samsung Galaxy",
    "most_played_champion_names": [
      "Janna",
      "Thresh",
      "Nami"
    ],
    "player_id": 3648,
    "games_played": 32,
    "total_gold": 239575,
    "first_name": "Ji-min",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SSG-Wraith-2015lck.jpg",
    "ign": "Wraith",
    "kda": 2.2826086956522,
    "gpm": 189.82502476065,
    "role": "Support",
    "most_played_champions": [
      40,
      412,
      267
    ],
    "bio": ""
  },
  "3777": {
    "last_name": "",
    "team_name": "Longzhu Incredible Miracle",
    "most_played_champion_names": [
      
    ],
    "player_id": 3777,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "DongGeun",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/IM-IgNar-2015lck.jpg",
    "ign": "Ignar",
    "kda": 0,
    "gpm": 0,
    "role": "Support",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4162": {
    "last_name": "",
    "team_name": "SKTelecom T1",
    "most_played_champion_names": [
      
    ],
    "player_id": 4162,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Jae-hyun",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SKT-Tom-2015lck.jpg",
    "ign": "Tom",
    "kda": 0,
    "gpm": 0,
    "role": "Jungler",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "2163": {
    "last_name": "",
    "team_name": "KT Rolster",
    "most_played_champion_names": [
      "Lucian",
      "Corki",
      "Kog'Maw"
    ],
    "player_id": 2163,
    "games_played": 6,
    "total_gold": 97236,
    "first_name": "Dongbin",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KT-Score-2015lck.jpg",
    "ign": "Score",
    "kda": 6,
    "gpm": 400.53274749416,
    "role": "Jungler",
    "most_played_champions": [
      236,
      42,
      96
    ],
    "bio": "Score is the AD carry for the KT Bullets. Once referred to as the \u201cKing of Survive,\u201d Scores positioning in teamfights is impeccable, taking full advantage of his responsibility to do as much damage as possible while staying alive. Particularly comfortable on Ezreal, look to Score as a major source of stunning play on the KT Bullets.  "
  },
  "3190": {
    "last_name": "",
    "team_name": "Rebels Anarchy",
    "most_played_champion_names": [
      "Lulu",
      "Twisted Fate",
      "Ahri"
    ],
    "player_id": 3190,
    "games_played": 5,
    "total_gold": 61450,
    "first_name": "Yongmin",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/Anarchy-Mickey-2015lck.jpg",
    "ign": "Mickey",
    "kda": 2.1428571428571,
    "gpm": 370.25507129946,
    "role": "Mid Lane",
    "most_played_champions": [
      117,
      4,
      103
    ],
    "bio": ""
  },
  "886": {
    "last_name": "",
    "team_name": "KOO Tigers",
    "most_played_champion_names": [
      "LeBlanc",
      "Kassadin",
      "Viktor"
    ],
    "player_id": 886,
    "games_played": 31,
    "total_gold": 469539,
    "first_name": "Seohang",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KOO-Kuro-2015lck.jpg",
    "ign": "KurO",
    "kda": 5,
    "gpm": 387.80838323353,
    "role": "Mid Lane",
    "most_played_champions": [
      7,
      38,
      112
    ],
    "bio": ""
  },
  "2167": {
    "last_name": "",
    "team_name": "Najin e-mFire",
    "most_played_champion_names": [
      
    ],
    "player_id": 2167,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Jinsun",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/NJE-Pure-2015lck.jpg",
    "ign": "Pure",
    "kda": 0,
    "gpm": 0,
    "role": "Support",
    "most_played_champions": [
      
    ],
    "bio": "Formerly the support for Prime Sentinel, Pure now subs for Najin White Shield as a support. Like his name suggests, he is a pure competitor and a strong addition to NWS."
  },
  "4685": {
    "last_name": "",
    "team_name": "SBENU SONICBOOM",
    "most_played_champion_names": [
      
    ],
    "player_id": 4685,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Gang-Pyo",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/templateSilhoutte_3.jpg",
    "ign": "SoaR",
    "kda": 0,
    "gpm": 0,
    "role": "Top Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "2126": {
    "last_name": "",
    "team_name": "Longzhu Incredible Miracle",
    "most_played_champion_names": [
      "Lucian",
      "Jinx"
    ],
    "player_id": 2126,
    "games_played": 4,
    "total_gold": 58221,
    "first_name": "Hyun-Il",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/wfx-paragon-2015.jpg",
    "ign": "Paragon",
    "kda": 15.333333333333,
    "gpm": 411.50429968194,
    "role": "AD Carry",
    "most_played_champions": [
      236,
      222
    ],
    "bio": ""
  },
  "2807": {
    "last_name": "",
    "team_name": "Jin Air Green Wings",
    "most_played_champion_names": [
      
    ],
    "player_id": 2807,
    "games_played": 6,
    "total_gold": 0,
    "first_name": "Sanghyun",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/chaser-headshot.jpg",
    "ign": "Chaser",
    "kda": 0,
    "gpm": 0,
    "role": "Jungler",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4344": {
    "last_name": "",
    "team_name": "SBENU SONICBOOM",
    "most_played_champion_names": [
      "Lulu",
      "Morgana",
      "Ziggs"
    ],
    "player_id": 4344,
    "games_played": 5,
    "total_gold": 75193,
    "first_name": "Oh",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SBE-SaSin-2015lck.jpg",
    "ign": "SaSin",
    "kda": 7,
    "gpm": 344.26402136589,
    "role": "Mid Lane",
    "most_played_champions": [
      117,
      25,
      115
    ],
    "bio": ""
  },
  "2147": {
    "last_name": "",
    "team_name": "KT Rolster",
    "most_played_champion_names": [
      
    ],
    "player_id": 2147,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Chanho",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KT-SSumday-2015lck.jpg",
    "ign": "Ssumday",
    "kda": 0,
    "gpm": 0,
    "role": "Top Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4345": {
    "last_name": "",
    "team_name": "SBENU SONICBOOM",
    "most_played_champion_names": [
      
    ],
    "player_id": 4345,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Kim",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SBE-dan-2015lck.jpg",
    "ign": "dan",
    "kda": 0,
    "gpm": 0,
    "role": "AD Carry",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "370": {
    "last_name": "",
    "team_name": "CJ ENTUS",
    "most_played_champion_names": [
      "Annie",
      "Leona",
      "Alistar"
    ],
    "player_id": 370,
    "games_played": 6,
    "total_gold": 56579,
    "first_name": "Mingi",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/CJ-Madlife-2015lck.png",
    "ign": "MadLife",
    "kda": 6.6666666666667,
    "gpm": 264.32609203457,
    "role": "Support",
    "most_played_champions": [
      1,
      89,
      12
    ],
    "bio": "Madlife, CJ Entus Frost\u2019s support, is the most popular pro in Korea. Eternally capable of carrying games from the support role, Madlife is particularly well known for his exceptional non-target skills. He is so impactful that opposing teams will ban him out entirely, using all three bans on champions like Thresh, Blitzcrank, and Sona. Putting the icing on the cake, Madlife is often referred to as \u2018God\u2019 by Korean fans, a title earned many times over by this incredible talent. His celebrity is well reinforced, as his fans have spoken and earned Madlife enough votes to head to Paris for the 2014 All-Star Challenge alongside teammate Shy. It\u2019s always a treat to see Madlife play internationally, and All-Star Challenge viewers are in for a serious showing this year. "
  },
  "4388": {
    "last_name": "",
    "team_name": "Rebels Anarchy",
    "most_played_champion_names": [
      
    ],
    "player_id": 4388,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Ik-su",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/Anarchy-Ikssu-2015lck.jpg",
    "ign": "ikssu",
    "kda": 0,
    "gpm": 0,
    "role": "Top Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "881": {
    "last_name": "",
    "team_name": "SKTelecom T1",
    "most_played_champion_names": [
      "Lucian",
      "Caitlyn",
      "Sivir"
    ],
    "player_id": 881,
    "games_played": 7,
    "total_gold": 85383,
    "first_name": "Junsik",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SKT-Bang-2015lck.jpg",
    "ign": "Bang",
    "kda": 2.875,
    "gpm": 351.56327202855,
    "role": "AD Carry",
    "most_played_champions": [
      236,
      51,
      15
    ],
    "bio": "Junsik \"Bang\" Bae launched his professional gaming career in 2012 with NaJin Shield and Xenics Storm before joining SKT T1 S in 2013. When SKT T1 S secured 3rd place in the 2014 Summer OGN Champions league, Bang had officially arrived. When the SKT organization was consolidated into one squad, SK Telecom T1, Bang was partnered with Wolf in the bot lane. Their duo partnership has flourished, with Bang achieving a 6.4 KDA and a 100% win rate with Kalista in the LCK Spring Split."
  },
  "991": {
    "last_name": "",
    "team_name": "Jin Air Green Wings",
    "most_played_champion_names": [
      
    ],
    "player_id": 991,
    "games_played": 6,
    "total_gold": 0,
    "first_name": "Changdong",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/JinAir-TrAce-2015lck.jpg",
    "ign": "TrAce",
    "kda": 0,
    "gpm": 0,
    "role": "Top Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4683": {
    "last_name": "",
    "team_name": "CJ ENTUS",
    "most_played_champion_names": [
      
    ],
    "player_id": 4683,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Young Jae",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/CJ-Helper-2015lck.png",
    "ign": "Helper",
    "kda": 0,
    "gpm": 0,
    "role": "Top Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4347": {
    "last_name": "",
    "team_name": "SBENU SONICBOOM",
    "most_played_champion_names": [
      
    ],
    "player_id": 4347,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Han",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SBE-viviD-2015lck.jpg",
    "ign": "viviD",
    "kda": 0,
    "gpm": 0,
    "role": "Support",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4390": {
    "last_name": "",
    "team_name": "Samsung Galaxy",
    "most_played_champion_names": [
      
    ],
    "player_id": 4390,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Kyung-ho",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SSG-Luna-2015lck.jpg",
    "ign": "Luna",
    "kda": 0,
    "gpm": 0,
    "role": "Support",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "2151": {
    "last_name": "",
    "team_name": "KOO Tigers",
    "most_played_champion_names": [
      "Lulu",
      "Rumble"
    ],
    "player_id": 2151,
    "games_played": 31,
    "total_gold": 452030,
    "first_name": "Kyungho",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KOO-Smeb-2015lck.jpg",
    "ign": "Smeb",
    "kda": 5.2253521126761,
    "gpm": 373.34709890564,
    "role": "Top Lane",
    "most_played_champions": [
      117,
      68
    ],
    "bio": ""
  },
  "2152": {
    "last_name": "",
    "team_name": "Longzhu Incredible Miracle",
    "most_played_champion_names": [
      
    ],
    "player_id": 2152,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Ho-jin",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/IM-Lil4c-2015lck.jpg",
    "ign": "Lilac",
    "kda": 0,
    "gpm": 0,
    "role": "Top Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4348": {
    "last_name": "",
    "team_name": "SBENU SONICBOOM",
    "most_played_champion_names": [
      "Thresh",
      "Nautilus"
    ],
    "player_id": 4348,
    "games_played": 5,
    "total_gold": 44869,
    "first_name": "Park",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SBE-Secret-2015lck.jpg",
    "ign": "Secret",
    "kda": 3.4166666666667,
    "gpm": 205.42846241892,
    "role": "Support",
    "most_played_champions": [
      412,
      111
    ],
    "bio": ""
  },
  "874": {
    "last_name": "",
    "team_name": "Longzhu Incredible Miracle",
    "most_played_champion_names": [
      
    ],
    "player_id": 874,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Jangwon",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/IM-Roar-2015lck.jpg",
    "ign": "Roar",
    "kda": 0,
    "gpm": 0,
    "role": "AD Carry",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4331": {
    "last_name": "",
    "team_name": "Rebels Anarchy",
    "most_played_champion_names": [
      "Rengar",
      "Hecarim"
    ],
    "player_id": 4331,
    "games_played": 5,
    "total_gold": 58589,
    "first_name": "Kim",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/Anarchy-cyMax-2015lck.jpg",
    "ign": "cyMax",
    "kda": 1.6086956521739,
    "gpm": 353.01667001406,
    "role": "Top Lane",
    "most_played_champions": [
      107,
      120
    ],
    "bio": ""
  },
  "4332": {
    "last_name": "",
    "team_name": "Rebels Anarchy",
    "most_played_champion_names": [
      "Gragas",
      "Lee Sin"
    ],
    "player_id": 4332,
    "games_played": 5,
    "total_gold": 50080,
    "first_name": "Nam",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/Anarchy-Lira-2015LCK.jpg",
    "ign": "lira",
    "kda": 2.875,
    "gpm": 301.74733882306,
    "role": "Jungler",
    "most_played_champions": [
      79,
      64
    ],
    "bio": ""
  },
  "4077": {
    "last_name": "",
    "team_name": "KT Rolster",
    "most_played_champion_names": [
      
    ],
    "player_id": 4077,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Jung ",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KT-Fixer-2015lck.jpg",
    "ign": "Fixer",
    "kda": 0,
    "gpm": 0,
    "role": "Support",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4334": {
    "last_name": "",
    "team_name": "Rebels Anarchy",
    "most_played_champion_names": [
      "Sivir",
      "Ezreal",
      "Jinx"
    ],
    "player_id": 4334,
    "games_played": 5,
    "total_gold": 61938,
    "first_name": "Kwon",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/Anarchy-Sangyoon-2015lck.jpg",
    "ign": "Sangyoon",
    "kda": 2.4,
    "gpm": 373.19542076722,
    "role": "AD Carry",
    "most_played_champions": [
      15,
      81,
      222
    ],
    "bio": ""
  },
  "4335": {
    "last_name": "",
    "team_name": "Rebels Anarchy",
    "most_played_champion_names": [
      "Thresh",
      "Alistar",
      "Leona"
    ],
    "player_id": 4335,
    "games_played": 5,
    "total_gold": 36715,
    "first_name": "No",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/Anarchy-SnowFlower-2015lck.jpg",
    "ign": "SnowFlower",
    "kda": 1.7916666666667,
    "gpm": 221.21912030528,
    "role": "Support",
    "most_played_champions": [
      412,
      12,
      89
    ],
    "bio": ""
  },
  "2800": {
    "last_name": "",
    "team_name": "KOO Tigers",
    "most_played_champion_names": [
      "Jarvan IV",
      "Lee Sin",
      "Elise"
    ],
    "player_id": 2800,
    "games_played": 16,
    "total_gold": 174564,
    "first_name": "Tae-wan",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KOO-Wisdom-2015lck.jpg",
    "ign": "Wisdom",
    "kda": 2.3818181818182,
    "gpm": 274.25608798115,
    "role": "Jungler",
    "most_played_champions": [
      59,
      64,
      60
    ],
    "bio": ""
  },
  "369": {
    "last_name": "",
    "team_name": "KOO Tigers",
    "most_played_champion_names": [
      "Corki",
      "Kog'Maw",
      "Lucian"
    ],
    "player_id": 369,
    "games_played": 31,
    "total_gold": 502789,
    "first_name": "Kim",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KOO-Pray-2015lck.jpg",
    "ign": "PraY",
    "kda": 7.8260869565217,
    "gpm": 415.27069997935,
    "role": "AD Carry",
    "most_played_champions": [
      42,
      96,
      236
    ],
    "bio": "Joining him in the duo lane is Kim \"PraY\" Jong-in, NaJin Sword's potent AD carry. PraY demonstrated clear mastery of the metagame in Season 2 and has continued his success in Season 3. With his aggressive AD play and intense drive, PraY's prepared to show opponents in China there's only one thing left to do."
  },
  "2802": {
    "last_name": "",
    "team_name": "Longzhu Incredible Miracle",
    "most_played_champion_names": [
      
    ],
    "player_id": 2802,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Seungik",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/IM-Sonstar-2015lck.jpg",
    "ign": "SONSTAR",
    "kda": 0,
    "gpm": 0,
    "role": "AD Carry",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "371": {
    "last_name": "",
    "team_name": "CJ ENTUS",
    "most_played_champion_names": [
      "Renekton",
      "Shyvana"
    ],
    "player_id": 371,
    "games_played": 6,
    "total_gold": 80354,
    "first_name": "Sangmyun",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/CJ-Shy-2015lck.png",
    "ign": "Shy",
    "kda": 6.0833333333333,
    "gpm": 375.39827143191,
    "role": "Top Lane",
    "most_played_champions": [
      58,
      102
    ],
    "bio": ""
  },
  "372": {
    "last_name": "",
    "team_name": "CJ ENTUS",
    "most_played_champion_names": [
      
    ],
    "player_id": 372,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Chan-yong",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/CJ-Ambition-2015lck.png",
    "ign": "Ambition",
    "kda": 0,
    "gpm": 0,
    "role": "Jungler",
    "most_played_champions": [
      
    ],
    "bio": "Representing Korea and CJ Entus Blaze, Kang \"Ambition\" Chan-yong heads to China as the mid-lane player. His pool of champions rivals any of the players heading to Shanghai, and his sharp mechanics reinforced his solid play throughout the summer. Seeking to test his mettle against Alex Ich and the strongest mid lane players from around the globe, Ambition will attempt to live up to his nickname and help lead Korea to victory."
  },
  "4341": {
    "last_name": "",
    "team_name": "SBENU SONICBOOM",
    "most_played_champion_names": [
      "Rumble",
      "Kennen"
    ],
    "player_id": 4341,
    "games_played": 5,
    "total_gold": 67937,
    "first_name": "Seo",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SBE-Soul-2015lck.jpg",
    "ign": "Soul",
    "kda": 2.75,
    "gpm": 311.04311331553,
    "role": "Top Lane",
    "most_played_champions": [
      68,
      85
    ],
    "bio": ""
  },
  "4342": {
    "last_name": "",
    "team_name": "SBENU SONICBOOM",
    "most_played_champion_names": [
      "Gragas",
      "Sejuani"
    ],
    "player_id": 4342,
    "games_played": 5,
    "total_gold": 58284,
    "first_name": "Yoon",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SBE-Catch-2015lck.jpg",
    "ign": "Catch",
    "kda": 2.9333333333333,
    "gpm": 266.84776802747,
    "role": "Jungler",
    "most_played_champions": [
      79,
      113
    ],
    "bio": ""
  },
  "1015": {
    "last_name": "",
    "team_name": "CJ ENTUS",
    "most_played_champion_names": [
      "Nidalee",
      "LeBlanc",
      "Kassadin"
    ],
    "player_id": 1015,
    "games_played": 6,
    "total_gold": 84071,
    "first_name": "Jinyoung",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/CJ-Coco-2015lck.png",
    "ign": "CoCo",
    "kda": 10.444444444444,
    "gpm": 392.76337304368,
    "role": "Mid Lane",
    "most_played_champions": [
      76,
      7,
      38
    ],
    "bio": ""
  },
  "1016": {
    "last_name": "",
    "team_name": "KT Rolster",
    "most_played_champion_names": [
      
    ],
    "player_id": 1016,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Donghyun",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KT-Arrow-2015lck.jpg",
    "ign": "Arrow",
    "kda": 0,
    "gpm": 0,
    "role": "AD Carry",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "1017": {
    "last_name": "",
    "team_name": "KT Rolster",
    "most_played_champion_names": [
      
    ],
    "player_id": 1017,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Jong Beom",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KT-Piccaboo-2015lck.png",
    "ign": "Piccaboo",
    "kda": 0,
    "gpm": 0,
    "role": "Support",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "4346": {
    "last_name": "",
    "team_name": "SBENU SONICBOOM",
    "most_played_champion_names": [
      "Lucian",
      "Sivir",
      "Corki"
    ],
    "player_id": 4346,
    "games_played": 5,
    "total_gold": 84992,
    "first_name": "Shin",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SBE-Nuclear-2015lck.jpg",
    "ign": "Nuclear",
    "kda": 6.2857142857143,
    "gpm": 389.12781381152,
    "role": "AD Carry",
    "most_played_champions": [
      236,
      15,
      42
    ],
    "bio": ""
  },
  "2811": {
    "last_name": "",
    "team_name": "Najin e-mFire",
    "most_played_champion_names": [
      
    ],
    "player_id": 2811,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Hosung",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/NJE-Duke-2015lck.jpg",
    "ign": "Duke",
    "kda": 0,
    "gpm": 0,
    "role": "Top Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  },
  "892": {
    "last_name": "",
    "team_name": "Najin e-mFire",
    "most_played_champion_names": [
      "Nidalee",
      "LeBlanc",
      "Gragas"
    ],
    "player_id": 892,
    "games_played": 7,
    "total_gold": 117450,
    "first_name": "Byeong-jun",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/NJE-Ggoong-2015lck.jpg",
    "ign": "Ggoong",
    "kda": 8.3,
    "gpm": 368.66335338739,
    "role": "Mid Lane",
    "most_played_champions": [
      76,
      7,
      79
    ],
    "bio": ""
  },
  "894": {
    "last_name": "",
    "team_name": "KOO Tigers",
    "most_played_champion_names": [
      "Janna",
      "Nami",
      "Thresh"
    ],
    "player_id": 894,
    "games_played": 31,
    "total_gold": 291213,
    "first_name": "Beom-hyeon",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/KOO-gorilla-2015lck.jpg",
    "ign": "Gorilla",
    "kda": 4.5769230769231,
    "gpm": 240.52281643609,
    "role": "Support",
    "most_played_champions": [
      40,
      267,
      412
    ],
    "bio": "GorillA is Najin White Shield\u2019s support. Focusing mainly on ranged supports like Nami, Zyra, and Sona, GorillA looks to control the fights with precision and positioning at the forefront of his gameplay. His Thresh is known as one of the best in the world, and opposing teams should beware putting the champion in his hands. His Janna is also highly esteemed, and fans should look forward to an absolute treat if Thresh is banned and Janna falls into his hands."
  },
  "4343": {
    "last_name": "",
    "team_name": "SBENU SONICBOOM",
    "most_played_champion_names": [
      
    ],
    "player_id": 4343,
    "games_played": 0,
    "total_gold": 0,
    "first_name": "Lee",
    "image": "http:\/\/riot-web-cdn.s3-us-west-1.amazonaws.com\/lolesports\/s3fs-public\/SBE-do-it-2015lck.jpg",
    "ign": "do it",
    "kda": 0,
    "gpm": 0,
    "role": "Mid Lane",
    "most_played_champions": [
      
    ],
    "bio": ""
  }
}
        for story in expected_response:
            self.assertTrue(story in response_data)

    def test_get_player(self) :
        self.maxDiff = None
        expected_response = {"games_played": 6, "player_id": 2178, "ign": "Ohq", "team_name": "Najin e-mFire", "last_name": "", "most_played_champions": [15, 67, 236], "image": "http://riot-web-cdn.s3-us-west-1.amazonaws.com/lolesports/s3fs-public/NJE-Ohq-2015lck.jpg", "total_gold": 72298, "bio": "Ohq is the AD Carry for Xenics Storm. As an important member of this new squad, Ohq\u2019s performance will be crucial to their debut in the OGN Champions Spring. ", "first_name": "Gyumin", "role": "AD Carry", "kda": 3.4545454545455, "gpm": 339.05580740972}
        request = Request(self.url+"api/players/2178/")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        self.assertEqual(expected_response, response_data)
        response_body = response.read()

# -----
# Item
# -----

    def test_get_all_items(self) :
        request = Request(self.url+"api/items/")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)
        #response_objects = response_data["objects"]
        expected_response = {
  "3072": {
    "sell_gold": 2450,
    "into_items": [
      
    ],
    "total_gold": 3500,
    "item_id": 3072,
    "from_items": [
      1038,
      1053
    ],
    "name": "The Bloodthirster",
    "base_gold": 1150,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3072.png",
    "description": "+80 Attack Damage\n\nUNIQUE Passive: +20% Life Steal\nUNIQUE Passive: Your basic attacks can now overheal you. Excess life is stored as a shield that can block 50-350 damage, based on champion level.\n\nThis shield decays slowly if you haven't dealt or taken damage in the last 25 seconds."
  },
  "3073": {
    "sell_gold": 504,
    "into_items": [
      3007,
      3008
    ],
    "total_gold": 720,
    "item_id": 3073,
    "from_items": [
      1004,
      1027
    ],
    "name": "Tear of the Goddess (Crystal Scar)",
    "base_gold": 140,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3073.png",
    "description": "+250 Mana\n+25% Base Mana Regen \n\nUNIQUE Passive - Mana Charge: +5 maximum Mana on spell cast or Mana expenditure (up to 2 times per 6 seconds); \n+1 maximum Mana per 6 seconds;\nMax +750 Mana.\n\n(Unique Passives with the same name don't stack.)"
  },
  "1026": {
    "sell_gold": 602,
    "into_items": [
      3001,
      3135,
      3027,
      3029,
      3089,
      3116,
      3124,
      3188,
      3090,
      3003,
      3007
    ],
    "total_gold": 860,
    "item_id": 1026,
    "from_items": [
      
    ],
    "name": "Blasting Wand",
    "base_gold": 860,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1026.png",
    "description": "+40 Ability Power"
  },
  "3075": {
    "sell_gold": 1470,
    "into_items": [
      
    ],
    "total_gold": 2100,
    "item_id": 3075,
    "from_items": [
      1031,
      1029
    ],
    "name": "Thornmail",
    "base_gold": 1050,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3075.png",
    "description": "+100 Armor  \n\nUNIQUE Passive: Upon being hit by a basic attack, returns 30% of the incoming damage (before being reduced by defenses) to the attacker as magic damage."
  },
  "1028": {
    "sell_gold": 280,
    "into_items": [
      2051,
      2049,
      3067,
      3044,
      3211,
      3010,
      3105,
      3801,
      3136,
      2045,
      3185,
      3102,
      3071,
      3083,
      3084,
      3022,
      3056,
      1011,
      3709,
      3717,
      3721,
      3725
    ],
    "total_gold": 400,
    "item_id": 1028,
    "from_items": [
      
    ],
    "name": "Ruby Crystal",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1028.png",
    "description": "+150 Health"
  },
  "2053": {
    "sell_gold": 700,
    "into_items": [
      3056,
      3512
    ],
    "total_gold": 1000,
    "item_id": 2053,
    "from_items": [
      1006,
      1029
    ],
    "name": "Raptor Cloak",
    "base_gold": 520,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2053.png",
    "description": "+30 Armor\n+100% Base Health Regen \n\nUNIQUE Passive - Point Runner: Builds up to +30% Movement Speed over 2 seconds while near turrets."
  },
  "3078": {
    "sell_gold": 2592,
    "into_items": [
      
    ],
    "total_gold": 3703,
    "item_id": 3078,
    "from_items": [
      3044,
      3086,
      3057
    ],
    "name": "Trinity Force",
    "base_gold": 78,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3078.png",
    "description": "+30 Attack Damage\n+30 Ability Power\n+30% Attack Speed\n+10% Critical Strike Chance\n+8% Movement Speed\n+250 Health\n+200 Mana\n\nUNIQUE Passive - Rage: Basic attacks grant 20 Movement Speed for 2 seconds. Kills grant 60 Movement Speed instead. This Movement Speed bonus is halved for ranged champions.\nUNIQUE Passive - Spellblade: After using an ability, the next basic attack deals bonus physical damage equal to 200% of base Attack Damage on hit (1.5 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "1031": {
    "sell_gold": 525,
    "into_items": [
      3068,
      3026,
      3075
    ],
    "total_gold": 750,
    "item_id": 1031,
    "from_items": [
      1029
    ],
    "name": "Chain Vest",
    "base_gold": 450,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1031.png",
    "description": "+40 Armor"
  },
  "1033": {
    "sell_gold": 350,
    "into_items": [
      3111,
      3211,
      1057,
      3028,
      3112,
      3140,
      3155,
      3105,
      3091,
      3170,
      3180
    ],
    "total_gold": 500,
    "item_id": 1033,
    "from_items": [
      
    ],
    "name": "Null-Magic Mantle",
    "base_gold": 500,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1033.png",
    "description": "+25 Magic Resist"
  },
  "3082": {
    "sell_gold": 735,
    "into_items": [
      3110,
      3143
    ],
    "total_gold": 1050,
    "item_id": 3082,
    "from_items": [
      1029
    ],
    "name": "Warden's Mail",
    "base_gold": 450,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3082.png",
    "description": "+45 Armor\n\nUNIQUE Passive - Cold Steel: When hit by basic attacks, reduces the attacker's Attack Speed by 15% for 1 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3083": {
    "sell_gold": 1750,
    "into_items": [
      
    ],
    "total_gold": 2500,
    "item_id": 3083,
    "from_items": [
      3801,
      1028,
      1011
    ],
    "name": "Warmog's Armor",
    "base_gold": 300,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3083.png",
    "description": "+800 Health\n\nUNIQUE Passive: Restores 1% of maximum Health every 5 seconds. Health restore increases to 3% of maximum Health if damage hasn't been taken within 8 seconds."
  },
  "3084": {
    "sell_gold": 1719,
    "into_items": [
      
    ],
    "total_gold": 2455,
    "item_id": 3084,
    "from_items": [
      1028,
      1011
    ],
    "name": "Overlord's Bloodmail",
    "base_gold": 1055,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3084.png",
    "description": "+850 Health\n\nUNIQUE Passive: Upon champion kill or assist, restores 300 Health over 5 seconds."
  },
  "3085": {
    "sell_gold": 1680,
    "into_items": [
      
    ],
    "total_gold": 2400,
    "item_id": 3085,
    "from_items": [
      1043,
      1042
    ],
    "name": "Runaan's Hurricane (Ranged Only)",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3085.png",
    "description": "+70% Attack Speed\n\nUNIQUE Passive: When basic attacking, bolts are fired at up to 2 enemies near the target, each dealing 10 (+50% of Attack Damage) physical damage. These bolts apply on-hit effects."
  },
  "3086": {
    "sell_gold": 770,
    "into_items": [
      3046,
      3078,
      3087
    ],
    "total_gold": 1100,
    "item_id": 3086,
    "from_items": [
      1051,
      1042
    ],
    "name": "Zeal",
    "base_gold": 250,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3086.png",
    "description": "+20% Attack Speed\n+10% Critical Strike Chance\n+5% Movement Speed"
  },
  "3599": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3599,
    "from_items": [
      
    ],
    "name": "The Black Spear",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3599.png",
    "description": "\nActive: Offer to bind with an ally for the remainder of the game, becoming Oathsworn Allies. Oathsworn empowers you both while near one another."
  },
  "3089": {
    "sell_gold": 2310,
    "into_items": [
      
    ],
    "total_gold": 3300,
    "item_id": 3089,
    "from_items": [
      1026,
      1058
    ],
    "name": "Rabadon's Deathcap",
    "base_gold": 840,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3089.png",
    "description": "+120 Ability Power  \n\nUNIQUE Passive: Increases Ability Power by 30%."
  },
  "1042": {
    "sell_gold": 315,
    "into_items": [
      3006,
      3106,
      3086,
      3101,
      3153,
      3046,
      3154,
      3091,
      3085,
      3159,
      3710,
      3718,
      3722,
      3726
    ],
    "total_gold": 450,
    "item_id": 1042,
    "from_items": [
      
    ],
    "name": "Dagger",
    "base_gold": 450,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1042.png",
    "description": "+15% Attack Speed"
  },
  "2051": {
    "sell_gold": 711,
    "into_items": [
      
    ],
    "total_gold": 1015,
    "item_id": 2051,
    "from_items": [
      1006,
      1028
    ],
    "name": "Guardian's Horn",
    "base_gold": 435,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2051.png",
    "description": "+200 Health\n+125% Base Health Regeneration \n\nUNIQUE Passive: Enemy spellcasts reduce the cooldown of Battle Cry by 1 second.\nUNIQUE Active - Battle Cry: Gain 30% Movement Speed, 20 Armor, and 20 Magic Resist for 3 seconds. 25 second cooldown."
  },
  "3092": {
    "sell_gold": 880,
    "into_items": [
      
    ],
    "total_gold": 2200,
    "item_id": 3092,
    "from_items": [
      3108,
      3098
    ],
    "name": "Frost Queen's Claim",
    "base_gold": 515,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3092.png",
    "description": "+50 Ability Power\n+10% Cooldown Reduction\n+2 Gold per 10 seconds\n+50% Base Mana Regen \n\nUNIQUE Passive - Tribute: Spells and basic attacks against champions or buildings deal 15 additional damage and grant 10 Gold. This can occur up to three times every 30 seconds.\nUNIQUE Active: Fires an ice lance that explodes dealing 50 (+5 per champion level) magic damage to nearby enemies and slowing their Movement Speed by 80%, decaying over 2 seconds (60 second cooldown).\n\nLimited to 1 Gold Income item"
  },
  "3093": {
    "sell_gold": 320,
    "into_items": [
      3087,
      3142
    ],
    "total_gold": 800,
    "item_id": 3093,
    "from_items": [
      1051
    ],
    "name": "Avarice Blade",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3093.png",
    "description": "+10% Critical Strike Chance\n\nUNIQUE Passive - Avarice: +3 Gold per 10 seconds\nUNIQUE Passive - Greed: Grants 2 Gold upon killing a unit.\n\nMay be bought with another Gold Income item"
  },
  "3096": {
    "sell_gold": 346,
    "into_items": [
      3069
    ],
    "total_gold": 865,
    "item_id": 3096,
    "from_items": [
      3301
    ],
    "name": "Nomad's Medallion",
    "base_gold": 500,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3096.png",
    "description": "+25% Base Health Regen \n+25% Base Mana Regen \n+10 Movement Speed\n+2 Gold per 10 seconds\n\nUNIQUE Passive - Favor: Being near a minion death without dealing the killing blow grants 3 Gold and 5 Health.\n\nLimited to 1 Gold Income item\n\n''The medallion shines with the glory of a thousand voices when exposed to the sun.'' - Historian Shurelya, 22 June, 24 CLE\n\n"
  },
  "3097": {
    "sell_gold": 346,
    "into_items": [
      3401
    ],
    "total_gold": 865,
    "item_id": 3097,
    "from_items": [
      3302
    ],
    "name": "Targon's Brace",
    "base_gold": 500,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3097.png",
    "description": "+175 Health\n+50% Base Health Regen \n\nUNIQUE Passive - Spoils of War: Melee basic attacks execute minions below 240 Health. Killing a minion heals the owner and the nearest allied champion for 50 Health and grants them kill Gold.\n\nThese effects require a nearby allied champion. Recharges every 30 seconds. Max 3 charges.\n\nLimited to 1 Gold Income item"
  },
  "3098": {
    "sell_gold": 346,
    "into_items": [
      3092
    ],
    "total_gold": 865,
    "item_id": 3098,
    "from_items": [
      3303
    ],
    "name": "Frostfang",
    "base_gold": 500,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3098.png",
    "description": "+10 Ability Power\n+2 Gold per 10 seconds\n+50% Base Mana Regen \n\nUNIQUE Passive - Tribute: Spells and basic attacks against champions or buildings deal 15 additional damage and grant 10 Gold. This can occur up to 3 times every 30 seconds. Killing a minion disables this passive for 12 seconds.\n\nLimited to 1 Gold Income item"
  },
  "1051": {
    "sell_gold": 280,
    "into_items": [
      3086,
      3093,
      3122
    ],
    "total_gold": 400,
    "item_id": 1051,
    "from_items": [
      
    ],
    "name": "Brawler's Gloves",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1051.png",
    "description": "+8% Critical Strike Chance"
  },
  "1052": {
    "sell_gold": 305,
    "into_items": [
      3108,
      3191,
      3057,
      3136,
      3135,
      3145,
      3113,
      3090,
      3116,
      3151,
      3041
    ],
    "total_gold": 435,
    "item_id": 1052,
    "from_items": [
      
    ],
    "name": "Amplifying Tome",
    "base_gold": 435,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1052.png",
    "description": "+20 Ability Power"
  },
  "3101": {
    "sell_gold": 875,
    "into_items": [
      3115,
      3172,
      3137
    ],
    "total_gold": 1250,
    "item_id": 3101,
    "from_items": [
      1042
    ],
    "name": "Stinger",
    "base_gold": 350,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3101.png",
    "description": "+40% Attack Speed\n\nUNIQUE Passive: +10% Cooldown Reduction"
  },
  "3102": {
    "sell_gold": 1925,
    "into_items": [
      
    ],
    "total_gold": 2750,
    "item_id": 3102,
    "from_items": [
      1028,
      3211
    ],
    "name": "Banshee's Veil",
    "base_gold": 1150,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3102.png",
    "description": "+450 Health\n+55 Magic Resist\n+100% Base Health Regeneration \n\nUNIQUE Passive: Grants a spell shield that blocks the next enemy ability. This shield refreshes after no damage is taken from enemy champions for 40 seconds."
  },
  "1055": {
    "sell_gold": 176,
    "into_items": [
      
    ],
    "total_gold": 440,
    "item_id": 1055,
    "from_items": [
      
    ],
    "name": "Doran's Blade",
    "base_gold": 440,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1055.png",
    "description": "+70 Health\n+7 Attack Damage\n+3% Life Steal"
  },
  "3104": {
    "sell_gold": 2660,
    "into_items": [
      
    ],
    "total_gold": 3800,
    "item_id": 3104,
    "from_items": [
      1018,
      3122,
      1037
    ],
    "name": "Lord Van Damm's Pillager",
    "base_gold": 995,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3104.png",
    "description": "+80 Attack Damage\n+25% Critical Strike Chance\n\nUNIQUE Passive: Critical Strikes deal 250% damage instead of 200%."
  },
  "1057": {
    "sell_gold": 595,
    "into_items": [
      3001,
      3026,
      3512
    ],
    "total_gold": 850,
    "item_id": 1057,
    "from_items": [
      1033
    ],
    "name": "Negatron Cloak",
    "base_gold": 350,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1057.png",
    "description": "+45 Magic Resist"
  },
  "1058": {
    "sell_gold": 1120,
    "into_items": [
      3089,
      3157
    ],
    "total_gold": 1600,
    "item_id": 1058,
    "from_items": [
      
    ],
    "name": "Needlessly Large Rod",
    "base_gold": 1600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1058.png",
    "description": "+80 Ability Power"
  },
  "2139": {
    "sell_gold": 160,
    "into_items": [
      
    ],
    "total_gold": 400,
    "item_id": 2139,
    "from_items": [
      
    ],
    "name": "Elixir of Sorcery",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2139.png",
    "description": "Level 9 required to purchase.\n\nClick to Consume: Grants +40 Ability Power, 15 bonus Mana Regen per 5 seconds and Sorcery for 3 minutes. \n\nSorcery: Damaging a champion or turret deals 25 bonus True Damage. This effect has a 5 second cooldown versus champions but no cooldown versus turrets.\n\n(Only one Flask effect may be active at a time.)\n"
  },
  "3108": {
    "sell_gold": 574,
    "into_items": [
      3174,
      3092,
      3115,
      3188,
      3290,
      3165,
      3152,
      3060,
      3023,
      3708,
      3716,
      3720,
      3724
    ],
    "total_gold": 820,
    "item_id": 3108,
    "from_items": [
      1052
    ],
    "name": "Fiendish Codex",
    "base_gold": 385,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3108.png",
    "description": "+30 Ability Power\n\nUNIQUE Passive: +10% Cooldown Reduction"
  },
  "2054": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 2054,
    "from_items": [
      
    ],
    "name": "Diet Poro-Snax",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2054.png",
    "description": "All the flavor of regular Poro-Snax, without the calories! Keeps your Poro happy AND healthy.\n\nClick to Consume: Gives your Poros a delicious healthy treat."
  },
  "3110": {
    "sell_gold": 1715,
    "into_items": [
      
    ],
    "total_gold": 2450,
    "item_id": 3110,
    "from_items": [
      3082,
      3024
    ],
    "name": "Frozen Heart",
    "base_gold": 450,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3110.png",
    "description": "+100 Armor\n+20% Cooldown Reduction\n+400 Mana\n\nUNIQUE Aura: Reduces the Attack Speed of nearby enemies by 15%."
  },
  "1063": {
    "sell_gold": 380,
    "into_items": [
      
    ],
    "total_gold": 950,
    "item_id": 1063,
    "from_items": [
      
    ],
    "name": "Prospector's Ring",
    "base_gold": 950,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1063.png",
    "description": "+35 Ability Power\n\nPassive : +6 Mana Regen per 5 seconds\nUNIQUE Passive - Prospector: +150 Health\n\n(Unique Passives with the same name don't stack.)"
  },
  "3112": {
    "sell_gold": 1547,
    "into_items": [
      
    ],
    "total_gold": 2210,
    "item_id": 3112,
    "from_items": [
      1006,
      1033
    ],
    "name": "Orb of Winter",
    "base_gold": 850,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3112.png",
    "description": "+70 Magic Resist\n+100% Base Health Regeneration \n\nUNIQUE Passive: Grants a shield that absorbs up to 30 (+10 per level) damage. The shield will refresh after 9 seconds without receiving damage."
  },
  "3113": {
    "sell_gold": 595,
    "into_items": [
      3023,
      3290,
      3100,
      3504
    ],
    "total_gold": 850,
    "item_id": 3113,
    "from_items": [
      1052
    ],
    "name": "Aether Wisp",
    "base_gold": 415,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3113.png",
    "description": "+30 Ability Power\n\nUNIQUE Passive: +5% Movement Speed"
  },
  "3114": {
    "sell_gold": 420,
    "into_items": [
      3069,
      3165,
      3222,
      3504
    ],
    "total_gold": 600,
    "item_id": 3114,
    "from_items": [
      1004
    ],
    "name": "Forbidden Idol",
    "base_gold": 240,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3114.png",
    "description": "+50% Base Mana Regen \n\nUNIQUE Passive: +10% Cooldown Reduction"
  },
  "3115": {
    "sell_gold": 2044,
    "into_items": [
      
    ],
    "total_gold": 2920,
    "item_id": 3115,
    "from_items": [
      3108,
      3101
    ],
    "name": "Nashor's Tooth",
    "base_gold": 850,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3115.png",
    "description": "+50% Attack Speed\n+60 Ability Power\n\nUNIQUE Passive: +20% Cooldown Reduction\nUNIQUE Passive: Basic attacks deal 15 (+15% of Ability Power) bonus magic damage on hit.\n"
  },
  "3116": {
    "sell_gold": 2030,
    "into_items": [
      
    ],
    "total_gold": 2900,
    "item_id": 3116,
    "from_items": [
      1011,
      1026,
      1052
    ],
    "name": "Rylai's Crystal Scepter",
    "base_gold": 605,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3116.png",
    "description": "+400 Health\n+100 Ability Power\n\nUNIQUE Passive: Dealing spell damage slows the target's Movement Speed by 35% for 1.5 seconds (15% for multi-target and damage-over-time spells)."
  },
  "3117": {
    "sell_gold": 560,
    "into_items": [
      3274,
      3273,
      3272,
      3271,
      3270
    ],
    "total_gold": 800,
    "item_id": 3117,
    "from_items": [
      1001
    ],
    "name": "Boots of Mobility",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3117.png",
    "description": "UNIQUE Passive - Enhanced Movement: +25 Movement Speed. Increases to +105 Movement Speed when out of combat for 5 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "1074": {
    "sell_gold": 176,
    "into_items": [
      
    ],
    "total_gold": 440,
    "item_id": 1074,
    "from_items": [
      
    ],
    "name": "Doran's Shield (Showdown)",
    "base_gold": 440,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1074.png",
    "description": "+100 Health\n+10 Health Regen per 5 seconds\n\nUNIQUE Passive: Blocks 8 damage from champion basic attacks.\n\nLimited to 2 Doran's items on Showdown\n\n"
  },
  "1075": {
    "sell_gold": 176,
    "into_items": [
      
    ],
    "total_gold": 440,
    "item_id": 1075,
    "from_items": [
      
    ],
    "name": "Doran's Blade (Showdown)",
    "base_gold": 440,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1075.png",
    "description": "+70 Health\n+7 Attack Damage\n+3% Life Steal\n\nLimited to 2 Doran's items on Showdown\n\n"
  },
  "3124": {
    "sell_gold": 1820,
    "into_items": [
      
    ],
    "total_gold": 2600,
    "item_id": 3124,
    "from_items": [
      1037,
      1026
    ],
    "name": "Guinsoo's Rageblade",
    "base_gold": 865,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3124.png",
    "description": "+30 Attack Damage\n+40 Ability Power\n\nPassive: Basic attacks (on attack) and spell casts grant +4% Attack Speed and +4 Ability Power for 8 seconds (stacks up to 8 times).\nUNIQUE Passive: Falling below 50% Health grants +20% Attack Speed, +10% Life Steal, and +10% Spell Vamp until out of combat (30 second cooldown)."
  },
  "3252": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3252,
    "from_items": [
      3006
    ],
    "name": "Enchantment: Furor",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3252.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Furor bonus.\n\nUNIQUE Passive - Furor: Upon dealing damage with a single target spell or attack (on hit), grants +12% Movement Speed that decays over 2 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3134": {
    "sell_gold": 936,
    "into_items": [
      3142,
      3071,
      3707,
      3714,
      3719,
      3723
    ],
    "total_gold": 1337,
    "item_id": 3134,
    "from_items": [
      1036
    ],
    "name": "The Brutalizer",
    "base_gold": 617,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3134.png",
    "description": "+25 Attack Damage\n\nUNIQUE Passive: +10% Cooldown Reduction\nUNIQUE Passive: +10 Armor Penetration\n\n(Armor Penetration: Physical damage is increased by ignoring an amount of the target's Armor equal to Armor Penetration.)"
  },
  "3135": {
    "sell_gold": 1607,
    "into_items": [
      
    ],
    "total_gold": 2295,
    "item_id": 3135,
    "from_items": [
      1026,
      1052
    ],
    "name": "Void Staff",
    "base_gold": 1000,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3135.png",
    "description": "+70 Ability Power\n\nUNIQUE Passive: Magic damage ignores 35% of the target's Magic Resist (applies before Magic Penetration)."
  },
  "3136": {
    "sell_gold": 1040,
    "into_items": [
      3151
    ],
    "total_gold": 1485,
    "item_id": 3136,
    "from_items": [
      1028,
      1052
    ],
    "name": "Haunting Guise",
    "base_gold": 650,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3136.png",
    "description": "+25 Ability Power\n+200 Health\n\nUNIQUE Passive - Eyes of Pain: +15 Magic Penetration\n\n(Magic Penetration: Magic damage is increased by ignoring an amount of the target's Magic Resist equal to Magic Penetration.)\n\n(Unique Passives with the same name do not stack.)"
  },
  "3137": {
    "sell_gold": 1890,
    "into_items": [
      
    ],
    "total_gold": 2700,
    "item_id": 3137,
    "from_items": [
      3140,
      3101
    ],
    "name": "Dervish Blade",
    "base_gold": 200,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3137.png",
    "description": "+50% Attack Speed\n+45 Magic Resist\n+10% Cooldown Reduction\n\nUNIQUE Active - Quicksilver: Removes all debuffs, and if champion is melee, also grants +50% bonus Movement Speed for 1 second (90 second cooldown)."
  },
  "3139": {
    "sell_gold": 2590,
    "into_items": [
      
    ],
    "total_gold": 3700,
    "item_id": 3139,
    "from_items": [
      3140,
      1038
    ],
    "name": "Mercurial Scimitar",
    "base_gold": 900,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3139.png",
    "description": "+80 Attack Damage\n+35 Magic Resist\n\nUNIQUE Active - Quicksilver: Removes all debuffs and also grants +50% bonus Movement Speed for 1 second (90 second cooldown)."
  },
  "3140": {
    "sell_gold": 875,
    "into_items": [
      3139,
      3137
    ],
    "total_gold": 1250,
    "item_id": 3140,
    "from_items": [
      1033
    ],
    "name": "Quicksilver Sash",
    "base_gold": 750,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3140.png",
    "description": "+30 Magic Resist\n\nUNIQUE Active - Quicksilver: Removes all debuffs (90 second cooldown)."
  },
  "3141": {
    "sell_gold": 980,
    "into_items": [
      
    ],
    "total_gold": 1400,
    "item_id": 3141,
    "from_items": [
      1036
    ],
    "name": "Sword of the Occult",
    "base_gold": 1040,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3141.png",
    "description": "+10 Attack Damage \n\nUNIQUE Passive: Grants +5 Attack Damage per stack and 5 stacks upon first purchase. Grants 2 stacks for a kill or 1 stack for an assist (max 20 stacks). Half of the stacks are lost upon death. At 20 stacks, grants +20% bonus Attack Speed."
  },
  "3142": {
    "sell_gold": 1890,
    "into_items": [
      
    ],
    "total_gold": 2700,
    "item_id": 3142,
    "from_items": [
      3134,
      3093
    ],
    "name": "Youmuu's Ghostblade",
    "base_gold": 563,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3142.png",
    "description": "+30 Attack Damage\n+15% Critical Strike Chance\n+10% Cooldown Reduction\n\nUNIQUE Passive: +20 Armor Penetration\nUNIQUE Active: Grants +20% Movement Speed and +40% Attack Speed for 6 seconds (45 second cooldown).\n\n(Armor Penetration: Physical damage is increased by ignoring an amount of the target's Armor equal to Armor Penetration.)"
  },
  "3143": {
    "sell_gold": 1995,
    "into_items": [
      
    ],
    "total_gold": 2850,
    "item_id": 3143,
    "from_items": [
      3082,
      1011
    ],
    "name": "Randuin's Omen",
    "base_gold": 800,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3143.png",
    "description": "+500 Health\n+70 Armor\n\nUNIQUE Passive - Cold Steel: When hit by basic attacks, reduces the attacker's Attack Speed by 15%.\nUNIQUE Active: Slows the Movement Speed of nearby enemy units by 35% for 2 seconds (+1 second per 200 Armor and +1 second per 200 Magic Resist) (60 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "3144": {
    "sell_gold": 980,
    "into_items": [
      3146,
      3153
    ],
    "total_gold": 1400,
    "item_id": 3144,
    "from_items": [
      1036,
      1053
    ],
    "name": "Bilgewater Cutlass",
    "base_gold": 240,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3144.png",
    "description": "+25 Attack Damage\n+8% Life Steal\n\nUNIQUE Active: Deals 100 magic damage and slows the target champion's Movement Speed by 25% for 2 seconds (90 second cooldown)."
  },
  "3145": {
    "sell_gold": 840,
    "into_items": [
      3146,
      3152
    ],
    "total_gold": 1200,
    "item_id": 3145,
    "from_items": [
      1052
    ],
    "name": "Hextech Revolver",
    "base_gold": 330,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3145.png",
    "description": "+40 Ability Power\n\nUNIQUE Passive: +12% Spell Vamp\n\n(Spell Vamp: Abilities heal for a percentage of the damage they deal. Area of Effect spells only grant one-third of the healing from Spell Vamp.)"
  },
  "3146": {
    "sell_gold": 2380,
    "into_items": [
      
    ],
    "total_gold": 3400,
    "item_id": 3146,
    "from_items": [
      3144,
      3145
    ],
    "name": "Hextech Gunblade",
    "base_gold": 800,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3146.png",
    "description": "+40 Attack Damage\n+80 Ability Power\n+10% Life Steal\n\nUNIQUE Passive: +20% Spell Vamp\nUNIQUE Passive: Basic attacks (on hit) and single-target spells against champions reduce the cooldown of this item by 3 seconds.\nUNIQUE Active: Deals 150 (+40% of Ability Power) magic damage and slows the target champion's Movement Speed by 40% for 2 seconds (60 second cooldown).\n\n(Spell Vamp: Abilities heal for a percentage of the damage they deal. Area of Effect spells only grant one-third of the healing from Spell Vamp.)"
  },
  "3151": {
    "sell_gold": 2030,
    "into_items": [
      
    ],
    "total_gold": 2900,
    "item_id": 3151,
    "from_items": [
      3136,
      1052
    ],
    "name": "Liandry's Torment",
    "base_gold": 980,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3151.png",
    "description": "+50 Ability Power\n+300 Health\n\nUNIQUE Passive - Eyes of Pain: +15 Magic Penetration\nUNIQUE Passive: Dealing spell damage applies a damage-over-time effect for 3 seconds that deals bonus magic damage equal to 2% of the target's current Health per second. This bonus damage is doubled against movement-impaired units and capped at 100 damage per second vs. monsters.\n\n(A unit is movement-impaired if it is slowed, stunned, taunted, feared, or immobilized.)\n\n(Magic Penetration: Magic damage is increased by ignoring an amount of the target's Magic Resist equal to Magic Penetration.)\n\n(Unique Passives with the same name don't stack.)"
  },
  "3152": {
    "sell_gold": 1750,
    "into_items": [
      
    ],
    "total_gold": 2500,
    "item_id": 3152,
    "from_items": [
      3108,
      3145
    ],
    "name": "Will of the Ancients",
    "base_gold": 480,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3152.png",
    "description": "+80 Ability Power\n+10% Cooldown Reduction\n\nUNIQUE Passive: +20% Spell Vamp\n\n(Spell Vamp: Abilities heal for a percentage of the damage they deal. Area of Effect spells only grant one-third of the healing from Spell Vamp.)"
  },
  "3153": {
    "sell_gold": 2240,
    "into_items": [
      
    ],
    "total_gold": 3200,
    "item_id": 3153,
    "from_items": [
      3144,
      1042
    ],
    "name": "Blade of the Ruined King",
    "base_gold": 900,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3153.png",
    "description": "+25 Attack Damage\n+40% Attack Speed\n+10% Life Steal\n\nUNIQUE Passive: Basic attacks deal 8% of the target's current Health in bonus physical damage (max 60 vs. monsters and minions) on hit.\nUNIQUE Active: Deals 10% of target champion's maximum Health (min. 100) as physical damage, heals for the same amount, and steals 25% of the target's Movement Speed for 3 seconds (90 second cooldown)."
  },
  "3154": {
    "sell_gold": 710,
    "into_items": [
      
    ],
    "total_gold": 1775,
    "item_id": 3154,
    "from_items": [
      1036,
      3106,
      1042
    ],
    "name": "Wriggle's Lantern",
    "base_gold": 215,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3154.png",
    "description": "+12 Attack Damage\n+30% Attack Speed\n\nUNIQUE Passive - Maim: Basic attacks against monsters deal 75 bonus magic damage and heal 10 Health on hit.\nUNIQUE Passive: Gain 30% increased Gold from monsters.\nUNIQUE Active: Places a Stealth Ward that reveals the surrounding area for 180 seconds (180 second cooldown).\n\nTransforms into Feral Flare at 30 kills, assists and large monster kills.\n(Champions and monsters killed with Hunter's Machete and Madred's Razors count toward this transformation)\n\nLimited to 1 Gold Income item"
  },
  "3155": {
    "sell_gold": 1015,
    "into_items": [
      3156
    ],
    "total_gold": 1450,
    "item_id": 3155,
    "from_items": [
      1036,
      1033
    ],
    "name": "Hexdrinker",
    "base_gold": 590,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3155.png",
    "description": "+25 Attack Damage\n+30 Magic Resist\n\nUNIQUE Passive - Lifeline: Upon taking magic damage that would reduce Health below 30%, grants a shield that absorbs 250 magic damage for 5 seconds (90 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "3156": {
    "sell_gold": 2240,
    "into_items": [
      
    ],
    "total_gold": 3200,
    "item_id": 3156,
    "from_items": [
      1037,
      3155
    ],
    "name": "Maw of Malmortius",
    "base_gold": 875,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3156.png",
    "description": "+60 Attack Damage\n+40 Magic Resist\n\nUNIQUE Passive: Grants +1 Attack Damage for every 2% of missing Health, up to a maximum of 35 Attack Damage.\nUNIQUE Passive - Lifeline: Upon taking magic damage that would reduce Health below 30%, grants a shield that absorbs 400 magic damage for 5 seconds (90 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "1038": {
    "sell_gold": 1085,
    "into_items": [
      3031,
      3072,
      3139,
      3508
    ],
    "total_gold": 1550,
    "item_id": 1038,
    "from_items": [
      
    ],
    "name": "B. F. Sword",
    "base_gold": 1550,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1038.png",
    "description": "+50 Attack Damage"
  },
  "3158": {
    "sell_gold": 700,
    "into_items": [
      3279,
      3278,
      3277,
      3276,
      3275
    ],
    "total_gold": 1000,
    "item_id": 3158,
    "from_items": [
      1001
    ],
    "name": "Ionian Boots of Lucidity",
    "base_gold": 675,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3158.png",
    "description": "UNIQUE Passive: +15% Cooldown Reduction\nUNIQUE Passive - Enhanced Movement: +45 Movement Speed\n\n(Unique Passives with the same name don't stack.)\n\n''This item is dedicated in honor of Ionia's victory over Noxus in the Rematch for the Southern Provinces on 10 December, 20 CLE.''"
  },
  "3159": {
    "sell_gold": 696,
    "into_items": [
      
    ],
    "total_gold": 1740,
    "item_id": 3159,
    "from_items": [
      1036,
      1029,
      3106,
      1042
    ],
    "name": "Grez's Spectral Lantern",
    "base_gold": 180,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3159.png",
    "description": "+15 Attack Damage\n+30% Attack Speed\n\nUNIQUE Passive - Maim: Basic attacks against monsters deal 75 bonus magic damage and heal 10 Health on hit.\nUNIQUE Passive: Gain 30% increased Gold from monsters.\nUNIQUE Passive - Trap Detection: Nearby stealthed enemy traps are revealed.\nUNIQUE Active - Hunter's Sight: A stealth-detecting mist grants vision in the target area for 5 seconds, revealing enemy champions that enter for 3 seconds (60 second cooldown)."
  },
  "2137": {
    "sell_gold": 160,
    "into_items": [
      
    ],
    "total_gold": 400,
    "item_id": 2137,
    "from_items": [
      
    ],
    "name": "Elixir of Ruin",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2137.png",
    "description": "Level 9 required to purchase.\n\nClick to Consume: Grants +250 Health, 15% Bonus Damage to Towers and Siege Commander for 3 minutes.\n\nSiege Commander: Nearby minions gain 15% Bonus Damage to Towers and gain Movement Speed based on champion's Movement Speed.\n\n(Only one Flask effect may be active at a time.)"
  },
  "2138": {
    "sell_gold": 160,
    "into_items": [
      
    ],
    "total_gold": 400,
    "item_id": 2138,
    "from_items": [
      
    ],
    "name": "Elixir of Iron",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2138.png",
    "description": "Level 9 required to purchase.\n\nClick to Consume: Grants 25% increased Size, Slow Resistance, Tenacity and Path of Iron for 3 minutes.\n\nPath of Iron: Moving leaves a path behind that boosts allied champion's Movement Speed by 15%.\n\n(Only one Flask effect may be active at a time.)"
  },
  "3087": {
    "sell_gold": 1750,
    "into_items": [
      
    ],
    "total_gold": 2500,
    "item_id": 3087,
    "from_items": [
      3093,
      3086
    ],
    "name": "Statikk Shiv",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3087.png",
    "description": "+40% Attack Speed\n+20% Critical Strike Chance\n+6% Movement Speed\n\nUNIQUE Passive: Grants Static Charges upon moving or attacking. At 100 Charges, basic attacking expends all Charges to deal 100 bonus magic damage to up to 4 targets on hit (this damage can critically strike)."
  },
  "2140": {
    "sell_gold": 160,
    "into_items": [
      
    ],
    "total_gold": 400,
    "item_id": 2140,
    "from_items": [
      
    ],
    "name": "Elixir of Wrath",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2140.png",
    "description": "Level 9 required to purchase.\n\nClick to Consume: Grants +25 Attack Damage and Bloodlust for 3 minutes.\n\nBloodlust: Dealing physical damage to champions heals for 10% of the damage dealt. Scoring a Kill or Assist extends the duration of this Flask by 30 seconds.\n\n(Only one Flask effect may be active at a time.)"
  },
  "3165": {
    "sell_gold": 1610,
    "into_items": [
      
    ],
    "total_gold": 2300,
    "item_id": 3165,
    "from_items": [
      3108,
      3114
    ],
    "name": "Morellonomicon",
    "base_gold": 880,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3165.png",
    "description": "+80 Ability Power\n+20% Cooldown Reduction\n+100% Base Mana Regen \n\nUNIQUE Passive: Dealing magic damage to enemy champions below 40% Health inflicts Grievous Wounds for 4 seconds.\n\n(Grievous Wounds reduces incoming healing and regeneration effects by 50%.)"
  },
  "3166": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3166,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3166.png",
    "description": "UNIQUE Active - Bonetooth Totem: Places a Stealth Ward that lasts 60 seconds (120 Second cooldown). Active upgrades at 6 Trophies. \n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3167": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3167,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3167.png",
    "description": "UNIQUE Active - Bonetooth Totem: Places a Stealth Ward that lasts 60 seconds (120 Second cooldown). Active upgrades at 6 Trophies.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "1043": {
    "sell_gold": 630,
    "into_items": [
      3091,
      3085
    ],
    "total_gold": 900,
    "item_id": 1043,
    "from_items": [
      
    ],
    "name": "Recurve Bow",
    "base_gold": 900,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1043.png",
    "description": "+30% Attack Speed"
  },
  "3169": {
    "sell_gold": 0,
    "into_items": [
      3175,
      3410,
      3416,
      3422,
      3455
    ],
    "total_gold": 0,
    "item_id": 3169,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3169.png",
    "description": "UNIQUE Active - Bonetooth Totem: Places a Stealth Ward that lasts 120 seconds (120 Second cooldown). Active upgrades at 20 Trophies.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3170": {
    "sell_gold": 1834,
    "into_items": [
      
    ],
    "total_gold": 2620,
    "item_id": 3170,
    "from_items": [
      1033,
      3191
    ],
    "name": "Moonflair Spellblade",
    "base_gold": 920,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3170.png",
    "description": "+50 Ability Power\n+50 Armor\n+50 Magic Resist\n\nUNIQUE Passive - Tenacity: Reduces the duration of stuns, slows, taunts, fears, silences, blinds, polymorphs, and immobilizes by 35%.\n\n(Unique Passives with the same name do not stack.)"
  },
  "3171": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3171,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3171.png",
    "description": "UNIQUE Active - Bonetooth Totem: Places a Stealth Ward that lasts 180 seconds (60 Second cooldown).\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3172": {
    "sell_gold": 1995,
    "into_items": [
      
    ],
    "total_gold": 2850,
    "item_id": 3172,
    "from_items": [
      3101,
      1037
    ],
    "name": "Zephyr",
    "base_gold": 725,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3172.png",
    "description": "+25 Attack Damage\n+50% Attack Speed\n+10% Movement Speed\n+10% Cooldown Reduction\n\nUNIQUE Passive - Tenacity: Reduces the duration of stuns, slows, taunts, fears, silences, blinds, polymorphs, and immobilizes by 35%.\n\n(Unique Passives with the same name do not stack.)"
  },
  "3174": {
    "sell_gold": 1890,
    "into_items": [
      
    ],
    "total_gold": 2700,
    "item_id": 3174,
    "from_items": [
      3108,
      3028
    ],
    "name": "Athene's Unholy Grail",
    "base_gold": 880,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3174.png",
    "description": "+60 Ability Power\n+25 Magic Resist\n+20% Cooldown Reduction\n+50% Base Mana Regen \n\nUNIQUE Passive: Restores 15% of maximum Mana on kill or assist.\nUNIQUE Passive - Mana Font: Restores 2% of missing Mana every 5 seconds.\n\n(Unique Passives with the same name do not stack.)"
  },
  "3175": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3175,
    "from_items": [
      3169
    ],
    "name": "Head of Kha'Zix",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3175.png",
    "description": "UNIQUE Active - Bonetooth Totem: Places a Stealth Ward that lasts 180 seconds (90 Second cooldown). Limit 3 Stealth Wards on the map per player.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Rengar gains the movement speed bonus of Thrill of the Hunt while he is stealthed."
  },
  "3180": {
    "sell_gold": 1750,
    "into_items": [
      
    ],
    "total_gold": 2500,
    "item_id": 3180,
    "from_items": [
      3010,
      1033
    ],
    "name": "Odyn's Veil",
    "base_gold": 800,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3180.png",
    "description": "+350 Health\n+350 Mana\n+50 Magic Resist\n\nUNIQUE Passive: Reduces and stores 10% of magic damage received. \nUNIQUE Active: Deals 200 + (stored magic) (max 400) magic damage to nearby enemy units (90 second cooldown)."
  },
  "3181": {
    "sell_gold": 1593,
    "into_items": [
      
    ],
    "total_gold": 2275,
    "item_id": 3181,
    "from_items": [
      1037,
      1053
    ],
    "name": "Sanguine Blade",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3181.png",
    "description": "+45 Attack Damage\n+10% Life Steal\n\nUNIQUE Passive: Basic attacks grant +6 Attack Damage and +1% Life Steal for 8 seconds on hit (effect stacks up to 5 times)."
  },
  "3184": {
    "sell_gold": 1890,
    "into_items": [
      
    ],
    "total_gold": 2700,
    "item_id": 3184,
    "from_items": [
      1037,
      3044
    ],
    "name": "Entropy",
    "base_gold": 500,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3184.png",
    "description": "+275 Health\n+55 Attack Damage\n\nUNIQUE Passive - Rage: Basic attacks grant 20 Movement Speed for 2 seconds on hit. Kills grant 60 Movement Speed for 2 seconds. This Movement Speed bonus is halved for ranged champions.\nUNIQUE Active: For the next 5 seconds, basic attacks reduce the target's Movement Speed by 30% and deal 80 true damage over 2.5 seconds on hit (60 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "3185": {
    "sell_gold": 1596,
    "into_items": [
      
    ],
    "total_gold": 2280,
    "item_id": 3185,
    "from_items": [
      1018,
      1028,
      3122
    ],
    "name": "The Lightbringer",
    "base_gold": 350,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3185.png",
    "description": "+30 Attack Damage\n+30% Critical Strike Chance\n\nUNIQUE Passive: Critical Strikes cause enemies to bleed for an additional 90% of bonus Attack Damage as physical damage over 3 seconds and reveal them for the duration.\nUNIQUE Passive - Trap Detection: Nearby stealthed enemy traps are revealed.\nUNIQUE Active - Hunter's Sight: A stealth-detecting mist grants vision in the target area for 5 seconds, revealing enemy champions that enter for 3 seconds (60 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "3091": {
    "sell_gold": 1820,
    "into_items": [
      
    ],
    "total_gold": 2600,
    "item_id": 3091,
    "from_items": [
      1043,
      1033,
      1042
    ],
    "name": "Wit's End",
    "base_gold": 750,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3091.png",
    "description": "+50% Attack Speed\n+30 Magic Resist\n\nUNIQUE Passive: Basic attacks deal 42 bonus magic damage on hit.\nUNIQUE Passive: Basic attacks steal 5 Magic Resist from the target on hit (stacks up to 5 times.)"
  },
  "3188": {
    "sell_gold": 1855,
    "into_items": [
      
    ],
    "total_gold": 2650,
    "item_id": 3188,
    "from_items": [
      3108,
      1026
    ],
    "name": "Blackfire Torch",
    "base_gold": 970,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3188.png",
    "description": "+80 Ability Power\n+10% Cooldown Reduction\n\nUNIQUE Active: Deals 20% of target champion's maximum Health in magic damage over 4 seconds and increases all subsequent magic damage taken by the target by 20% (90 second cooldown)."
  },
  "3190": {
    "sell_gold": 1960,
    "into_items": [
      
    ],
    "total_gold": 2800,
    "item_id": 3190,
    "from_items": [
      3067,
      3105
    ],
    "name": "Locket of the Iron Solari",
    "base_gold": 50,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3190.png",
    "description": "+400 Health\n+20 Magic Resistance\n+10% Cooldown Reduction\n\nUNIQUE Active: Grants a shield to nearby allies for 5 seconds that absorbs up to 50 (+10 per level) damage (60 second cooldown).\nUNIQUE Aura - Legion: Grants nearby allies +20 Magic Resist and +75% Base Health Regen.\n\n(Unique Auras with the same name don't stack.)"
  },
  "3191": {
    "sell_gold": 840,
    "into_items": [
      3090,
      3157,
      3170
    ],
    "total_gold": 1200,
    "item_id": 3191,
    "from_items": [
      1029,
      1052
    ],
    "name": "Seeker's Armguard",
    "base_gold": 465,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3191.png",
    "description": "+30 Armor\n+25 Ability Power\n\nUNIQUE Passive: Killing a unit grants 0.5 bonus Armor and Ability Power. This bonus stacks up to 30 times."
  },
  "3706": {
    "sell_gold": 595,
    "into_items": [
      3707,
      3708,
      3709,
      3710
    ],
    "total_gold": 850,
    "item_id": 3706,
    "from_items": [
      1039
    ],
    "name": "Stalker's Blade",
    "base_gold": 450,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3706.png",
    "description": "+30 Bonus Gold per Large Monster Kill\nPassive - Chilling Smite: Smite can be cast on enemy champions, dealing reduced true damage and stealing 20% movement speed for 2 seconds. \n\nPassive - Jungler:  Deal 45 additional magic damage to monsters over 2 seconds and gain 10 Health Regen and 5 Mana Regen per second while in combat with monsters.\n\nLimited to 1 Jungle item"
  },
  "3707": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3707,
    "from_items": [
      3134,
      3706
    ],
    "name": "Enchantment: Warrior",
    "base_gold": 63,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3707.png",
    "description": "+45 Attack Damage\n+10% Cooldown Reduction\n+10 Armor Penetration"
  },
  "3708": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3708,
    "from_items": [
      3108,
      3706
    ],
    "name": "Enchantment: Magus",
    "base_gold": 580,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3708.png",
    "description": "+80 Ability Power\n+20% Cooldown Reduction"
  },
  "3197": {
    "sell_gold": 1400,
    "into_items": [
      3198
    ],
    "total_gold": 2000,
    "item_id": 3197,
    "from_items": [
      3196
    ],
    "name": "The Hex Core mk-2",
    "base_gold": 1000,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3197.png",
    "description": "+5 Ability Power per level\n+40 Ability Power\n+300 Mana\n\nUNIQUE Passive - Progress: Viktor can upgrade one of his basic spells."
  },
  "3710": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3710,
    "from_items": [
      3706,
      1042
    ],
    "name": "Enchantment: Devourer",
    "base_gold": 500,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3710.png",
    "description": "+50% Attack Speed\n+25 Magic Damage on Hit\n\nPassive - Devouring: Killing large monsters increases the magic damage of this item by +1. Champion kills or assists increases the magic damage of this item by +2."
  },
  "3711": {
    "sell_gold": 595,
    "into_items": [
      3719,
      3720,
      3721,
      3722
    ],
    "total_gold": 850,
    "item_id": 3711,
    "from_items": [
      1039
    ],
    "name": "Poacher's Knife",
    "base_gold": 450,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3711.png",
    "description": "+30 Bonus Gold per Large Monster Kill\nPassive - Scavenging Smite: When you Smite a large monster in the enemy jungle, you gain half a charge of Smite. If you kill that monster, you gain +20 bonus Gold, and you gain 175% increased Movement Speed decaying over 2 seconds.\n\nPassive - Jungler:  Deal 45 additional magic damage to monsters over 2 seconds and gain 10 Health Regen and 5 Mana Regen per second while in combat with monsters.\n\nLimited to 1 Jungle item"
  },
  "3200": {
    "sell_gold": 0,
    "into_items": [
      3196
    ],
    "total_gold": 0,
    "item_id": 3200,
    "from_items": [
      
    ],
    "name": "Prototype Hex Core",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3200.png",
    "description": "+3 Ability Power per level\n\nUNIQUE Passive - Progress: This item can be upgraded three times to enhance Viktor's basic abilities."
  },
  "3713": {
    "sell_gold": 595,
    "into_items": [
      3723,
      3724,
      3725,
      3726
    ],
    "total_gold": 850,
    "item_id": 3713,
    "from_items": [
      1039
    ],
    "name": "Ranger's Trailblazer",
    "base_gold": 450,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3713.png",
    "description": "+30 Bonus Gold per Large Monster Kill\nPassive - Blasting Smite:  Smite deals damage in an area, dealing half damage to all monsters and enemy minions near the target and stuns them for 1.5 seconds. Casting Smite on a monster restores 15% of missing Health and Mana. \n\nPassive - Jungler: Deal 45 additional magic damage to monsters over 2 seconds and gain 10 Health Regen and 5 Mana Regen per second while in combat with monsters.\n\nLimited to 1 Jungle item"
  },
  "3090": {
    "sell_gold": 2478,
    "into_items": [
      
    ],
    "total_gold": 3540,
    "item_id": 3090,
    "from_items": [
      1026,
      3191,
      1052
    ],
    "name": "Wooglet's Witchcap",
    "base_gold": 1045,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3090.png",
    "description": "+100 Ability Power\n+45 Armor  \n\nUNIQUE Passive: Increases Ability Power by 25%\nUNIQUE Active: Champion becomes invulnerable and untargetable for 2.5 seconds, but is unable to move, attack, cast spells, or use items during this time (90 second cooldown)."
  },
  "3715": {
    "sell_gold": 595,
    "into_items": [
      3714,
      3716,
      3717,
      3718
    ],
    "total_gold": 850,
    "item_id": 3715,
    "from_items": [
      1039
    ],
    "name": "Skirmisher's Sabre",
    "base_gold": 450,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3715.png",
    "description": "+30 Bonus Gold per Large Monster Kill\nPassive - Challenging Smite: Smite can be cast on enemy champions, marking them for 6 seconds. While marked, basic attacks deal true damage over 3 seconds, you have vision of them, and their damage to you is reduced by 20%.\n\nPassive - Jungler:  Deal 45 additional magic damage to monsters over 2 seconds and gain 10 Health Regen and 5 Mana Regen per second while in combat with monsters.\n\nLimited to 1 Jungle item"
  },
  "3716": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3716,
    "from_items": [
      3108,
      3715
    ],
    "name": "Enchantment: Magus",
    "base_gold": 580,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3716.png",
    "description": "+80 Ability Power\n+20% Cooldown Reduction"
  },
  "3717": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3717,
    "from_items": [
      1028,
      3715,
      3067
    ],
    "name": "Enchantment: Juggernaut",
    "base_gold": 150,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3717.png",
    "description": "+500 Health\n+10% Cooldown Reduction\n\nUNIQUE Passive - Tenacity: Reduces the duration of stuns, slows, taunts, fears, silences, blinds, polymorphs, and immobilizes by 35%.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3718": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3718,
    "from_items": [
      3715,
      1042
    ],
    "name": "Enchantment: Devourer",
    "base_gold": 500,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3718.png",
    "description": "+50% Attack Speed\n+25 Magic Damage on Hit\n\nPassive - Devouring: Killing large monsters increases the magic damage of this item by +1. Champion kills or assists increases the magic damage of this item by +2."
  },
  "3265": {
    "sell_gold": 1173,
    "into_items": [
      
    ],
    "total_gold": 1675,
    "item_id": 3265,
    "from_items": [
      3111
    ],
    "name": "Enchantment: Homeguard",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3265.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Homeguard bonus.\n\nUNIQUE Passive - Homeguard: Visiting the shop vastly increases Health and Mana Regeneration and grants 200% bonus Movement Speed that decays over 8 seconds. Bonus Movement Speed and regeneration are disabled for 6 seconds upon dealing or taking damage.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3720": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3720,
    "from_items": [
      3108,
      3711
    ],
    "name": "Enchantment: Magus",
    "base_gold": 580,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3720.png",
    "description": "+80 Ability Power\n+20% Cooldown Reduction"
  },
  "3721": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3721,
    "from_items": [
      1028,
      3711,
      3067
    ],
    "name": "Enchantment: Juggernaut",
    "base_gold": 150,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3721.png",
    "description": "+500 Health\n+10% Cooldown Reduction\n\nUNIQUE Passive - Tenacity: Reduces the duration of stuns, slows, taunts, fears, silences, blinds, polymorphs, and immobilizes by 35%.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3722": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3722,
    "from_items": [
      3711,
      1042
    ],
    "name": "Enchantment: Devourer",
    "base_gold": 500,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3722.png",
    "description": "+50% Attack Speed\n+25 Magic Damage on Hit\n\nPassive - Devouring: Killing large monsters increases the magic damage of this item by +1. Champion kills or assists increases the magic damage of this item by +2."
  },
  "3723": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3723,
    "from_items": [
      3713,
      3134
    ],
    "name": "Enchantment: Warrior",
    "base_gold": 63,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3723.png",
    "description": "+45 Attack Damage\n+10% Cooldown Reduction\n+10 Armor Penetration"
  },
  "3724": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3724,
    "from_items": [
      3108,
      3713
    ],
    "name": "Enchantment: Magus",
    "base_gold": 580,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3724.png",
    "description": "+80 Ability Power\n+20% Cooldown Reduction"
  },
  "2050": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 2050,
    "from_items": [
      
    ],
    "name": "Explorer's Ward",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2050.png",
    "description": "Click to Consume: Places an invisible ward that reveals the surrounding area for 60 seconds."
  },
  "3726": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3726,
    "from_items": [
      3713,
      1042
    ],
    "name": "Enchantment: Devourer",
    "base_gold": 500,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3726.png",
    "description": "+50% Attack Speed\n+25 Magic Damage on Hit\n\nPassive - Devouring: Killing large monsters increases the magic damage of this item by +1. Champion kills or assists increases the magic damage of this item by +2."
  },
  "3222": {
    "sell_gold": 1715,
    "into_items": [
      
    ],
    "total_gold": 2450,
    "item_id": 3222,
    "from_items": [
      3028,
      3114
    ],
    "name": "Mikael's Crucible",
    "base_gold": 850,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3222.png",
    "description": "+40 Magic Resist\n+10% Cooldown Reduction\n+100% Base Mana Regen \n\nUNIQUE Passive - Mana Font: Restores 2% of missing Mana every 5 seconds.\nUNIQUE Active: Removes all stuns, roots, taunts, fears, silences, and slows on an allied champion and heals that champion for 150 (+10% of maximum Health) (180 second cooldown).\n\n(Unique Passives with the same name do not stack.)"
  },
  "1062": {
    "sell_gold": 380,
    "into_items": [
      
    ],
    "total_gold": 950,
    "item_id": 1062,
    "from_items": [
      
    ],
    "name": "Prospector's Blade",
    "base_gold": 950,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1062.png",
    "description": "+16 Attack Damage\n+15% Attack Speed \n\nUNIQUE Passive - Prospector: +150 Health\n\n(Unique Passives with the same name don't stack.)"
  },
  "2052": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 2052,
    "from_items": [
      
    ],
    "name": "Poro-Snax",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2052.png",
    "description": "This savory blend of free-range, grass-fed Avarosan game hens and organic, non-ZMO Freljordian herbs contains the essential nutrients necessary to keep your Poro purring with pleasure.\n\nAll proceeds will be donated towards fighting Noxian animal cruelty."
  },
  "3074": {
    "sell_gold": 2310,
    "into_items": [
      
    ],
    "total_gold": 3300,
    "item_id": 3074,
    "from_items": [
      3077,
      1053
    ],
    "name": "Ravenous Hydra (Melee Only)",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3074.png",
    "description": "+75 Attack Damage\n+100% Base Health Regen \n+12% Life Steal\n\nPassive: Life Steal applies to damage dealt by this item.\nUNIQUE Passive - Cleave: Basic attacks deal 20% to 60% of total Attack Damage as bonus physical damage to enemies near the target on hit (enemies closest to the target take the most damage).\nUNIQUE Active - Crescent: Deals 60% to 100% of total Attack Damage as physical damage to nearby enemy units (closest enemies take the most damage) (10 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "3100": {
    "sell_gold": 2100,
    "into_items": [
      
    ],
    "total_gold": 3000,
    "item_id": 3100,
    "from_items": [
      3113,
      3057
    ],
    "name": "Lich Bane",
    "base_gold": 950,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3100.png",
    "description": "+80 Ability Power\n+5% Movement Speed\n+250 Mana\n\nUNIQUE Passive - Spellblade: After using an ability, the next basic attack deals 75% Base Attack Damage (+50% of Ability Power) bonus magic damage on hit (1.5 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "1053": {
    "sell_gold": 560,
    "into_items": [
      3144,
      3181,
      3072,
      3074,
      3508,
      3050
    ],
    "total_gold": 800,
    "item_id": 1053,
    "from_items": [
      1036
    ],
    "name": "Vampiric Scepter",
    "base_gold": 440,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1053.png",
    "description": "+10 Attack Damage\n+8% Life Steal"
  },
  "3250": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3250,
    "from_items": [
      3006
    ],
    "name": "Enchantment: Homeguard",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3250.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Homeguard bonus.\n\nUNIQUE Passive - Homeguard: Visiting the shop vastly increases Health and Mana Regeneration and grants 200% bonus Movement Speed that decays over 8 seconds. Bonus Movement Speed and regeneration are disabled for 6 seconds upon dealing or taking damage.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3251": {
    "sell_gold": 1120,
    "into_items": [
      
    ],
    "total_gold": 1600,
    "item_id": 3251,
    "from_items": [
      3006
    ],
    "name": "Enchantment: Captain",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3251.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Captain bonus.\n\nUNIQUE Passive - Captain: Grants +10% Movement Speed to nearby approaching allied champions.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3211": {
    "sell_gold": 840,
    "into_items": [
      3065,
      3102
    ],
    "total_gold": 1200,
    "item_id": 3211,
    "from_items": [
      1028,
      1033
    ],
    "name": "Spectre's Cowl",
    "base_gold": 300,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3211.png",
    "description": "+200 Health\n+35 Magic Resist\n\nUNIQUE Passive: Grants 100% Base Health Regen for up to 10 seconds after taking damage from an enemy champion.\n\n"
  },
  "1054": {
    "sell_gold": 176,
    "into_items": [
      
    ],
    "total_gold": 440,
    "item_id": 1054,
    "from_items": [
      
    ],
    "name": "Doran's Shield",
    "base_gold": 440,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1054.png",
    "description": "+80 Health\n\nPassive:  Restores 6 Health every 5 seconds.\nUNIQUE Passive: Blocks 8 damage from single target attacks and spells from champions."
  },
  "3254": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3254,
    "from_items": [
      3006
    ],
    "name": "Enchantment: Alacrity",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3254.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Alacrity bonus. \n\nUNIQUE Passive - Alacrity: +20 Movement Speed\n\n(Unique Passives with the same name don't stack.)"
  },
  "3255": {
    "sell_gold": 1103,
    "into_items": [
      
    ],
    "total_gold": 1575,
    "item_id": 3255,
    "from_items": [
      3020
    ],
    "name": "Enchantment: Homeguard",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3255.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Homeguard bonus.\n\nUNIQUE Passive - Homeguard: Visiting the shop vastly increases Health and Mana Regeneration and grants 200% bonus Movement Speed that decays over 8 seconds. Bonus Movement Speed and regeneration are disabled for 6 seconds upon dealing or taking damage.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3256": {
    "sell_gold": 1190,
    "into_items": [
      
    ],
    "total_gold": 1700,
    "item_id": 3256,
    "from_items": [
      3020
    ],
    "name": "Enchantment: Captain",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3256.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Captain bonus.\n\nUNIQUE Passive - Captain: Grants +10% Movement Speed to nearby approaching allied champions.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3257": {
    "sell_gold": 1103,
    "into_items": [
      
    ],
    "total_gold": 1575,
    "item_id": 3257,
    "from_items": [
      3020
    ],
    "name": "Enchantment: Furor",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3257.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Furor bonus.\n\nUNIQUE Passive - Furor: Upon dealing damage with a single target spell or attack (on hit), grants +12% Movement Speed that decays over 2 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3258": {
    "sell_gold": 1103,
    "into_items": [
      
    ],
    "total_gold": 1575,
    "item_id": 3258,
    "from_items": [
      3020
    ],
    "name": "Enchantment: Distortion",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3258.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Distortion bonus.\n\nUNIQUE Passive - Distortion: Teleport, Flash, and Ghost summoner spell cooldowns are reduced by 20% and are granted additional mobility: \n\nGhost: Grants 40% Movement Speed from 27%.\nFlash: 20% Movement Speed bonus for 1 second after cast.\nTeleport: 30% Movement Speed bonus for 3 seconds after use.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3259": {
    "sell_gold": 1103,
    "into_items": [
      
    ],
    "total_gold": 1575,
    "item_id": 3259,
    "from_items": [
      3020
    ],
    "name": "Enchantment: Alacrity",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3259.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Alacrity bonus. \n\nUNIQUE Passive - Alacrity: +20 Movement Speed\n\n(Unique Passives with the same name don't stack.)"
  },
  "3260": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3260,
    "from_items": [
      3047
    ],
    "name": "Enchantment: Homeguard",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3260.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Homeguard bonus.\n\nUNIQUE Passive - Homeguard: Visiting the shop vastly increases Health and Mana Regeneration and grants 200% bonus Movement Speed that decays over 8 seconds. Bonus Movement Speed and regeneration are disabled for 6 seconds upon dealing or taking damage.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3261": {
    "sell_gold": 1120,
    "into_items": [
      
    ],
    "total_gold": 1600,
    "item_id": 3261,
    "from_items": [
      3047
    ],
    "name": "Enchantment: Captain",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3261.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Captain bonus.\n\nUNIQUE Passive - Captain: Grants +10% Movement Speed to nearby approaching allied champions.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3262": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3262,
    "from_items": [
      3047
    ],
    "name": "Enchantment: Furor",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3262.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Furor bonus.\n\nUNIQUE Passive - Furor: Upon dealing damage with a single target spell or attack (on hit), grants +12% Movement Speed that decays over 2 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3263": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3263,
    "from_items": [
      3047
    ],
    "name": "Enchantment: Distortion",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3263.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Distortion bonus.\n\nUNIQUE Passive - Distortion: Teleport, Flash, and Ghost summoner spell cooldowns are reduced by 20% and are granted additional mobility: \n\nGhost: Grants 40% Movement Speed from 27%.\nFlash: 20% Movement Speed bonus for 1 second after cast.\nTeleport: 30% Movement Speed bonus for 3 seconds after use.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3264": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3264,
    "from_items": [
      3047
    ],
    "name": "Enchantment: Alacrity",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3264.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Alacrity bonus. \n\nUNIQUE Passive - Alacrity: +20 Movement Speed\n\n(Unique Passives with the same name don't stack.)"
  },
  "1056": {
    "sell_gold": 160,
    "into_items": [
      
    ],
    "total_gold": 400,
    "item_id": 1056,
    "from_items": [
      
    ],
    "name": "Doran's Ring",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1056.png",
    "description": "+60 Health\n+15 Ability Power\n\nPassive: +3 Mana Regen per 5 seconds.\nPassive: Restores 4 Mana upon killing a unit."
  },
  "3266": {
    "sell_gold": 1260,
    "into_items": [
      
    ],
    "total_gold": 1800,
    "item_id": 3266,
    "from_items": [
      3111
    ],
    "name": "Enchantment: Captain",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3266.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Captain bonus.\n\nUNIQUE Passive - Captain: Grants +10% Movement Speed to nearby approaching allied champions.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3267": {
    "sell_gold": 1173,
    "into_items": [
      
    ],
    "total_gold": 1675,
    "item_id": 3267,
    "from_items": [
      3111
    ],
    "name": "Enchantment: Furor",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3267.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Furor bonus.\n\nUNIQUE Passive - Furor: Upon dealing damage with a single target spell or attack (on hit), grants +12% Movement Speed that decays over 2 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3268": {
    "sell_gold": 1173,
    "into_items": [
      
    ],
    "total_gold": 1675,
    "item_id": 3268,
    "from_items": [
      3111
    ],
    "name": "Enchantment: Distortion",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3268.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Distortion bonus.\n\nUNIQUE Passive - Distortion: Teleport, Flash, and Ghost summoner spell cooldowns are reduced by 20% and are granted additional mobility: \n\nGhost: Grants 40% Movement Speed from 27%.\nFlash: 20% Movement Speed bonus for 1 second after cast.\nTeleport: 30% Movement Speed bonus for 3 seconds after use.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3269": {
    "sell_gold": 1173,
    "into_items": [
      
    ],
    "total_gold": 1675,
    "item_id": 3269,
    "from_items": [
      3111
    ],
    "name": "Enchantment: Alacrity",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3269.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Alacrity bonus. \n\nUNIQUE Passive - Alacrity: +20 Movement Speed\n\n(Unique Passives with the same name don't stack.)"
  },
  "3270": {
    "sell_gold": 893,
    "into_items": [
      
    ],
    "total_gold": 1275,
    "item_id": 3270,
    "from_items": [
      3117
    ],
    "name": "Enchantment: Homeguard",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3270.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Homeguard bonus.\n\nUNIQUE Passive - Homeguard: Visiting the shop vastly increases Health and Mana Regeneration and grants 200% bonus Movement Speed that decays over 8 seconds. Bonus Movement Speed and regeneration are disabled for 6 seconds upon dealing or taking damage.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3271": {
    "sell_gold": 980,
    "into_items": [
      
    ],
    "total_gold": 1400,
    "item_id": 3271,
    "from_items": [
      3117
    ],
    "name": "Enchantment: Captain",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3271.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Captain bonus.\n\nUNIQUE Passive - Captain: Grants +10% Movement Speed to nearby approaching allied champions.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3272": {
    "sell_gold": 893,
    "into_items": [
      
    ],
    "total_gold": 1275,
    "item_id": 3272,
    "from_items": [
      3117
    ],
    "name": "Enchantment: Furor",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3272.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Furor bonus.\n\nUNIQUE Passive - Furor: Upon dealing damage with a single target spell or attack (on hit), grants +12% Movement Speed that decays over 2 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3273": {
    "sell_gold": 893,
    "into_items": [
      
    ],
    "total_gold": 1275,
    "item_id": 3273,
    "from_items": [
      3117
    ],
    "name": "Enchantment: Distortion",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3273.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Distortion bonus.\n\nUNIQUE Passive - Distortion: Teleport, Flash, and Ghost summoner spell cooldowns are reduced by 20% and are granted additional mobility: \n\nGhost: Grants 40% Movement Speed from 27%.\nFlash: 20% Movement Speed bonus for 1 second after cast.\nTeleport: 30% Movement Speed bonus for 3 seconds after use.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3274": {
    "sell_gold": 893,
    "into_items": [
      
    ],
    "total_gold": 1275,
    "item_id": 3274,
    "from_items": [
      3117
    ],
    "name": "Enchantment: Alacrity",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3274.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Alacrity bonus. \n\nUNIQUE Passive - Alacrity: +20 Movement Speed\n\n(Unique Passives with the same name don't stack.)"
  },
  "3275": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3275,
    "from_items": [
      3158
    ],
    "name": "Enchantment: Homeguard",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3275.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Homeguard bonus.\n\nUNIQUE Passive - Homeguard: Visiting the shop vastly increases Health and Mana Regeneration and grants 200% bonus Movement Speed that decays over 8 seconds. Bonus Movement Speed and regeneration are disabled for 6 seconds upon dealing or taking damage.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3276": {
    "sell_gold": 1120,
    "into_items": [
      
    ],
    "total_gold": 1600,
    "item_id": 3276,
    "from_items": [
      3158
    ],
    "name": "Enchantment: Captain",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3276.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Captain bonus.\n\nUNIQUE Passive - Captain: Grants +10% Movement Speed to nearby approaching allied champions.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3106": {
    "sell_gold": 525,
    "into_items": [
      3154,
      3159
    ],
    "total_gold": 750,
    "item_id": 3106,
    "from_items": [
      1042
    ],
    "name": "Madred's Razors",
    "base_gold": 300,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3106.png",
    "description": "+15% Attack Speed\n\nUNIQUE Passive - Maim: Basic attacks against monsters deal 50 bonus magic damage and heal 8 Health on hit.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3278": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3278,
    "from_items": [
      3158
    ],
    "name": "Enchantment: Distortion",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3278.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Distortion bonus.\n\nUNIQUE Passive - Distortion: Teleport, Flash, and Ghost summoner spell cooldowns are reduced by 20% and are granted additional mobility: \n\nGhost: Grants 40% Movement Speed from 27%.\nFlash: 20% Movement Speed bonus for 1 second after cast.\nTeleport: 30% Movement Speed bonus for 3 seconds after use.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3277": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3277,
    "from_items": [
      3158
    ],
    "name": "Enchantment: Furor",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3277.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Furor bonus.\n\nUNIQUE Passive - Furor: Upon dealing damage with a single target spell or attack (on hit), grants +12% Movement Speed that decays over 2 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3280": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3280,
    "from_items": [
      3009
    ],
    "name": "Enchantment: Homeguard",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3280.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Homeguard bonus.\n\nUNIQUE Passive - Homeguard: Visiting the shop vastly increases Health and Mana Regeneration and grants 200% bonus Movement Speed that decays over 8 seconds. Bonus Movement Speed and regeneration are disabled for 6 seconds upon dealing or taking damage.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3281": {
    "sell_gold": 1120,
    "into_items": [
      
    ],
    "total_gold": 1600,
    "item_id": 3281,
    "from_items": [
      3009
    ],
    "name": "Enchantment: Captain",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3281.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Captain bonus.\n\nUNIQUE Passive - Captain: Grants +10% Movement Speed to nearby approaching allied champions.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3105": {
    "sell_gold": 1330,
    "into_items": [
      3190,
      3060
    ],
    "total_gold": 1900,
    "item_id": 3105,
    "from_items": [
      1006,
      1028,
      1033
    ],
    "name": "Aegis of the Legion",
    "base_gold": 820,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3105.png",
    "description": "+200 Health\n+20 Magic Resistance\n\nUNIQUE Aura - Legion: Grants nearby allies +20 Magic Resist and +75% Base Health Regen.\n\n(Unique Auras with the same name don't stack.)"
  },
  "3283": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3283,
    "from_items": [
      3009
    ],
    "name": "Enchantment: Distortion",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3283.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Distortion bonus.\n\nUNIQUE Passive - Distortion: Teleport, Flash, and Ghost summoner spell cooldowns are reduced by 20% and are granted additional mobility: \n\nGhost: Grants 40% Movement Speed from 27%.\nFlash: 20% Movement Speed bonus for 1 second after cast.\nTeleport: 30% Movement Speed bonus for 3 seconds after use.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3284": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3284,
    "from_items": [
      3009
    ],
    "name": "Enchantment: Alacrity",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3284.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Alacrity bonus. \n\nUNIQUE Passive - Alacrity: +20 Movement Speed\n\n(Unique Passives with the same name don't stack.)"
  },
  "3800": {
    "sell_gold": 1750,
    "into_items": [
      
    ],
    "total_gold": 2500,
    "item_id": 3800,
    "from_items": [
      3801,
      3010
    ],
    "name": "Righteous Glory",
    "base_gold": 700,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3800.png",
    "description": "+500 Health\n+300 Mana\n+100% Base Health Regen \n\nUNIQUE Passive - Valor's Reward: Upon leveling up, restores 150 Health and 200 Mana over 8 seconds.\nUNIQUE Active: Grants +60% Movement Speed to nearby allies when moving towards enemies or enemy turrets for 3 seconds. After 3 seconds, a shockwave is emitted, slowing nearby enemy champion Movement Speed by 80% for 1 second(s) (60 second cooldown).\n\nThis effect may be reactivated early to instantly release the shockwave."
  },
  "3801": {
    "sell_gold": 420,
    "into_items": [
      3083,
      3800
    ],
    "total_gold": 600,
    "item_id": 3801,
    "from_items": [
      1006,
      1028
    ],
    "name": "Crystalline Bracer",
    "base_gold": 20,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3801.png",
    "description": "+200 Health\n+50% Base Health Regen "
  },
  "3290": {
    "sell_gold": 1610,
    "into_items": [
      
    ],
    "total_gold": 2300,
    "item_id": 3290,
    "from_items": [
      3108,
      3113
    ],
    "name": "Twin Shadows",
    "base_gold": 630,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3290.png",
    "description": "+80 Ability Power\n+10% Cooldown Reduction\n+6% Movement Speed\n\nUNIQUE Passive - Trap Detection: Nearby stealthed enemy traps are revealed.\nUNIQUE Active - Hunt: Summons up to 2 invulnerable ghosts that seek out the 2 nearest enemy champions for 6 seconds. If a ghost reaches its target, it reveals the target and reduces their Movement Speed by 40% for 2.5 seconds.\n\nIf a ghost cannot find a target, it tries to return to the caster. Ghosts that successfully return in this way reduce the item's cooldown by 20 seconds (60 second cooldown)."
  },
  "3279": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3279,
    "from_items": [
      3158
    ],
    "name": "Enchantment: Alacrity",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3279.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Alacrity bonus. \n\nUNIQUE Passive - Alacrity: +20 Movement Speed\n\n(Unique Passives with the same name don't stack.)"
  },
  "3301": {
    "sell_gold": 146,
    "into_items": [
      3096
    ],
    "total_gold": 365,
    "item_id": 3301,
    "from_items": [
      
    ],
    "name": "Ancient Coin",
    "base_gold": 365,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3301.png",
    "description": "+25% Base Mana Regen \n\nUNIQUE Passive - Favor: Being near a minion death without dealing the killing blow grants 2 Gold and 5 Health.\n\nLimited to 1 Gold Income item\n\n''Gold dust rises from the desert and clings to the coin.'' - Historian Shurelya, 11 November, 23 CLE\n\n"
  },
  "3302": {
    "sell_gold": 146,
    "into_items": [
      3097
    ],
    "total_gold": 365,
    "item_id": 3302,
    "from_items": [
      
    ],
    "name": "Relic Shield",
    "base_gold": 365,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3302.png",
    "description": "+75 Health\n\nUNIQUE Passive - Spoils of War: Melee basic attacks execute minions below 200 Health. Killing a minion heals the owner and the nearest allied champion for 40 Health and grants them kill Gold.\n\nThese effects require a nearby allied champion. Recharges every 60 seconds. Max 2 charges. \n\nLimited to 1 Gold Income item"
  },
  "3303": {
    "sell_gold": 146,
    "into_items": [
      3098
    ],
    "total_gold": 365,
    "item_id": 3303,
    "from_items": [
      
    ],
    "name": "Spellthief's Edge",
    "base_gold": 365,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3303.png",
    "description": "+5 Ability Power\n+2 Gold per 10 seconds\n+25% Base Mana Regen \n\nUNIQUE Passive - Tribute: Spells and basic attacks against champions or buildings deal 10 additional damage and grant 5 Gold. This can occur up to three times every 30 seconds. Killing a minion disables this passive for 12 seconds.\n\nLimited to 1 Gold Income item"
  },
  "3196": {
    "sell_gold": 700,
    "into_items": [
      3197
    ],
    "total_gold": 1000,
    "item_id": 3196,
    "from_items": [
      3200
    ],
    "name": "The Hex Core mk-1",
    "base_gold": 1000,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3196.png",
    "description": "+4 Ability Power per level\n+20 Ability Power\n+150 Mana\n\nUNIQUE Passive - Progress: Viktor can upgrade one of his basic spells."
  },
  "3111": {
    "sell_gold": 840,
    "into_items": [
      3269,
      3268,
      3267,
      3266,
      3265
    ],
    "total_gold": 1200,
    "item_id": 3111,
    "from_items": [
      1033,
      1001
    ],
    "name": "Mercury's Treads",
    "base_gold": 375,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3111.png",
    "description": "+25 Magic Resist\n\nUNIQUE Passive - Enhanced Movement: +45 Movement Speed\nUNIQUE Passive - Tenacity: Reduces the duration of stuns, slows, taunts, fears, silences, blinds, polymorphs, and immobilizes by 35%.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3282": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3282,
    "from_items": [
      3009
    ],
    "name": "Enchantment: Furor",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3282.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Furor bonus.\n\nUNIQUE Passive - Furor: Upon dealing damage with a single target spell or attack (on hit), grants +12% Movement Speed that decays over 2 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3709": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3709,
    "from_items": [
      1028,
      3706,
      3067
    ],
    "name": "Enchantment: Juggernaut",
    "base_gold": 150,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3709.png",
    "description": "+500 Health\n+10% Cooldown Reduction\n\nUNIQUE Passive - Tenacity: Reduces the duration of stuns, slows, taunts, fears, silences, blinds, polymorphs, and immobilizes by 35%.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3027": {
    "sell_gold": 1960,
    "into_items": [
      
    ],
    "total_gold": 2800,
    "item_id": 3027,
    "from_items": [
      3010,
      1026
    ],
    "name": "Rod of Ages",
    "base_gold": 740,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3027.png",
    "description": "+450 Health\n+450 Mana\n+60 Ability Power\n\nPassive: Grants +20 Health, +20 Mana, and +2 Ability Power per stack (max +200 Health, +200 Mana, and +20 Ability Power). Grants 1 stack per minute (max 10 stacks).\nUNIQUE Passive - Valor's Reward: Upon leveling up, restores 150 Health and 200 Mana over 8 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3198": {
    "sell_gold": 2100,
    "into_items": [
      
    ],
    "total_gold": 3000,
    "item_id": 3198,
    "from_items": [
      3197
    ],
    "name": "Perfect Hex Core",
    "base_gold": 1000,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3198.png",
    "description": "+6 Ability Power per level\n+60 Ability Power\n+500 Mana\n\nUNIQUE Passive - Glorious Evolution: Viktor has reached the pinnacle of his power, upgrading Chaos Storm in addition to his basic spells."
  },
  "2004": {
    "sell_gold": 14,
    "into_items": [
      
    ],
    "total_gold": 35,
    "item_id": 2004,
    "from_items": [
      
    ],
    "name": "Mana Potion",
    "base_gold": 35,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2004.png",
    "description": "Limited to 5 at one time.\n\nClick to Consume: Restores 100 Mana over 15 seconds."
  },
  "3077": {
    "sell_gold": 1330,
    "into_items": [
      3074
    ],
    "total_gold": 1900,
    "item_id": 3077,
    "from_items": [
      1036,
      1006,
      1037
    ],
    "name": "Tiamat (Melee Only)",
    "base_gold": 305,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3077.png",
    "description": "+40 Attack Damage\n+100% Base Health Regen \n\nUNIQUE Passive - Cleave: Basic attacks deal 20% to 60% of total Attack Damage as bonus physical damage to enemies near the target on hit (enemies closest to the target take the most damage).\nUNIQUE Active - Crescent: Deals 60% to 100% of total Attack Damage as physical damage to nearby enemy units (closest enemies take the most damage) (10 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "3043": {
    "sell_gold": 3080,
    "into_items": [
      
    ],
    "total_gold": 2200,
    "item_id": 3043,
    "from_items": [
      3008
    ],
    "name": "Muramana",
    "base_gold": 2200,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3043.png",
    "description": "+25 Attack Damage\n+1000 Mana\n+25% Base Mana Regen \n\nUNIQUE Passive - Awe: Grants bonus Attack Damage equal to 2% of maximum Mana.\nUNIQUE Toggle: Single target spells and attacks (on hit) consume 3% of current Mana to deal bonus physical damage equal to twice the amount of Mana consumed.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3725": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3725,
    "from_items": [
      1028,
      3713,
      3067
    ],
    "name": "Enchantment: Juggernaut",
    "base_gold": 150,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3725.png",
    "description": "+500 Health\n+10% Cooldown Reduction\n\nUNIQUE Passive - Tenacity: Reduces the duration of stuns, slows, taunts, fears, silences, blinds, polymorphs, and immobilizes by 35%.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3340": {
    "sell_gold": 0,
    "into_items": [
      3361,
      3362
    ],
    "total_gold": 0,
    "item_id": 3340,
    "from_items": [
      
    ],
    "name": "Warding Totem (Trinket)",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3340.png",
    "description": "Limited to 1 Trinket.\n\nActive: Places a Stealth Ward that lasts 60 seconds (120 second cooldown).\n\nAt level 9, this ward's duration increases to 120 seconds.\n\nLimit 3 Stealth Wards on the map per player.\n\n(Trinkets cannot be used in the first 30 seconds of a game. Selling a Trinket will disable Trinket use for 120 seconds)."
  },
  "3341": {
    "sell_gold": 0,
    "into_items": [
      3364
    ],
    "total_gold": 0,
    "item_id": 3341,
    "from_items": [
      
    ],
    "name": "Sweeping Lens (Trinket)",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3341.png",
    "description": "Limited to 1 Trinket.\n\nActive: Reveals and disables nearby invisible traps and invisible wards for 6 seconds in a small radius (120 second cooldown).\n\nAt level 9, cast range and sweep radius increase by 50% each and the cooldown is reduced to 60 seconds.\n\n(Trinkets cannot be used in the first 30 seconds of a game. Selling a Trinket will disable Trinket use for 120 seconds)."
  },
  "3342": {
    "sell_gold": 0,
    "into_items": [
      3363
    ],
    "total_gold": 0,
    "item_id": 3342,
    "from_items": [
      
    ],
    "name": "Scrying Orb (Trinket)",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3342.png",
    "description": "Limited to 1 Trinket.\n\nActive: Reveals a small location within 2500 range for 2 seconds. Enemy champions found will be revealed for 5 seconds (120 second cooldown).\n\nAt level 9, cast range increases to 3500.\n\n(Trinkets cannot be used in the first 30 seconds of a game. Selling a Trinket will disable Trinket use for 120 seconds)."
  },
  "3345": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3345,
    "from_items": [
      
    ],
    "name": "Soul Anchor (Trinket)",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3345.png",
    "description": "Limited to 1 Trinket.\n\nActive: Consumes a charge to instantly revive at your Summoner Platform and grants 125% Movement Speed that decays over 12 seconds.\n\nAdditional charges are gained at levels 9 and 14.\n\n(Max: 2 charges)\n\n"
  },
  "3361": {
    "sell_gold": 175,
    "into_items": [
      
    ],
    "total_gold": 250,
    "item_id": 3361,
    "from_items": [
      3340
    ],
    "name": "Greater Stealth Totem (Trinket)",
    "base_gold": 250,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3361.png",
    "description": "Limited to 1 Trinket. *Level 9+ required to upgrade.\n\nUNIQUE Active: Places an invisible ward that reveals the surrounding area for 180 seconds (60 second cooldown). Limit 3 Stealth Wards on the map per player.\n\n(Trinkets cannot be used in the first 30 seconds of a game. Selling a Trinket will disable Trinket use for 120 seconds)."
  },
  "3362": {
    "sell_gold": 175,
    "into_items": [
      
    ],
    "total_gold": 250,
    "item_id": 3362,
    "from_items": [
      3340
    ],
    "name": "Greater Vision Totem (Trinket)",
    "base_gold": 250,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3362.png",
    "description": "Limited to 1 Trinket. *Level 9+ required to upgrade.\n\nUNIQUE Active: Places a visible ward that reveals the surrounding area and invisible units in the area until killed (120 second cooldown). Limit 1 Vision Ward on the map per player.\n\n(Trinkets cannot be used in the first 30 seconds of a game. Selling a Trinket will disable Trinket use for 120 seconds)."
  },
  "3363": {
    "sell_gold": 175,
    "into_items": [
      
    ],
    "total_gold": 250,
    "item_id": 3363,
    "from_items": [
      3342
    ],
    "name": "Farsight Orb (Trinket)",
    "base_gold": 250,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3363.png",
    "description": "Limited to 1 Trinket. *Level 9+ required to upgrade.\n\nUNIQUE Active: Reveals an area up to 4000 units away for 2 seconds. Enemy champions found will be revealed for 5 seconds (90 second cooldown).\n\n(Trinkets cannot be used in the first 30 seconds of a game. Selling a Trinket will disable Trinket use for 120 seconds)."
  },
  "3364": {
    "sell_gold": 333,
    "into_items": [
      
    ],
    "total_gold": 475,
    "item_id": 3364,
    "from_items": [
      3341
    ],
    "name": "Oracle's Lens (Trinket)",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3364.png",
    "description": "Limited to 1 Trinket. *Level 9+ required to upgrade.\n\nUNIQUE Active: Reveals and disables nearby invisible traps and invisible wards for 6 seconds in a medium radius and grants detection of nearby invisible units for 10 seconds (75 second cooldown).\n\n(Trinkets cannot be used in the first 30 seconds of a game. Selling a Trinket will disable Trinket use for 120 seconds)."
  },
  "3719": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3719,
    "from_items": [
      3134,
      3711
    ],
    "name": "Enchantment: Warrior",
    "base_gold": 63,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3719.png",
    "description": "+45 Attack Damage\n+10% Cooldown Reduction\n+10 Armor Penetration"
  },
  "3122": {
    "sell_gold": 840,
    "into_items": [
      3104,
      3185
    ],
    "total_gold": 1200,
    "item_id": 3122,
    "from_items": [
      1036,
      1051
    ],
    "name": "Wicked Hatchet",
    "base_gold": 440,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3122.png",
    "description": "+20 Attack Damage\n+10% Critical Strike Chance\n\nUNIQUE Passive: Critical Strikes cause your target to bleed for an additional 60% of your bonus Attack Damage as physical damage over 3 seconds."
  },
  "1076": {
    "sell_gold": 160,
    "into_items": [
      
    ],
    "total_gold": 400,
    "item_id": 1076,
    "from_items": [
      
    ],
    "name": "Doran's Ring (Showdown)",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1076.png",
    "description": "+60 Health\n+15 Ability Power\n+3 Mana Regen per 5 seconds\n\nPassive: Restores 4 Mana upon killing a unit.\n\nLimited to 2 Doran's items on Showdown\n\n"
  },
  "3187": {
    "sell_gold": 1491,
    "into_items": [
      
    ],
    "total_gold": 2130,
    "item_id": 3187,
    "from_items": [
      3024,
      3067
    ],
    "name": "Hextech Sweeper",
    "base_gold": 330,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3187.png",
    "description": "+225 Health\n+250 Mana\n+25 Armor\n+20% Cooldown Reduction\n\nUNIQUE Passive - Trap Detection: Nearby stealthed enemy traps are revealed.\nUNIQUE Active - Hunter's Sight: A stealth-detecting mist grants vision in the target area for 5 seconds, revealing enemy champions that enter for 3 seconds (60 second cooldown)."
  },
  "2047": {
    "sell_gold": 100,
    "into_items": [
      
    ],
    "total_gold": 250,
    "item_id": 2047,
    "from_items": [
      
    ],
    "name": "Oracle's Extract",
    "base_gold": 250,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2047.png",
    "description": "Click to Consume: Grants detection of nearby invisible units for up to 5 minutes or until death."
  },
  "3401": {
    "sell_gold": 880,
    "into_items": [
      
    ],
    "total_gold": 2200,
    "item_id": 3401,
    "from_items": [
      3067,
      3097
    ],
    "name": "Face of the Mountain",
    "base_gold": 485,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3401.png",
    "description": "+500 Health\n+100% Base Health Regen \n+10% Cooldown Reduction\n\nUNIQUE Passive - Spoils of War: Melee basic attacks execute minions below 400 Health. Killing a minion heals the owner and the nearest allied champion for 50 (+1% of your maximum Health) and grants them kill Gold.\n\nThese effects require a nearby allied champion. Recharges every 30 seconds. Max 4 charges.\nUNIQUE Active: Shield target ally for 10% of your maximum Health for 4 seconds. After 4 seconds, the target explodes dealing 100% of their total Attack Damage plus 30% of their Ability Power as magic damage in an area (60 second cooldown).\n\nLimited to 1 Gold Income item"
  },
  "3405": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3405,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3405.png",
    "description": "UNIQUE Active - Sweeping Lens: Reveals and disables nearby invisible traps and invisible wards for 4 seconds in a small radius (120 second cooldown). Active upgrades at 6 Trophies.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3406": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3406,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3406.png",
    "description": "UNIQUE Active - Sweeping Lens: Reveals and disables nearby invisible traps and invisible wards for 4 seconds in a small radius (120 second cooldown). Active upgrades at 6 Trophies.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3407": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3407,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3407.png",
    "description": "UNIQUE Active - Sweeping Lens: Reveals and disables nearby invisible traps and invisible wards for 6 seconds in a medium radius (60 second cooldown). Active upgrades at 20 Trophies.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3408": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3408,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3408.png",
    "description": "UNIQUE Active - Sweeping Lens: Reveals and disables nearby invisible traps and invisible wards for 6 seconds in a medium radius (60 second cooldown). Active upgrades at 20 Trophies.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3409": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3409,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3409.png",
    "description": "UNIQUE Active - Sweeping Lens: Reveals and disables nearby invisible traps and invisible wards for 6 seconds in a medium radius and grants detection of invisible units for 10 seconds (75 second cooldown).\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3410": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3410,
    "from_items": [
      3169
    ],
    "name": "Head of Kha'Zix",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3410.png",
    "description": "UNIQUE Active - Sweeping Lens: Reveals and disables nearby invisible traps and invisible wards for 6 seconds in a medium radius and grants detection of invisible units for 10 seconds (60 second cooldown).\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3411": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3411,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3411.png",
    "description": "UNIQUE Active - Scrying: Reveals a small location within 2500 range for 2 seconds. Enemy champions found will be revealed for 5 seconds (120 second cooldown). Active upgrades at 6 Trophies.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3412": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3412,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3412.png",
    "description": "UNIQUE Active - Scrying: Reveals a small location within 2500 range for 2 seconds. Enemy champions found will be revealed for 5 seconds (120 second cooldown). Active upgrades at 6 Trophies.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3413": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3413,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3413.png",
    "description": "UNIQUE Active - Scrying: Reveals a small location within 3500 range for 2 seconds. Enemy champions found will be revealed for 5 seconds (120 second cooldown). Active upgrades at 20 Trophies.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3414": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3414,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3414.png",
    "description": "UNIQUE Active - Scrying: Reveals a small location within 3500 range for 2 seconds. Enemy champions found will be revealed for 5 seconds (120 second cooldown). Active upgrades at 20 Trophies.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3415": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3415,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3415.png",
    "description": "UNIQUE Active - Scrying: Reveals a small location within 4000 range for 2 seconds. Enemy champions found will be revealed for 5 seconds (90 second cooldown).\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3416": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3416,
    "from_items": [
      3169
    ],
    "name": "Head of Kha'Zix",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3416.png",
    "description": "UNIQUE Active - Scrying: Reveals a small location within 4000 range for 2 seconds. Enemy champions found will be revealed for 5 seconds (90 second cooldown).\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3417": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3417,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3417.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3418": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3418,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3418.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3419": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3419,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3419.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3420": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3420,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3420.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3421": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3421,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3421.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3422": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3422,
    "from_items": [
      3169
    ],
    "name": "Head of Kha'Zix",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3422.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3048": {
    "sell_gold": 3780,
    "into_items": [
      
    ],
    "total_gold": 2700,
    "item_id": 3048,
    "from_items": [
      3007
    ],
    "name": "Seraph's Embrace",
    "base_gold": 2700,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3048.png",
    "description": "+60 Ability Power\n+1000 Mana\n+50% Base Mana Regen \n\nUNIQUE Passive - Insight: Grants Ability Power equal to 3% of maximum Mana.\nUNIQUE Active - Mana Shield: Consumes 20% of current Mana to grant a shield for 3 seconds that absorbs damage equal to 150 plus the amount of Mana consumed (120 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "2041": {
    "sell_gold": 138,
    "into_items": [
      
    ],
    "total_gold": 345,
    "item_id": 2041,
    "from_items": [
      
    ],
    "name": "Crystalline Flask",
    "base_gold": 345,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2041.png",
    "description": "UNIQUE Passive: Holds 3 charges and refills upon visiting the shop.\nUNIQUE Active: Consumes a charge to restore 120 Health and 60 Mana over 12 seconds."
  },
  "3450": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3450,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3450.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\nActive: Consumes a charge to instantly revive at the Summoner Platform and grants 125% Movement Speed that decays over 12 seconds.\n\nAdditional charges are gained at levels 9 and 14.\n\n(Max: 2 charges)\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3451": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3451,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3451.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3452": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3452,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3452.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3453": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3453,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3453.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3454": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3454,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3454.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3455": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3455,
    "from_items": [
      3169
    ],
    "name": "Head of Kha'Zix",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3455.png",
    "description": "UNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "3460": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3460,
    "from_items": [
      
    ],
    "name": "Golden Transcendence",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3460.png",
    "description": "Active: Use this trinket to teleport to one of the battle platforms. Can only be used from the summoning platform.\n\n''It is at this magical precipice where a champion is dismantled, reforged, and empowered.''"
  },
  "1036": {
    "sell_gold": 252,
    "into_items": [
      1053,
      3044,
      3134,
      3155,
      3077,
      3035,
      3154,
      3144,
      3122,
      3141,
      3159
    ],
    "total_gold": 360,
    "item_id": 1036,
    "from_items": [
      
    ],
    "name": "Long Sword",
    "base_gold": 360,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1036.png",
    "description": "+10 Attack Damage"
  },
  "3157": {
    "sell_gold": 2310,
    "into_items": [
      
    ],
    "total_gold": 3300,
    "item_id": 3157,
    "from_items": [
      3191,
      1058
    ],
    "name": "Zhonya's Hourglass",
    "base_gold": 500,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3157.png",
    "description": "+120 Ability Power\n+50 Armor  \n\nUNIQUE Active - Stasis: Champion becomes invulnerable and untargetable for 2.5 seconds, but is unable to move, attack, cast spells, or use items during this time (90 second cooldown)."
  },
  "1027": {
    "sell_gold": 280,
    "into_items": [
      3057,
      3070,
      3073,
      3010,
      3024
    ],
    "total_gold": 400,
    "item_id": 1027,
    "from_items": [
      
    ],
    "name": "Sapphire Crystal",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1027.png",
    "description": "+200 Mana"
  },
  "3253": {
    "sell_gold": 1033,
    "into_items": [
      
    ],
    "total_gold": 1475,
    "item_id": 3253,
    "from_items": [
      3006
    ],
    "name": "Enchantment: Distortion",
    "base_gold": 475,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3253.png",
    "description": "Limited to 1 of each enchantment type.\nEnchants boots to have Distortion bonus.\n\nUNIQUE Passive - Distortion: Teleport, Flash, and Ghost summoner spell cooldowns are reduced by 20% and are granted additional mobility: \n\nGhost: Grants 40% Movement Speed from 27%.\nFlash: 20% Movement Speed bonus for 1 second after cast.\nTeleport: 30% Movement Speed bonus for 3 seconds after use.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3168": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 3168,
    "from_items": [
      
    ],
    "name": "Bonetooth Necklace",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3168.png",
    "description": "UNIQUE Active - Bonetooth Totem: Places a Stealth Ward that lasts 120 seconds (120 Second cooldown). Active upgrades at 20 Trophies.\n\nUNIQUE Passive - Mementos of the Hunt: Rengar collects trophies when killing Champions and gains bonus effects based on how many trophies he has. Kills and assists grant 1 trophy.\n\n3 Trophies: Rengar gains 25 Movement Speed whilst out of combat or in brush. \n6 Trophies: Increases the range of Rengar's Leap by 125.\n12 Trophies: Thrill of the Hunt's duration is increased by 5 seconds.\n20 Trophies: Thrill of the Hunt's Movement Speed while stealthed is doubled."
  },
  "1037": {
    "sell_gold": 613,
    "into_items": [
      3035,
      3124,
      3031,
      3156,
      3077,
      3104,
      3184,
      3004,
      3008,
      3022,
      3172,
      3181
    ],
    "total_gold": 875,
    "item_id": 1037,
    "from_items": [
      
    ],
    "name": "Pickaxe",
    "base_gold": 875,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1037.png",
    "description": "+25 Attack Damage"
  },
  "1029": {
    "sell_gold": 210,
    "into_items": [
      3047,
      1031,
      3191,
      3024,
      3082,
      3159,
      2053,
      3075
    ],
    "total_gold": 300,
    "item_id": 1029,
    "from_items": [
      
    ],
    "name": "Cloth Armor",
    "base_gold": 300,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1029.png",
    "description": "+15 Armor"
  },
  "3504": {
    "sell_gold": 1470,
    "into_items": [
      
    ],
    "total_gold": 2100,
    "item_id": 3504,
    "from_items": [
      3113,
      3114
    ],
    "name": "Ardent Censer",
    "base_gold": 650,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3504.png",
    "description": "+40 Ability Power\n+10% Cooldown Reduction\n+100% Base Mana Regen \n\nUNIQUE Passive: +8% Movement Speed\nUNIQUE Passive: Your heals and shields on another unit grant them 25% Attack Speed for 6 seconds.\n\n(This does not include regeneration effects or effects on yourself.)"
  },
  "3508": {
    "sell_gold": 2240,
    "into_items": [
      
    ],
    "total_gold": 3200,
    "item_id": 3508,
    "from_items": [
      1038,
      1053
    ],
    "name": "Essence Reaver",
    "base_gold": 850,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3508.png",
    "description": "+80 Attack Damage\n+10% Life Steal\n+10% Cooldown Reduction\n\nUNIQUE Passive: Restores 2% to 8% of the damage dealt by basic attacks as Mana. This effect increases based on missing Mana."
  },
  "3714": {
    "sell_gold": 1575,
    "into_items": [
      
    ],
    "total_gold": 2250,
    "item_id": 3714,
    "from_items": [
      3134,
      3715
    ],
    "name": "Enchantment: Warrior",
    "base_gold": 63,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3714.png",
    "description": "+45 Attack Damage\n+10% Cooldown Reduction\n+10 Armor Penetration"
  },
  "3512": {
    "sell_gold": 1960,
    "into_items": [
      
    ],
    "total_gold": 2800,
    "item_id": 3512,
    "from_items": [
      2053,
      1057
    ],
    "name": "Zz'Rot Portal",
    "base_gold": 950,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3512.png",
    "description": "+50 Armor\n+50 Magic Resist\n+100% Base Health Regen \n\nUNIQUE Passive - Point Runner: Builds up to +30% Movement Speed over 2 seconds while near turrets or Void Gates.\n\nUNIQUE Active: Spawns a Void Gate at target location for 150 seconds. Every 4 seconds the gate makes a Voidspawn that travels down the nearest lane. Voidspawn explodes when attacking structures. Voidspawn ignore champions and void targets (150 second cooldown).\n\nThe first and every fourth Voidspawn gain 100% of Armor and Magic Resistance as damage."
  },
  "3001": {
    "sell_gold": 1708,
    "into_items": [
      
    ],
    "total_gold": 2440,
    "item_id": 3001,
    "from_items": [
      1057,
      1026
    ],
    "name": "Abyssal Scepter",
    "base_gold": 730,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3001.png",
    "description": "+70 Ability Power\n+50 Magic Resist\n\nUNIQUE Aura: Reduces the Magic Resist of nearby enemies by 20."
  },
  "3003": {
    "sell_gold": 1890,
    "into_items": [
      3040
    ],
    "total_gold": 2700,
    "item_id": 3003,
    "from_items": [
      1026,
      3070
    ],
    "name": "Archangel's Staff",
    "base_gold": 1120,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3003.png",
    "description": "+60 Ability Power\n+250 Mana\n+50% Base Mana Regen \n\nUNIQUE Passive - Insight: Grants Ability Power equal to 3% of maximum Mana.\nUNIQUE Passive - Mana Charge: Grants +8 maximum Mana (max +750 Mana) for each spell cast and Mana expenditure (occurs up to 2 times every 8 seconds). Transforms into Seraph's Embrace at +750 Mana.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3004": {
    "sell_gold": 1540,
    "into_items": [
      3042
    ],
    "total_gold": 2200,
    "item_id": 3004,
    "from_items": [
      1037,
      3070
    ],
    "name": "Manamune",
    "base_gold": 605,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3004.png",
    "description": "+25 Attack Damage\n+250 Mana\n+25% Base Mana Regen \n\nUNIQUE Passive - Awe: Grants bonus Attack Damage equal to 2% of maximum Mana.\nUNIQUE Passive - Mana Charge: Grants +4 maximum Mana (max +750 Mana) for each basic attack, spell cast, and Mana expenditure (occurs up to 2 times every 8 seconds).\n\nTransforms into Muramana at +750 Mana.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3006": {
    "sell_gold": 700,
    "into_items": [
      3254,
      3253,
      3252,
      3251,
      3250
    ],
    "total_gold": 1000,
    "item_id": 3006,
    "from_items": [
      1001,
      1042
    ],
    "name": "Berserker's Greaves",
    "base_gold": 225,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3006.png",
    "description": " +25% Attack Speed\n\nUNIQUE Passive - Enhanced Movement: +45 Movement Speed\n\n(Unique Passives with the same name don't stack.)"
  },
  "3007": {
    "sell_gold": 1890,
    "into_items": [
      3048
    ],
    "total_gold": 2700,
    "item_id": 3007,
    "from_items": [
      1026,
      3073
    ],
    "name": "Archangel's Staff (Crystal Scar)",
    "base_gold": 1120,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3007.png",
    "description": "+60 Ability Power\n+250 Mana\n+50% Base Mana Regen \n\nUNIQUE Passive - Insight: Grants Ability Power equal to 3% of maximum Mana.\nUNIQUE Passive - Mana Charge: Grants +10 maximum Mana (max +750 Mana) for each spell cast and Mana expenditure (occurs up to 2 times every 6 seconds). Transforms into Seraph's Embrace at +750 Mana.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3008": {
    "sell_gold": 1540,
    "into_items": [
      3043
    ],
    "total_gold": 2200,
    "item_id": 3008,
    "from_items": [
      1037,
      3073
    ],
    "name": "Manamune (Crystal Scar)",
    "base_gold": 605,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3008.png",
    "description": "+25 Attack Damage\n+250 Mana\n+25% Base Mana Regen \n\nUNIQUE Passive - Awe: Grants bonus Attack Damage equal to 2% of maximum Mana.\nUNIQUE Passive - Mana Charge: Grants +8 maximum Mana (max +750 Mana) for each basic attack, spell cast, and Mana expenditure (occurs up to 2 times every 6 seconds).\n\nTransforms into Muramana at +750 Mana.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3009": {
    "sell_gold": 700,
    "into_items": [
      3284,
      3283,
      3282,
      3281,
      3280
    ],
    "total_gold": 1000,
    "item_id": 3009,
    "from_items": [
      1001
    ],
    "name": "Boots of Swiftness",
    "base_gold": 675,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3009.png",
    "description": "UNIQUE Passive - Enhanced Movement: +60 Movement Speed\nUNIQUE Passive - Slow Resist: Movement slowing effects are reduced by 25%.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3010": {
    "sell_gold": 840,
    "into_items": [
      3027,
      3029,
      3180,
      3800
    ],
    "total_gold": 1200,
    "item_id": 3010,
    "from_items": [
      1028,
      1027
    ],
    "name": "Catalyst the Protector",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3010.png",
    "description": "+200 Health\n+300 Mana\n\nUNIQUE Passive - Valor's Reward: Upon leveling up, restores 150 Health and 200 Mana over 8 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3020": {
    "sell_gold": 770,
    "into_items": [
      3259,
      3258,
      3257,
      3256,
      3255
    ],
    "total_gold": 1100,
    "item_id": 3020,
    "from_items": [
      1001
    ],
    "name": "Sorcerer's Shoes",
    "base_gold": 775,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3020.png",
    "description": "+15 Magic Penetration\n\nUNIQUE Passive - Enhanced Movement: +45 Movement Speed\n\n(Magic Penetration: Magic damage is increased by ignoring an amount of the target's Magic Resist equal to Magic Penetration.)\n\n(Unique Passives with the same name don't stack.)"
  },
  "3022": {
    "sell_gold": 2310,
    "into_items": [
      
    ],
    "total_gold": 3300,
    "item_id": 3022,
    "from_items": [
      1028,
      1011,
      1037
    ],
    "name": "Frozen Mallet",
    "base_gold": 1025,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3022.png",
    "description": "+700 Health\n+30 Attack Damage\n\nUNIQUE Passive - Icy: Basic attacks slow the target's Movement Speed for 1.5 seconds on hit (40% slow for melee attacks, 30% slow for ranged attacks).\n\n(Unique Passives with the same name don't stack.)"
  },
  "3023": {
    "sell_gold": 1680,
    "into_items": [
      
    ],
    "total_gold": 2400,
    "item_id": 3023,
    "from_items": [
      3108,
      3113
    ],
    "name": "Twin Shadows",
    "base_gold": 730,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3023.png",
    "description": "+80 Ability Power\n+10% Cooldown Reduction\n+6% Movement Speed\n\nUNIQUE Active - Hunt: Summons up to 2 invulnerable ghosts that seek out the 2 nearest enemy champions for 6 seconds. If a ghost reaches its target, it reveals the target and reduces their Movement Speed by 40% for 2.5 seconds.\n\nIf a ghost cannot find a target, it tries to return to the caster. Ghosts that successfully return in this way reduce the item's cooldown by 40 seconds (120 second cooldown)."
  },
  "3024": {
    "sell_gold": 665,
    "into_items": [
      3110,
      3025,
      3187
    ],
    "total_gold": 950,
    "item_id": 3024,
    "from_items": [
      1027,
      1029
    ],
    "name": "Glacial Shroud",
    "base_gold": 250,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3024.png",
    "description": "+20 Armor\n+250 Mana\n\nUNIQUE Passive: +10% Cooldown Reduction"
  },
  "3025": {
    "sell_gold": 2030,
    "into_items": [
      
    ],
    "total_gold": 2900,
    "item_id": 3025,
    "from_items": [
      3024,
      3057
    ],
    "name": "Iceborn Gauntlet",
    "base_gold": 750,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3025.png",
    "description": "+60 Armor\n+30 Ability Power\n+10% Cooldown Reduction\n+500 Mana\n\nUNIQUE Passive - Spellblade: After using an ability, the next basic attack (on hit) deals bonus physical damage equal to 125% of base Attack Damage to enemies near the target, and creates a field around the target for 2 seconds that slows enemy Movement Speed by 30% (1.5 second cooldown, half-sized field if ranged).\n\n(Unique Passives with the same name don't stack.)"
  },
  "3026": {
    "sell_gold": 1120,
    "into_items": [
      
    ],
    "total_gold": 2800,
    "item_id": 3026,
    "from_items": [
      1057,
      1031
    ],
    "name": "Guardian Angel",
    "base_gold": 1200,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3026.png",
    "description": "+50 Armor\n+50 Magic Resist\n\nUNIQUE Passive: Upon taking lethal damage, restores 30% of maximum Health and Mana after 4 seconds of stasis (300 second cooldown)."
  },
  "2003": {
    "sell_gold": 14,
    "into_items": [
      
    ],
    "total_gold": 35,
    "item_id": 2003,
    "from_items": [
      
    ],
    "name": "Health Potion",
    "base_gold": 35,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2003.png",
    "description": "Limited to 5 at one time.\n\nClick to Consume: Restores 150 Health over 15 seconds."
  },
  "3028": {
    "sell_gold": 700,
    "into_items": [
      3174,
      3222
    ],
    "total_gold": 1000,
    "item_id": 3028,
    "from_items": [
      1004,
      1033
    ],
    "name": "Chalice of Harmony",
    "base_gold": 140,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3028.png",
    "description": "+25 Magic Resist\n+50% Base Mana Regen \n\nUNIQUE Passive - Mana Font: Restores 2% of missing Mana every 5 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3029": {
    "sell_gold": 1960,
    "into_items": [
      
    ],
    "total_gold": 2800,
    "item_id": 3029,
    "from_items": [
      3010,
      1026
    ],
    "name": "Rod of Ages (Crystal Scar)",
    "base_gold": 740,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3029.png",
    "description": "+450 Health\n+450 Mana\n+60 Ability Power\n\nPassive: Grants +20 Health, +20 Mana, and +2 Ability Power per stack (max +200 Health, +200 Mana, and +20 Ability Power). Grants 1 stack per 40 seconds (max 10 stacks).\nUNIQUE Passive - Valor's Reward: Upon leveling up, restores 150 Health and 200 Mana over 8 seconds.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3031": {
    "sell_gold": 2660,
    "into_items": [
      
    ],
    "total_gold": 3800,
    "item_id": 3031,
    "from_items": [
      1018,
      1037,
      1038
    ],
    "name": "Infinity Edge",
    "base_gold": 645,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3031.png",
    "description": "+80 Attack Damage\n+20% Critical Strike Chance\n\nUNIQUE Passive: Critical strikes deal 250% damage instead of 200%."
  },
  "2009": {
    "sell_gold": 0,
    "into_items": [
      
    ],
    "total_gold": 0,
    "item_id": 2009,
    "from_items": [
      
    ],
    "name": "Total Biscuit of Rejuvenation",
    "base_gold": 0,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2009.png",
    "description": "Click to Consume: Restores 80 Health and 50 Mana over 10 seconds."
  },
  "2010": {
    "sell_gold": 14,
    "into_items": [
      
    ],
    "total_gold": 35,
    "item_id": 2010,
    "from_items": [
      
    ],
    "name": "Total Biscuit of Rejuvenation",
    "base_gold": 35,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2010.png",
    "description": "Click to Consume: Restores 20 health and 10 mana immediately and then 150 Health over 15 seconds."
  },
  "3035": {
    "sell_gold": 1610,
    "into_items": [
      
    ],
    "total_gold": 2300,
    "item_id": 3035,
    "from_items": [
      1036,
      1037
    ],
    "name": "Last Whisper",
    "base_gold": 1065,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3035.png",
    "description": "+40 Attack Damage\n\nUNIQUE Passive: Physical damage ignores 35% of the target's Armor (applies before Armor Penetration)."
  },
  "3040": {
    "sell_gold": 3780,
    "into_items": [
      
    ],
    "total_gold": 2700,
    "item_id": 3040,
    "from_items": [
      3003
    ],
    "name": "Seraph's Embrace",
    "base_gold": 2700,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3040.png",
    "description": "+60 Ability Power\n+1000 Mana\n+50% Base Mana Regen \n\nUNIQUE Passive - Insight: Grants Ability Power equal to 3% of maximum Mana.\nUNIQUE Active - Mana Shield: Consumes 20% of current Mana to grant a shield for 3 seconds that absorbs damage equal to 150 plus the amount of Mana consumed (120 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "3041": {
    "sell_gold": 980,
    "into_items": [
      
    ],
    "total_gold": 1400,
    "item_id": 3041,
    "from_items": [
      1052
    ],
    "name": "Mejai's Soulstealer",
    "base_gold": 965,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3041.png",
    "description": "+20 Ability Power  \n\nUNIQUE Passive: Grants +8 Ability Power per stack and 5 stacks upon first purchase. Grants 2 stacks for a kill or 1 stack for an assist (max 20 stacks). Half of the stacks are lost upon death. At 20 stacks, grants +15% Cooldown Reduction."
  },
  "3042": {
    "sell_gold": 3080,
    "into_items": [
      
    ],
    "total_gold": 2200,
    "item_id": 3042,
    "from_items": [
      3004
    ],
    "name": "Muramana",
    "base_gold": 2200,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3042.png",
    "description": "+25 Attack Damage\n+1000 Mana\n+25% Base Mana Regen \n\nUNIQUE Passive - Awe: Grants bonus Attack Damage equal to 2% of maximum Mana.\nUNIQUE Toggle: Single target spells and attacks (on hit) consume 3% of current Mana to deal bonus physical damage equal to twice the amount of Mana consumed.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3067": {
    "sell_gold": 595,
    "into_items": [
      3187,
      3401,
      3065,
      3190,
      3050,
      3056,
      3709,
      3717,
      3721,
      3725
    ],
    "total_gold": 850,
    "item_id": 3067,
    "from_items": [
      1028
    ],
    "name": "Kindlegem",
    "base_gold": 450,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3067.png",
    "description": "+200 Health  \n\nUNIQUE Passive: +10% Cooldown Reduction"
  },
  "3044": {
    "sell_gold": 927,
    "into_items": [
      3078,
      3184
    ],
    "total_gold": 1325,
    "item_id": 3044,
    "from_items": [
      1036,
      1028
    ],
    "name": "Phage",
    "base_gold": 565,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3044.png",
    "description": "+200 Health\n+20 Attack Damage\n\nUNIQUE Passive - Rage: Basic attacks grant 20 Movement Speed for 2 seconds. Kills grant 60 Movement Speed instead. This Movement Speed bonus is halved for ranged champions.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3046": {
    "sell_gold": 1960,
    "into_items": [
      
    ],
    "total_gold": 2800,
    "item_id": 3046,
    "from_items": [
      1018,
      1042,
      3086
    ],
    "name": "Phantom Dancer",
    "base_gold": 520,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3046.png",
    "description": "+50% Attack Speed\n+35% Critical Strike Chance\n+5% Movement Speed\n\nUNIQUE Passive: Champion can move through units."
  },
  "3047": {
    "sell_gold": 700,
    "into_items": [
      3264,
      3263,
      3262,
      3261,
      3260
    ],
    "total_gold": 1000,
    "item_id": 3047,
    "from_items": [
      1029,
      1001
    ],
    "name": "Ninja Tabi",
    "base_gold": 375,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3047.png",
    "description": "+25 Armor\n\nUNIQUE Passive: Blocks 10% of the damage from basic attacks.\nUNIQUE Passive - Enhanced Movement: +45 Movement Speed\n\n(Unique Passives with the same name don't stack.)"
  },
  "1039": {
    "sell_gold": 280,
    "into_items": [
      3706,
      3711,
      3715,
      3713
    ],
    "total_gold": 400,
    "item_id": 1039,
    "from_items": [
      
    ],
    "name": "Hunter's Machete",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1039.png",
    "description": "+15 Bonus Gold per Large Monster Kill\nPassive - Jungler:  Deal 30 magic damage on hit to monsters over 2 seconds and gain 7 Health and 3 Mana per second while in combat with monsters.\n\nLimited to 1 Jungle item"
  },
  "1001": {
    "sell_gold": 227,
    "into_items": [
      3006,
      3047,
      3020,
      3158,
      3111,
      3117,
      3009
    ],
    "total_gold": 325,
    "item_id": 1001,
    "from_items": [
      
    ],
    "name": "Boots of Speed",
    "base_gold": 325,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1001.png",
    "description": "Limited to 1.\n\nUNIQUE Passive - Enhanced Movement: +25 Movement Speed\n\n(Unique Passives with the same name don't stack.)"
  },
  "3050": {
    "sell_gold": 1715,
    "into_items": [
      
    ],
    "total_gold": 2450,
    "item_id": 3050,
    "from_items": [
      3067,
      1053
    ],
    "name": "Zeke's Herald",
    "base_gold": 800,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3050.png",
    "description": "+250 Health\n+20% Cooldown Reduction\n\nUNIQUE Aura: Grants allied champions +10% Life Steal and +20 Attack Damage."
  },
  "1004": {
    "sell_gold": 126,
    "into_items": [
      3028,
      3070,
      3073,
      3114
    ],
    "total_gold": 180,
    "item_id": 1004,
    "from_items": [
      
    ],
    "name": "Faerie Charm",
    "base_gold": 180,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1004.png",
    "description": "+25% Base Mana Regen "
  },
  "3068": {
    "sell_gold": 1820,
    "into_items": [
      
    ],
    "total_gold": 2600,
    "item_id": 3068,
    "from_items": [
      1031,
      1011
    ],
    "name": "Sunfire Cape",
    "base_gold": 850,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3068.png",
    "description": "+450 Health\n+45 Armor  \n\nUNIQUE Passive: Deals 25 (+1 per champion level) magic damage per second to nearby enemies."
  },
  "1006": {
    "sell_gold": 126,
    "into_items": [
      3077,
      3112,
      2051,
      2053,
      3105,
      3801
    ],
    "total_gold": 180,
    "item_id": 1006,
    "from_items": [
      
    ],
    "name": "Rejuvenation Bead",
    "base_gold": 180,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1006.png",
    "description": "+50% Base Health Regen "
  },
  "2045": {
    "sell_gold": 640,
    "into_items": [
      
    ],
    "total_gold": 1600,
    "item_id": 2045,
    "from_items": [
      1028,
      2049
    ],
    "name": "Ruby Sightstone",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2045.png",
    "description": "+400 Health\n\nUNIQUE Passive - Ward Refresh: Holds 5 charges and refills upon visiting the shop.\nUNIQUE Active - Ghost Ward: Consumes a charge to place a Stealth Ward that reveals the surrounding area for 3 minutes. A player may only have 3 Stealth Wards on the map at one time.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3056": {
    "sell_gold": 1820,
    "into_items": [
      
    ],
    "total_gold": 2600,
    "item_id": 3056,
    "from_items": [
      2053,
      1028,
      3067
    ],
    "name": "Ohmwrecker",
    "base_gold": 750,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3056.png",
    "description": "+300 Health\n+50 Armor\n+100% Base Health Regen \n+10% Cooldown Reduction\n\nUNIQUE Active: Prevents nearby enemy turrets from attacking for 3 seconds (120 second cooldown). This effect cannot be used against the same turret more than once every 8 seconds.\n\nUNIQUE Passive - Point Runner: Builds up to +30% Movement Speed over 2 seconds while near turrets.\n"
  },
  "3057": {
    "sell_gold": 840,
    "into_items": [
      3078,
      3100,
      3025
    ],
    "total_gold": 1200,
    "item_id": 3057,
    "from_items": [
      1027,
      1052
    ],
    "name": "Sheen",
    "base_gold": 365,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3057.png",
    "description": "+25 Ability Power\n+200 Mana\n\nUNIQUE Passive - Spellblade: After using an ability, the next basic attack deals bonus physical damage equal to 100% base Attack Damage on hit (1.5 second cooldown).\n\n(Unique Passives with the same name don't stack.)"
  },
  "1011": {
    "sell_gold": 700,
    "into_items": [
      3068,
      3143,
      3116,
      3083,
      3084,
      3022
    ],
    "total_gold": 1000,
    "item_id": 1011,
    "from_items": [
      1028
    ],
    "name": "Giant's Belt",
    "base_gold": 600,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1011.png",
    "description": "+380 Health"
  },
  "3060": {
    "sell_gold": 2100,
    "into_items": [
      
    ],
    "total_gold": 3000,
    "item_id": 3060,
    "from_items": [
      3108,
      3105
    ],
    "name": "Banner of Command",
    "base_gold": 280,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3060.png",
    "description": "+200 Health\n+60 Ability Power\n+20 Magic Resist\n+10% Cooldown Reduction\n\nUNIQUE Aura - Legion: Grants nearby allies +20 Magic Resist and +75% Base Health Regen.\nUNIQUE Active - Promote: Greatly increases the power of a lane minion and grants it immunity to magic damage (120 second cooldown).\n\n(Unique Auras with the same name do not stack.)"
  },
  "2049": {
    "sell_gold": 320,
    "into_items": [
      2045
    ],
    "total_gold": 800,
    "item_id": 2049,
    "from_items": [
      1028
    ],
    "name": "Sightstone",
    "base_gold": 400,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2049.png",
    "description": "+150 Health\n\nUNIQUE Passive - Ward Refresh: Holds 4 charges and refills upon visiting the shop.\nUNIQUE Active - Ghost Ward: Consumes a charge to place a Stealth Ward that reveals the surrounding area for 3 minutes. A player may only have 3 Stealth Wards on the map at one time.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3065": {
    "sell_gold": 1925,
    "into_items": [
      
    ],
    "total_gold": 2750,
    "item_id": 3065,
    "from_items": [
      3211,
      3067
    ],
    "name": "Spirit Visage",
    "base_gold": 700,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3065.png",
    "description": "+400 Health\n+55 Magic Resist\n+100% Base Health Regen \n+10% Cooldown Reduction\n\nUNIQUE Passive: Increases self-healing, Health Regen, Lifesteal, and Spell Vamp effects by 20%."
  },
  "1018": {
    "sell_gold": 511,
    "into_items": [
      3046,
      3031,
      3104,
      3185
    ],
    "total_gold": 730,
    "item_id": 1018,
    "from_items": [
      
    ],
    "name": "Cloak of Agility",
    "base_gold": 730,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/1018.png",
    "description": "+15% Critical Strike Chance"
  },
  "2043": {
    "sell_gold": 40,
    "into_items": [
      
    ],
    "total_gold": 100,
    "item_id": 2043,
    "from_items": [
      
    ],
    "name": "Vision Ward",
    "base_gold": 100,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2043.png",
    "description": "Can only carry 2 Vision Wards in inventory.\n\nClick to Consume: Places a visible ward that reveals the surrounding area and invisible units in the area until killed. Limit 1 Vision Ward on the map per player.\n\n(Revealing a ward in this manner grants a portion of the gold reward when that unit is killed.)"
  },
  "2044": {
    "sell_gold": 30,
    "into_items": [
      
    ],
    "total_gold": 75,
    "item_id": 2044,
    "from_items": [
      
    ],
    "name": "Stealth Ward",
    "base_gold": 75,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/2044.png",
    "description": "Can only carry 3 Stealth Wards in inventory.\n\nClick to Consume: Places an invisible ward that reveals the surrounding area for 3 minutes. Limit 3 Stealth Wards on the map per player."
  },
  "3069": {
    "sell_gold": 840,
    "into_items": [
      
    ],
    "total_gold": 2100,
    "item_id": 3069,
    "from_items": [
      3114,
      3096
    ],
    "name": "Talisman of Ascension",
    "base_gold": 635,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3069.png",
    "description": "+100% Base Health Regen \n+100% Base Mana Regen \n+20 Movement Speed\n+10% Cooldown Reduction\n+2 Gold per 10 seconds\n\nUNIQUE Passive - Favor: Being near a minion death without dealing the killing blow grants 3 Gold and 10 Health.\nUNIQUE Active: Grants nearby allies +40% Movement Speed for 3 seconds (60 second cooldown).\n\nLimited to 1 Gold Income item\n\n''Praise the sun.'' - Historian Shurelya, 22 September, 25 CLE\n\n"
  },
  "3070": {
    "sell_gold": 504,
    "into_items": [
      3003,
      3004
    ],
    "total_gold": 720,
    "item_id": 3070,
    "from_items": [
      1004,
      1027
    ],
    "name": "Tear of the Goddess",
    "base_gold": 140,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3070.png",
    "description": "+250 Mana\n+25% Base Mana Regen \n\nUNIQUE Passive - Mana Charge: Grants 4 maximum Mana on spell cast or Mana expenditure (up to 2 times per 8 seconds). Grants 1 maximum Mana every 8 seconds.\n\nCaps at +750 Mana.\n\n(Unique Passives with the same name don't stack.)"
  },
  "3071": {
    "sell_gold": 2100,
    "into_items": [
      
    ],
    "total_gold": 3000,
    "item_id": 3071,
    "from_items": [
      1028,
      3134
    ],
    "name": "The Black Cleaver",
    "base_gold": 1263,
    "image": "http:\/\/ddragon.leagueoflegends.com\/cdn\/5.2.1\/img\/item\/3071.png",
    "description": "+200 Health\n+50 Attack Damage\n+10% Cooldown Reduction\n\nUNIQUE Passive: +10 Armor Penetration\nPassive: Dealing physical damage to an enemy champion reduces their Armor by 5% for 4 seconds (stacks up to 5 times, up to 25%).\n\n(Armor Penetration: Physical damage is increased by ignoring an amount of the target's Armor equal to Armor Penetration.)"
  }
}
        for culture in expected_response:
            self.assertTrue(culture in response_data)

    def test_get_item(self) :
        self.maxDiff = None
        expected_response = {"sell_gold": 2450, "item_id": 3072, "name": "The Bloodthirster", "total_gold": 3500, "from_items": [1038, 1053], "into_items": [], "base_gold": 1150, "description": "+80 Attack Damage\n\nUNIQUE Passive: +20% Life Steal\nUNIQUE Passive: Your basic attacks can now overheal you. Excess life is stored as a shield that can block 50-350 damage, based on champion level.\n\nThis shield decays slowly if you haven't dealt or taken damage in the last 25 seconds.", "image": "http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/3072.png"}
        request = Request(self.url+"api/items/3072/")
        response = urlopen(request)
        response_body = response.read().decode("utf-8")
        self.assertEqual(response.getcode(), 200)
        response_data = loads(response_body)

        self.assertEqual(expected_response, response_data)

# ----
# main
# ----

if __name__ == "__main__":
    main()

