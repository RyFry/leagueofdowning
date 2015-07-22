# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Champion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('champion_id', models.IntegerField(default=0)),
                ('champion_name', models.CharField(max_length=200)),
                ('champion_role', models.CharField(max_length=100)),
                ('champion_title', models.CharField(max_length=100)),
                ('champion_lore', models.CharField(max_length=5000)),
                ('champion_image', models.CharField(max_length=100)),
                ('champion_passive_name', models.CharField(max_length=100)),
                ('champion_passive_image', models.CharField(max_length=100)),
                ('champion_passive_description', models.CharField(max_length=1000)),
                ('champion_q_name', models.CharField(max_length=100)),
                ('champion_q_image', models.CharField(max_length=100)),
                ('champion_q_description', models.CharField(max_length=1000)),
                ('champion_w_name', models.CharField(max_length=100)),
                ('champion_w_image', models.CharField(max_length=100)),
                ('champion_w_description', models.CharField(max_length=1000)),
                ('champion_e_name', models.CharField(max_length=100)),
                ('champion_e_image', models.CharField(max_length=100)),
                ('champion_e_description', models.CharField(max_length=1000)),
                ('champion_r_name', models.CharField(max_length=100)),
                ('champion_r_image', models.CharField(max_length=100)),
                ('champion_r_description', models.CharField(max_length=1000)),
                ('champion_champion_to_item', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('item_id', models.IntegerField(default=0)),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.CharField(max_length=5000)),
                ('item_base_gold', models.IntegerField(default=0)),
                ('item_sell_gold', models.IntegerField(default=0)),
                ('item_total_gold', models.IntegerField(default=0)),
                ('item_image', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('player_id', models.IntegerField(default=0)),
                ('player_first_name', models.CharField(max_length=100)),
                ('player_last_name', models.CharField(max_length=100)),
                ('player_ign', models.CharField(max_length=100)),
                ('player_bio', models.CharField(max_length=5000)),
                ('player_image', models.CharField(max_length=100)),
                ('player_role', models.CharField(max_length=100)),
                ('player_kda', models.FloatField(default=0)),
                ('player_gpm', models.FloatField(default=0)),
                ('player_total_gold', models.IntegerField(default=0)),
                ('player_games_played', models.IntegerField(default=0)),
                ('player_player_to_champion', models.CharField(max_length=1000)),
            ],
        ),
    ]
