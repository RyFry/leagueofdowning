
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.conf import settings

    # -------------
    # Champion_model
    # -------------

class Champion(models.Model):
    """
    The model contains a Champion name, role, lane, counters, items, and abilities.
    The __str__ method is used to return the name of the Champion as string.
    """
    champion_champion_id = models.IntegerField(default=0)
    champion_name = models.CharField(max_length=200)
    champion_role = models.CharField(max_length=100)
    champion_title = models.CharField(max_length=100)
    champion_lore = models.CharField(max_length=5000)
    champion_image = models.CharField(max_length=100)
    champion_passive_name = models.CharField(max_length=100)
    champion_passive_image = models.CharField(max_length=100)
    champion_passive_description = models.CharField(max_length=1000)
    champion_q_name = models.CharField(max_length=100)
    champion_q_image = models.CharField(max_length=100)
    champion_q_description = models.CharField(max_length=1000)
    champion_w_name = models.CharField(max_length=100)
    champion_w_image = models.CharField(max_length=100)
    champion_w_description = models.CharField(max_length=1000)
    champion_e_name = models.CharField(max_length=100)
    champion_e_image = models.CharField(max_length=100)
    champion_e_description = models.CharField(max_length=1000)
    champion_r_name = models.CharField(max_length=100)
    champion_r_image = models.CharField(max_length=100)
    champion_r_description = models.CharField(max_length=1000)
    champion_champion_to_item = models.CharField(max_length=1000)


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
    player_id = models.IntegerField(default=0)
    player_first_name = models.CharField(max_length=100)
    player_last_name = models.CharField(max_length=100)
    player_ign = models.CharField(max_length=100)
    player_bio = models.CharField(max_length=5000)
    player_image = models.CharField(max_length=100)
    player_role = models.CharField(max_length=100)
    player_kda = models.FloatField(default=0)
    player_gpm = models.FloatField(default=0)
    player_total_gold = models.IntegerField(default=0)
    player_games_played = models.IntegerField(default=0)
    player_player_to_champion = models.CharField(max_length=1000)


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
    item_item_id = models.IntegerField(default=0)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=5000)
    item_base_gold = models.IntegerField(default=0)
    item_sell_gold = models.IntegerField(default=0)
    item_total_gold = models.IntegerField(default=0)
    item_image = models.CharField(max_length=100)

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
