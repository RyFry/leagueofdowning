from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import relationship, sessionmaker, backref
from app.database import database

import json


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

#
# Table Pages
#

def players(request):
    template = loader.get_template('app/players.html')
    context = RequestContext(request, {
        'playerdata' : ''
    })
    return HttpResponse(template.render(context))

def items(request):
    template = loader.get_template('app/items.html')

    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

    result = engine.execute('select * from "Item"')
    List = {}
    for row in result:
        List[row['item_id']] = {'item_id': row['item_id'], 'name': row['name'], 'description': row['description'], 'base_gold': row['base_gold'], 'sell_gold': row['sell_gold'], 'total_gold': row['total_gold'], 'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/' + row['image'][-8:]}

    jsonout = json.dumps(List)
    jsonout = jsonout[1:-1]

    context = RequestContext(request, {
        'itemdata' : '' + jsonout
    })
    return HttpResponse(template.render(context))

def champions(request):
    template = loader.get_template('app/champions.html')
    context = RequestContext(request, {
        'championdata' : ''
    })
    return HttpResponse(template.render(context))



#
# Champion Pages
#

def champion(request, id):
    template = loader.get_template('app/champion.html')
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

    result = engine.execute('select * from "Champion" where champion_id=' + id)
    jsonout = {}
    for row in result:
        champ_name = row['champion_id']
        result1 = engine.execute('select item_id from "ChampionToItem" where champion_id = %s' % champ_name)

        itemlist = []
        for row1 in result1:
            itemlist.append(row1['item_id'])

        jsonout = {'champion_id': row['champion_id'], 'name': row['name'], 'role': row['role'], 'title': row['title'], 'lore': row['lore'],  'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/champion/' + row['image'][58:], 'passive_name': row['passive_name'], 'passive_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/passive/' + row['passive_image'][-8:], 'passive_description': row['passive_description'], 'q_name': row['q_name'], 'q_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['q_image'][-8:], 'q_description': row['q_description'], 'w_name': row['w_name'], 'w_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['w_image'][-8:], 'w_description': row['w_description'], 'e_name': row['e_name'], 'e_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['e_image'][-8:], 'e_description': row['e_description'], 'r_name': row['r_name'], 'r_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['r_image'][-8:], 'r_description': row['r_description'], 'recommended_items': itemlist}

    context = RequestContext(request, jsonout)
    return HttpResponse(template.render(context))

#
# Item Pages
#

def item(request, id):
    template = loader.get_template('app/item.html')
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

    result = engine.execute('select * from "Item" where item_id=' + id)
    jsonout = {}

    for row in result:
        jsonout = {'item_id': row['item_id'], 'name': row['name'], 'description': row['description'], 'base_gold': row['base_gold'], 'sell_gold': row['sell_gold'], 'total_gold': row['total_gold'], 'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/' + row['image'][-8:]}

    context = RequestContext(request, jsonout)
    return HttpResponse(template.render(context))

#
# Player Pages
#

def player(request, id):
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {
        'id' : id
    })
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
        List[row['champion_id']] = {'champion_id': row['champion_id'], 'name': row['name'], 'role': row['role'], 'title': row['title'], 'lore': row['lore'],  'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/champion/' + row['image'][-8:], 'passive_name': row['passive_name'], 'passive_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/passive/' + row['passive_image'][-8:], 'passive_description': row['passive_description'], 'q_name': row['q_name'], 'q_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['q_image'][-8:], 'q_description': row['q_description'], 'w_name': row['w_name'], 'w_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['w_image'][-8:], 'w_description': row['w_description'], 'e_name': row['e_name'], 'e_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['e_image'][-8:], 'e_description': row['e_description'], 'r_name': row['r_name'], 'r_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['r_image'][-8:], 'r_description': row['r_description']}
        result1 = engine.execute('select item_id from "ChampionToItem" where champion_id = %s' % champ_name)
        dic = List[champ_name]
        itemlist = []
        for row1 in result1:
            itemlist.append(row1['item_id'])
        dic['recommended_items'] = itemlist

    return HttpResponse(json.dumps(List), content_type='application/json')

def Champion_ID_API(request, id):
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

    result = engine.execute('select * from "Champion" where champion_id=' + id)
    jsonout = {}
    for row in result:
        champ_name = row['champion_id']
        result1 = engine.execute('select item_id from "ChampionToItem" where champion_id = %s' % champ_name)

        itemlist = []
        for row1 in result1:
            itemlist.append(row1['item_id'])

        jsonout = {'champion_id': row['champion_id'], 'name': row['name'], 'role': row['role'], 'title': row['title'], 'lore': row['lore'],  'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/champion/' + row['image'][-8:], 'passive_name': row['passive_name'], 'passive_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/passive/' + row['passive_image'][-8:], 'passive_description': row['passive_description'], 'q_name': row['q_name'], 'q_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['q_image'][-8:], 'q_description': row['q_description'], 'w_name': row['w_name'], 'w_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['w_image'][-8:], 'w_description': row['w_description'], 'e_name': row['e_name'], 'e_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['e_image'][-8:], 'e_description': row['e_description'], 'r_name': row['r_name'], 'r_image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/spell/' + row['r_image'][-8:], 'r_description': row['r_description'], 'recommended_items': itemlist}

    if jsonout == {}:
        h = HttpResponse(json.dumps({"error": "Champion " + id + " does not exist."}),   content_type="application/json")
        h.status_code = 404
        return h

    return HttpResponse(json.dumps(jsonout), content_type='application/json')    


def Player_List_API(request):
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def Player_ID_API(request, id):
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {
        'id' : id
    })
    return HttpResponse(template.render(context))

def Item_List_API(request):
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

    result = engine.execute('select * from "Item"')
    List = {}
    for row in result:
        List[row['item_id']] = {'item_id': row['item_id'], 'name': row['name'], 'description': row['description'], 'base_gold': row['base_gold'], 'sell_gold': row['sell_gold'], 'total_gold': row['total_gold'], 'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/' + row['image'][-8:]}

    return HttpResponse(json.dumps(List), content_type='application/json')

def Item_ID_API(request, id):
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

    result = engine.execute('select * from "Item" where item_id=' + id)
    jsonout = {}
    for row in result:
        jsonout = {'item_id': row['item_id'], 'name': row['name'], 'description': row['description'], 'base_gold': row['base_gold'], 'sell_gold': row['sell_gold'], 'total_gold': row['total_gold'], 'image': 'http://ddragon.leagueoflegends.com/cdn/5.2.1/img/item/' + row['image'][-8:]}
    if jsonout == {}:
        h = HttpResponse(json.dumps({"error": "Item " + id + " does not exist."}),   content_type="application/json")
        h.status_code = 404
        return h

    return HttpResponse(json.dumps(jsonout), content_type='application/json')    
    


