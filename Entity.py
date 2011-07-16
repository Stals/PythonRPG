
#TODO Пишет всё здесь а после делаем refactor -> move


from Item import *

from Elements import Elements
class Entity:
    name = ""
    hp = 0
    maxHp = 0
    gold = 0
    stats = stats()
    damage = damage()
    resists = Elements()

    def __init__(self):
        pass
    def doTurn(self):#used by Battle to make one turn
        pass
    def simpleAttack(self):#simple attack with a weapon
        pass
    def isDead(self): #returns true if entity is dead
        return self.hp<=0

    def __str__(self):
        pass


