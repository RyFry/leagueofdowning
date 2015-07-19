
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.conf import settings

# -------------
# model
# -------------

class Champion(models.Model):
    """
    The model contains a champion id, name, role, title, lore, image, the name, image, and description for each ability, and recommended items.
    The __str__ method is used to return the name of the champion as string.
    """
    class Meta:
        db_table = 'Champion'

    champion_id = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    lore = models.CharField(max_length=5000)
    image = models.CharField(max_length=100)
    passive_name = models.CharField(max_length=100)
    passive_image = models.CharField(max_length=100)
    passive_description = models.CharField(max_length=1000)
    q_name = models.CharField(max_length=100)
    q_image = models.CharField(max_length=100)
    q_description = models.CharField(max_length=1000)
    w_name = models.CharField(max_length=100)
    w_image = models.CharField(max_length=100)
    w_description = models.CharField(max_length=1000)
    e_name = models.CharField(max_length=100)
    e_image = models.CharField(max_length=100)
    e_description = models.CharField(max_length=1000)
    r_name = models.CharField(max_length=100)
    r_image = models.CharField(max_length=100)
    r_description = models.CharField(max_length=1000)
    recommended_items = models.ManyToManyField(Item)


    def get_absolute_url(self):
        return "/champions/%s/" % self.name

    def __str__ (self):
        return self.name


# ------------
# player_model
# ------------

class Player(models.Model):
    """
    The model contains a player id, first name, last name, team name, in-game name, bio, image, role, kda, gpm, total gold, games played, and played champions.

    The __str__ method is used to return the name of the player.
    The get_absolute_url method overrides the default url so that watson get the correct url as a link.
    """
    player_id = models.IntegerField(default=0)
    player_first_name = models.CharField(max_length=100)
    player_last_name = models.CharField(max_length=100)
    player_team_name = models.CharField(max_length=100)
    player_ign = models.CharField(max_length=100)
    player_bio = models.CharField(max_length=5000)
    player_image = models.CharField(max_length=100)
    player_role = models.CharField(max_length=100)
    player_kda = models.FloatField(default=0)
    player_gpm = models.FloatField(default=0)
    player_total_gold = models.IntegerField(default=0)
    player_games_played = models.IntegerField(default=0)
    player_most_played_champions = models.CharField(max_length=1000)


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
    The model contains an item id, name, description, base gold, sell gold, total gold, and an image.

    The __str__ method is used to return the item name. 
    The get_absolute_url method overrides the default url so that watson get the correct url as a link. 
    """
    item_id = models.IntegerField(default=0)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=5000)
    item_base_gold = models.IntegerField(default=0)
    item_sell_gold = models.IntegerField(default=0)
    item_total_gold = models.IntegerField(default=0)
    item_image = models.CharField(max_length=100)
    item_from_items = models.CharField(max_length=100)
    item_into_items = models.CharField(max_length=100)

    def get_absolute_url(self):
        return "/items/%d/" % self.item_name

    def __str__ (self):
        return self.item_name




#import watson

"""
This is where the models are registered. Only the text fields can be registered or else and error will
occur. 
"""

#watson.register(Champion,fields=("name","role", "lane", "counters", 
#                                    "items", "abilities"))

#watson.register(Player,fields=("player_name","player_age","player_position", "total_wins", "season_wins", 
#                               "season_losses", "team_name", "average_kda", "average_gold_match", 
#                               "average_gold_total", "pref_champions" ))

#watson.register(Item,fields=("item_name", "item_stats", "recommended_for", "item_cost", "item_recipe"))

# watson.register(Champion)
# watson.register(Player)
# watson.register(Item)
