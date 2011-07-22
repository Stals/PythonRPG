#функция __str__() в класса позволяет очень просто выводит их содержимое через print(MagicBow) например
import random
from statistics import *

#bonusStats является оберткой вокруг Stats
class bonusStats:
    def __init__(self,stats):
        self.stats = stats

    def str(self):
        return self.stats.str()
    def dex(self):
        return self.stats.dex()
    def mag(self):
        return self.stats.mag()
    def con(self):
        return self.stats.con()
    def __str__(self):
        result = ""
        for key,value in self.stats.items():
            if value!=0:
                if value>0:
                    sign="+"
                else:
                    sign=""#минус будет ставится автоматически прямо в числе
                result+="{0}:{1}{2} ".format(key,sign,value)
        return result

    #TODO из него наследуется то что может выпасть из моба , типо шкура и тд.
class Item:#TODO Сдлеать специфичные для класса вещи - типо одеть magicWand может только wizard/mage/cleric
    #TODO сделать getStr() и другие методы если будет необходимо
    def __init__(self,name,stats,piece,type,price=0):
        self.name = name
        self.bonusStats=bonusStats(stats)#Вещь может иметь статы
        self.piece = piece #Weapon or Boots,Chest ect #TODO Если определение оружие это или нет не нужно - убрать

        self.price=price #Необходимо для продажи в магазине

    def __str__(self): #переопределен в наследниках
        pass

    def isWeapon(self):
        return self.piece=="Weapon"
    def isArmour(self):#TODO поменять если будут еще и урашения наследоваться из Item
        return self.piece!="Weapon"


class Weapon(Item):
    def __init__(self,name,stats,damage,price=0):
        super().__init__(name,stats,"Weapon",price)
        self.damage = damage

    def __str__(self):
        return '"{0}" {1} {2}'.format(self.name,self.damage,self.bonusStats)

class armourType:
    Head = "Head"
    Gloves = "Gloves"
    Chest = "Chest"
    Leggings = "Leggings"
    Boots = "Boots"

#armourType can be "Head" "Gloves" "Chest" "Leggings" or "Boots"
class Armour(Item):

    def __init__(self,name,stats,defence,armourType,price=0):
        super().__init__(name,stats,armourType,price)
        self.defence = defence

    def __str__(self):
        return '"{0}"  Defence:{1} {2}'.format(self.name,self.defence,self.bonusStats)