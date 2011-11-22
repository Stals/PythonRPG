from Entity import Entity
from Inventory import Inventory
from Equipment import *
from Potion import PotionsPocket
from Elements import *
from Stats import *

#Класс хранит Имя рассы и те бонусы которые она даёт
import utils.getChoice as utils

## Расса
class Race:
    def __init__(self,name="",stats=Stats()):
        self.name = name
        self.stats = stats

    ## Возвращает название рассы
    def name(self):
        return self.name

    ## Возвращает описание Рассы в виде строки
    def __str__(self):
        return "{0}\n{1}".format(self.name,self.stats)

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

## Герой 
class Hero(Entity):

    def __init__(self):

        self.heroRace = Race()
        self.heroClass = ""

        #Получаем Данные от пользователя
        self.getName()
        self.getClass()
        self.getRace()

        super().__init__(self.name,self.heroRace.stats,Elements(),0)

        ## Инвентарь героя
        self.inventory = Inventory()
        ## Обмундирование героя
        self.equipment = Equipment()
        ## Карман с Лечебками героя
        self.potionsPocket = PotionsPocket()

    ## Получает имя Персонажа
    def getName(self): #TODO! Не получать пустую строку , и чтобы ввод был норм.
        self.name = input("Input you name:")

    ## Получает Рассу
    def getRace(self):
        #Получаем Расу
        self.heroRace = utils.getChoice("Choose your Race:",races)
        
    ## Получает Класс
    def getClass(self): #TODO Сдлеать сразу содание класса, при выборе одного из классов(вызывается создание класса) http://stackoverflow.com/questions/8141165/how-to-dynamically-select-a-method-call-in-python
        self.heroClass = utils.getChoice("Choose Your Class:",[
            "Warrior",
            "Ranger",
            "Mage"
        ])

            
    ## Выводит полный перечень Того что есть у Персонажа:
    ## Статистики (stats, hp, mp, money)
    ## Урон
    ## Вещи в inventory (инвентаре)
    ## Вещи в equipment (обмундировании)
    ## Лечебки в potionsPocket
    ## Резисты Персонажа
    ## Квесты в QuestJournal
    ## Заклинания в SpellBook

    def showStats(self):
        #TODO showStats() в hero делать с переносом на новую строку при выводе каждого объекта. При этом с использованием \n и дальше на новой строке код
#        +Stats
#        +Damage
#        +inventory
#        +equipment
#        +potionsPocket
#        +resists
#        -questJournal
#        -spellbook
#
        pass

    ## восстанавливает hp и mp
    def heal(self):
        self.hp = self.maxHp
        self.mp = self.maxMp

    ## Кастует Заклинание
    def castSpell(self, spell): #TODOlater Сделать когда будет готов класс Spell и SpellBook
        pass
    
    ## Даёт выбор что сделать в бою
    def getBattleChoice(self):
        actions = []
        actions.append("Attack with \"{0}\"".format(self.equipment.weapon()))
        #TODOlater вернуть когда сделаю заклинания
        #if not self.spellBook.isEmpty():
        #    actions.append("Cast Spell")
        if not self.potionsPocket.isEmpty():
            actions.append("Use Potion")
        actions.append("Flee")
        choice = utils.getChoice("What would you do?",actions)
        return choice

    ## Одевает item в equipment и убирает из inventory
    def equip(self, item):
        if self.equipment.equipment[item.piece] != "empty":#if there is an item
            self.unequip(self.equipment.equipment[item.piece])
        #now the slot is empty
        self.equipment.equipment[item.piece]=item
        #Если вещь в инвентаре - убрать её оттуда
        self.inventory.removeItem(item)
        #give items Stats bonus and damage/defence
        self.stats.addStats(item.bonusStats,self)
        if item.isWeapon():
            self.damage.addDamage(item.damage)
        if item.isArmour():
            self.defence+=item.defence

	#Think Нужен ли equipList() - который будет просто вызывать equip для каждой вещи

    ## Снимает item из equipment и кладёт в inventory
    def unequip(self, item):
        #remove Stats that this item added
        self.stats.removeStats(self.equipment.equipment[item.piece].bonusStats,self)
        if item.isWeapon():
            self.damage.removeDamage(item.damage)
        if item.isArmour():
            self.defence-=item.defence
        #add it to inventory
        self.inventory.addItem(self.equipment.equipment[item.piece])
        #make this slot empty
        self.equipment.equipment[item.piece] = "empty"


    ## Использует вещь на героя (например Зелье)
    def use(self, item):
        item.use(self)

    def __str__(self):
        return '"{0}" Health: {1}/{2} Mana: {3}/{4} {5} Defence: {6}'.format(self.name,self.hp,self.maxHp,self.mp,self.maxMp,self.damage,self.defence)
