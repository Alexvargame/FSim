from models import Type, Production, AnimalType, Animal, Barn, Player, Productions, ProductionsSum, ProductionsSell

import random
from datetime import datetime, timedelta
def show_all_type_production():
    return [tuple([type.id,type.name]) for type in Type.all()]
def get_type_by_id(type_id):
    return Type.find_by_id(type_id)

def get_animal_by_barns(barn_id):
    return Animal.find_by_barns(barn_id)
def get_type_by_name(name):
    return Type.find_by_name(name)
def show_all_animals():
    return [tuple([anim.id,anim.id_number, anim.animal_type.name]) for anim in Animal.all()]

def get_all_animals():
    return Animal.all()

def delete_animal(animal):
    Barn.change_capacity(animal.barn_id, -animal.animal_type.capacity)
    return Animal.delete_by_id(animal.id)

def animal_production_change(animal, prod):
    return Animal.change_production(animal.id, prod)
def show_all_animals_types():
    return AnimalType.all()
def delete_animal_type(an_type_id):
    return AnimalType.delete_by_id(an_type_id)

def get_all_production():
    return Production.all()
def get_animal_type_for_id(animal_type_id):
    return AnimalType.find_by_id(animal_type_id)
def get_production_by_name_animal(name, animal=None):
    if animal:
        if name!= 'Мясо':
            an_type = AnimalType.find_by_name(animal)
            return Production.find_by_name_animal(name, an_type.production_id)
        elif name == 'Мясо':
            return Production.find_by_name(name, animal)
    else:
        return Production.find_by_name(name, animal)

def delete_production(prod_id):
    return Production.delete_by_id(prod_id)
def get_production_by_id(prod_id):
    return Production.find_by_id(prod_id)
def get_barn_for_id(barn_id):
    return Barn.find_by_id(barn_id)
def get_barns():
    return Barn.all()

def get_player(player_id):
    return Player.find_by_id(player_id)

def player_autorization(name, password):
    if Player.check_autorization(name, password):
        return Player.check_autorization(name, password)
    return False

def player_registration(name, password):
    print('NAME',Player.find_by_name(name))
    if Player.find_by_name(name):
        return False, f"Такой ник уже существует"
    else:
        return Player.add(name, password), ''


def show_barn_animals(barn_id):
    return [a for a in Animal.all() if a.barn_id==int(barn_id.split('_')[-1])]
# def production_saver(name, typ, prod_min, prod_max):
#     if name and typ and prod_min and prod_max:
#         type_id = Type.find_by_name(typ)
#         if type_id:
#             Production.add(name, type_id.id, prod_min,prod_max)
#             return True
#         return False
#     return False
#
# def show_production():
#     for prod in Production.all():
#         return [tuple([prod.id,prod.name,Type.find_by_id(prod.type_id).name,
#                    prod.production_min, prod.production_max, [ant.name for ant in prod.animal_type]])
#             for prod in Production.all()]

def animal_saver(animal_type, barn, count, player):
    print('PBALANCE',player.balance, animal_type, barn)
    # if player.balance <= animal_type.cost*count:
    #     return False, f"Недостаточно средств"
    # elif barn.capacity < animal_type.capacity*count:
    #     return False, f'Недостаточно места, нужно покупать хлев'
    # else:
    #     if animal_type and barn:
    #         an = Animal.add(animal_type, barn)
    #         if an:
    #             # if type(an) is not str:
    #             print('IDNUMBER', an.id_number)
    #             an.id_number += str(count)
    #             an.weight = round(random.uniform(an.animal_type.weight * 0.85, an.animal_type.weight * 1.15), 2)
    #             Barn.change_capacity(an.barn_id, an.animal_type.capacity)
    #             return True, ''
    #     else:
    #         return False, f'Неправильный ввод'
    #
    #
    if animal_type and barn:
        an = Animal.add(animal_type, barn)
        if an:
            #if type(an) is not str:
            print('IDNUMBER',an.id_number)
            an.id_number += str(count)
            an.weight = round(random.uniform(an.animal_type.weight*0.85, an.animal_type.weight*1.15),2)
            Barn.change_capacity(an.barn_id, an.animal_type.capacity)
            Player.change_balance(player.id, an.cost)
            return True, ''
        else:
            return False, f'Недостаточно места, нужно покупать хлев'
    return False, f'Неправильный ввод'

def barn_saver(name, capacity, player):
    print(player.balance, capacity / 100 * Barn.const_cost)
    #print(Barn.get_const_cost(), Barn.const_cost)
    if player.balance >= capacity / 100 * Barn.const_cost:
        print(name, capacity, type(capacity), capacity in [100,200])
        if name and capacity in [100, 200]:
            b = Barn.add(name, capacity)
            #if type(b) is not str:  ################# instance(b, types.StringType)
            b.player_id = player.id
            #player.balance -= b.cost

            Player.change_balance(player.id, b.cost)
            print(player.balance)
            return True, ''
        else:
            return False, f"Неправильный ввод"
    else:
        return False, f"Недостаточно средств"

def production_saver(item_id, name, type_id, minn, maxx, cost):
    if item_id is None:
        if name:
            Production.add(name, type_id, minn, maxx, cost)
            return True
        return False
    else:
        if name:
            Production.update(item_id, name, type_id, minn, maxx, cost)
            return True
        return False


def animal_type_saver(item_id, name, breed, weight, capacity, cost, lifespan, production):
    if item_id is None:
        if name and breed:
            AnimalType.add(name, breed, weight, capacity, cost, lifespan, production)
            return True
        else:
            return False
    else:
        if name and breed:
            AnimalType.update(item_id, name, breed, weight, capacity, cost, lifespan, production)
            return True
        else:
            return False
def add_animal_production(animal_id, prod):
    if prod and animal_id:
        Animal.add_production(animal_id, prod)

def productions_saver(name, count, animal, player):
    if name and count:
        Productions.add(name, count, animal, player.id)

def get_productions_last_date():
    if [pr.date_created for pr in Productions.all()]:
        return max([pr.date_created for pr in Productions.all()])
    else:
        return datetime.today().date() - timedelta(days=1)
def productions_sum_change(name, count, animal, player):
    if ProductionsSum.find_by_name_animal(name, animal):
        ProductionsSum.add_production_to_sum(name, count, animal, player.id)
    else:
        ProductionsSum.add(name, count, animal, player.id)

def get_productions_sum_by_player(player):
    return ProductionsSum.find_by_player(player.id)

def get_player_barns(player):
    return Barn.find_by_player(player.id)
def productions_sell_change(name, count, animal, player, cost):
    # if ProductionsSell.find_by_name(name):
    #     ProductionsSell.add_production_to_sell(name, count, player.id)
    # else:
        print(name, count, animal, player, cost)
        ProductionsSell.add(name, count, animal, player.id, cost)
        Player.change_balance(player.id, -count*cost)