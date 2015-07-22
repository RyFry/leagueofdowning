from sqlalchemy import Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy import create_engine, insert, update
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship, sessionmaker, backref
from sqlalchemy.ext.declarative import declarative_base
import json
from pprint import pprint

Base = declarative_base()


champion_to_item = Table('ChampionToItem', Base.metadata,
		         Column('id', Integer, primary_key=True),
			 Column('champion_id', Integer, ForeignKey('Champion.champion_id')),
                         Column('item_id', Integer, ForeignKey('Item.item_id'))
		   )

player_to_champion = Table('PlayerToChampion', Base.metadata,
			   Column('id', Integer, primary_key=True),
                           Column('player_id', Integer, ForeignKey('Player.player_id')),
                           Column('champion_id', Integer, ForeignKey('Champion.champion_id')))


item_to_item = Table('ItemToItem', Base.metadata,
                     Column('id', Integer, primary_key=True),
                     Column('from_id', Integer, ForeignKey('Item.item_id')),
                     Column('into_id', Integer, ForeignKey('Item.item_id'))
                 )



class Champion (Base) :
    __tablename__ = "Champion"

    # We need a primary key for SQLAlchemy to not puke on us, but we don't need
    # to actually use the primary key, because 'id' is our unique key
    id = Column(Integer, primary_key=True)
    champion_id = Column(Integer, nullable=False, unique=True)
    name = Column(String)
    role = Column(String)
    title = Column(String)
    lore = Column(String(4000))
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

"""
class ItemToItem (Base) :
    __tablename__ = "ItemToItem"
    
    from_id = relationship("Item", foreign_keys=[item_id])
    into_id = relationship("Item", foreign_keys=[item_id])

    def __repr__ (self) :
        return ("<Item(from_id='%d', into_id='%d'") % \
               (self.from_id, self.into_id)
"""


class Item (Base) :
    __tablename__ = "Item"
    
    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, unique=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    base_gold = Column(Integer)
    sell_gold = Column(Integer, nullable=False)
    total_gold = Column(Integer, nullable=False)
    image = Column(String, nullable=False)

    from_into = relationship("Item", secondary=item_to_item,
                                     primaryjoin=item_id==item_to_item.c.from_id,
                                     secondaryjoin=item_id==item_to_item.c.into_id)


    def __repr__ (self) :
        return ("<Item(item_id='%d', name='%s', description='%s', base_gold='%d', sell_gold='%d',"\
                "total_gold='%d', image='%s'") % \
               (self.item_id, self.name, self.description, self.base_gold, self.sell_gold,\
                self.total_gold, self.image)

    

class Player (Base) :
    __tablename__ = "Player"

    # We need a primary key for SQLAlchemy to not puke on us, but we don't need
    # to actually use the primary key, because 'id' is our unique key 
    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, unique=True)
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
                "kda='%f', gpm='%f', total_gold='%d', games_played='%d', player_id='%d')") % \
               (self.first_name, self.last_name, self.ign, self.bio, self.image, self.role, \
                self.kda, self.gpm, self.total_gold, self.games_played, self.player_id)



def load_items(items, session) :
    for k, v in items.items() :
        if not session.query(Item).filter_by(item_id=int(k)).first() :
            item = Item(description=v['description'],
                        base_gold=int(v['gold']['base']),
                        sell_gold=int(v['gold']['sell']),
                        total_gold=int(v['gold']['total']),
                        name=v['name'],
                        image=v['image'],
                        item_id=int(k))
            session.add(item)
    session.commit()
"""
        for frm in v['fromItem'] :
            session.add(ItemToItem(from_id=int(frm), into_id=int(k)))
        for into in v['intoItem'] :
            session.add(ItemToItem(from_id=int(k), into_id=int(into)))
"""




def load_players(players, session):
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
    with session.no_autoflush:
        for k, v in players.items() :
            if not session.query(Player).filter_by(player_id=int(k)).first() :
                player = Player(bio=(v['bio'] if v['bio'] else ''),
                                first_name=(v['firstname'] if v['firstname'] else ''),
                                last_name=(v['lastname'] if v['lastname'] else ''),
                                ign=(v['name'] if v['name'] else ''),
                                player_id=(int(v['id']) if v['id'] else 0),
                                image=(v['photoUrl'] if v['photoUrl'] else ''),
                                role=(v['role'] if v['role'] else ''),
                                team_name=(v['teamName'] if v['teamName'] else 'No Team'),
                                kda=(float(v['kda']) if v['kda'] else 0.0),
                                gpm=(float(v['gpm']) if v['gpm'] else 0.0),
                                total_gold=(int(v['totalGold']) if v['totalGold'] else  0),
                                games_played=(int(v['gamesPlayed']) if v['gamesPlayed'] else 0))
                session.add(player)
        session.commit()

def load_players_to_champions(players, session):
    with session.no_autoflush :
        for k, v in players.items() :
            player = session.query(Player).filter_by(player_id=int(k)).first()
            for champ in v['champions'] :
                if champ is not None:
                    champion = session.query(Champion).filter_by(champion_id=int(champ)).first()
                    if champion is not None :
                        player.played_champions.append(champion)
                else :
                    champion = session.query(Champion).filter_by(name='dummy').first()
                    player.played_champions.append(champion)
            if len(player.played_champions) == 0 :
                print(player.played_champions)
            session.add(player)
        session.commit()

def load_item_to_item(items, session):
    with session.no_autoflush :
        for k, v in items.items() :
            this_item = session.query(Item).filter_by(item_id=int(k)).first()
            for into in v['intoItem'] :
                into_itm = session.query(Item).filter_by(item_id=int(into)).first()
                this_item.from_into.append(into_itm)
                session.add(this_item)
        session.commit()


def load_champions(champions, session, engine):
    with session.no_autoflush :
        for k, v in champions.items() :
            engine.execute(text('update "Champion" set q_description = :desc where champion_id = :id'), desc = v['q_description'].replace('<br>', '\n'), id = int(v['key'])) 
            engine.execute(text('update "Champion" set w_description = :desc where champion_id = :id'), desc = v['w_description'].replace('<br>', '\n'), id = int(v['key'])) 
            engine.execute(text('update "Champion" set e_description = :desc where champion_id = :id'), desc = v['e_description'].replace('<br>', '\n'), id = int(v['key'])) 
            engine.execute(text('update "Champion" set r_description = :desc where champion_id = :id'), desc = v['r_description'].replace('<br>', '\n'), id = int(v['key'])) 
            '''
            champion = Champion(champion_id = int(v['key']),
                                name = v['name'],
                                role = v['role'],
                                title = v['title'],
                                lore = v['lore'],
                                image = v['image'],
                                passive_name = v['passive_name'],
                                passive_image = v['passive_image'],
                                passive_description = v['passive_description'],
                                q_name = v['q_name'],
                                q_image = v['q_image'],
                                q_description = v['q_description'],
                                w_name = v['w_name'],
                                w_image = v['w_image'],
                                w_description = v['w_description'],
                                e_name = v['e_name'],
                                e_image = v['e_image'],
                                e_description = v['e_description'],
                                r_name = v['r_name'],
                                r_image = v['r_image'],
                                r_description = v['r_description'])
            try:
                for item in v['recommended_items'] :
                    i = session.query(Item).filter_by(item_id=int(item)).first()
                    champion.recommended_items.append(i)
                    session.add(champion)
            except KeyError as e:
                pass
            '''
        session.commit()

    

def delete_all(session) :
    for row in session.query(Item).all():
        session.delete(row)
    session.commit()


if __name__ == "__main__" :
    # Connect to the SQL database
    engine = create_engine ('postgresql://postgres:h1Ngx0@localhost/leagueofdowning')
    # Add all of the tables to the database, first checking to make sure that the table
    # does not already exist
    Session = sessionmaker(bind=engine)

    session = Session()
    
    #delete_all(session)

    items = json.load(open("items"))
    champions = json.load(open("champions"))
    players = json.load(open("players"))

    load_items(items, session)
    load_champions(champions, session, engine)
    load_players(players, session)
    load_players_to_champions(players, session)
    load_item_to_item(items, session)
    
    session.close()


