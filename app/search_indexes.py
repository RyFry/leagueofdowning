from haystack import indexes
from app.models import *



# ---------------------
# Champion Search Index
# ---------------------

class ChampionIndex (indexes.SearchIndex, indexes.Indexable) :
    text = indexes.CharField(document=True, use_template=True, template_name="search/indexes/app/champion_text.txt")
    champion_id = indexes.IntegerField(model_attr='champion_id')
    champion_name = indexes.CharField(model_attr='name')
    champion_role = indexes.CharField(model_attr='role')
    title = indexes.CharField(model_attr='title')
    lore = indexes.CharField(model_attr='lore')
    champion_image = indexes.CharField(model_attr='image')
    passive_name = indexes.CharField(model_attr='passive_name')
    passive_image = indexes.CharField(model_attr='passive_image')
    passive_description = indexes.CharField(model_attr='passive_description')
    q_name = indexes.CharField(model_attr='q_name')
    q_image = indexes.CharField(model_attr='q_image')
    q_description = indexes.CharField(model_attr='q_description')
    w_name = indexes.CharField(model_attr='w_name')
    w_image = indexes.CharField(model_attr='w_image')
    w_description = indexes.CharField(model_attr='w_description')
    e_name = indexes.CharField(model_attr='e_name')
    e_image = indexes.CharField(model_attr='e_image')
    e_description = indexes.CharField(model_attr='e_description')
    r_name = indexes.CharField(model_attr='r_name')
    r_image = indexes.CharField(model_attr='r_image')
    r_description = indexes.CharField(model_attr='r_description')

    
    def get_model (self) :
        return Champion

    def index_queryset (self, using=None) :
        """
        Used when the entire index for model is updated
        """
        return self.get_model().objects



# -----------------
# Item Search Index
# -----------------
class Item(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/indexes/app/item_text.txt")
    item_id = indexes.IntegerField(model_attr= 'item_id')
    item_name = indexes.CharField(model_attr= 'name')
    item_description = indexes.CharField(model_attr= 'description')
    base_gold = indexes.IntegerField(model_attr= 'base_gold')
    sell_gold = indexes.IntegerField(model_attr= 'sell_gold')
    total_gold = indexes.IntegerField(model_attr= 'total_gold')
    item_image = indexes.CharField(model_attr= 'image')

    def get_model (self) :
        return Item

    def index_queryset (self, using=None) :
        """
        Used when the entire index for model is updated
        """
        return self.get_model().objects



# -------------------
# Player Search Index
# -------------------
class Player(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True, template_name="search/indexes/app/player_text.txt")
    player_id = indexes.IntegerField(model_attr= 'player_id')
    first_name = indexes.CharField(model_attr= 'first_name')
    last_name = indexes.CharField(model_attr= 'last_name')
    team_name = indexes.CharField(model_attr= 'team_name')
    ign = indexes.CharField(model_attr= 'ign')
    bio = indexes.CharField(model_attr= 'bio')
    player_image = indexes.CharField(model_attr= 'image')
    player_role = indexes.CharField(model_attr= 'role')
    kda = indexes.FloatField(model_attr= 'kda')
    gpm = indexes.FloatField(model_attr= 'gpm')
    total_gold = indexes.IntegerField(model_attr= 'total_gold')
    games_played = indexes.IntegerField(model_attr= 'games_played')


    
    def get_model (self) :
        return Player

    def index_queryset (self, using=None) :
        """
        Used when the entire index for model is updated
        """
        return self.get_model().objects
