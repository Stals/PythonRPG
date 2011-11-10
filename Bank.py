from Inventory import *
## Класс хранит список вещей и деньги игрока
class Bank():
	def __init__(self):
		storage = Inventory()
		gold = 0

	## Добавляет item в банк
	def addItem(self, item):
		pass

	## Убирает item из банка
	def removeItem(self, item):
		pass

	## Возвращает список всех вещей в банке
	def items(self):
		pass

	## Возвращает золото и список всех вещей в банке в виде строке
	def __str__(self):
		pass

