from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import relationship, sessionmaker, backref
from app.database import database

import json
import re
from urllib.request import urlopen
import urllib
import requests


# Create your views here.

def index(request):
    template = loader.get_template('app/splash.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def about(request):
    template = loader.get_template('app/about.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def test(request):
    template = loader.get_template('app/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def error(request):
    template = loader.get_template('app/error.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

#
# Table Pages
#

def players(request):
    template = loader.get_template('app/players.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def items(request):
    template = loader.get_template('app/items.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def champions(request):
    template = loader.get_template('app/champions.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))



#
# Champion Pages
#

def champion(request, id):
    try:
        int(id)
        engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

        result = engine.execute('select * from "Champion" where champion_id=' + id)
        jsonout = {}
        for row in result:
            champ_name = row['champion_id']
            result1 = engine.execute('select item_id from "ChampionToItem" where champion_id = %s' % champ_name)

            itemlist = []
            for row1 in result1:
                itemlist.append(row1['item_id'])

            jsonout = {'champion_id': row['champion_id'], 'name': row['name'], 'role': row['role'], 'title': row['title'], 'lore': row['lore'],  'image': re.sub("5.13.1", "5.2.1", row['image']), 'passive_name': row['passive_name'], 'passive_image': re.sub("5.13.1", "5.2.1", row['passive_image']), 'passive_description': row['passive_description'], 'q_name': row['q_name'], 'q_image': re.sub("5.13.1", "5.2.1", row['q_image']), 'q_description': row['q_description'], 'w_name': row['w_name'], 'w_image': re.sub("5.13.1", "5.2.1", row['w_image']), 'w_description': row['w_description'], 'e_name': row['e_name'], 'e_image': re.sub("5.13.1", "5.2.1", row['e_image']), 'e_description': row['e_description'], 'r_name': row['r_name'], 'r_image': re.sub("5.13.1", "5.2.1", row['r_image']), 'r_description': row['r_description'], 'recommended_items': itemlist}


        if jsonout == {}:
            template = loader.get_template('app/error.html')
            context = RequestContext(request, {})
            return HttpResponse(template.render(context))
        else:
            template = loader.get_template('app/champion.html')
            context = RequestContext(request, jsonout)
            return HttpResponse(template.render(context))
    except ValueError:
        template = loader.get_template('app/error.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

   

#
# Item Pages
#

def item(request, id):
    try:
        int(id)
        engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

        result = engine.execute('select * from "Item" where item_id=' + id)
        jsonout = {}

        for row in result:
            jsonout = {'item_id': row['item_id'], 'name': row['name'], 'description': row['description'], 'base_gold': row['base_gold'], 'sell_gold': row['sell_gold'], 'total_gold': row['total_gold'], 'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/' + row['image'][-8:]}

        if jsonout == {}:
            template = loader.get_template('app/error.html')
            context = RequestContext(request, {})
            return HttpResponse(template.render(context))
        else:
            template = loader.get_template('app/item.html')
            context = RequestContext(request, jsonout)
            return HttpResponse(template.render(context))
    except ValueError:
        template = loader.get_template('app/error.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

#
# Player Pages
#

def player(request, id):
    try:
        int(id)
        engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

        result = engine.execute('select * from "Player" where player_id=' + id)
        jsonout = {}

        for row in result:
            player_id = row['player_id']
            result1 = engine.execute('select champion_id from "PlayerToChampion" where player_id = %d' % player_id)

            itemlist = []

            for row1 in result1:
                if row1['champion_id'] != 0 :
                    itemlist.append(row1['champion_id'])


            jsonout = {'player_id': row['player_id'], 'first_name': row['first_name'], 'last_name': row['last_name'], 'team_name': row['team_name'], 'ign': row['ign'], 'bio': row['bio'], 'image': re.sub("5.13.1", "5.2.1", row['image']), 'role': row['role'], 'kda': round(row['kda'], 2), 'gpm': round(row['gpm'],2), 'total_gold': row['total_gold'], 'games_played': row['games_played'], 'most_played_champions' : itemlist}

        if jsonout == {}:
            template = loader.get_template('app/error.html')
            context = RequestContext(request, {})
            return HttpResponse(template.render(context))
        else:
            template = loader.get_template('app/player.html')
            context = RequestContext(request, jsonout)
            return HttpResponse(template.render(context))
    except ValueError:
        template = loader.get_template('app/error.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))

#
#Artist Page
#
def artists(request):
    artisturl = 'http://volumemax.me/api/artists/1'
    artist_info = urlopen(artisturl).info()
    raw_artist = urlopen(artisturl).read().decode(artist_info.get_content_charset('utf8'))
    artist = json.loads(raw_artist)  

    template = loader.get_template('app/artist.html')
    context = RequestContext(request, artist)
    return HttpResponse(template.render(context))

def artist(request, id):
    try:
        int(id)
        artisturl = 'http://volumemax.me/api/artists/' + str(id)
        artist_info = urlopen(artisturl).info()
        raw_artist = urlopen(artisturl).read().decode(artist_info.get_content_charset('utf8'))
        artist = json.loads(raw_artist)   

        if artist == {}:
            template = loader.get_template('app/error.html')
            context = RequestContext(request, {})
            return HttpResponse(template.render(context))
        else:
            template = loader.get_template('app/artist.html')
            context = RequestContext(request, artist)
            return HttpResponse(template.render(context))
    except ValueError:
        template = loader.get_template('app/error.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))




#
#API Pages
#
def Champion_List_API(request):
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

    result = engine.execute('select * from "Champion"')
    List = {}
    for row in result:
        champ_name = row['champion_id']
        List[row['champion_id']] = {'champion_id': row['champion_id'], 'name': row['name'], 'role': row['role'], 'title': row['title'], 'lore': row['lore'],  'image': re.sub("5.13.1", "5.2.1", row['image']), 'passive_name': row['passive_name'], 'passive_image': re.sub("5.13.1", "5.2.1", row['passive_image']), 'passive_description': row['passive_description'], 'q_name': row['q_name'], 'q_image': re.sub("5.13.1", "5.2.1", row['q_image']), 'q_description': row['q_description'], 'w_name': row['w_name'], 'w_image': re.sub("5.13.1", "5.2.1", row['w_image']), 'w_description': row['w_description'], 'e_name': row['e_name'], 'e_image': re.sub("5.13.1", "5.2.1", row['e_image']), 'e_description': row['e_description'], 'r_name': row['r_name'], 'r_image': re.sub("5.13.1", "5.2.1", row['r_image']), 'r_description': row['r_description']}
        result1 = engine.execute('select item_id from "ChampionToItem" where champion_id = %s' % champ_name)
        dic = List[champ_name]
        itemlist = []
        for row1 in result1:
            itemlist.append(row1['item_id'])
        dic['recommended_items'] = itemlist

    return HttpResponse(json.dumps(List), content_type='application/json')

def Champion_ID_API(request, id):
    try:
        int(id)
        engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

        result = engine.execute('select * from "Champion" where champion_id=' + id)
        jsonout = {}
        for row in result:
            champ_name = row['champion_id']
            result1 = engine.execute('select item_id from "ChampionToItem" where champion_id = %s' % champ_name)

            itemlist = []
            for row1 in result1:
                itemlist.append(row1['item_id'])

            jsonout = {'champion_id': row['champion_id'], 'name': row['name'], 'role': row['role'], 'title': row['title'], 'lore': row['lore'],  'image': re.sub("5.13.1", "5.2.1", row['image']), 'passive_name': row['passive_name'], 'passive_image': re.sub("5.13.1", "5.2.1", row['passive_image']), 'passive_description': row['passive_description'], 'q_name': row['q_name'], 'q_image': re.sub("5.13.1", "5.2.1", row['q_image']), 'q_description': row['q_description'], 'w_name': row['w_name'], 'w_image': re.sub("5.13.1", "5.2.1", row['w_image']), 'w_description': row['w_description'], 'e_name': row['e_name'], 'e_image': re.sub("5.13.1", "5.2.1", row['e_image']), 'e_description': row['e_description'], 'r_name': row['r_name'], 'r_image': re.sub("5.13.1", "5.2.1", row['r_image']), 'r_description': row['r_description'], 'recommended_items': itemlist}

        if jsonout == {}:
            h = HttpResponse(json.dumps({"error": "Champion ID " + id + " does not exist."}),   content_type="application/json")
            h.status_code = 404
            return h

        return HttpResponse(json.dumps(jsonout), content_type='application/json')    
    except ValueError:
        h = HttpResponse(json.dumps({"error": "Champion ID " + id + " does not exist."}),   content_type="application/json")
        h.status_code = 404
        return h


def Player_List_API(request):
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

    result = engine.execute('select * from "Player"')
    List = {}
    for row in result:
        List[row['player_id']] = {'player_id': row['player_id'], 'first_name': row['first_name'], 'last_name': row['last_name'], 'team_name': row['team_name'], 'ign': row['ign'], 'bio': row['bio'], 'image': re.sub("5.13.1", "5.2.1", row['image']), 'role': row['role'], 'kda': row['kda'], 'gpm': row['gpm'], 'total_gold': row['total_gold'], 'games_played': row['games_played']}

    return HttpResponse(json.dumps(List), content_type='application/json')

def Player_ID_API(request, id):
    try:
        int(id)
        engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

        result = engine.execute('select * from "Player" where player_id=' + id)
        jsonout = {}
        for row in result:
            player_name = row['player_id']
            result1 = engine.execute('select champion_id from "PlayerToChampion" where player_id = %d' % player_name)

            itemlist = []
            for row1 in result1:
                if row1['champion_id'] != 0 :
                    itemlist.append(row1['champion_id'])


            jsonout = {'player_id': row['player_id'], 'first_name': row['first_name'], 'last_name': row['last_name'], 'team_name': row['team_name'], 'ign': row['ign'], 'bio': row['bio'], 'image': re.sub("5.13.1", "5.2.1", row['image']), 'role': row['role'], 'kda': row['kda'], 'gpm': row['gpm'], 'total_gold': row['total_gold'], 'games_played': row['games_played'], 'most_played_champions' : itemlist}
        if jsonout == {}:
            h = HttpResponse(json.dumps({"error": "Player ID " + id + " does not exist."}),   content_type="application/json")
            h.status_code = 404
            return h

        return HttpResponse(json.dumps(jsonout), content_type='application/json') 
    except ValueError:
        h = HttpResponse(json.dumps({"error": "Player ID " + id + " does not exist."}),   content_type="application/json")
        h.status_code = 404
        return h  

def Item_List_API(request):
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

    result = engine.execute('select * from "Item"')
    List = {}
    for row in result:
        List[row['item_id']] = {'item_id': row['item_id'], 'name': row['name'], 'description': row['description'], 'base_gold': row['base_gold'], 'sell_gold': row['sell_gold'], 'total_gold': row['total_gold'], 'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/' + row['image'][-8:]}

    return HttpResponse(json.dumps(List), content_type='application/json')

def Item_ID_API(request, id):
    try:
        int(id)
        engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

        result = engine.execute('select * from "Item" where item_id=' + id)
        jsonout = {}
        for row in result:
            jsonout = {'item_id': row['item_id'], 'name': row['name'], 'description': row['description'], 'base_gold': row['base_gold'], 'sell_gold': row['sell_gold'], 'total_gold': row['total_gold'], 'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/' + row['image'][-8:]}
        if jsonout == {}:
            h = HttpResponse(json.dumps({"error": "Item ID " + id + " does not exist."}),   content_type="application/json")
            h.status_code = 404
            return h

        return HttpResponse(json.dumps(jsonout), content_type='application/json')    
    except ValueError:
        h = HttpResponse(json.dumps({"error": "Item ID " + id + " does not exist."}),   content_type="application/json")
        h.status_code = 404
        return h


