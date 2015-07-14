from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from django.contrib.auth.models import Champion, Player, Item
from rest_framework import viewsets
from tutorial.quickstart.serializers import ChampionSerializer, PlayerSerializer, ItemSerializer

class ChampionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Champion.objects.all()
    serializer_class = ChampionSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


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

