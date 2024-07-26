from datetime import datetime
import random
from sqlalchemy import ForeignKey, Column, Integer, String, JSON, Float, Select, Date
from sqlalchemy.orm import relationship, sessionmaker, scoped_session,declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

engine = create_engine('sqlite:///farms.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
# class FarmAminal(Base):
#     def __init__(self,production={},sum_production=0):
#         self.id_number = datetime.strftime(datetime.now(), '%Y%m%d%H%M%S')
#         self.production = {'edge':[0,0], 'meet':[0,0], 'milk':[0,0]}
#         self.sum_production = sum_production
#
#     def get_production(self,products=[]):
#         res={}
#         for key, value in self.production.items():
#             if key in products:
#                 res[key] = random.randint(value[0],value[1])
#                 self.sum_production += res[key]
#         return res
#
#     def __str__(self):
#         return f'{self.id_number}'
#

class Player(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    name = Column(String(50),default='nobody')
    password = Column(String(50), default='')
    balance = Column(Float, default=100)
    productionssum = relationship('ProductionsSum',back_populates='player')
    productionssell = relationship('ProductionsSell', back_populates='player')
    productions = relationship('Productions', back_populates='player')
    products = Column(JSON, default={})
    barns = relationship('Barn')

    def __str__(self):
        return self.name
    @classmethod
    def find_by_id(cls, player_id):
        return session.query(cls).filter_by(id=player_id).first()

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()
    @classmethod
    def check_autorization(cls, name, password):
        return session.query(cls).filter_by(name=name, password=password).first()
    def get_free_capacity(self):
        return sum([b.capacity for b in self.barns])
    @classmethod
    def change_balance(cls, player_id, cost):
        player = session.query(cls).filter_by(id=player_id).first()
        player.balance -= cost
        session.commit()
        return player

    @classmethod
    def add(cls, name, password):
        player = cls(name=name, password=password)
        session.add(player)
        session.commit()
        return player
class Type(Base):
    __tablename__ = 'type_prod'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    #animals = Column(String(100), default='')
    prods = relationship('Production')

    def __str__(self):
        return self.name

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, type_id):
        return session.query(cls).filter_by(id=type_id).first()


    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()
    @classmethod
    def add(cls, name):
        typ = cls(name=name)
        session.add(typ)
        session.commit()
        return typ


class Production(Base):
    __tablename__ = 'production'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    type_id = Column(Integer,ForeignKey('type_prod.id'))
    type = relationship('Type', back_populates='prods')
    production_min = Column(Float,default=0)
    production_max = Column(Float,default=0)
    animal_type = relationship('AnimalType', back_populates='production')
    cost = Column(Float, default=1.0)

    def __str__(self):
        return f'{self.name}:{self.type_id}'

    @classmethod
    def find_by_name_animal(cls, name, prod_id):

        return session.query(cls).filter_by(name=name, id=prod_id).first()

    @classmethod
    def find_by_name(cls, name, animal):
        if animal:
            name=name+'.'+animal
        return session.query(cls).filter_by(name=name).first()
    @classmethod
    def find_by_id(cls, prod_id):
        return session.query(cls).filter_by(id=prod_id).first()
    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def delete_by_id(cls, prod_id):
        prod = session.query(cls).filter_by(id=prod_id).first()
        if prod:
            session.delete(prod)
            session.commit()
            return True
        return False

    @classmethod
    def add(cls, name, type_id, prod_min, prod_max, cost):
        prod = cls(name=name, type_id=type_id,production_min=prod_min,production_max=prod_max, cost=cost)
        session.add(prod)
        session.commit()
        return prod

    @classmethod
    def update(cls, item_id, name, type_id, prod_min, prod_max, cost):
        prod = session.query(cls).filter_by(id=item_id).first()
        prod.name = name
        prod.type_id = type_id
        prod.production_min = prod_min
        prod.production_max = prod_max
        prod.cost = cost
        session.commit()
        return prod

class AnimalType(Base):
    __tablename__ = 'animal_type'
    id = Column(Integer, primary_key=True)
    name = Column(String(100),nullable=False)
    breed = Column(String(100), nullable=True)
    weight = Column(Float,default=0)
    production_id = Column(ForeignKey('production.id'))
    production = relationship('Production',back_populates='animal_type')
    production_limits = Column(JSON, nullable=True)
    animal = relationship('Animal')
    capacity = Column(Integer, default=1)
    cost = Column(Float, default=1.0)
    lifespan = Column(Integer, default=10)

    def __str__(self):
        return f'{self.name}:{self.breed}'

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, animal_type_id):
        return session.query(cls).filter_by(id=animal_type_id).first()

    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter_by(name=name).first()

    @classmethod
    def add(cls, name, breed, weight, capacity, cost, lifespan, production):
        animal_type = cls(name=name, breed=breed, weight=weight, capacity=capacity,
                          cost=cost, lifespan=lifespan, production_id=production.id)
        session.add(animal_type)
        animal_type.production_limits = dict.fromkeys(['min', 'max'], 0)
        animal_type.production_limits['min'] = production.production_min
        animal_type.production_limits['max'] = production.production_max
        session.commit()
        return animal_type


    @classmethod
    def update(cls,item_id, name, breed, weight, capacity, cost, lifespan, production):
        animal_type = session.query(cls).filter_by(id=item_id).first()
        animal_type.name = name
        animal_type.breed = breed
        animal_type.weight = weight
        animal_type.capacity = capacity
        animal_type.cost = cost
        animal_type.lifespan = lifespan
        animal_type.production_id = production.id
        animal_type.production_limits = dict.fromkeys(['min', 'max'], 0)
        animal_type.production_limits['min'] = production.production_min
        animal_type.production_limits['max'] = production.production_max
        session.commit()
        return animal_type

    @classmethod
    def delete_by_id(cls, an_type_id):
        an_type = session.query(cls).filter_by(id=an_type_id).first()
        if an_type:
            session.delete(an_type)
            session.commit()
            return True
        return False
class Animal(Base):
    __tablename__ = 'animal'
    id = Column(Integer, primary_key=True)
    id_number = Column(String, default=datetime.strftime(datetime.now(), '%Y%m%d%H%M%S'))
    animal_type = relationship('AnimalType',back_populates='animal')
    animal_type_id = Column(ForeignKey('animal_type.id'))
    # breed = Column(String(100), nullable=True)
    weight = Column(Float,default=0)
    barn = relationship('Barn', back_populates='animals')
    barn_id = Column(ForeignKey('barn.id'))
    cost = Column(Float, default=1.0)
    production = Column(Float, default=0)
    date_created = Column(Date, default=datetime.today())


    def __str__(self):
        return f'{self.id_number}:{self.animal_type}'

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def add_production(cls, animal_id, prod):
        animal = session.query(cls).filter_by(id=animal_id).first()
        animal.production += prod
        session.commit()
        return animal


    @classmethod
    def add(cls, animal_type, barn):
        animal_type = AnimalType.find_by_id(animal_type)
        barn = Barn.find_by_id(barn)
        animal = cls(animal_type=animal_type, barn=barn, cost=animal_type.cost)
        session.add(animal)
        session.commit()
        return animal

    @classmethod
    def delete_by_id(cls, an_id):
        an = session.query(cls).filter_by(id=an_id).first()
        if an:
            session.delete(an)
            session.commit()
            return True
        return False

    @classmethod
    def find_by_barns(cls, barn_id):
        return session.query(cls).filter_by(barn_id=barn_id).all()

    @classmethod
    def change_production(cls, animal_id, prod):
        animal = session.query(cls).filter_by(id=animal_id).first()
        animal.production += prod
        session.commit()
        return animal
class Barn(Base):
    __tablename__ = 'barn'
    const_cost = 50
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    animals = relationship('Animal')
    capacity = Column(Integer, default=100)
    player_id =Column(ForeignKey('player.id'), default=1)
    player = relationship('Player', back_populates='barns')
    cost = Column(Float, default=0)

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def all(cls):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, barn_id):
        return session.query(cls).filter_by(id=barn_id).first()
    @classmethod
    def change_capacity(cls, barn_id, capacity):
        barn = session.query(cls).filter_by(id=barn_id).first()
        barn.capacity -=capacity
        session.commit()
        return barn

    @classmethod
    def find_by_player(cls, player_id):
        return session.query(cls).filter_by(player_id=player_id)
    @classmethod
    def add(cls, name, capacity):
        name = 'barn_'+name
        barn = cls(name=name, capacity=capacity, cost=cls.const_cost*capacity/100)
        session.add(barn)
        session.commit()
        return barn


class Productions(Base):
    __tablename__ = 'productions'
    id = Column(Integer, primary_key=True)
    name = Column(String, default='')
    count = Column(Integer, default=0)
    animal = Column(String(100), default='')
    date_created = Column(Date, default=datetime.today())
    player_id = Column(ForeignKey('player.id'))
    player = relationship('Player', back_populates='productions')

    def __str__(self):
        return f'{self.name}:{self.count}:{self.date_created}'

    @classmethod
    def add(cls, name, count, animal, player_id):
        prod = cls(name=name, count=count, animal=animal, player_id=player_id)
        session.add(prod)
        session.commit()
        return prod

    @classmethod
    def all(cls):
        return session.query(cls).all()
class ProductionsSum(Base):
    __tablename__ = 'productionssum'
    id = Column(Integer, primary_key=True)
    player_id = Column(ForeignKey('player.id'))
    name = Column(String, default='')
    animal = Column(String(100), default='')
    count = Column(Integer, default=0)
    player = relationship('Player', back_populates='productionssum')

    def __str__(self):
        return f'{self.name}:{self.count}'

    @classmethod
    def find_by_name_animal(cls, name, animal):
        return session.query(cls).filter_by(name=name, animal=animal).first()

    @classmethod
    def find_by_id(cls, prodsum_id):
        return session.query(cls).filter_by(id=prodsum_id).first()

    @classmethod
    def find_by_player(cls, player_id):
        return session.query(cls).filter_by(player_id=player_id)
    @classmethod
    def add_production_to_sum(cls, name, count, animal, player_id):
        prodsum = session.query(cls).filter_by(name=name, animal=animal).first()
        prodsum.count +=count
        session.commit()
        return prodsum

    @classmethod
    def add(cls, name, count, animal, player_id):
        prodsum = cls(name=name, count=count, animal=animal, player_id=player_id)
        session.add(prodsum)
        session.commit()
        return prodsum

    @classmethod
    def all(cls):
        return session.query(cls).all()


class ProductionsSell(Base):
    __tablename__ = 'productionssell'
    id = Column(Integer, primary_key=True)
    player_id = Column(ForeignKey('player.id'))
    name = Column(String, default='')
    animal = Column(String(100), default='')
    count = Column(Integer, default=0)
    player = relationship('Player', back_populates='productionssell')
    date_created = Column(Date, default=datetime.today())
    cost = Column(Float, default=0.0)
    summa = Column(Float, default=0.0)

    def __str__(self):
        return f'{self.name}:{self.count}'

    @classmethod
    def find_by_name_animal(cls, name, animal):
        return session.query(cls).filter_by(name=name, animal=animal).first()

    @classmethod
    def find_by_id(cls, prodsum_id):
        return session.query(cls).filter_by(id=prodsum_id).first()

    @classmethod
    def find_by_player(cls, player_id):
        return session.query(cls).filter_by(player_id=player_id)
    @classmethod
    def add_production_to_sell(cls, name, count, animal, player_id):
        prodsum = session.query(cls).filter_by(name=name, animal=animal).first()
        prodsum.count +=count
        session.commit()
        return prodsum

    @classmethod
    def add(cls, name, count, animal, player_id, cost):
        prodsum = cls(name=name, count=count, animal=animal, player_id=player_id, cost=cost, summa=cost*count)
        session.add(prodsum)
        session.commit()
        return prodsum

    @classmethod
    def all(cls):
        return session.query(cls).all()

class Cow(Base):
    __tablename__ = 'cows'
    id = Column(Integer, primary_key=True)
    id_number = Column(String,default=datetime.strftime(datetime.now(), '%Y%m%d%H%M%S'))
    production = Column(JSON,default={'edge': [0, 0], 'meet': [0, 0], 'milk': [0, 0]})
    sum_production = Column(Float,default=0)

    def __str__(self):
        return self.id_number



    @classmethod
    def add(cls, name):
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user



    # def __init__(self,production={}):
    #     super().__init__()
    #     self.id_number = self.get_id_number()
    #     self.production = {'milk':[8,12]}#, 'meet':[50,150]}
    # def get_id_number(self):
    #     if self.__class__.__name__ in self.id_number:
    #         return self.id_number
    #     else:
    #         self.id_number = self.__class__.__name__+self.id_number
    #         return self.id_number

# class Chicken(FarmAminal,Base):
#     def __init__(self,production={}):
#         super().__init__()
#         self.id_number = self.get_id_number()
#         self.production = {'edge':[0,1]}#, 'meet':[2,5]}
#     def get_id_number(self):
#         if self.__class__.__name__ in self.id_number:
#             return self.id_number
#         else:
#             self.id_number = self.__class__.__name__+self.id_number
#             return self.id_number
#
# class Rabbit(FarmAminal,Base):
#     def __init__(self,production={}):
#         super().__init__()
#         self.id_number = self.get_id_number()
#         self.production = {'meet':[2,7]}
#     def get_id_number(self):
#         if self.__class__.__name__ in self.id_number:
#             return self.id_number
#         else:
#             self.id_number = self.__class__.__name__+self.id_number
#             return self.id_number
#
#
# class Barn(Base):
#     def __init__(self,animals=[],types={'Cow':20,'Chicken':30},sum_production=0):
#         self.animals = animals
#         self.types = types
#         self.sum_production = dict.fromkeys(self.types.keys(),0)
#
#     def add_animals(self,animal):
#         if animal.__class__.__name__  in self.types.keys():
#             types_count = self.get_count_animals_for_type()
#             if types_count[animal.__class__.__name__] < self.types[animal.__class__.__name__]:
#                 self.animals.append(animal)
#                 return self
#             else:
#                 print("FULL")
#                 return self
#         else:
#             self.types[animal.__class__.__name__] = 0
#             self.animals.append(animal)
#         return self
#
#     def get_count_animals_for_type(self):
#         types_count=dict.fromkeys(self.types.keys(),0)
#         for animal in self.animals:
#             types_count[animal.__class__.__name__]+=1
#         return types_count
#
#     def get_production(self):
#         res = dict.fromkeys(self.types.keys(),0)
#         for animal in self.animals:
#             for product in animal.get_production(animal.production):
#                 res[animal.__class__.__name__]+=animal.get_production(animal.production)[product]
#         return res
#
#     def __str__(self):
#         return f'{self.animals}'
#
#     def get_animals_production(self):
#         for animal in self.animals:
#             print(f"{animal.id_number}:{animal.sum_production}")


Base.metadata.create_all(engine)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
