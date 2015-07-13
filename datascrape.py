import json
import pprint
from urllib.request import urlopen
import urllib
import re
import requests

raw_playerlist = '{"4388":{"kda":1.9719626168224,"average total_gold":11478.392857143,"gpm":315.52104978975},"4332":{"kda":2.4742268041237,"average total_gold":10785.774193548,"gpm":294.57645037664},"3190":{"kda":2.0082644628099,"average total_gold":13179.838709677,"gpm":359.96211620633},"4334":{"kda":2.3888888888889,"average total_gold":13574.677419355,"gpm":370.74578212414},"4335":{"kda":1.7906976744186,"average total_gold":7749.4193548387,"gpm":211.64882604291},"2811":{"kda":4.0526315789474,"average total_gold":14032,"gpm":344.28529125598},"663":{"kda":4.0327868852459,"average total_gold":11456.517241379,"gpm":281.09395490503},"892":{"kda":4.6071428571429,"average total_gold":15369.137931034,"gpm":377.09293963366},"2178":{"kda":6.275,"average total_gold":16068.172413793,"gpm":394.24425737129},"2167":{"kda":3.0123456790123,"average total_gold":8773.8275862069,"gpm":215.27221963704},"3645":{"kda":2.4404761904762,"average total_gold":13514.464285714,"gpm":341.44371757275},"3646":{"kda":3.3880597014925,"average total_gold":11658.142857143,"gpm":294.54364989849},"4389":{"kda":2.8405797101449,"average total_gold":14991.321428571,"gpm":378.75659824047},"3722":{"kda":3.9661016949153,"average total_gold":15323.714285714,"gpm":387.15452289646},"4390":{"kda":2,"average total_gold":8199.8461538462,"gpm":216.62591024555},"4341":{"kda":1.4943820224719,"average total_gold":11335.739130435,"gpm":299.87578116014},"4342":{"kda":1.5434782608696,"average total_gold":9913.72,"gpm":263.57397330686},"4344":{"kda":1.6976744186047,"average total_gold":12678.5,"gpm":336.12018336801},"4346":{"kda":2.5689655172414,"average total_gold":13439.416666667,"gpm":356.29287331775},"4348":{"kda":1.0649350649351,"average total_gold":7096,"gpm":199.22091595017},"4343":{"kda":3,"average total_gold":11733,"gpm":334.90960989534},"4345":{"kda":3,"average total_gold":9983,"gpm":284.95718363463},"4347":{"kda":1.9032258064516,"average total_gold":8347.4444444444,"gpm":202.81754780652},"371":{"kda":3.4615384615385,"average total_gold":12850.666666667,"gpm":351.44452463251},"372":{"kda":3.8481012658228,"average total_gold":11697.206896552,"gpm":301.56374088781},"1015":{"kda":3.8481012658228,"average total_gold":14840.862068966,"gpm":382.60979079002},"918":{"kda":3.7435897435897,"average total_gold":14698.551724138,"gpm":378.94091151544},"370":{"kda":3.9466666666667,"average total_gold":8595.5,"gpm":219.32957669466},"2147":{"kda":4.9259259259259,"average total_gold":14147.615384615,"gpm":365.78957836118},"2163":{"kda":5.1698113207547,"average total_gold":11459.269230769,"gpm":296.28182179793},"686":{"kda":4.8974358974359,"average total_gold":15032.388888889,"gpm":383.97814621225},"1016":{"kda":6.1333333333333,"average total_gold":14639,"gpm":378.49443118536},"4077":{"kda":3.9272727272727,"average total_gold":8343.9047619048,"gpm":220.1742408377},"991":{"kda":4.1694915254237,"average total_gold":12997.666666667,"gpm":316.91606086603},"2807":{"kda":5.0877192982456,"average total_gold":12786.740740741,"gpm":311.77315211993},"2160":{"kda":5.7352941176471,"average total_gold":14758.619047619,"gpm":362.90977927831},"2805":{"kda":5.3913043478261,"average total_gold":15556.571428571,"gpm":377.78317432784},"4391":{"kda":3.4583333333333,"average total_gold":8195.2222222222,"gpm":209.4179443498},"2125":{"kda":2.3529411764706,"average total_gold":12792.136363636,"gpm":313.69584602809},"2803":{"kda":2.7820512820513,"average total_gold":11688.12,"gpm":284.11979191988},"2801":{"kda":2.8783783783784,"average total_gold":14558.925925926,"gpm":359.43582553568},"874":{"kda":2.6666666666667,"average total_gold":15027.904761905,"gpm":374.84232406216},"3777":{"kda":2.7954545454545,"average total_gold":8274.1481481481,"gpm":204.27504648115},"877":{"kda":5.7083333333333,"average total_gold":14379.961538462,"gpm":400.04172908196},"4162":{"kda":3.25,"average total_gold":13002.5,"gpm":294.22968131246},"880":{"kda":4.0555555555556,"average total_gold":17070.857142857,"gpm":398.7852494577},"881":{"kda":8.15625,"average total_gold":14464.730769231,"gpm":402.39995720094},"882":{"kda":8.2222222222222,"average total_gold":8796.0384615385,"gpm":244.70040659105},"693":{"kda":5.4090909090909,"average total_gold":10967.272727273,"gpm":318.38135034088},"692":{"kda":6.1764705882353,"average total_gold":14156.210526316,"gpm":423.60500826837},"2151":{"kda":4.921875,"average total_gold":13597.821428571,"gpm":352.43277434086},"2812":{"kda":6.2,"average total_gold":11375.545454545,"gpm":293.37892227736},"886":{"kda":6.8936170212766,"average total_gold":15168.678571429,"gpm":393.14676252333},"369":{"kda":5.5333333333333,"average total_gold":15199.178571429,"gpm":393.93727147904},"894":{"kda":4.0963855421687,"average total_gold":9058.25,"gpm":234.7746802635},"2800":{"kda":4.6216216216216,"average total_gold":11976.411764706,"gpm":311.40868767207},"4331":{"kda":2.3636363636364,"average total_gold":12462,"gpm":321.09361580303},"3648":{"kda":4.3793103448276,"average total_gold":8625.5333333333,"gpm":209.9805247498},"4386":{"kda":5.1818181818182,"average total_gold":15471.666666667,"gpm":366.43421052632},"934":{"kda":5.75,"average total_gold":16239.846153846,"gpm":397.69803145898},"2808":{"kda":4.5,"average total_gold":8914.6111111111,"gpm":212.49155796862},"4643":{"kda":3.2631578947368,"average total_gold":14070.625,"gpm":374.07366380504},"2152":{"kda":1.375,"average total_gold":9450.5,"gpm":256.57466063348},"2802":{"kda":5.8888888888889,"average total_gold":16571.6,"gpm":383.80915618004},"3644":{"kda":0.25,"average total_gold":5202,"gpm":188.82032667877},"1017":{"kda":3.8461538461538,"average total_gold":9476,"gpm":225.8700143016},"662":{"kda":1.6428571428571,"average total_gold":13116.666666667,"gpm":344.11893310013},"2126":{"kda":12,"average total_gold":13896,"gpm":387.79534883721},"4683":{"kda":2.7333333333333,"average total_gold":15594.2,"gpm":315.28912252325},"4685":{"kda":0.8,"average total_gold":10346.5,"gpm":291.93040206913}}'

itemsurl = 'http://ddragon.leagueoflegends.com/cdn/5.2.1/data/en_US/item.json'

championlisturl = 'http://ddragon.leagueoflegends.com/cdn/5.2.1/data/en_US/champion.json'

playerlisturl = 'http://na.lolesports.com/api/all-player-stats.json'

playerurl = 'http://na.lolesports.com/api/player/'

playerurl1 = 'http://na.lolesports.com/api/playerStats.json'

playerurl2 = 'http://na.lolesports.com:80/api/all-player-champs/' 

championurl = 'http://ddragon.leagueoflegends.com/cdn/5.2.1/data/en_US/champion/'

teamurl = 'http://na.lolesports.com:80/api/team/'
 


pp = pprint.PrettyPrinter(indent=1)


playerlist = json.loads(raw_playerlist)


entries = ['bio', 'firstname', 'lastname', 'name', 'photoUrl', 'role']
entries1 = ['kda', 'gpm', 'totalGold', 'gamesPlayed']
player_data = {}
for k in playerlist :
    tempurl = playerurl + k + ".json"
    tempurl1 = playerurl1 + "?playerId=" + k
    player = json.loads(requests.get(tempurl).text)
    player1 = json.loads(requests.get(tempurl1).text)
    tempurl3 = teamurl + str(player.get('teamId')) + '.json'
    player3 = json.loads(requests.get(tempurl3).text)
    #pp.pprint(player)
    player_data[k] = {}
    player_data[k]['teamName'] = player3.get('name')
    player_data[k]['id'] = k
    for i in entries :
        player_data[k][i] = player.get(i) 
    for j in entries1 :
        player_data[k][j] = player1['tournaments'][0].get(j)
        tempurl2 = playerurl2 + k + ".json?tournamentId=" + str(player1['tournaments'][0].get('tournamentId'))
        player2 = json.loads(requests.get(tempurl2).text)
        championarray = []
        for p in player2[k] :
            championarray.append(p.get('cid'))
        player_data[k]['champions'] = championarray
    #pp.pprint(player_data[k])  
        
with open('players', 'w') as outfile:
    json.dump(player_data, outfile)

item_info = urlopen(itemsurl).info()
raw_items = urlopen(itemsurl).read().decode(item_info.get_content_charset('utf8'))
items = json.loads(raw_items)   

entries = ['description', 'gold','name']
item_data = {}
for k, v in items['data'].items() :
    item_data[k] = {}
    item_data[k]['image'] = 'http://ddragon.leagueoflegends.com/cdn/5.13.1/img/item/' + v['image']['full']
    try:
        item_data[k]['fromItem'] = v['from']
    except KeyError :
        item_data[k]['fromItem'] = []
    item_data[k]['intoItem'] = v['into']
    for i in entries :
        item_data[k][i] = v[i]
        if i == 'description' :
            item_data[k][i] = re.sub("<br>", "\n", item_data[k][i])
            item_data[k][i] = re.sub("<.*?>", "", item_data[k][i])
    #pp.pprint(item_data[k])

with open('items', 'w') as outfile1:
    json.dump(item_data, outfile1)


championlist_info = urlopen(championlisturl).info()
raw_championlist = urlopen(championlisturl).read().decode(championlist_info.get_content_charset('utf8'))
championlist = json.loads(raw_championlist)    

entries = ['lore', 'key', 'name', 'title'] #spells, passive, items

champion_data = {}

for k in championlist["data"] :
    tempurl = championurl + k + ".json"
    champion_info = urlopen(tempurl).info()
    raw_champion = urlopen(tempurl).read().decode(champion_info.get_content_charset('utf8'))
    championdata = json.loads(raw_champion)
    #pp.pprint(championdata)
    for k1, champion in championdata.items() :
        if(k1 == 'data') :
            for k2, v in champion.items() :
                champion_data[k1] = {}
                champion_data[k1]['passive_description'] = v['passive']['description']
                champion_data[k1]['passive_image'] = 'http://ddragon.leagueoflegends.com/cdn/5.13.1/img/passive/' + v['passive']['image']['full']
                champion_data[k1]['passive_name'] = v['passive']['name']
                
                champion_data[k1]['q_description'] = v['spells'][0]['description']
                champion_data[k1]['q_image'] = 'http://ddragon.leagueoflegends.com/cdn/5.13.1/img/spell/' + v['spells'][0]['image']['full']
                champion_data[k1]['q_name'] =  v['spells'][0]['name']                 
                champion_data[k1]['w_description'] = v['spells'][1]['description']
                champion_data[k1]['w_image'] = 'http://ddragon.leagueoflegends.com/cdn/5.13.1/img/spell/' + v['spells'][1]['image']['full']
                champion_data[k1]['w_name'] =  v['spells'][1]['name']  
                champion_data[k1]['e_description'] = v['spells'][2]['description']
                champion_data[k1]['e_image'] = 'http://ddragon.leagueoflegends.com/cdn/5.13.1/img/spell/' + v['spells'][2]['image']['full']
                champion_data[k1]['e_name'] =  v['spells'][2]['name']  
                champion_data[k1]['r_description'] = v['spells'][3]['description']
                champion_data[k1]['r_image'] = 'http://ddragon.leagueoflegends.com/cdn/5.13.1/img/spell/' + v['spells'][3]['image']['full']
                champion_data[k1]['r_name'] =  v['spells'][3]['name']  
                champion_data[k1]['role'] = v['tags'][0]
                champion_data[k1]['image'] = 'http://ddragon.leagueoflegends.com/cdn/5.13.1/img/champion/' + v['image']['full']

                for i in range(len(v['recommended'])):
                    if(v['recommended'][i]['map'] == 'SR'):
                        item_array = []
                        x = v['recommended'][i]['blocks']
                        for p in range(len(x)):
                            item_array.append(x[p]['items'][0]['id'])
                        
                        champion_data[k1]['recommended_items'] = item_array
                    

                for i in entries :
                    if('lore' == i):
                        champion_data[k1][i] = re.sub("<br>", "\n", v[i])
                        champion_data[k1][i] = re.sub("<.*?>", "", champion_data[k1][i])
                    else:
                        champion_data[k1][i] = v[i]
                #pp.pprint(champion_data[k1])
    

with open('champions', 'w') as outfile2:
    json.dump(champion_data, outfile2)



#pp.pprint(player_data)


        







