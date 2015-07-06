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

def players(request):
    template = loader.get_template('app/players.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def mundo(request):
    template = loader.get_template('app/champions/champion.html')
    context = RequestContext(request, {
        'champion_name' : "Dr. Mundo",
        'image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/DrMundo.png",
        'passive_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img//passive/DrMundo_AdrenalineRush2.png",
        'q_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/InfectedCleaverMissileCast.png",
        'w_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/BurningAgony.png",
        'e_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/Masochism.png",
        'r_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/Sadism.png",
        'passive_name' : "Adrenaline Rush",
        'passive_description' : "Dr. Mundo regenerates 0.3% of his maximum Health each second.",
        'q' : "Infected Cleaver",
        'q_description' : "Dr. Mundo hurls his cleaver, dealing damage equal to a portion of his target's current Health and slowing them for a short time. Dr. Mundo delights in the suffering of others, so he is returned half of the Health cost when he successfully lands a cleaver (increased to the full Health cost on killing blows).\n\nDr. Mundo hurls his cleaver, dealing magic damage equal to 15/18/21/23/25% of the target's current Health (80/130/180/230/280 damage minimum) and slowing them by 40% for 2 seconds.Half of the Health cost is refunded if the cleaver hits a target (increased to the full Health cost on killing blows).",
        'w' : "Burning Agony",
        'w_description' : "Dr. Mundo drains his Health to reduce the duration of disables and deal continual damage to nearby enemies.\n\nToggle: Dr. Mundo deals 35/50/65/80/95 (+20% Ability Power) magic damage to nearby enemies, and reduces the duration of disables on Dr. Mundo by 10/15/20/25/30%.",
        'e' : "Masochism",
        'e_description' : "Masochism increases Dr. Mundo's Attack Damage by a flat amount for 5 seconds. In addition, Dr. Mundo also gains an additional amount of Attack Damage for each percentage of Health he is missing.\n\nIncreases Attack Damage by 40/55/70/85/100 for 5 seconds. Dr. Mundo gains an additional +0.4/0.55/0.7/0.85/1 Attack Damage for each percentage of Health he is missing.",
        'r' : "Sadism",
        'r_description' : "Dr. Mundo sacrifices a portion of his Health for increased Movement Speed and drastically increased Health Regeneration.\n\nDr. Mundo regenerates 0 health (40/50/60% of max health) over 12 seconds. Additionally, he gains 15/25/35% movement speed during this time.",
    })
    return HttpResponse(template.render(context))

def test(request):
    template = loader.get_template('app/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))


#role, lane, counters, abilities, essential items
