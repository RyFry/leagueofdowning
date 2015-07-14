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

def players(request):
    template = loader.get_template('app/players.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def items(request):
    template = loader.get_template('app/items.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def test(request):
    template = loader.get_template('app/index.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))

def champions(request):
    template = loader.get_template('app/champions.html')
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))



#
# Champion Pages
#

def mundo(request):
    template = loader.get_template('app/champion.html')
    context = RequestContext(request, {
        'champion_name' : "Dr. Mundo",
        'image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/DrMundo.png",
        'passive_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img//passive/DrMundo_AdrenalineRush2.png",
        'q_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/InfectedCleaverMissileCast.png",
        'w_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/BurningAgony.png",
        'e_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/Masochism.png",
        'r_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/Sadism.png",
        'passive' : "Adrenaline Rush",
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

def azir(request):
    template = loader.get_template('app/champion.html')
    context = RequestContext(request, {
        'champion_name' : "Azir",
        'image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Azir.png",
        'passive_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/passive/Azir_Passive.png",
        'q_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/AzirQ.png",
        'w_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/AzirW.png",
        'e_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/AzirE.png",
        'r_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/AzirR.png",
        'passive' : "Shurima's Legacy",
        'passive_description' : "Azir can summon the Disc of the Sun from the ruins of allied or enemy turrets. Additionally, Azir gains Attack Speed based on the amount of Cooldown Reduction he has.",
        'q' : "Conquering Sands",
        'q_description' : "Azir sends all Sand Soldiers toward a target location. Sand Soldiers deal magic damage to all targets they pass through and apply a stacking slow for 1 second.\n\nAzir sends all Sand Soldiers toward a target location. Sand Soldiers deal 65/85/105/125/145 (+50% Ability Power) magic damage to all enemies they pass through and apply a stacking 25% slow for 1 second.",
        'w' : "Arise!",
        'w_description' : "Azir summons a Sand Soldier to attack nearby targets for him, replacing his basic attack against targets within the soldier's range. Their attacks deal magic damage to enemies in a line.\n\nAzir summons a Sand Soldier for 9 seconds. When Azir attacks an enemy in a soldier's range, the soldier attacks instead of Azir, dealing 0 (+60% Ability Power) magic damage to enemies in a line. If multiple soldiers strike the same target, each soldier after the first deals 25% damage. Soldiers attack even if Azir himself isn't in basic attack range.Azir can store up to {{ maxammo }} Sand Soldiers at a time. A new soldier becomes available every 0 seconds. Moving too far away from soldiers deactivates them. Sand Soldiers expire twice as fast when near an enemy turret.Azir can expend a soldier to damage an enemy turret by summoning it on top of the turret. This deals 0 (+40% Ability Power) magic damage to the turret.",
        'e' : "Shifting Sands",
        'e_description' : "Azir dashes to one of his Sand Soldiers, knocking up and damaging enemies. If he hits an enemy champion, he gains a shield.\n\nAzir dashes to one of his Sand Soldiers, damaging enemies hit for 60/90/120/150/180 (+40% Ability Power) magic damage and knocking them up for 0.5 seconds. If Azir hits an enemy champion, he stops and gains a 4 second shield that absorbs 80/120/160/200/240 (+0) damage.",
        'r' : "Emperor's Divide",
        'r_description' : "Azir summons a wall of soldiers which charge forward, knocking back and damaging enemies.\n\nAzir summons a wall of armored soldiers that charge forward, knocking back enemies and dealing 150/225/300 (+60% Ability Power) magic damage. The soldiers then remain as a wall for 5/6/7 seconds.Enemies will be stopped by Emperor's Divide, even if they attempt to dash over the wall, but Azir and his allies can pass freely and gain 20% Movement Speed for 1 second when they pass through the wall.Emperor's Divide does not interact with Azir's basic attacks or spells.",
    })
    return HttpResponse(template.render(context))

def ezreal(request):
    template = loader.get_template('app/champion.html')
    context = RequestContext(request, {
        'champion_name' : "Ezreal",
        'image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Ezreal.png",
        'passive_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/passive/Ezreal_RisingSpellForce.png",
        'q_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/EzrealMysticShot.png",
        'w_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/EzrealEssenceFlux.png",
        'e_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/EzrealArcaneShift.png",
        'r_image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/spell/EzrealTrueshotBarrage.png",
        'passive' : "Rising Spell Force",
        'passive_description' : "Hitting a target with any of Ezreal's abilities increases his Attack Speed by 10% for 6 seconds (effect stacks up to 5 times). ",
        'q' : "Mystic Shot",
        'q_description' : "Ezreal fires a damaging bolt of energy which reduces all of his cooldowns by 1 second if it strikes an enemy unit.\n\nEzreal fires a bolt of energy, dealing 35/55/75/95/115 (+0) (+40% Ability Power) physical damage (applies on-hit effects). Ezreal's cooldowns are reduced by 1 second if Mystic Shot hits a target.",
        'w' : "Essence Flux",
        'w_description' : "Ezreal fires a fluctuating wave of energy, dealing magic damage to enemy champions, while increasing the Attack Speed of allied champions.\n\nEzreal fires a wave of energy that damages all enemy champions it passes through for 70/115/160/205/250 (+80% Ability Power) magic damage. If Ezreal or his Allied champions are hit by the wave, their Attack Speed is increased by 20/25/30/35/40% for 5 seconds.",
        'e' : "Arcane Shift",
        'e_description' : "Ezreal teleports to a target nearby location and fires a homing bolt which strikes the nearest enemy unit.\n\nEzreal teleports to a target nearby location and fires a homing bolt at the nearest enemy unit, dealing 75/125/175/225/275 (+75% Ability Power) magic damage.",
        'r' : "Trueshot Barrage",
        'r_description' : "Ezreal winds up for 1 second to fire a powerful barrage of energy missiles which do massive damage to each unit they pass through (deals 10% less damage to each unit it passes through).\n\nEzreal winds up for 1 second to fire a barrage of missiles dealing 350/500/650 (+100% bonus Attack Damage) (+90% Ability Power) magic damage to each unit it passes through. However, it deals 10% less damage for each unit it hits (minimum 30%).",
    })
    return HttpResponse(template.render(context))

#
# Item Pages
#

def athenes(request):
    template = loader.get_template('app/item.html')
    context = RequestContext(request, {
        'item_name' : "Athene's Unholy Grail",
        'image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/item/3174.png",
        'stats' : "+60 Ability Power\n+25 Magic Resist\n+20% Cooldown Reduction\n+100% Base Mana Regen\n\nUNIQUE Passive: Restores 30% of maximum Mana on kill or assist.\nUNIQUE Passive - Mana Font: Restores 2% of missing Mana every 5 seconds.",
        'recommended_roles' : "Mage",
        'cost' : "2700 g"
    })
    return HttpResponse(template.render(context))

def rabadons(request):
    template = loader.get_template('app/item.html')
    context = RequestContext(request, {
        'item_name' : "Rabadon's Deathcap",
        'image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/item/3089.png",
        'stats' : "+120 Ability Power\n\nUNIQUE Passive: Increases Ability Power by 30%.",
        'recommended_roles' : "Mage",
        'cost' : "3300 g"
    })
    return HttpResponse(template.render(context))

def sorc_shoes(request):
    template = loader.get_template('app/item.html')
    context = RequestContext(request, {
        'item_name' : "Sorcerer's Shoes",
        'image' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/item/3020.png",
        'stats' : "+15 Magic Penetration\n\nUNIQUE Passive - Enhanced Movement: +45 Movement Speed",
        'recommended_roles' : "Mage",
        'cost' : "1100 g"
    })
    return HttpResponse(template.render(context))

#
# Player Pages
#

def balls(request):
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {
        'player_name' : 'An "Balls" Le',
        'image' : "http://hydra-media.cursecdn.com/lol.gamepedia.com/b/bc/BALLS.C9_lolesports.PP_0.jpg",
        'age' : "21",
        'position' : "Top",
        'total_wins' : "3",
        'season_record' : "3-9",
        'team' : "Cloud9 (C9)",
        'kda' : "1.8",
        'avg_gpm' : "21",
        'avg_gold' : "11k",
        'most_played' : {
            'first': "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Fizz.png",
            'second' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Maokai.png",
            'third' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Rumble.png"
        }        
    })
    return HttpResponse(template.render(context))

def bjergsen(request):
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {
        'player_name' : 'Søren "Bjergsen" Bjerg',
        'image' : "http://hydra-media.cursecdn.com/lol.gamepedia.com/7/7f/TSM_Bjergsen.jpg",
        'age' : "19",
        'position' : "Mid",
        'total_wins' : "9",
        'season_record' : "9-3",
        'team' : "Team SoloMid (TSM)",
        'kda' : "4.7",
        'avg_gpm' : "408",
        'avg_gold' : "18k",
        'most_played' : {
            'first': "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Azir.png",
            'second' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Ezreal.png",
            'third' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Ekko.png"
        }        
    })
    return HttpResponse(template.render(context))

def doublelift(request):
    template = loader.get_template('app/player.html')
    context = RequestContext(request, {
        'player_name' : 'Yiliang "Doublelift" Peng',
        'image' : "http://hydra-media.cursecdn.com/lol.gamepedia.com/b/b8/DOUBLELIFT.CLG_lolesports.PP_.jpg",
        'age' : "21",
        'position' : "ADC",
        'total_wins' : "7",
        'season_record' : "7-5",
        'team' : "Counter Logic Gaming (CLG)",
        'kda' : "4.1",
        'avg_gpm' : "426",
        'avg_gold' : "16k",
        'most_played' : {
            'first': "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Ashe.png",
            'second' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Sivir.png",
            'third' : "http://ddragon.leagueoflegends.com/cdn/5.10.1/img/champion/Kalista.png"
        }        
    })
    return HttpResponse(template.render(context))


