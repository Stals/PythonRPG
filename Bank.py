from Inventory import *
from Money import *
## Класс хранит список вещей и деньги игрока
class Bank():#Think придумать как будет выглядеть взаимодействие с банком
	#TODO Если тут есть removeGold() который будет вызываться, то видимо нужно сделать такойже для hero?
	def __init__(self):
		self.storage = Inventory()
		self.money = Money()

	## Добавляет money денег в банк
	def addMoney(self, money):
		self.money += money

	## Убирает money денег из банка, если хватит золота
	def removeMoney(self, money):
		if self.money >= money:
			self.money -= money
		else:
			print("Money is not enough.\nBank stores only {0}".format(self.money))

	## Возвращает true если в банке есть столько денег
	def enoughMoney(self, money):
		if self.money >= money:
			return True
		else:
			return False

	## Добавляет item в банк
	def addItem(self, item):
		self.storage.addItem(item)

	## Убирает item из банка
	def removeItem(self, item):
		self.storage.removeItem(item)

	## Возвращает список всех вещей в банке
	def items(self):
		return self.storage.items()

	## Возвращает Кол-во денег и список всех вещей в банке в виде строки
	def __str__(self):
		result = "{0}\n".format(self.money)
		result += self.storage.__str__()
		return result
	