from Damage import Damage
#Позволяет не думать о том какие статы сейчас есть, за счёт того что они пределены только в одном месте
#Но чтобы создать вещь вам обязательно нужно знать о Stats

## Хранит характеристики self и его наследников
class Stats: #TODOlater Question может N кол-во Con даёт резист? типо 10 Con +1 resist ко всему
	def __init__(self, Str=0,Con=0,Int=0,Wis=0,Agi=0,Dex=0):
		self.stats={
			"Str" : Str,# Strength - Влияет на урон оружием
			"Con" : Con,# Construction - Влияет на кол-во Hp
			"Wis" : Wis,# Wisdom - Влияет на урон магии
			"Int" : Int,# Intellect - Влияет на кол-во Mp
			"Agi" : Agi,# Agility - влияет на способность уворота и попадания по противнику
			"Dex" : Dex # Dexterity - влияет на очередность ходов
		}

		self._HpMultiplier = 10 # 1 Con даёт 10 Hp
		self._MpMultiplier = 10 # 1 Int даёт 10 Mp

		#Note: Кол-во hp и mp определяется статистиками Con и Int
		self.maxHp = self.con() * self._HpMultiplier
		self.hp = self.maxHp
		self.maxMp = self.int() * self._MpMultiplier
		self.mp = self.maxMp

		#Note: базовое кол-во урона определяется кол-вом str
		self.damage = Damage()

	## Возвращает элементы словаря stats
	## позволяет не обращаться к словарю на прямую для вывода статистик
	def items(self):
		return self.stats.items()

	def str(self):
		return self.stats["Str"]

	def con(self):
		return self.stats["Con"]

	def wis(self):
		return self.stats["Wis"]

	def int(self):
		return self.stats["Int"]

	def agi(self):
		return self.stats["Agi"]

	def dex(self):
		return self.stats["Dex"]

	## Добавляет статистики к своим и перещитывает hp mp и damage в self
	def addStats(self, stats):#stats - that should be added to self
		self.stats["Str"] += stats.str()
		self.stats["Con"] += stats.con()
		self.stats["Wis"] += stats.wis()
		self.stats["Int"] += stats.int()
		self.stats["Agi"] += stats.agi()
		self.stats["Dex"] += stats.dex()

		self.maxHp += stats.con() * self._HpMultiplier
		self.hp += stats.con() * self._HpMultiplier

		self.maxMp += stats.int() * self._MpMultiplier
		self.mp += stats.int() * self._MpMultiplier

		self.damage.addDamage(Damage(stats.str(), stats.str()))

	## Отнимает статистики от своих и перещитывает hp mp и damage в self
	def removeStats(self, stats):#stats - that should be removed from self
		self.stats["Str"] -= stats.str()
		self.stats["Con"] -= stats.con()
		self.stats["Wis"] -= stats.wis()
		self.stats["Int"] -= stats.int()
		self.stats["Agi"] -= stats.agi()
		self.stats["Dex"] -= stats.dex()

		self.maxHp -= stats.con() * self._HpMultiplier
		self.hp -= stats.con() * self._HpMultiplier

		self.maxMp -= stats.int() * self._MpMultiplier
		self.mp -= stats.int() * self._MpMultiplier

		self.damage.removeDamage(Damage(stats.str(), stats.str()))

	## Возвращает характеристики в виде строки
	def __str__(self):
		result=""
		for statistic, value in self.items():
			result+="{0}: {1}\n".format(statistic, value)
		return result