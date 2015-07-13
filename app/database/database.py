from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy import create_engine

import json

player_to_champion = Table('PlayerToChampion', Base.metadata,
                           Column('player_id', Integer),
                           Column('champion_id', Integer))
champion_to_item = Table('ChampionToItem', Base.metadata,
                         Column('champion_id', Integer),
                         Column('item_id', Integer))

from_item_to_item = Table('FromItemToItem', Base.metadata,
                          Column('from_id', Integer),
                          Column('to_id', Integer))

class Champion (Base) :
    __tablename__ = "Champion"

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

    champion_to_item = relationship('Item', secondary=champion_to_item)


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
    
    id = Column(Integer)
    name = Column(String)
    description = Column(String)
    base_gold = Column(Integer)
    sell_gold = Column(Integer)
    total_gold = Column(Integer)
    image = Column(String)

    from_item_to_item = relationship('Item', secondary=from_item_to_item)
    
    def __repr__ (self) :
        return ("<Item(name='%s', role='%s', base_gold='%d', sell_gold='%d', total_gold='%d',"
                "image='%s'") % \
               (self.name, self.role, self.base_gold, self.sell_gold, self.total_gold, self.image)


class Player (Base) :
    __tablename__ = "Player"

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
    
    player_to_champion = relationship("Champion", secondary=player_to_champion)

    def __repr__ (self) :
        return ("<Player(first_name='%s', last_name='%s', ign='%s', bio='%s', image='%s', role='%s'"\
                "kda='%f', gpm='%f', total_gold='%d', games_played='%d')") % \
               (self.first_name, self.last_name, self.ign, self.bio, self.image, self.role, \
                self.kda, self.gpm, self.total_gold, self.games_played)



if __name__ == '__main__': 
    # Connect to the SQL database
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')
    # Add all of the tables to the database, first checking to make sure that the table
    # does not already exist
    Base.metadata.create_all(engine, checkFirst=True)
    
    champions = json.loads("champions")
    items = json.loads("items")
    players = json.loads("players")

    load_players(players)
