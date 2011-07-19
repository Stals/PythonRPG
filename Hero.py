from Entity import Entity
from Inventory import Inventory
from Equipment import *
from Potion import PotionsPocket
from Elements import *
from statistics import *

#Класс хранит Имя рассы и те бонусы которые она даёт
import usefullFunctions.getChoice as func

class Race:
    def __init__(self,name="",stats=Stats()):
        self.name = name
        self.stats = stats
    def __str__(self):
        return "{0}\n{1}".format(self.name,self.stats)
    def name(self):
        return self.name
#TODO Сдлеать чтобы маны было меньше , и также как и hp примерно для среднего класса Human Может для human все статы по 5 ?
races=[
    Race("Ogre",Stats(9,2,2,5)),
    Race("Were-Wolf",Stats(7,5,2,4)),
    Race("Elf",Stats(4,7,3,4)),
    Race("Human",Stats(5,5,5,3)),
    Race("Hobbit",Stats(2,9,4,3)),
    Race("Lepricone",Stats(2,5,8,3)),
    Race("Fairy",Stats(1,5,9,3))
]
class Hero(Entity):

    def __init__(self):

        self.heroRace = Race()
        self.heroClass = ""

        #Получаем Данные от пользователя
        self.getName()
        self.getClass()
        self.getRace()

        super().__init__(self.name,self.heroRace.stats,Elements(),0)

        self.inventory = Inventory()
        self.equipment = Equipment()
        self.potionsPocket = PotionsPocket()

    def getName(self): #TODO Не получать пустую строку , и чтобы ввод был норм.
        self.name = input("Input you name:")
    def getRace(self):
        #Получам Рассу
        self.heroRace = func.getChoice("Choose your Race:",races)

        ##Теперь они добавляются при вызове super().__init__()
        #Получаем статистики для Героя из Рассы которую он выбрал
        #self.Stats.addStats(self.heroRace.Stats)

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

    def showStats(self):
        #TODO showStats() в hero делать с переносом на новую строку при выводе каждого объекта. При этом с использованием \n и дальше на новой строке код
#        +Stats
#        +Damage
#        +inventory
#        +potionsPocket
#        +resists
#        -questJournal
#        -equipment
#        -spellbook
#
        pass

    def heal(self): # TODO в наследниках востанавливать ману и rage
        self.hp = self.maxHp
    def castSpell(self,spell): #TODO Сделать когда будет готов класс Spell и SpellBook
        pass
    def __str__(self):
        return '"{0}" Health: {1}/{2} Mana: {3}/{4}'.format(self.name,self.hp,self.maxHp,self.mp,self.maxMp)
