
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

    champion_id = models.IntegerField(default=0, db_column = 'champion_id')
    name = models.CharField(max_length=200, db_column = 'name')
    role = models.CharField(max_length=100, db_column = 'role')
    title = models.CharField(max_length=100, db_column = 'title')
    lore = models.CharField(max_length=5000, db_column = 'lore')
    image = models.CharField(max_length=100, db_column = 'image')
    passive_name = models.CharField(max_length=100, db_column = 'passive_name')
    passive_image = models.CharField(max_length=100, db_column = 'passive_image')
    passive_description = models.CharField(max_length=1000, db_column = 'passive_description')
    q_name = models.CharField(max_length=100, db_column = 'q_name')
    q_image = models.CharField(max_length=100, db_column = 'q_image')
    q_description = models.CharField(max_length=1000, db_column = 'q_description')
    w_name = models.CharField(max_length=100, db_column = 'w_name')
    w_image = models.CharField(max_length=100, db_column = 'w_image')
    w_description = models.CharField(max_length=1000, db_column = 'w_description')
    e_name = models.CharField(max_length=100, db_column = 'e_name')
    e_image = models.CharField(max_length=100, db_column = 'e_image')
    e_description = models.CharField(max_length=1000, db_column = 'e_description')
    r_name = models.CharField(max_length=100, db_column = 'r_name')
    r_image = models.CharField(max_length=100, db_column = 'r_image')
    r_description = models.CharField(max_length=1000, db_column = 'r_description')


    def get_absolute_url(self):
        return "/champions/%s/" % self.name

    def __str__ (self):
        return self.name


class ChampionToItem(models.Model):
    class Meta:
        db_table = 'ChampionToItem'

    id = models.IntegerField(primary_key = True)
    champion_id = models.ForeignKey(Champion)
    item_id = models.ForeignKey(Item)


# ------------
# player_model
# ------------

class Player(models.Model):
    """
    The model contains a player id, first name, last name, team name, in-game name, bio, image, role, kda, gpm, total gold, games played, and played champions.

    The __str__ method is used to return the name of the player.
    The get_absolute_url method overrides the default url so that watson get the correct url as a link.
    """

    class Meta:
        db_table = 'Player'

    player_id = models.IntegerField(default=0, db_column = 'player_id')
    first_name = models.CharField(max_length=100, db_column = 'first_name')
    last_name = models.CharField(max_length=100, db_column = 'last_name')
    team_name = models.CharField(max_length=100, db_column = 'team_name')
    ign = models.CharField(max_length=100, db_column = 'ign')
    bio = models.CharField(max_length=5000, db_column = 'bio')
    image = models.CharField(max_length=100,db_column = 'image')
    role = models.CharField(max_length=100, db_column = 'role')
    kda = models.FloatField(default=0, db_column = 'kda')
    gpm = models.FloatField(default=0, db_column = 'gpm')
    total_gold = models.IntegerField(default=0, db_column = 'total_gold')
    games_played = models.IntegerField(default=0, db_column = 'games_played')


    """
    def get_absolute_url(self):
        url_name = self.player_name.replace(' ', '_')
        return "/players/%s/" % url_name
    """
    def __str__ (self):
        return self.player_name

class PlayerToChampion(models.Model):
    class Meta:
        db_table = 'PlayerToChampion'

    id = models.IntegerField(primary_key = True)
    player_id = models.ForeignKey(Player)
    champion_id = models.ForeignKey(Champion)





