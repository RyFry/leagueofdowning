from haystack import indexes
from app.models import *



# ---------------------
# Champion Search Index
# ---------------------

class ChampionIndex (indexes.SearchIndex, indexes.Indexable) :
    text = indexes.CharField(document=True, use_template=True)
    id = models.IntegerField(model_attr='champion_id')
    name = indexes.CharField(model_attr='champion_name')
    role = indexes.CharField(model_attr='champion_role')
    title = indexes.CharField(model_attr='champion_title')
    lore = indexes.CharField(model_attr='champion_lore')
    image = indexes.CharField(model_attr='champion_image')
    passive_name = indexes.CharField(model_attr='champion_passive_name')
    passive_image = indexes.CharField(model_attr='champion_passive_image')
    passive_description = indexes.CharField(model_attr='champion_passive_description')
    q_name = indexes.CharField(model_attr='champion_q_name')
    q_image = indexes.CharField(model_attr='champion_q_image')
    q_description = indexes.CharField(model_attr='champion_q_description')
    w_name = indexes.CharField(model_attr='champion_w_name')
    w_image = indexes.CharField(model_attr='champion_w_image')
    w_description = indexes.CharField(model_attr='champion_w_description')
    e_name = indexes.CharField(model_attr='champion_e_name')
    e_image = indexes.CharField(model_attr='champion_e_image')
    e_description = indexes.CharField(model_attr='champion_e_description')
    r_name = indexes.CharField(model_attr='champion_r_name')
    r_image = indexes.CharField(model_attr='champion_r_image')
    r_description = indexes.CharField(model_attr='champion_r_description')
    recommended_items = indexes.CharField(model_attr='champion_recommended_items')
    
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




# -------------------
# Player Search Index
# -------------------
