#Тут хранятся вещи необходимые в построении других классов Например такого как Hero

import random

#Позволяет не думать о том какие статы сейчас есть, за счёт того что они пределены только в одном месте
#Но чтобы создать вещь вам обязательно нужно знать о Stats
class Stats:
    def __init__(self,Str=0,Dex=0,Mag=0,Con=0):
        self.stats={
            "Str":Str,#Strength
            "Dex":Dex,#Dextirity
            "Mag":Mag,#Magic
            "Con":Con #Construction

        }
    def __str__(self):
        result=""
        for key,value in self.stats.items():
            result+="{0}: {1} \n".format(key,value)
        return result
    def items(self): #позволяет не обращаться к словарю на прямую для вывода статистик
        return self.stats.items()
    def str(self):
        return self.stats["Str"]
    def dex(self):
        return self.stats["Dex"]
    def mag(self):
        return self.stats["Mag"]
    def con(self):
        return self.stats["Con"]
    def addStats(self,stats,entity):
        #TODO В момент когда человеку добавляются или отнимаются статы - у него должны перещитываться Damage , hp и mp

        self.stats["Str"]+=stats.str()
        self.stats["Dex"]+=stats.dex()
        self.stats["Mag"]+=stats.mag()
        self.stats["Con"]+=stats.con()
        self.recalculateStats(entity)
    def removeStats(self,stats,entity):
        self.stats["Str"]-=stats.str()
        self.stats["Dex"]-=stats.dex()
        self.stats["Mag"]-=stats.mag()
        self.stats["Con"]-=stats.con()
        self.recalculateStats(entity)
    def recalculateStats(self,entity):#TODO Если игрок в городе выбирает что одеть - то у него hp восстаноятся - нада этого избежать. И мне нужно добавить с максимуму и минимуму именно столько сколько приехало.
        entity.maxHp = entity.stats.con()*10
        entity.hp = entity.stats.con()*10
        
        entity.maxMp = entity.stats.mag()*10
        entity.mp = entity.stats.mag()*10

        entity.damage.min = entity.stats.str()
        entity.damage.max = entity.stats.str()

class Damage:
    def __init__(self,min=0,max=0):
        self.min=min
        self.max=max
    def __str__(self):
        return " Damage:{0}-{1} ".format(self.min,self.max)
    #Возвращает число (между min и max)
    def getDamage(self):
        return random.randint(self.min,self.max)
    def addDamage(self,damage):
        self.min+=damage.min
        self.max+=damage.max
    def removeDamage(self,damage):
        self.min-=damage.min
        self.max-=damage.max
