#Тут хранятся вещи необходимые в построении других классов Например такого как Hero

import random

## Класс хранит урон (минимальный и максимальный) и позволяет получить случайный урон между этими двумя значениями
class Damage:
    def __init__(self,min=0,max=0):
        self.min=min
        self.max=max

    ## Возвращает число (между min и max)
    def getDamage(self):
        return random.randint(self.min,self.max)

    ## Добавляет урон к текущему урону
    def addDamage(self,damage):
        self.min+=damage.min
        self.max+=damage.max

    ## Отнемает урон от текущего
    def removeDamage(self,damage):
        self.min-=damage.min
        self.max-=damage.max

    ## Возвращает Урон в виде строки
    def __str__(self):
        return " Damage: {0}-{1} ".format(self.min,self.max)



#Позволяет не думать о том какие статы сейчас есть, за счёт того что они пределены только в одном месте
#Но чтобы создать вещь вам обязательно нужно знать о Stats

#TODO может hp и mp перенести внутрь? не в нутрь статов, а как и stats является переменной.
## Хранит статистики Entity и его наследников
class Stats:
    def __init__(self,Str=0,Dex=0,Mag=0,Con=0):
        self.stats={
            "Str":Str,#Strength
            "Dex":Dex,#Dextirity
            "Mag":Mag,#Magic
            "Con":Con #Construction

        }
    ## Возвращает элементы словаря stats
    ## позволяет не обращаться к словарю на прямую для вывода статистик
    def items(self): #TODO переназвать чтобы не походило на методы equipment,inventory и тд
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
    def __str__(self):
        result=""
        for key,value in self.stats.items():
            result+="{0}: {1} \n".format(key,value)
        return result