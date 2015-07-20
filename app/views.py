from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from sqlalchemy import create_engine
from app.database import database

import json
import re
from urllib.request import urlopen
import urllib
import requests

from django.db.models import Q

from haystack.query import SearchQuerySet

from .search_indexes import Champion, Item, Player



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

def search(request):
    template = loader.get_template('app/searchpage.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def search_results(request):
    query = request.GET.get('q', default='')

    template = loader.get_template('app/searchpage.html')

    # We want to search for terms separated by ' ' individually
    query_list = query.split(" ")

    sqs = SearchQuerySet().all()

    query_result = sqs.filter(champion_name__in=query_list).load_all().highlight()

    and_data = []
    for q in query_result:
        if q is not None:
            and_data += [
                { 
                    'page_title' : q.highlighted.champion_name if q.highlighted else q.champion_name,
                    'role' : q.highlighted.champion_role if q.highlighted else q.champion_role,
                    'link' : 'http://leagueofdowning.me/champions/' + str(q.champion_id),
                    'lore' : (q.highlighted.lore[:500] if q.highlighted else q.lore[:500]) if q.lore is not None else '',
                    'passive_name' : q.highlighted.passive_name if q.highlighted else q.passive_name,
                    'q_name' : q.highlighted.q_name if q.highlighted else q.q_name,
                    'w_name' : q.highlighted.w_name if q.highlighted else q.w_name,
                    'e_name' : q.highlighted.e_name if q.highlighted else q.e_name,
                    'r_name' : q.highlighted.r_name if q.highlighted else q.r_name,
                    'image'  : q.champion_image,
                }
            ]

    or_data = {}
    if len(query_list) > 1:
        for q in query_list:
            sqs = SearchQuerySet().all()
            query_result = sqs.filter(champion_name=q).load_all().highlight()
            for r in query_result:
                if len(list(filter(lambda v : v['image'] == r.champion_image, and_data))) == 0:
                    data = {
                        'result' : r,
                        'page_title' : r.highlighted.champion_name if r.highlighted else r.champion_name,
                        'role' : r.highlighted.champion_role if r.highlighted else r.champion_role,
                        'link' : 'http://leagueofdowning.me/champions/' + str(r.champion_id),
                        'lore' : (r.highlighted.lore[:500] if r.highlighted else r.lore[:500]) if r.lore is not None else '',
                        'passive_name' : r.highlighted.passive_name if r.highlighted else r.passive_name,
                        'q_name' : r.highlighted.q_name if r.highlighted else r.q_name,
                        'w_name' : r.highlighted.w_name if r.highlighted else r.w_name,
                        'e_name' : r.highlighted.e_name if r.highlighted else r.e_name,
                        'r_name' : r.highlighted.r_name if r.highlighted else r.r_name,
                        'image'  : r.champion_image,
                    }

                    if q not in or_data:
                        or_data[q] = [data]
                    else:
                        or_data[q] += [data]
    
    context = RequestContext(request, {
        'query_string' : query,
        'query_list' : query_list,
        'and_entries' : and_data,
        'or_entries' : or_data,
    })
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
    # champion_id 0 is the dummy champion that doesn't actually exist
    if id == 0 :
        template = loader.get_template('app/error.html')
        context = RequestContext(request, {})
        return HttpResponse(template.render(context))  
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
                item = engine.execute('select item_id, image from "Item" where item_id= %s' % row1['item_id'])
                for i in item:
                    itemlist.append({'image' : re.sub("5.13.1", "5.2.1", i['image']), 'item_id' : i['item_id']})

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
            item_id = row['item_id']
            intoresult = engine.execute('select into_id as item_id from "ItemToItem" where from_id = %d' % int(item_id))
            fromresult = engine.execute('select from_id as item_id from "ItemToItem" where into_id = %d' % int(item_id))

            intolist = []
            for row1 in intoresult:
                item = engine.execute('select item_id, image from "Item" where item_id= %s' % row1['item_id'])
                for i in item:
                    intolist.append({'image' : re.sub("5.13.1", "5.2.1", i['image']), 'item_id' : i['item_id']})

            fromlist = []
            for row2 in fromresult:
                item = engine.execute('select item_id, image from "Item" where item_id= %s' % row2['item_id'])
                for i in item:
                    fromlist.append({'image' : re.sub("5.13.1", "5.2.1", i['image']), 'item_id' : i['item_id']})

                
            jsonout = {'item_id': row['item_id'], 'name': row['name'], 'description': row['description'], 'base_gold': row['base_gold'], 'sell_gold': row['sell_gold'], 'total_gold': row['total_gold'], 'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/' + row['image'][-8:], 'from_items' : fromlist, 'into_items' : intolist, 'num_from' : str(max(2, 12 // max(len(fromlist), 1))), 'num_into' : str(max(2, 12 // max(len(intolist), 1))) }

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

            champlist = []

            for row1 in result1:
                champ = engine.execute('select champion_id, image from "Champion" where champion_id= %s' % row1['champion_id'])
                for i in champ:
                    if row1['champion_id'] != 0 :
                        champlist.append({'champion_id' : i['champion_id'], 'image' : re.sub("5.13.1", "5.2.1", i['image'])})


            jsonout = {'player_id': row['player_id'], 'first_name': row['first_name'], 'last_name': row['last_name'], 'team_name': row['team_name'], 'ign': row['ign'], 'bio': row['bio'], 'image': re.sub("5.13.1", "5.2.1", row['image']), 'role': row['role'], 'kda': round(row['kda'], 2), 'gpm': round(row['gpm'], 2), 'total_gold': row['total_gold'], 'games_played': row['games_played'], 'most_played_champions' : champlist}

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

    result = engine.execute('select * from "Champion" where name != \'dummy\'')
    List = {}
    for row in result:
        champ_name = row['champion_id']
        List[row['champion_id']] = {'champion_id': row['champion_id'], 'name': row['name'], 'role': row['role'], 'title': row['title'], 'lore': row['lore'],  'image': re.sub("5.13.1", "5.2.1", row['image']), 'passive_name': row['passive_name'], 'passive_image': re.sub("5.13.1", "5.2.1", row['passive_image']), 'passive_description': row['passive_description'], 'q_name': row['q_name'], 'q_image': re.sub("5.13.1", "5.2.1", row['q_image']), 'q_description': row['q_description'], 'w_name': row['w_name'], 'w_image': re.sub("5.13.1", "5.2.1", row['w_image']), 'w_description': row['w_description'], 'e_name': row['e_name'], 'e_image': re.sub("5.13.1", "5.2.1", row['e_image']), 'e_description': row['e_description'], 'r_name': row['r_name'], 'r_image': re.sub("5.13.1", "5.2.1", row['r_image']), 'r_description': row['r_description']}
        result1 = engine.execute('select c.item_id, i.name from "ChampionToItem" c inner join "Item" i on c.item_id = i.item_id where champion_id = %s' % champ_name)
        dic = List[champ_name]
        dic_name = List[champ_name]
        itemNameList = []
        itemlist = []
        for row1 in result1:
            itemlist.append(row1['item_id'])
            itemNameList.append(row1['name'])
        dic['recommended_items'] = itemlist
        dic_name['recommended_item_names'] = itemNameList

    return HttpResponse(json.dumps(List), content_type='application/json')

def Champion_ID_API(request, id):
    if int(id) == 0 :
        h = HttpResponse(json.dumps({"error": "Champion ID " + id + " does not exist."}),   content_type="application/json")
        h.status_code = 404
        return h  
    else:
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
        player_name = row['player_id']
        result1 = engine.execute('select champion_id from "PlayerToChampion" where player_id = %d' % player_name)

        itemlist = []
        for row1 in result1:
            if row1['champion_id'] != 0 :
                itemlist.append(row1['champion_id'])

        List[row['player_id']] = {'player_id': row['player_id'], 'first_name': row['first_name'], 'last_name': row['last_name'], 'team_name': row['team_name'], 'ign': row['ign'], 'bio': row['bio'], 'image': re.sub("5.13.1", "5.2.1", row['image']), 'role': row['role'], 'kda': row['kda'], 'gpm': row['gpm'], 'total_gold': row['total_gold'], 'games_played': row['games_played'], 'most_played_champions' : itemlist}

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
        item_id = row['item_id']
        intoresult = engine.execute('select into_id from "ItemToItem" where from_id = %d' % item_id)
        fromresult = engine.execute('select from_id from "ItemToItem" where into_id = %d' % item_id)

        intolist = []
        for row1 in intoresult:
            intolist.append(row1['into_id'])

        fromlist = []
        for row2 in fromresult:
            fromlist.append(row2['from_id'])

        List[row['item_id']] = {'item_id': row['item_id'], 'name': row['name'], 'description': row['description'], 'base_gold': row['base_gold'], 'sell_gold': row['sell_gold'], 'total_gold': row['total_gold'], 'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/' + row['image'][-8:], 'from_items' : fromlist, 'into_items' : intolist}

    return HttpResponse(json.dumps(List), content_type='application/json')

def Item_ID_API(request, id):
    try:
        int(id)
        engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

        result = engine.execute('select * from "Item" where item_id=' + id)
        jsonout = {}
        for row in result:
            item_id = row['item_id']
            intoresult = engine.execute('select into_id from "ItemToItem" where from_id = %d' % item_id)
            fromresult = engine.execute('select from_id from "ItemToItem" where into_id = %d' % item_id)

            intolist = []
            for row1 in intoresult:
                intolist.append(row1['into_id'])

            fromlist = []
            for row2 in fromresult:
                fromlist.append(row2['from_id'])


            jsonout = {'item_id': row['item_id'], 'name': row['name'], 'description': row['description'], 'base_gold': row['base_gold'], 'sell_gold': row['sell_gold'], 'total_gold': row['total_gold'], 'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/' + row['image'][-8:], 'from_items' : fromlist, 'into_items' : intolist}
        if jsonout == {}:
            h = HttpResponse(json.dumps({"error": "Item ID " + id + " does not exist."}),   content_type="application/json")
            h.status_code = 404
            return h

        return HttpResponse(json.dumps(jsonout), content_type='application/json')    
    except ValueError:
        h = HttpResponse(json.dumps({"error": "Item ID " + id + " does not exist."}),   content_type="application/json")
        h.status_code = 404
        return h


