from haystack.query import SearchQuerySet

from .search_indexes import Champion, Item, Player


def lod_search(query):
    """
    Returns a tuple of the result of the query as a whole string (i.e. the 'and' result)
    and the query as a list of individuals queries (i.e. the 'or' result)

    and_data is a dictionaryies with 3 elements each, 'Champion', 'Item', and 'Player'
    These three keys map to a list of dictionaries matching search results for the query
    and_data['Champion'] = [{
    'page_title' : q.champion_name 
    'role' : qed.champion_role 
    'link' : 'http://leagueofdowning.me/champions/' + str(q.champion_id),
    'lore' : (qed.lore[:500] 
    'passive_name' : qed.passive_name 
    'q_name' : qed.q_name 
    'w_name' : qed.w_name 
    'e_name' : qed.e_name 
    'r_name' : qed.r_name 
    'image'  : q.champion_image,
    }, ...]
    
    and_data['Player'] = [{
    'page_title' : first_name + ign + last_name,
    'role' : player_role,
    'link' : link to player's page,
    'bio' : player_bio,
    'team_name' : player's team name,
    }]

    and_data['Item'] = [{
    'page_title' : item_name,
    'description' : ,
    'image' : ,
    }]

    The or_data is a list of N 3 key dictionaries, where N is the length of the query split on spaces.
    Each of the dictionaries in or_data is formatted exactly as the dictionaries in and_data. The or_data
    is treated as a list of queries, where and_data just does one query.
    """
    and_data = {}
    
    or_data = {}
    for q in query.split(' '):
        or_data[q] = {}

    and_data['Player'] = player_search(query)
    for q in query.split(' '):
        or_data[q]['Player'] = player_search(q)

    and_data['Champion'] = champion_search(query)
    for q in query.split(' '):
        or_data[q]['Champion'] = champion_search(q)
    
    and_data['Item'] = item_search(query)
    for q in query.split(' '):
        or_data[q]['Item'] = item_search(q)

    return and_data, or_data
    
    

def player_search(query):
    def get_player_results(sqs):
        query_result = list(sqs.filter(first_name=query).load_all())
        query_result += list(sqs.filter(ign=query).load_all())
        query_result += list(sqs.filter(last_name=query).load_all())
        query_result += list(sqs.filter(player_role=query).load_all())
        query_result += list(sqs.filter(bio=query).load_all())
        query_result += list(sqs.filter(team_name=query).load_all())
        return query_result

    and_data = []

    sqs = SearchQuerySet().models(Player).load_all()

    query_result = get_player_results(sqs)

    for q in query_result:
        if q is not None:
            and_data += [
                {
                    'text' : q.text,
                    'page_title' : q.first_name + ' "' + q.ign + '" ' + q.last_name,
                    'role' : q.player_role,
                    'link' : 'http://leagueofdowning.link/players/' + str(q.player_id),
                    'bio' : q.bio,
                    'team_name' : q.team_name,
                    'image' : q.player_image,
                }
            ]
    
    and_data = remove_duplicates(and_data)

    return and_data



def champion_search(query):
    def get_champ_results(sqs):
        query_result = list(sqs.filter(champion_name=query).load_all())
        query_result += list(sqs.filter(champion_role=query).load_all())
        query_result += list(sqs.filter(lore=query).load_all())
        query_result += list(sqs.filter(passive_name=query).load_all())
        query_result += list(sqs.filter(q_name=query).load_all())
        query_result += list(sqs.filter(w_name=query).load_all())
        query_result += list(sqs.filter(e_name=query).load_all())
        query_result += list(sqs.filter(r_name=query).load_all())
        return query_result

    and_data = []

    sqs = SearchQuerySet().models(Champion).load_all()

    query_result = get_champ_results(sqs)

    for q in query_result:
        if q is not None:
            and_data += [
                { 
                    'page_title' : q.champion_name,
                    'role' : q.champion_role, 
                    'link' : 'http://leagueofdowning.link/champions/' + str(q.champion_id),
                    'lore' : q.lore,
                    'passive_name' : q.passive_name,
                    'q_name' : q.q_name,
                    'w_name' : q.w_name,
                    'e_name' : q.e_name,
                    'r_name' : q.r_name,
                    'image'  : q.champion_image.replace('5.13.1', '5.2.1'),
                }
            ]
    
    and_data = remove_duplicates(and_data)

    return and_data



            



def item_search(query):
    def get_item_results(sqs):
        query_result = list(sqs.filter(item_name=query).load_all())
        query_result += list(sqs.filter(description=query).load_all())
        return query_result

    and_data = []

    sqs = SearchQuerySet().models(Item).load_all()

    query_result = get_item_results(sqs)


    for q in query_result:
        if q is not None:
            and_data += [
                { 
                    'page_title' : q.item_name,
                    'description' : q.item_description,
                    'link' : 'http://leagueofdowning.link/items/' + str(q.item_id),
                    'image' : q.item_image.replace('5.13.1', '5.2.1'),
                }
            ]
    
    and_data = remove_duplicates(and_data)

    return and_data
    


def remove_duplicates(data):
    unique = set()
    for d in data:
        unique.add(d['page_title'])

    result = list()
    for d in data:
        if d['page_title'] in unique:
            result.append(d)
            unique.discard(d['page_title'])

    return result
