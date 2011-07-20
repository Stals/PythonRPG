#Тут хранятся вещи необходимые в построении других классов Например такого как Hero

import random
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
    def addStats(self,stats,entity):#stats - that should be added to entity
        self.stats["Str"]+=stats.str()
        self.stats["Dex"]+=stats.dex()
        self.stats["Mag"]+=stats.mag()
        self.stats["Con"]+=stats.con()
        entity.maxHp += stats.con()*10
        entity.hp += stats.con()*10

        entity.maxMp += stats.mag()*10
        entity.mp += stats.mag()*10

        entity.damage.addDamage(Damage(stats.str(),stats.str()))
    def removeStats(self,stats,entity):#stats - that should be removed from entity
        self.stats["Str"]-=stats.str()
        self.stats["Dex"]-=stats.dex()
        self.stats["Mag"]-=stats.mag()
        self.stats["Con"]-=stats.con()
        entity.maxHp -= stats.con()*10
        entity.hp -= stats.con()*10

        entity.maxMp -= stats.mag()*10
        entity.mp -= stats.mag()*10

        entity.damage.removeDamage(Damage(stats.str(),stats.str()))