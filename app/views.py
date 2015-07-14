from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from sqlalchemy import create_engine, insert
from sqlalchemy.orm import relationship, sessionmaker, backref
import app.database




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
    context = RequestContext(request, {
        'itemdata' : ''
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
    context = RequestContext(request, {
        'id' : id,
        'champion_name' : id
    })
    return HttpResponse(template.render(context))

#
# Item Pages
#

def item(request, id):
    template = loader.get_template('app/item.html')
    context = RequestContext(request, {
        'id' : id
    })
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
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {
             
    })
    return HttpResponse(template.render(context))

def Champion_ID_API(request, id):
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {
        'id' : id       
    })
    return HttpResponse(template.render(context))

def Player_List_API(request):
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {
             
    })
    return HttpResponse(template.render(context))

def Player_ID_API(request, id):
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {
        'id' : id       
    })
    return HttpResponse(template.render(context))

def Item_List_API(request):
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')

    Session = sessionmaker(bind=engine)

    session = Session()   

    Item1 = session.query(database.Item).filter((database.Item).item_id == 3266).one()
   
    jsonout = {'id': Item1.id, 'description': Item1.description}

    return HttpResponse(json.dumps(jsonout), content_type="application/json")


def Item_ID_API(request, id):
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {
        'id' : id       
    })
    return HttpResponse(template.render(context))
    


