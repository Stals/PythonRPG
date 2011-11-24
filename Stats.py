from Damage import Damage
#Позволяет не думать о том какие статы сейчас есть, за счёт того что они пределены только в одном месте
#Но чтобы создать вещь вам обязательно нужно знать о Stats

## Хранит статистики self и его наследников
class Stats:
    def __init__(self,Str=0,Dex=0,Mag=0,Con=0):
        self.stats={
            "Str" : Str,# Strength
            "Dex" : Dex,# Dexterity #TODO! переименовать в agility , так как именно этот стат отвечает за уваротливость. (+ добавить Dex для того чтобы определять очередность ходов)
            "Mag" : Mag,# Magic
            "Con" : Con # Construction

        }
        self._HpMultiplier = 10
        self._MpMultiplier = 10
		
        #Note: Кол-во hp и mp определяется статистиками Con и Mag
        self.maxHp = self.con() * self._HpMultiplier
        self.hp = self.maxHp
        self.maxMp = self.mag() * self._MpMultiplier
        self.mp = self.maxMp

        #Note: базовое кол-во урона определяется кол-вом str
        self.damage = Damage()

    ## Возвращает элементы словаря stats
    ## позволяет не обращаться к словарю на прямую для вывода статистик
    def items(self):
        return self.stats.items()

    def str(self):
        return self.stats["Str"]

    def dex(self):
        return self.stats["Dex"]

    def mag(self):
        return self.stats["Mag"]

    def con(self):
        return self.stats["Con"]

    ## Добавляет статистики к своим и перещитывает hp mp и damage в self
    def addStats(self, stats):#stats - that should be added to self
        self.stats["Str"] += stats.str()
        self.stats["Dex"] += stats.dex()
        self.stats["Mag"] += stats.mag()
        self.stats["Con"] += stats.con()

        self.maxHp += stats.con() * self._HpMultiplier
        self.hp += stats.con() * self._HpMultiplier

        self.maxMp += stats.mag() * self._MpMultiplier
        self.mp += stats.mag() * self._MpMultiplier

        self.damage.addDamage(Damage(stats.str(), stats.str()))

    ## Отнимает статистики от своих и перещитывает hp mp и damage в self
    def removeStats(self,stats):#stats - that should be removed from self
        self.stats["Str"] -= stats.str()
        self.stats["Dex"] -= stats.dex()
        self.stats["Mag"] -= stats.mag()
        self.stats["Con"] -= stats.con()
        self.maxHp -= stats.con() * self._HpMultiplier
        self.hp -= stats.con() * self._HpMultiplier

        self.maxMp -= stats.mag() * self._MpMultiplier
        self.mp -= stats.mag() * self._MpMultiplier

        self.damage.removeDamage(Damage(stats.str(), stats.str()))

    ## Возвращает статистики в виде строки
    def __str__(self):
        result=""
        for key,value in self.stats.items():
            result+="{0}: {1} \n".format(key, value)
        return result