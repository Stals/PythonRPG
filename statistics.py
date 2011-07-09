#Тут хранятся вещи необходимые в построении других классов Например такого как Hero

import random

#Позволяет не думать о том какие статы сейчас есть, за счёт того что они пределены только в одном месте
#Но чтобы создать вещь вам обязательно нужно знать о stats
class stats:
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


class damage:
    def __init__(self,min=0,max=0):
        self.min=min
        self.max=max
    def __str__(self):
        return " Damage:{0}-{1} ".format(self.min,self.max)
    #Возвращает число (между min и max)
    def getDamage(self):
        return random.randint(self.min,self.max)

