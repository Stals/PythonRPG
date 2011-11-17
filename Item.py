#функция __str__() в класса позволяет очень просто выводит их содержимое через print(MagicBow) например
import random
from statistics import *
from Money import *
## является оберткой вокруг Stats
class bonusStats:

    def __init__(self,stats):
        self.stats = stats

    ## Возвращает показатель силы
    def str(self):
        return self.stats.str()

    ## Возвращает показатель ловкости
    def dex(self):
        return self.stats.dex()

    ## Возвращает показатель Магии
    def mag(self):
        return self.stats.mag()

    ## Возвращает показатель Конструкции
    def con(self):
        return self.stats.con()

    ## Возвращет бонусные статистики в виде строки
    def __str__(self):
        result = ""
        for key,value in self.stats.items():
            if value != 0:
                if value > 0:
                    sign = "+"
                else:
                    sign = ""#минус будет ставится автоматически прямо в числе
                result+="{0}:{1}{2} ".format(key,sign,value)
        return result

#TODO из него наследуется то что может выпасть из моба , типо шкура и тд.
class Item:#TODO Сдлеать специфичные для класса вещи - типо одеть magicWand может только wizard/mage/cleric
    #TODO сделать getStr() и другие методы если будет необходимо

    def __init__(self,name,stats,piece,price=Money()):
        self.name = name
        self.bonusStats = bonusStats(stats)#Вещь может иметь статы
        self.piece = piece #Weapon or Boots,Chest ect #TODO Если определение оружие это или нет не нужно - убрать

        self.price = Money() #Необходимо для продажи в магазине

    ## Возвращает True если вещь является Оружием
    def isWeapon(self):
        return self.piece=="Weapon"

    ## Возвращает True если вещь является Броней
    def isArmour(self):#TODO поменять если будут еще и урашения наследоваться из Item
        return self.piece != "Weapon"

    ## переопределен в наследниках
    def __str__(self):
        pass

## Оружие
class Weapon(Item):
    def __init__(self,name,stats,damage,price=0):
        super().__init__(name,stats,"Weapon",price)
        self.damage = damage

    ## Возвращает описание оружия в виде строки
    def __str__(self):
        return '"{0}" {1} {2}'.format(self.name,self.damage,self.bonusStats)

## Является enum'ом для класса Armour
class armourType:
    Head = "Head"
    Gloves = "Gloves"
    Chest = "Chest"
    Leggings = "Leggings"
    Boots = "Boots"

#armourType can be "Head" "Gloves" "Chest" "Leggings" or "Boots"
## Броня
class Armour(Item):

    def __init__(self,name,stats,defence,armourType,price=0):
        super().__init__(name,stats,armourType,price)
        self.defence = defence

    ## Возвращает описание Брони в виде строки
    def __str__(self):
        return '"{0}"  Defence:{1} {2}'.format(self.name,self.defence,self.bonusStats)