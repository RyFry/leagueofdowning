from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

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

def champion(request, name):
    template = loader.get_template('app/champion.html')
    context = RequestContext(request, {
        'champion_name' : name
    })
    return HttpResponse(template.render(context))

#
# Item Pages
#

def item(request, name):
    template = loader.get_template('app/item.html')
    context = RequestContext(request, {
        'item_name' : name
    })
    return HttpResponse(template.render(context))

#
# Player Pages
#

def player(request, name):
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {
        'player_name' : name       
    })
    return HttpResponse(template.render(context))

