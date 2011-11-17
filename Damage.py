import random
#TODO! Разнести на файл Damage.py и Stats.py
## Класс хранит урон (минимальный и максимальный) и позволяет получить случайный урон между этими двумя значениями
import random

class Damage:
    def __init__(self,min=0,max=0):
        self.min=min
        self.max=max

    ## Возвращает число (между min и max)
    def getDamage(self):
        return random.randint(self.min, self.max)

    ## Добавляет урон к текущему урону
    def addDamage(self,damage):
        self.min += damage.min
        self.max += damage.max

    ## Отнемает урон от текущего
    def removeDamage(self,damage):
        self.min -= damage.min
        self.max -= damage.max

    ## Возвращает Урон в виде строки
    def __str__(self):
        return " Damage: {0}-{1} ".format(self.min,self.max)



