from django.test import TestCase
from app.models import *

# Create your tests here.

# Create your tests here.
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

from tastypie.test import ResourceTestCase

import json
import watson
#end New Imports

    # -----------
    # TestModels
    # -----------

class ModelTestCase(TestCase):
    # -------------
    # champion_model
    # -------------

    def test_champion_model1(self):
        #Dictionary Key: Country Name
        #Dictionary Value: [Country_code, country_rank]

        Champions.objects.create(champions_name="dr_mundo", picture = "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/DrMundo.png", "abilities": {"q" : 
                                    "Q: Infected CleaverDr. Mundo hurls his cleaver, dealing damage equal to a portion of his target's current Health and slowing them for a short time. Dr. Mundo delights in the suffering of others, so he is returned half of the Health cost when he successfully lands a cleaver (increased to the full Health cost on killing blows).Dr. Mundo hurls his cleaver, dealing magic damage equal to 15/18/21/23/25% of the target's current Health (80/130/180/230/280 damage minimum) and slowing them by 40% for 2 seconds.Half of the Health cost is refunded if the cleaver hits a target (increased to the full Health cost on killing blows)." , 
                                "w": 
                                    "W: Burning Agony   Dr. Mundo drains his Health to reduce the duration of disables and deal continual damage to nearby enemies.Toggle: Dr. Mundo deals 35/50/65/80/95 (+20% Ability Power) magic damage to nearby enemies, and reduces the duration of disables on Dr. Mundo by 10/15/20/25/30%.", 
                                "e": 
                                    "E: Masochism Masochism increases Dr. Mundo's Attack Damage by a flat amount for 5 seconds. In addition, Dr. Mundo also gains an additional amount of Attack Damage for each percentage of Health he is missing. Increases Attack Damage by 40/55/70/85/100 for 5 seconds. Dr. Mundo gains an additional +0.4/0.55/0.7/0.85/1 Attack Damage for each percentage of Health he is missing.", 
                                "r": 
                                    "R: Sadism Dr. Mundo sacrifices a portion of his Health for increased Movement Speed and drastically increased Health Regeneration. Dr. Mundo regenerates 0 health (40/50/60% of max health) over 12 seconds. Additionally, he gains 15/25/35% movement speed during this time." }, champion_role = "fighter", champion_lane = "top", champion_counters = ["olaf", "kog_maw", "trundle"], champion_items = ["sunfire_cape", "spirit_visage", "randuins_omen"], resource_uri = "/api/champions/dr_mundo/")
 
        Champion_Mundo = Champion.objects.get(champion_name="dr_mundo")
        self.assertEqual(Country_Brazil.country_name, "Brazil")
        self.assertEqual(Country_Brazil.country_code, "BRA")
        self.assertEqual(Country_Brazil.rank, 3)
        self.assertEqual(Country_Brazil.flag, "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/brazil.png")
        self.assertEqual(Country_Brazil.symbol_flag, "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/brazil.jpg")
        self.assertEqual(Country_Brazil.map_url, "https://www.google.com/maps/embed/v1/place?q=Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ")

    def test_country_model2(self):
        #Dictionary Key: Country Name
        #Dictionary Value: [Country_code, country_rank]
        country_test_dict2 = {"Brazil": ["BRA", 3,"https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/brazil.png","https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/brazil.jpg","https://www.google.com/maps/embed/v1/place?q=Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ"], "Italy": ["ITA", 9,"https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/flags/italy.png","https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/symbol_flags/italy.jpg","https://www.google.com/maps/embed/v1/place?q=Italy&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ"]}

        Country.objects.create(country_name="Brazil", country_code=country_test_dict2["Brazil"][0], rank = country_test_dict2["Brazil"][1], flag = country_test_dict2["Brazil"][2], symbol_flag = country_test_dict2["Brazil"][3], map_url = country_test_dict2["Brazil"][4])
        Country.objects.create(country_name="Italy", country_code=country_test_dict2["Italy"][0], rank = country_test_dict2["Italy"][1], flag = country_test_dict2["Italy"][2], symbol_flag = country_test_dict2["Italy"][3], map_url = country_test_dict2["Italy"][4])

        #Brazil check      
        Country_Brazil = Country.objects.get(country_name="Brazil")
        self.assertEqual(Country_Brazil.country_name, "Brazil")
        self.assertEqual(Country_Brazil.country_code, "BRA")
        self.assertEqual(Country_Brazil.rank, 3)
        self.assertEqual(Country_Brazil.flag, country_test_dict2["Brazil"][2])
        self.assertEqual(Country_Brazil.symbol_flag, country_test_dict2["Brazil"][3])
        self.assertEqual(Country_Brazil.map_url, country_test_dict2["Brazil"][4])

        #Italy check       
        Country_Brazil = Country.objects.get(country_name="Italy")
        self.assertEqual(Country_Brazil.country_name, "Italy")
        self.assertEqual(Country_Brazil.country_code, 'ITA')
        self.assertEqual(Country_Brazil.rank, 9)
        self.assertEqual(Country_Brazil.flag, country_test_dict2["Italy"][2])
        self.assertEqual(Country_Brazil.symbol_flag, country_test_dict2["Italy"][3])
        self.assertEqual(Country_Brazil.map_url, country_test_dict2["Italy"][4])


    def test_country_model3(self):
        ########################################
        #Kim change the file location to your computer thanks
        #########################################
         s = open("wc_app/testing_country_date.json")
         country_test_dic = json.load(s)
         s.close()

         for country in country_test_dic.keys():
            Country.objects.create(country_name=country, country_code=country_test_dic[country][0], rank = country_test_dic[country][1], flag = country_test_dic[country][2], symbol_flag = country_test_dic[country][3], map_url = country_test_dic[country][4])

         for current_country in country_test_dic.keys():
            temp = Country.objects.get(country_name=current_country)
            self.assertEqual(temp.country_name, current_country)
            self.assertEqual(temp.country_code, country_test_dic[current_country][0])
            self.assertEqual(temp.rank, country_test_dic[current_country][1])
            self.assertEqual(temp.flag, country_test_dic[current_country][2])
            self.assertEqual(temp.symbol_flag, country_test_dic[current_country][3])
            self.assertEqual(temp.map_url, country_test_dic[current_country][4])
            
            

    # -------------
    # Player_model
    # -------------


    # country = models.ForeignKey(Country)
    # sur_name = models.CharField(max_length=200)
    # full_name = models.CharField(max_length=200)
    # clubname = models.CharField(max_length=200)
    # position = models.CharField(max_length=64)
    # birth_date = models.DateField()

    def test_player_model1(self):
        #Dictionary Key: Player full name
        #Dictionary Value: [sur_name, country,Clubname,Position,Birthdate, something, image, something, first international appearance, something, somethingthing, bio]
        player_test_dict1 = {"Andrea Barzagli": ["Barzagli", "Italy", "Juventus FC", "Defender", "1981-05-08", 15, "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Italy/Andrea_BARZAGLI.png", 50, "Italy - Finland 17 Nov 2004", 0, 186, "Formidable in the air and a fine tackler who gives away very few fouls, centre-back Andrea Barzagli is viewed by Italy coach Cesare Prandelli as a defensive stand-in of the highest quality. Since joining Juventus in 2011, he has played regularly alongside Giorgio Chiellini and Leonardo Bonucci in a three-man back line, and the trio have developed an understanding crucial to their performances with "]}

        Country.objects.create(country_name = player_test_dict1["Andrea Barzagli"][1])
        c1 = Country.objects.create(country_name = player_test_dict1["Andrea Barzagli"][1])

        Player.objects.create(country=c1, sur_name= player_test_dict1["Andrea Barzagli"][0],full_name = "Andrea Barzagli" ,clubname = player_test_dict1["Andrea Barzagli"][2], position = player_test_dict1["Andrea Barzagli"][3], birth_date =player_test_dict1["Andrea Barzagli"][4], player_image = player_test_dict1["Andrea Barzagli"][6], international_caps = player_test_dict1["Andrea Barzagli"][5], goals = player_test_dict1["Andrea Barzagli"][5], height = player_test_dict1["Andrea Barzagli"][5], first_international_appearance = player_test_dict1["Andrea Barzagli"][8], biography = player_test_dict1["Andrea Barzagli"][11])
        
        player_get = Player.objects.get(full_name = "Andrea Barzagli")
        self.assertEqual(player_get.country.__str__(), player_test_dict1["Andrea Barzagli"][1])
        self.assertEqual(player_get.sur_name, player_test_dict1["Andrea Barzagli"][0])
        self.assertEqual(player_get.full_name, "Andrea Barzagli")
        self.assertEqual(player_get.clubname, player_test_dict1["Andrea Barzagli"][2])
        self.assertEqual(player_get.position, player_test_dict1["Andrea Barzagli"][3])
        self.assertEqual(player_get.birth_date.__str__(), player_test_dict1["Andrea Barzagli"][4])
        self.assertEqual(player_get.player_image, player_test_dict1["Andrea Barzagli"][6]) #string
        self.assertEqual(player_get.international_caps, player_test_dict1["Andrea Barzagli"][5]) #int
        self.assertEqual(player_get.goals, player_test_dict1["Andrea Barzagli"][5]) #int
        self.assertEqual(player_get.height, player_test_dict1["Andrea Barzagli"][5]) #int
        self.assertEqual(player_get.first_international_appearance, player_test_dict1["Andrea Barzagli"][8]) #string
        self.assertEqual(player_get.biography, player_test_dict1["Andrea Barzagli"][11]) #string




    def test_player_model2(self):
        #Dictionary Key: Player full name
        #Dictionary Value: [sur_name, country,Clubname,Position,Birthdate, something, image, something, first international appearance, something, somethingthing, bio]
        player_test_dict1 = {"Andrea Barzagli": ["Barzagli", "Italy", "Juventus FC", "Defender", "1981-05-08", 15, "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Italy/Andrea_BARZAGLI.png", 50, "Italy - Finland 17 Nov 2004", 0, 186, "Formidable in the air and a fine tackler who gives away very few fouls, centre-back Andrea Barzagli is viewed by Italy coach Cesare Prandelli as a defensive stand-in of the highest quality. Since joining Juventus in 2011, he has played regularly alongside Giorgio Chiellini and Leonardo Bonucci in a three-man back line, and the trio have developed an understanding crucial to their performances with "],
        "Yoshito Okubo": ["Okubo", "Japan", "Kawasaki Frontale", "Forward", "1982-06-09", 13, "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/players/Japan/Yoshito_OKUBO.png", 60, "Japan - Korea Republic 31 May 2003", 6, 170, "After winning the J.League golden boot in 2013, striker Yoshito Okubo will be brimming with confidence as he appears at his second FIFA World Cup. Even so, the inclusion of the seasoned Kawasaki Frontale forward for Brazil 2014 was something of a surprise, as his last game for the Samurai Blue came more than two years ago. "]}

        Country.objects.create(country_name = player_test_dict1["Andrea Barzagli"][1])
        Country.objects.create(country_name = player_test_dict1["Yoshito Okubo"][1])

        c1 = Country.objects.get(country_name = player_test_dict1["Andrea Barzagli"][1])
        c2 = Country.objects.get(country_name = player_test_dict1["Yoshito Okubo"][1])

        player1_name= "Andrea Barzagli"
        player2_name= "Yoshito Okubo"

        Player.objects.create(country=c1, sur_name= player_test_dict1[player1_name][0],full_name = "Andrea Barzagli" ,clubname = player_test_dict1[player1_name][2], position = player_test_dict1[player1_name][3], birth_date =player_test_dict1[player1_name][4], player_image = player_test_dict1[player1_name][6], international_caps = player_test_dict1[player1_name][5], goals = player_test_dict1[player1_name][5], height = player_test_dict1[player1_name][5], first_international_appearance = player_test_dict1[player1_name][8], biography = player_test_dict1[player1_name][11])
        Player.objects.create(country=c2, sur_name= player_test_dict1[player2_name][0],full_name = "Yoshito Okubo" ,clubname = player_test_dict1[player2_name][2], position = player_test_dict1[player2_name][3], birth_date =player_test_dict1[player2_name][4], player_image = player_test_dict1[player2_name][6], international_caps = player_test_dict1[player2_name][5], goals = player_test_dict1[player2_name][5], height = player_test_dict1[player2_name][5], first_international_appearance = player_test_dict1[player2_name][8], biography = player_test_dict1[player2_name][11])
        

        player_get = Player.objects.get(full_name = player1_name)
        self.assertEqual(player_get.country.__str__(), player_test_dict1[player1_name][1])
        self.assertEqual(player_get.sur_name, player_test_dict1[player1_name][0])
        self.assertEqual(player_get.full_name, player1_name)
        self.assertEqual(player_get.clubname, player_test_dict1[player1_name][2])
        self.assertEqual(player_get.position, player_test_dict1[player1_name][3])
        self.assertEqual(player_get.birth_date.__str__(), player_test_dict1[player1_name][4])

        self.assertEqual(player_get.player_image, player_test_dict1[player1_name][6])
        self.assertEqual(player_get.international_caps, player_test_dict1[player1_name][5])
        self.assertEqual(player_get.goals, player_test_dict1[player1_name][5])
        self.assertEqual(player_get.height, player_test_dict1[player1_name][5])
        self.assertEqual(player_get.first_international_appearance, player_test_dict1[player1_name][8])
        self.assertEqual(player_get.biography, player_test_dict1[player1_name][11])

        
        player_get = Player.objects.get(full_name = player2_name)
        self.assertEqual(player_get.country.__str__(), player_test_dict1[player2_name][1])
        self.assertEqual(player_get.sur_name, player_test_dict1[player2_name][0])
        self.assertEqual(player_get.full_name, player2_name)
        self.assertEqual(player_get.clubname, player_test_dict1[player2_name][2])
        self.assertEqual(player_get.position, player_test_dict1[player2_name][3])
        self.assertEqual(player_get.birth_date.__str__(), player_test_dict1[player2_name][4])

        self.assertEqual(player_get.player_image, player_test_dict1[player2_name][6])
        self.assertEqual(player_get.international_caps, player_test_dict1[player2_name][5])
        self.assertEqual(player_get.goals, player_test_dict1[player2_name][5])
        self.assertEqual(player_get.height, player_test_dict1[player2_name][5])
        self.assertEqual(player_get.first_international_appearance, player_test_dict1[player2_name][8])
        self.assertEqual(player_get.biography, player_test_dict1[player2_name][11])

    def test_player_model3(self):
        #Dictionary Key: Player full name
        #Dictionary Value: [sur_name, country,Clubname,Position,Birthdate, something, image, something, first international appearance, something, somethingthing, bio]

        s = open("wc_app/testing_player_data.json")
        player_test_diction = json.load(s)
        s.close()

        s = open("wc_app/testing_country_date.json")
        country_test_dic = json.load(s)
        s.close()

        for country_name in country_test_dic.keys():
            Country.objects.create(country_name = country_name)
        
        for player_name in player_test_diction.keys(): 
            c1 = Country.objects.get(country_name = player_test_diction[player_name][1])
            Player.objects.create(country=c1, sur_name= player_test_diction[player_name][0],full_name = player_name ,clubname = player_test_diction[player_name][2], position = player_test_diction[player_name][3], birth_date =player_test_diction[player_name][4], player_image = player_test_diction[player_name][6], international_caps = player_test_diction[player_name][5], goals = player_test_diction[player_name][5], height = player_test_diction[player_name][5], first_international_appearance = player_test_diction[player_name][8], biography = player_test_diction[player_name][11])

        for player_name in player_test_diction.keys():
            player_get = Player.objects.get(full_name = player_name)
            self.assertEqual(player_get.country.__str__(), player_test_diction[player_name][1])
            self.assertEqual(player_get.sur_name, player_test_diction[player_name][0])
            self.assertEqual(player_get.full_name, player_name)
            self.assertEqual(player_get.clubname, player_test_diction[player_name][2])
            self.assertEqual(player_get.position, player_test_diction[player_name][3])
            self.assertEqual(player_get.birth_date.__str__(), player_test_diction[player_name][4])

            self.assertEqual(player_get.player_image, player_test_diction[player_name][6])
            self.assertEqual(player_get.international_caps, player_test_diction[player_name][5])
            self.assertEqual(player_get.goals, player_test_diction[player_name][5])
            self.assertEqual(player_get.height, player_test_diction[player_name][5])
            self.assertEqual(player_get.first_international_appearance, player_test_diction[player_name][8])
            self.assertEqual(player_get.biography, player_test_diction[player_name][11])


    # -------------
    # Match_model
    # -------------

    # match_num = models.IntegerField(default=0)
    # country_A = models.ForeignKey(Country, related_name='country_A')
    # country_B = models.ForeignKey(Country, related_name='country_B')
    # winner = models.CharField(max_length=200)
    # score = models.CharField(max_length=64)
    # location = models.CharField(max_length=200)
    # match_date = models.DateField()


    def test_match_model1(self):
        #Dictionary Key: HomeTeam vs AwayTeam
        #Dictionary Value: [Match_Number, HomeTeam, HomeTeamScore,AwayTeam, AwayTeamScore, Winner, Location, date, merged flag, maps location, hightlights]
        match_test_dict1 = { "Ivory Coast-Japan" : [ 6, "Ivory Coast", 2, "Japan", 1, "Ivory Coast", "Arena Pernambuco", "2014-06-14", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/civ_jpn.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pernambuco+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1881469" ]}

        score_cat = str(match_test_dict1["Ivory Coast-Japan"][2]) + "-" + str(match_test_dict1["Ivory Coast-Japan"][4])
                
        Country.objects.create(country_name = "Ivory Coast")
        Country.objects.create(country_name = "Japan")
        
        Match.objects.create(match_num = match_test_dict1["Ivory Coast-Japan"][0], country_A = Country.objects.get(country_name = match_test_dict1["Ivory Coast-Japan"][1]), country_B = Country.objects.get(country_name = match_test_dict1["Ivory Coast-Japan"][3]), winner = match_test_dict1["Ivory Coast-Japan"][5], score = score_cat, location = match_test_dict1["Ivory Coast-Japan"][6], match_date = match_test_dict1["Ivory Coast-Japan"][7], merge_flag = match_test_dict1["Ivory Coast-Japan"][8], map_location = match_test_dict1["Ivory Coast-Japan"][9], highlight_url = match_test_dict1["Ivory Coast-Japan"][10])

        #need to create country objects and add __str__ methods assert equals
        match_get = Match.objects.get(match_num = match_test_dict1["Ivory Coast-Japan"][0])
        self.assertEqual(match_get.match_num, match_test_dict1["Ivory Coast-Japan"][0])
        self.assertEqual(match_get.country_A.country_name, match_test_dict1["Ivory Coast-Japan"][1])
        self.assertEqual(match_get.country_B.country_name, match_test_dict1["Ivory Coast-Japan"][3])
        self.assertEqual(match_get.winner, match_test_dict1["Ivory Coast-Japan"][5])
        self.assertEqual(match_get.score, score_cat)
        self.assertEqual(match_get.location, match_test_dict1["Ivory Coast-Japan"][6])
        self.assertEqual(match_get.match_date.__str__(), match_test_dict1["Ivory Coast-Japan"][7])
        self.assertEqual(match_get.merge_flag, match_test_dict1["Ivory Coast-Japan"][8])
        self.assertEqual(match_get.map_location, match_test_dict1["Ivory Coast-Japan"][9])
        self.assertEqual(match_get.highlight_url, match_test_dict1["Ivory Coast-Japan"][10])

    def test_match_model2(self):
        #Dictionary Key: HomeTeam vs AwayTeam
        #Dictionary Value: [Match_Number, HomeTeam, HomeTeamScore,AwayTeam, AwayTeamScore, Winner, Location, date]
        match_test_dict1 ={ "Ivory Coast-Japan" : [ 6, "Ivory Coast", 2, "Japan", 1, "Ivory Coast", "Arena Pernambuco", "2014-06-14", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/civ_jpn.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Pernambuco+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1881469" ] , "Cameroon-Croatia" : [ 18, "Cameroon", 0, "Croatia", 4, "Croatia", "Arena Amazonia", "2014-06-18", "https://googledrive.com/host/0B3-zO2AfoiQjWXRqUVVUX19mdFk/match_symbol/cmr_cro.jpg", "https://www.google.com/maps/embed/v1/place?q=Arena Amazonia+Brazil&key=AIzaSyDZQEI-0qREquMzHQf8Gl6Z2zYt_YBjrmQ", "http://player.espn.com/player.js?pcode=B4a3E63GKeEtO92XK7NI067ak980&width=576&height=324&externalId=intl:1891625 " ]}

        Country.objects.create(country_name = "Ivory Coast")
        Country.objects.create(country_name = "Japan")
        Country.objects.create(country_name = "Cameroon")
        Country.objects.create(country_name = "Croatia")

        score_cat = str(match_test_dict1["Ivory Coast-Japan"][2]) + "-" + str(match_test_dict1["Ivory Coast-Japan"][4])
        Match.objects.create(match_num = match_test_dict1["Ivory Coast-Japan"][0],
                             country_A = Country.objects.get(country_name = match_test_dict1["Ivory Coast-Japan"][1]),
                             country_B = Country.objects.get(country_name = match_test_dict1["Ivory Coast-Japan"][3]),
                             winner = match_test_dict1["Ivory Coast-Japan"][5], score = score_cat,
                             location = match_test_dict1["Ivory Coast-Japan"][6],
                             match_date = match_test_dict1["Ivory Coast-Japan"][7],
                             merge_flag = match_test_dict1["Ivory Coast-Japan"][8],
                             map_location = match_test_dict1["Ivory Coast-Japan"][9],
                             highlight_url = match_test_dict1["Ivory Coast-Japan"][10])
        
        score_cat2 = str(match_test_dict1["Cameroon-Croatia"][2]) + "-" + str(match_test_dict1["Cameroon-Croatia"][4])
        Match.objects.create(match_num = match_test_dict1["Cameroon-Croatia"][0], country_A = Country.objects.get(country_name = match_test_dict1["Cameroon-Croatia"][1]), country_B = Country.objects.get(country_name = match_test_dict1["Cameroon-Croatia"][3]), winner = match_test_dict1["Cameroon-Croatia"][5], score = score_cat2, location = match_test_dict1["Cameroon-Croatia"][6], match_date = match_test_dict1["Cameroon-Croatia"][7], merge_flag = match_test_dict1["Cameroon-Croatia"][8], map_location = match_test_dict1["Cameroon-Croatia"][9], highlight_url = match_test_dict1["Cameroon-Croatia"][10])

        match_get = Match.objects.get(match_num = match_test_dict1["Ivory Coast-Japan"][0])
        self.assertEqual(match_get.match_num, match_test_dict1["Ivory Coast-Japan"][0])
        self.assertEqual(match_get.country_A.country_name, match_test_dict1["Ivory Coast-Japan"][1])
        self.assertEqual(match_get.country_B.country_name, match_test_dict1["Ivory Coast-Japan"][3])
        self.assertEqual(match_get.winner, match_test_dict1["Ivory Coast-Japan"][5])
        self.assertEqual(match_get.score, score_cat)
        self.assertEqual(match_get.location, match_test_dict1["Ivory Coast-Japan"][6])
        self.assertEqual(match_get.match_date.__str__(), match_test_dict1["Ivory Coast-Japan"][7])

        self.assertEqual(match_get.merge_flag, match_test_dict1["Ivory Coast-Japan"][8])
        self.assertEqual(match_get.map_location, match_test_dict1["Ivory Coast-Japan"][9])
        self.assertEqual(match_get.highlight_url, match_test_dict1["Ivory Coast-Japan"][10])



        match_get = Match.objects.get(match_num = match_test_dict1["Cameroon-Croatia"][0])
        self.assertEqual(match_get.match_num, match_test_dict1["Cameroon-Croatia"][0])
        self.assertEqual(match_get.country_A.country_name, match_test_dict1["Cameroon-Croatia"][1])
        self.assertEqual(match_get.country_B.country_name, match_test_dict1["Cameroon-Croatia"][3])
        self.assertEqual(match_get.winner, match_test_dict1["Cameroon-Croatia"][5])
        self.assertEqual(match_get.score, score_cat2)
        self.assertEqual(match_get.location, match_test_dict1["Cameroon-Croatia"][6])
        self.assertEqual(match_get.match_date.__str__(), match_test_dict1["Cameroon-Croatia"][7])

        self.assertEqual(match_get.merge_flag, match_test_dict1["Cameroon-Croatia"][8])
        self.assertEqual(match_get.map_location, match_test_dict1["Cameroon-Croatia"][9])
        self.assertEqual(match_get.highlight_url, match_test_dict1["Cameroon-Croatia"][10])


    def test_match_model3(self):
        #Dictionary Key: HomeTeam vs AwayTeam
        #Dictionary Value: [Match_Number, HomeTeam, HomeTeamScore,AwayTeam, AwayTeamScore, Winner, Location, date]
        s = open("wc_app/testing_match_data.json")
        match_test_diction = json.load(s)
        s.close()

        s = open("wc_app/testing_country_date.json")
        country_test_dic = json.load(s)
        s.close()

        for country_name in country_test_dic.keys():
            Country.objects.create(country_name = country_name)
        
        for match_vs in match_test_diction:
            score_cat = str(match_test_diction[match_vs][2]) + "-" + str(match_test_diction[match_vs][4])
            Match.objects.create(match_num = match_test_diction[match_vs][0], country_A = Country.objects.get(country_name = match_test_diction[match_vs][1]), country_B = Country.objects.get(country_name = match_test_diction[match_vs][3]), winner = match_test_diction[match_vs][5], score = score_cat, location = match_test_diction[match_vs][6], match_date = match_test_diction[match_vs][7], merge_flag = match_test_diction[match_vs][8], map_location = match_test_diction[match_vs][9], highlight_url = match_test_diction[match_vs][10])
            
        for match_vs in match_test_diction:    
            match_get = Match.objects.get(match_num = match_test_diction[match_vs][0])
            self.assertEqual(match_get.match_num, match_test_diction[match_vs][0])
            self.assertEqual(match_get.country_A.country_name, match_test_diction[match_vs][1])
            self.assertEqual(match_get.country_B.country_name, match_test_diction[match_vs][3])
            self.assertEqual(match_get.winner, match_test_diction[match_vs][5])
            self.assertEqual(match_get.score, str(match_test_diction[match_vs][2]) + "-" + str(match_test_diction[match_vs][4]))
            self.assertEqual(match_get.location, match_test_diction[match_vs][6])
            self.assertEqual(match_get.match_date.__str__(), match_test_diction[match_vs][7])
            self.assertEqual(match_get.merge_flag, match_test_diction[match_vs][8])
            self.assertEqual(match_get.map_location, match_test_diction[match_vs][9])
            self.assertEqual(match_get.highlight_url, match_test_diction[match_vs][10])


# ----
# main
# ----

if __name__ == "__main__" :
    main()

