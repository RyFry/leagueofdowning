from sqlalchemy import create_engine
from app.database import database

import re


def search (terms) :
    """
    Returns a list of urls that need to be linked after
    performing the desired search. i.e. if we search for:
    "annie"
    Then this function will return something like:
    "champions/1"
    where 1 is the id of Annie
    """
    
