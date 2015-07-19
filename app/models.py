
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.conf import settings

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

    champion_id = models.IntegerField(default=0, verbose_name = 'champion_id')
    name = models.CharField(max_length=200, verbose_name = 'name')
    role = models.CharField(max_length=100, verbose_name = 'role')
    title = models.CharField(max_length=100, verbose_name = 'title')
    lore = models.CharField(max_length=5000, verbose_name = 'lore')
    image = models.CharField(max_length=100, verbose_name = 'image')
    passive_name = models.CharField(max_length=100, verbose_name = 'passive_name')
    passive_image = models.CharField(max_length=100, verbose_name = 'passive_image')
    passive_description = models.CharField(max_length=1000, verbose_name = 'passive_description')
    q_name = models.CharField(max_length=100, verbose_name = 'q_name')
    q_image = models.CharField(max_length=100, verbose_name = 'q_image')
    q_description = models.CharField(max_length=1000, verbose_name = 'q_description')
    w_name = models.CharField(max_length=100, verbose_name = 'w_name')
    w_image = models.CharField(max_length=100, verbose_name = 'w_image')
    w_description = models.CharField(max_length=1000, verbose_name = 'w_description')
    e_name = models.CharField(max_length=100, verbose_name = 'e_name')
    e_image = models.CharField(max_length=100, verbose_name = 'e_image')
    e_description = models.CharField(max_length=1000, verbose_name = 'e_description')
    r_name = models.CharField(max_length=100, verbose_name = 'r_name')
    r_image = models.CharField(max_length=100, verbose_name = 'r_image')
    r_description = models.CharField(max_length=1000, verbose_name = 'r_description')
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
