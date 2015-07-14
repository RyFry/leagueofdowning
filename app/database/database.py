from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table, MetaData
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import relationship, sessionmaker, backref

import json

"""
metadata = MetaData()

champion = Table('Champion', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('champion_id', Integer, nullable=False, unique=True),
                 Column('name', String(50)),
                 Column('role', String(10)),
                 Column('title', String(50)),
                 Column('lore', String(1000)),
                 Column('image', String(1000)),
                 Column('passive_name', String(20)),
                 Column('passive_image', String(1000)),
                 Column('passive_description', String(1000)),
                 Column('q_name', String(20)),
                 Column('q_image', String(1000)),
                 Column('q_description', String(1000)),
                 Column('w_name', String(20)),
                 Column('w_image', String(1000)),
                 Column('w_description', String(1000)),
                 Column('e_name', String(20)),
                 Column('e_image', String(1000)),
                 Column('e_description ', String(1000)),
                 Column('r_name', String(20)),
                 Column('r_image', String(1000)),
                 Column('r_description', String(2000))
             )
"""
champion_to_item = Table('ChampionToItem', metadata,
		         Column('id', Integer, primary_key=True),
			 Column('champion_id', Integer, ForeignKey('Champion.champion_id')),
                         Column('item_id', Integer, ForeignKey('Item.item_id'))
		   )
"""
item = Table('Item', metadata,
             Column('id', Integer, primary_key=True),
             Column('item_id', Integer, unique=True, nullable=False),
             Column('name', String),
             Column('description', String),
             Column('base_gold', Integer),
             Column('sell_gold', Integer),
             Column('total_gold', Integer),
             Column('image', String)
)


player = Table('Player', metadata,
               Column('id', Integer, primary_key=True),
               Column('first_name', String),
               Column('last_name', String),
               Column('team_name', String),
               Column('ign', String),
               Column('bio', String),
               Column('image', String),
               Column('role', String), 
               Column('kda', Float),
               Column('gpm', Float),
               Column('total_gold', Integer),
               Column('games_played', Integer)
           )
"""
player_to_champion = Table('PlayerToChampion', metadata,
			   Column('id', Integer, primary_key=True),
                           Column('player_id', Integer, ForeignKey('Player.id')),
                           Column('champion_id', Integer, ForeignKey('Champion.id')))
"""
class PlayerToChampion (Base) :
    __tablename__ = "PlayerToChampion"
    
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('Player.id'))
    champion_id = Column(Integer, ForeignKey('Champion.id'))
"""

class Champion (Base) :
    __tablename__ = "Champion"

    # We need a primary key for SQLAlchemy to not puke on us, but we don't need
    # to actually use the primary key, because 'id' is our unique key
    id = Column(Integer, primary_key=True)
    champion_id = Column(Integer, nullable=False, unique=True)
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
    item_id = Column(Integer, unique=True, nullable=False)
    name = Column(String)
    description = Column('description', String),
    base_gold = Column(Integer),
    sell_gold = Column(Integer),
    total_gold = Column(Integer),
    image = Column(String)
    

    def __repr__ (self) :
        return ("<Item(item_id='%d', name='%s', description='%s', base_gold='%d', sell_gold='%d',"\
                "total_gold='%d', image='%s'") % \
               (self.item_id, self.name, self.description, self.base_gold, self.sell_gold,\
                self.total_gold, self.image)

'''
class ItemToItem (Base) :
    __tablename__ = "ItemToItem"
    


    from_item = relationship("Item", foreign_keys=[from_id])
    into_item = relationship("Item", foreign_keys=[into_id])

    def __repr__ (self) :
        return ("<Item(from_id='%d', into_id='%d'") % \
               (self.from_id, self.into_id)
'''    

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
        item.insert({'description' : v['description'],
                     'base_gold' : int(v['gold']['base']),
                     'sell_gold' : int(v['gold']['sell']),
                     'total_gold' : int(v['gold']['total']),
                     'name' : v['name'],
                     'image' : v['image'],
                     'item_id' : int(k)})
<<<<<<< HEAD
        session.add(item)
=======
    engine.execute(item.)
>>>>>>> e3bba7f1e6b4ce26052030769649ec47b0f1e1a1
    session.commit()
"""
        for frm in v['fromItem'] :
            session.add(ItemToItem(from_id=int(frm), into_id=int(k)))
        for into in v['intoItem'] :
            session.add(ItemToItem(from_id=int(k), into_id=int(into)))
"""



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
    


<<<<<<< HEAD
if __name__ == "__main__" :
    # Connect to the SQL database
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')
    # Add all of the tables to the database, first checking to make sure that the table
    # does not already exist
    Session = sessionmaker(bind=engine)

    session = Session()
=======
# Connect to the SQL database
engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')
# Add all of the tables to the database, first checking to make sure that the table
# does not already exist

metadata.create_all(engine, checkfirst=True)
>>>>>>> e3bba7f1e6b4ce26052030769649ec47b0f1e1a1

    items = json.load(open("items"))
    champions = json.load(open("champions"))
    players = json.load(open("players"))

<<<<<<< HEAD
    load_items(items, session)
    #    load_champions(champions)
    #    load_players(players)
=======
load_items(items, session)
#    load_champions(champions)
#    load_players(players)
>>>>>>> e3bba7f1e6b4ce26052030769649ec47b0f1e1a1

