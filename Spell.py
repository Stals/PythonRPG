#TODO! Сделать AOE = TRUE/FALSE
# Aoe true false
# Баффы должны действовать опр кол-во ходов, так что в бою нужно проверять не нужно ли снять их действие
class Spell:
	def __init__(self,name,mpCost):
		self.name = name
		self.mpCost = mpCost

	## Применяет spell на target
	#TODO! Target может быть списком если это AOE spell
	## Переопределяется в наследниках (Зависит от типа заклинания)
	def use(self, target):
		pass

	##todo! Проверяет можно ли использовать спелл основываясь на requirements (Мана кост )
	def canUse(self, hero):
		pass

	#def isMultiTarget(self):
	#	return


	#Переопределяется в наследниках (Зависит от типа заклинания)
	def __str__(self):
		pass
##
class SpellBook:#TODO сделать ограничение в количество которое можно носить с собой
	def __init__(self):
		self.book = []

	## Добавлет spell в книгу
	def addSpell(self, spell):
		self.book.append(spell)
		self.__sort()

	## Уберает spell из книги
	#Question нужно ли?
	def removeSpell(self, spell):
		pass

	## Возвращает список всех заклинаний в книге
	def items(self):
		return self.book

	## Возвращает True если книга заклинаний пуста
	def isEmpty(self):
		return not len(self.book)

	##Question Может сделать сортировку по типу или стоимости маны?
	def __sort(self):
		def name(spell):
			return spell.name
		self.book.sort(key = name)

	## Возвращает список всех заклинаний в виде
	def __str__(self):
		result = ""
		if len(self.book)!=0:
			for spell in self.book:
				result+="{0} \n".format(spell)
		else: #Spell book is empty
			result = "empty"
		return result
