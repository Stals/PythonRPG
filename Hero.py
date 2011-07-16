from Entity import Entity
from Inventory import Inventory
from Potion import PotionsPocket
from statistics import stats

#Класс хранит Имя рассы и те бонусы которые она даёт
import usefullFunctions.getChoice as func

class Race:
    def __init__(self,name="",stats=stats()):
        self.name = name
        self.stats = stats
    def __str__(self):
        return "{0}\n{1}".format(self.name,self.stats)
    def name(self):
        return self.name

races=[
    Race("Ogre",stats(9,2,2,5)),
    Race("Were-Wolf",stats(7,5,2,4)),
    Race("Elf",stats(4,7,3,4)),
    Race("Human",stats(5,5,5,3)),
    Race("Hobbit",stats(2,9,4,3)),
    Race("Lepricone",stats(2,5,8,3)),
    Race("Fairy",stats(1,5,9,3))
]
class Hero(Entity):

    mp = 0
    maxMp = 0
    inventory = Inventory()
    potionsPocket = PotionsPocket()
    heroRace = Race()
    heroClass = ""

    def __init__(self):
        super().__init__()
    def getName(self):
        self.name = input("Input you name:")
    def getRace(self):
        self.heroRace = func.getChoice("Choose your Race:",races)
        self.stats.addStats(self.heroRace.stats)
        #TODO сделать добавление статов из за рассы  к статам героя ( вызывается self.stats.addStats(Race.stats) )

    def getClass(self):
        temp=func.getChoice("Choose Your Class:",[
            "Warrior - major stat is Strength",
            "Ranger  - major stat is Dexterity",
            "Mage    - major stat is Magick"
        ])
        if temp[0]=="W":
            self.heroClass="Warrior"
        elif temp[0]=="R":
            self.heroClass="Ranger"
        elif temp[0]=="M":
            self.heroClass="Mage"

    # TODO в наследниках востанавливать ману и rage
    def heal(self):
        self.hp = self.maxHp
    def castSpell(self,spell):
        #TODO Сделать когда будет готов класс Spell и SpellBook
        pass
    def __str__(self):
        #TODO __str__() в hero делать с переносом на новую строку при выводе каждого объекта. При этом с использованием \n и дальше на новой строке код
        pass