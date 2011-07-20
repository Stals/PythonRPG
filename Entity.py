from Item import *

from Elements import Elements
from statistics import *
class Entity:
    def __init__(self,name,stats,resists,gold):


        self.name = name
        self.damage = Damage()
        self.hp = 0
        self.maxHp = 0
        self.mp = 0
        self.maxMp = 0
        self.defence = 0
        self.stats = Stats()
        self.stats.addStats(stats,self)



        self.resists=resists
        self.gold = gold

    def doTurn(self):#used by Battle to make one turn
        pass

    def simpleAttack(self,target):#simple attack with a weapon #TODO Переписать в зависимости от оружия и силы и defence противника
        #TODO писать каким оружием бъеш - только имя (а если оружие не надаето ==empty писать что бъеш руками)
        dmg=self.damage.getDamage()
        target.hp-=dmg
        print('"{0}" hits "{1}" for {2} damage.'.format(self.name,target.name,dmg))
    def isDead(self): #returns true if entity is dead
        return self.hp<=0
    def __str__(self):
        return '"{0}" Health: {1}/{2} Mana: {3}/{4} {5} Defence:{6}'.format(self.name,self.hp,self.maxHp,self.mp,self.maxMp,self.damage,self.defence)


