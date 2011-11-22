from Damage import Damage
#Позволяет не думать о том какие статы сейчас есть, за счёт того что они пределены только в одном месте
#Но чтобы создать вещь вам обязательно нужно знать о Stats

#Question может hp и mp перенести внутрь? не в нутрь статов, а как и stats является переменной. Тогда обновление Жизни и маны будет происзодить прямо в классе stats
## Хранит статистики Entity и его наследников
class Stats:
    def __init__(self,Str=0,Dex=0,Mag=0,Con=0):
        self.stats={
            "Str" : Str,# Strength
            "Dex" : Dex,# Dexterity
            "Mag" : Mag,# Magic
            "Con" : Con # Construction

        }
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

	#TODO! перенести magick number - 10 в переменную
    ## Добавляет статистики к своим и перещитывает hp mp и damage в entity
    def addStats(self,stats,entity):#stats - that should be added to entity
        self.stats["Str"]+=stats.str()
        self.stats["Dex"]+=stats.dex()
        self.stats["Mag"]+=stats.mag()
        self.stats["Con"]+=stats.con()

        entity.maxHp += stats.con()*10
        entity.hp += stats.con()*10

        entity.maxMp += stats.mag()*10
        entity.mp += stats.mag()*10

        entity.damage.addDamage(Damage(stats.str(), stats.str()))

    ## Отнимает статистики от своих и перещитывает hp mp и damage в entity
    def removeStats(self,stats,entity):#stats - that should be removed from entity
        self.stats["Str"]-=stats.str()
        self.stats["Dex"]-=stats.dex()
        self.stats["Mag"]-=stats.mag()
        self.stats["Con"]-=stats.con()
        entity.maxHp -= stats.con()*10
        entity.hp -= stats.con()*10

        entity.maxMp -= stats.mag()*10
        entity.mp -= stats.mag()*10

        entity.damage.removeDamage(Damage(stats.str(), stats.str()))

    ## Возвращает статистики в виде строки
    def __str__(self):
        result=""
        for key,value in self.stats.items():
            result+="{0}: {1} \n".format(key, value)
        return result