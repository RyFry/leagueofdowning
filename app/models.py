
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html


    # -------------
    # Champion_model
    # -------------

class Champion(models.Model):
    """
    The model contains a Champion name, role, lane, counters, items, and abilities.
    The __str__ method is used to return the name of the Champion as string.
    """

    champion_name = models.CharField(max_length=200)
    champion_role = models.CharField(max_length=100)
    champion_lane = models.CharField(max_length=100)
    champion_counters = models.CharField(max_length=500)
    champion_items = models.CharField(max_length=1000)

    # champion Statistics
    champion_abilities = models.CharField(max_length=2000)

    """
    champion_passive = models.CharField(max_length=2000)
    champion_Q = models.CharField(max_length=2000)
    champion_W = models.CharField(max_length=2000)
    champion_E = models.CharField(max_length=2000)
    champion_R = models.CharField(max_length=2000)
    """


    def get_absolute_url(self):
        return "/champions/%s/" % self.champion_name

    def __str__ (self):
        return self.champion_name


    # ------------
    # player_model
    # ------------

class Player(models.Model):
    """
    The model contains a player name, age, position, total_wins, season_wins, season_losses, team_name, average_kda, 
    average_gold_item, average_gold_total, pref_champions.

    The __str__ method is used to return the name of the player.
    The get_absolute_url method overrides the default url so that watson get the correct url as a link.
    """

    player_name = models.CharField(max_length=200)
    player_age = models.IntegerField(default=0)
    
    player_position = models.CharField(max_length=50)
    total_wins = models.IntegerField(default=0)
    season_wins = models.IntegerField(default=0)
    season_losses = models.IntegerField(default=0)
    team_name = models.CharField(max_length=200)

    average_kda = models.IntegerField(default=0)
    average_gold_match = models.IntegerField(default=0)
    average_gold_total = models.IntegerField(default=0)

    pref_champions = models.CharField(max_length=1000)


    """
    def get_absolute_url(self):
        url_name = self.player_name.replace(' ', '_')
        return "/players/%s/" % url_name
    """
    def __str__ (self):
        return self.player_name

    # ------------
    # Item_model
    # ------------

class Item(models.Model):
    """
    The model contains a item_name, item_stats, recommended_for, item_cost, item_recipe.

    The __str__ method is used to return the item name. 
    The get_absolute_url method overrides the default url so that watson get the correct url as a link. 
    """

    item_name = models.CharField(max_length=200)
    item_stats = models.CharField(max_length=2000)
    recommended_for = models.CharField(max_length=2000)
    item_cost = models.IntegerField(default=0)
    average_kda = models.IntegerField(default=0)
    item_recipe = models.CharField(max_length=2000)

    def get_absolute_url(self):
        return "/items/%d/" % self.item_name

    def __str__ (self):
        return self.item_name




#import watson

"""
This is where the models are registered. Only the text fields can be registered or else and error will
occur. 
"""

#watson.register(Champion,fields=("champion_name","champion_role", "champion_lane", "champion_counters", 
#                                    "champion_items", "champion_abilities"))

#watson.register(Player,fields=("player_name","player_age","player_position", "total_wins", "season_wins", 
#                               "season_losses", "team_name", "average_kda", "average_gold_match", 
#                               "average_gold_total", "pref_champions" ))

#watson.register(Item,fields=("item_name", "item_stats", "recommended_for", "item_cost", "item_recipe"))

# watson.register(Champion)
# watson.register(Player)
# watson.register(Item)
