
#TODO Пишет всё здесь а после делаем refactor -> move


from Item import *

from Elements import Elements
class Entity:


    def __init__(self):
        self.name = ""
        self.hp = 0
        self.maxHp = 0
        self.mp = 0
        self.maxMp = 0
        self.gold = 0
        self.stats = stats()
        self.damage = damage()
        self.resists = Elements()

    def doTurn(self):#used by Battle to make one turn
        pass
    #TODO Переписать в зависимости от оружия и силы+зависит от коэфицента силы
    def simpleAttack(self,target):#simple attack with a weapon
        dmg=self.stats.str()
        target.hp-=dmg
        print('"{0}" hits "{1}" for {2} damage.'.format(self.name,target.name,dmg))
    def isDead(self): #returns true if entity is dead
        return self.hp<=0

    def __str__(self):
        return '"{0}" Health : {1}/{2}'.format(self.name,self.hp,self.maxHp)


