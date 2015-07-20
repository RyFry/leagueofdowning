from haystack.query import SearchQuerySet

from .search_indexes import Champion, Item, Player


def search(query):
    """
    Returns a tuple of the result of the query as a whole string (i.e. the 'and' result)
    and the query as a list of individuals queries (i.e. the 'or' result)
    """
    player_search(
    
    

def player_search(query):


def champion_search_and(query):


def item_search_and(query):




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
    
