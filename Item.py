#функция __str__() в класса позволяет очень просто выводит их содержимое через print(MagicBow) например
import random

#Позволяет не думать о том какие статы сейчас есть, за счёт того что они пределены только в одном месте
#Но чтобы создать вещь вам обязательно нужно знать о stats

#TODO перетащить в другой файл так как еще понадобится при создании монстров и Героя
class stats:
    def __init__(self,Str=0,Dex=0,Con=0,Mag=0):
        self.stats={"Str":Str,"Dex":Dex,"Con":Con,"Mag":Mag}

#TODO я думаю тоже нужно вытеснить, так как у монстров будет не оружие а урон (хотя не факт) Короче если где еще будет нужно то вытащить отсюда
class damage:
    def __init__(self,min,max):
        self.min=min
        self.max=max
    def __str__(self):
        return " Damage:{0}-{1} ".format(self.min,self.max)
    #Возвращает урон (между min и max)
    def getDamage(self):
        return random.randint(self.min,self.max)

#Необходим только для вещей (Брони/Оружия) так что он останется тут
#bonusStats является оберткой вокруг stats чтобы
class bonusStats:
    def __init__(self,stats):
        self.stats=stats
    def __str__(self):
        result=""
        for key,value in self.stats.stats.items():
            if value!=0:
                if value>0:
                    sign="+"
                else:
                    sign=""#минус будет ставится автоматически прямо в числе
                result+="{0}:{1}{2} ".format(key,sign,value)
        return result


class Item:
    #TODO сделать getStr() и другие методы если будет необходимо
    def __init__(self,name,stats):
        self.name=name
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
        self.damage=damage
    def __str__(self):
        return '"{0}" {1} {2}'.format(self.name,self.damage,self.bonusStats)



magicBow=Weapon("Magic Bow",stats(1,3,3,4),damage(5,10))
fireSword=Weapon("Fire Sword",stats(1,2,3,4),damage(1,10))
print(fireSword.damage.getDamage())

