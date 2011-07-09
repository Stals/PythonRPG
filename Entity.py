#TODO Пишет всё здесь а после делаем refactor -> move
from statistics import stats, damage
from Item import *
from Inventory import Inventory
from usefullFunctions import getChoice as func
from Elements import Elements
class Entity:
    name = ""
    hp = 0
    maxHp = 0
    gold = 0
    stats = stats()
    damage = damage()
    Resists = Elements()

    def __init__(self):
        pass
    def doTurn(self):#used by Battle to make one turn
        pass
    def simpleAttack(self):#simple attack with a weapon
        pass
    def isDead(self): #returns true if entity is dead
        return self.hp<=0

    def __str__(self):
        pass



class Hero(Entity):

    mp = 0
    maxMp = 0
    inventory = Inventory()
    heroRace = ""
    heroClass = ""

    def __init__(self):
        super().__init__()
    def getName(self):
        self.name=input("Input you name:")
    def getRace(self):
        #TODO реализовать Race в одельном классе в файле hero
        self.heroRace=func.getChoice("Choose Your Race:",[
            "Ogre      Str:9 Dex:2 Mag:2 Con:5",
            "Were-Wolf Str:7 Dex:5 Mag:2 Con:4",
            "Elf       Str:4 Dex:7 Mag:3 Con:4",
            "Human     Str:5 Dex:5 Mag:5 Con:3",
            "Hobbit    Str:2 Dex:9 Mag:4 Con:3",
            "Lepricone Str:2 Dex:5 Mag:8 Con:3",
            "Fairy     Str:1 Dex:5 Mag:9 Con:3"
        ])
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
        self.hp=self.maxHp



#TODO __str__() в hero делать с переносом на новую строку при выводе каждого объекта. При этом с использованием \n и дальше на новой строке код