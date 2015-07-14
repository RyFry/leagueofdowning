from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import relationship, sessionmaker

import json

player_to_champion = Table('PlayerToChampion', Base.metadata,
                           Column('player_id', Integer, ForeignKey('Player.id')),
                           Column('champion_id', Integer, ForeignKey('Champion.id')))
item_to_item = Table('ItemToItem', Base.metadata,
                     Column('item_id', Integer, ForeignKey('Item.id')),
                     Column('item_id', Integer, ForeignKey('Item.id')))
champion_to_item = Table('ChampionToItem', Base.metadata,
                         Column('champion_id', Integer, ForeignKey('Champion.id')),
                         Column('item_id', Integer, ForeignKey('Item.id')))



class Champion (Base) :
    __tablename__ = "Champion"

    # We need a primary key for SQLAlchemy to not puke on us, but we don't need
    # to actually use the primary key, because 'id' is our unique key
    dummy = Column(Integer, primary_key=True)
    id = Column(Integer)
    name = Column(String)
    role = Column(String)
    title = Column(String)
    lore = Column(String)
    image = Column(String)
    passive_name = Column(String)
    passive_image = Column(String)
    passive_description = Column(String)
    q_name = Column(String)
    q_image = Column(String)
    q_description = Column(String)
    w_name = Column(String)
    w_image = Column(String)
    w_description = Column(String)
    e_name = Column(String)
    e_image = Column(String)
    e_description = Column(String)
    r_name = Column(String)
    r_image = Column(String)
    r_description = Column(String)

    recommended_items = relationship('Item', secondary=champion_to_item)

    def __repr__ (self) :
        return ("<Champion(name='%s', role='%s', title='%s', image='%s', passive_name='%s',"
                "passive_image='%s', passive_description='%s', q_name='%s', q_image='%s',"
                "q_description='%s', w_name='%s', w_image='%s', w_description='%s',"
                "e_name='%s', e_image='%s', e_description='%s', r_name='%s', r_image='%s',"
                "r_description='%s')>") % \
                (self.name, self.role, self.title, self.image, self.passive_name, \
                 self.passive_image, self.passive_description, self.q_name, self.q_image,\
                 self.q_description, self.w_name, self.w_image, self.w_description, \
                 self.e_name, self.e_image, self.e_description, self.r_name, self.r_image, \
                 self.r_description)


class Item (Base) :
    __tablename__ = "Item"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    base_gold = Column(Integer)
    sell_gold = Column(Integer)
    total_gold = Column(Integer)
    image = Column(String)

    from_items = relationship('Item', secondary=item_to_item)
    into_items = relationship('Item', secondary=item_to_item)

    def __repr__ (self) :
        return ("<Item(name='%s', role='%s', base_gold='%d', sell_gold='%d', total_gold='%d',"
                "image='%s'") % \
               (self.name, self.role, self.base_gold, self.sell_gold, self.total_gold, self.image)


class Player (Base) :
    __tablename__ = "Player"

    # We need a primary key for SQLAlchemy to not puke on us, but we don't need
    # to actually use the primary key, because 'id' is our unique key 
    dummy = Column(Integer, primary_key=True)
    id = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    team_name = Column(String)
    ign = Column(String)
    bio = Column(String)
    image = Column(String)
    role = Column(String)
    kda = Column(Float)
    gpm = Column(Float)
    total_gold = Column(Integer)
    games_played = Column(Integer)

    played_champions = relationship('Champion', secondary=player_to_champion)
    
    def __repr__ (self) :
        return ("<Player(first_name='%s', last_name='%s', ign='%s', bio='%s', image='%s', role='%s'"\
                "kda='%f', gpm='%f', total_gold='%d', games_played='%d')") % \
               (self.first_name, self.last_name, self.ign, self.bio, self.image, self.role, \
                self.kda, self.gpm, self.total_gold, self.games_played)



def load_items(items, session) :
    
    for k, v in items.items() :
        item = Item(description=v['description'],
                    base_gold=int(v['gold']['base']),
                    sell_gold=int(v['gold']['sell']),
                    total_gold=int(v['gold']['total']),
                    name=v['name'],
                    image=v['image'],
                    id=int(k))
        for frm in v['fromItem'] :
            item.from_items += [int(frm)]
        for into in v['intoItem'] :
            item.into_items += [int(into)]
        session.add(item)
    session.commit()


"""
def load_players(players):
    '''
    players is a dictionary of player information loaded from a json of the form:
    {
       "playername" : {"bio" : "",
                       "champions : [len <= 3 <champion_id>],
                       "firstname" : "",
                       "lastname" : "",
                       "name" : "<ign>",
                       "photoUrl" : "",
                       "role" : "",
                       "teamName" : "",
                       "id" : "<player_id>",
                       "kda" : "<float>",
                       "gpm" : "<int>",
                       "totalGold": "<int>",
                       "gamesPlayed": "<int>"                      
    }
    '''
    for k, v in players :
"""        
    


if __name__ == '__main__': 
    # Connect to the SQL database
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')
    # Add all of the tables to the database, first checking to make sure that the table
    # does not already exist
    Base.metadata.bind = engine
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    
    
    items = json.load(open("items"))
    champions = json.load(open("champions"))
    players = json.load(open("players"))

    load_items(items, session)
#    load_champions(champions)
#    load_players(players)


