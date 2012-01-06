from Entity import Entity
from Inventory import Inventory
from Equipment import *
from Potion import PotionsPocket
from Elements import *
from Stats import *

#Класс хранит Имя расы и те бонусы которые она даёт
import utils.getChoice as utils

## Раса
class Race:
	def __init__(self,name="",stats=Stats()):
		self.name = name
		self.stats = stats

	## Возвращает название расы
	def name(self):
		return self.name

	## Возвращает описание Расы в виде строки
	def __str__(self):
		return "{0}\n{1}".format(self.name,self.stats)

#TODO Сдлеать чтобы маны было меньше , и также как и hp примерно для среднего класса Human Может для human все статы по 5 ?
races=[ #TODO! Переписать дома с листочка + можно тоже сделать и для Классов
	Race( "Dwarf",		Stats(7,7,4,4,4,4) ),
	Race( "Wood Elf",	Stats(5,4,3,4,7,7) ),
	Race( "Human",		Stats(5,5,5,5,5,5) ),
	Race( "High Elf",	Stats(3,4,8,8,3,4) ),
	Race( "Orc",		Stats(7,6,3,4,4,5) )
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
		while True:
			self.name = input("Input you name:")
			if self.name:
				# Если что-то было введено - прекратить цикл
				break
				
	## Получает Расу
	def getRace(self):
		#Получаем Расу
		self.heroRace = utils.getChoice("Choose your Race:",races) #TODOlater Сделать вывод по горизонтали

	## Получает Класс
	def getClass(self): #TODO Сделать сразу содание класса, при выборе одного из классов(вызывается создание класса) http://stackoverflow.com/questions/8141165/how-to-dynamically-select-a-method-call-in-python
		self.heroClass = utils.getChoice("Choose Your Class:",[
			"Warrior",
			"Ranger",
			"Mage"
		])


		## Выводит полный перечень Того что есть у Персонажа:
	## Уровень Опыт Класс Рассу
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
	#        -Level exp
	#		 +Race Class
	# 		 +Stats
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
		self.stats.hp = self.stats.maxHp
		self.stats.mp = self.stats.maxMp

	## Кастует Заклинание
	def castSpell(self, spell): #TODOlater Сделать когда будет готов класс Spell и SpellBook
		pass

		#TODO Переименовать на action? или еще что-то
	def castSpellChoice(self, hero, enemies):
		pass

	def usePotionChoice(self, hero, enemies):
		choosedPotion = utils.getChoice("What potion to use?", self.potionsPocket.items(), cancel=True)
		if choosedPotion:
			# Если было выбрано одно из зелий
			self.use(choosedPotion)
		else:
			#TODO! Выбрали отмену
			return False

		#вызывает simpleAttack для выбранного монстра
	def attackChoice(self, hero, enemies):
		if len(enemies) > 1:
			choosedEnemy = utils.getChoice("Choose your target:", enemies, cancel=True)
			if choosedEnemy == 0:
				#TODO! Выбрана отмена
				return False
		else:
		# Если один противник - его бьёт автоматически
			choosedEnemy = enemies[0]
		self.simpleAttack(choosedEnemy)

	def doTurn(self, hero, enemies):
		availableBattleChoices = self.getAvailableBattleChoices()
		selectedBattleChoice = utils.getChoice("What would you do?", list(availableBattleChoices.keys()))
		availableBattleChoices[selectedBattleChoice](hero, enemies)


		## Возвращает Словарь с возможными вариантами хода и методом за них отвечающим
	def getAvailableBattleChoices(self):
		battleChoices = {}
		# Simple attack is always available
		battleChoices["Attack with \"{0}\"".format(self.equipment.weapon())] = self.attackChoice
		#if not self.spellBook.isEmpty():
		#   battleChoices["Cast Spell"] = self.castSpellChoice
		if not self.potionsPocket.isEmpty():
			battleChoices["Use Potion"] = self.usePotionChoice
		return battleChoices

		## Одевает item в equipment и убирает из inventory
	def equip(self, item):
		if self.equipment.equipment[item.piece] != "empty":#if there is an item
			self.unequip(self.equipment.equipment[item.piece])
		#now the slot is empty
		self.equipment.equipment[item.piece]=item
		#Если вещь в инвентаре - убрать её оттуда
		self.inventory.removeItem(item)
		#give items Stats bonus and damage/defence
		self.stats.addStats(item.bonusStats)
		if item.isWeapon():
			self.stats.damage.addDamage(item.damage)
		if item.isArmor():
			self.defence+=item.defence

	#Think Нужен ли equipList() - который будет просто вызывать equip для каждой вещи

	## Снимает item из equipment и кладёт в inventory
	def unequip(self, item):
		#remove Stats that this item added
		self.stats.removeStats(self.equipment.equipment[item.piece].bonusStats)
		if item.isWeapon():
			self.stats.damage.removeDamage(item.damage)
		if item.isArmor():
			self.defence-=item.defence
			#add it to inventory
		self.inventory.addItem(self.equipment.equipment[item.piece])
		#make this slot empty
		self.equipment.equipment[item.piece] = "empty"


	## Использует вещь на героя (например Зелье)
	def use(self, item):
		item.use(self)

	## Возвращает true Если герой может использовать это (Spell, weapon, armor и т.п.)
	def canUse(self, object):
		return object.canUse(hero)

	def __str__(self):
		#return '"{0}" Health: {1}/{2} Mana: {3}/{4} {5} Defence: {6}'.format(self.name,self.hp,self.maxHp,self.mp,self.maxMp,self.stats.damage,self.defence)
		return '"{0}"  Health: {1.hp}/{1.maxHp}  Mana: {1.mp}/{1.maxMp}  {1.damage}  Defence: {2}'.format(self.name, self.stats, self.defence)
