from app.models import Champion, Player, Item
from rest_framework import serializers


class ChampionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Champion
        fields = ('champion_id', 'champion_name', 'champion_role', 'champion_title', 'champion_lore', 'champion_image', 'champion_passive_name', 'champion_passive_image', 'champion_passive_description', 'champion_q_name', 'champion_q_image', 'champion_q_description', 'champion_w_name', 'champion_w_image', 'champion_w_description', 'champion_e_name', 'champion_e_image', 'champion_e_description','champion_r_name', 'champion_r_image', 'champion_r_description', 'champion_champion_to_item')

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('player_id', 'player_first_name', 'player_last_name', 'player_ign', 'player_bio', 'player_image', 'player_role', 'player_kda', 'player_gpm', 'player_total_gold', 'player_games_played', 'player_player_to_champion')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('item_id', 'item_name', 'item_description', 'item_base_gold', 'item_sell_gold', 'item_total_gold', 'item_image')
