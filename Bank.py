from Inventory import *
## Класс хранит список вещей и деньги игрока
class Bank():#TODO придумать как будет выглядеть взаимодействие с банком
	#TODO Если тут есть removeGold() который будет вызываться, то видимо нужно сделать такойже для hero?
	def __init__(self):
		storage = Inventory()
		gold = 0

	## Добавляет gold золота в банк
	def addGold(self, gold):
		self.gold += gold

	## Убирает gold золота из банка, если хватит золота
	def removeGold(self, gold):
		if self.enoughGold(gold):
			self.gold -= gold
		else:
			print("Gold is not enough.\n Bank stores only {0} gold\n".format(self.gold))

	## Возвращает true если в банке есть столько денег
	def enoughGold(self, gold):
		if self.gold >= gold:
			return True
		else:
			return False

	## Добавляет item в банк
	def addItem(self, item):
		pass

	## Убирает item из банка
	def takeItem(self, item):
		pass

	## Возвращает список всех вещей в банке
	def items(self):
		pass

	## Возвращает золото и список всех вещей в банке в виде строке
	def __str__(self):
		pass

