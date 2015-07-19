from haystack import indexes
from app.models import *



# ---------------------
# Champion Search Index
# ---------------------

class ChampionIndex (indexes.SearchIndex, indexes.Indexable) :
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.IntegerField(model_attr='champion_id')
    name = indexes.CharField(model_attr='name')
    role = indexes.CharField(model_attr='role')
    title = indexes.CharField(model_attr='title')
    lore = indexes.CharField(model_attr='lore')
    image = indexes.CharField(model_attr='image')
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




# -------------------
# Player Search Index
# -------------------
