
from statistics import *
import random
class Entity:

    def __init__(self,name,stats,resists,gold):

        self.name = name
        self.damage = Damage()
        self.hp = 0
        self.maxHp = 0
        self.mp = 0
        self.maxMp = 0
        ## Показатель защиты
        self.defence = 0
        self.stats = Stats()
        self.stats.addStats(stats,self)

        self.resists=resists
        self.gold = gold #TODO вставить Money() вместо int

    ## Функция переопределяется в наследниках
    ## Даёт выбор что сделать в бою
    def getBattleChoice(self):
        pass

    ## Обычная атака оружием
    def simpleAttack(self,target):#simple attack with a weapon // returns true if this killed an enemy  #TODO писать каким оружием бъеш - только имя (а если оружие не надаето ==empty писать что бъеш руками)
        #TODO тут действуют только defence и damage(weapon+str) , а dex будет влиять в battle на то как часто ты бъеш...
        #Разность в Dex влияет на попадание
        hitChance=self.stats.dex()/target.stats.dex()
        if hitChance > 1 or random.random() < hitChance: #Если у вас Dex больше или random попал в шанс попадания
            dmg=self.damage.getDamage()-round(target.defence/2)
            if dmg < 0:
                dmg = 0

            target.hp-=dmg
            if target.isDead():
                print('"{0}" kills "{1}" with {2} damage.'.format(self.name,target.name,dmg))
                return True
            else:
                print('"{0}" hits "{1}" for {2} damage. ({3}/{4} hp left)'.format(self.name,target.name,dmg,target.hp,target.maxHp))
                return False
        else: #you missed
            print('"{0}" missed "{1}" with {2}% hit chance.'.format(self.name,target.name,hitChance*100))

    ## Возвращает true если Entity мертв
    def isDead(self):
        return self.hp<=0
    ## Возвращает описание Entity в виде строки
    def __str__(self):
        return '"{0}" Health: {1}/{2} Mana: {3}/{4} {5} Defence: {6}'.format(self.name,self.hp,self.maxHp,self.mp,self.maxMp,self.damage,self.defence)


