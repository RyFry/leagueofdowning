from sqlalchemy import create_engine
from app.database import database

import re



def search (query_string) :
    """
    Returns a list of urls that need to be linked after
    performing the desired search. i.e. if we search for:
    "annie"
    Then this function will return something like:
    "champions/1"
    where 1 is the id of Annie
    """
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')
    
    terms = re.split(" ", query_string)
    
    

