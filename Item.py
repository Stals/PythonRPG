#функция __str__() в класса позволяет очень просто выводит их содержимое через print(MagicBow) например
import random
from statistics import stats, damage

#bonusStats является оберткой вокруг stats
class bonusStats:
    def __init__(self,stats):
        self.stats = stats
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
    def str(self):
        return self.stats.str()
    def dex(self):
        return self.stats.dex()
    def mag(self):
        return self.stats.mag()
    def con(self):
        return self.stats.con()

class Item:
    #TODO сделать getStr() и другие методы если будет необходимо
    def __init__(self,name,stats):
        self.name = name
        #TODO перенести отдельно в Armour и Weapon , если potion будет наследоваться от item
        self.bonusStats=bonusStats(stats)#Вещь может иметь статы
    def __str__(self): #переопределен в наследниках
        pass
    #TODO Так как equip для каждого куска брони будет уникален, в него можно заложить каую именно часть он будет снимать и куда надеваться
    #TODO Написать в Human функции addBonusStats и deleteBonusStats
    def equip(self,hero):
        #Снимает вещь в томже слоте делая takeOff после чего одевает Item и добавляет bonusStats к статистикам игрока
        pass
    def takeOff(self,hero):
        #Снимает вещь, убирая те эффекты которые она давала и кладёт её в инвентарь
        pass

class Weapon(Item):
    def __init__(self,name,stats,damage):
        super().__init__(name,stats)
        self.damage = damage
    def __str__(self):
        return '"{0}" {1} {2}'.format(self.name,self.damage,self.bonusStats)

class Armour(Item):

    def __init__(self,name,stats,defence,armourType):
        super().__init__(name,stats)
        self.defence = defence
        self.armourType = armourType
    def __str__(self):
        return '"{0}"  Defence:{1} {2}'.format(self.name,self.defence,self.bonusStats)



#TODO убрать отсюда
magicBow=Weapon("Magic Bow",stats(1,3,3,4),damage(5,10))
fireSword=Weapon("Fire Sword",stats(1,2,3,4),damage(1,10))

ironBoots=Armour("Iron Boots",stats(3,2,0,0),10,"Boots")

#print(fireSword)
#print(ironBoots)