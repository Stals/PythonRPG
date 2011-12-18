from utils import getChoice as utils
from utils.printList import *
## Отвечает за бой между героем и монстрами
class Battle:
## Принемает героя и монстра или список монстров как противника
	def __init__(self, hero, enemies):
		self.enemies = enemies[:] # Список живых монтров
		self.deadEnemies = [] # Список умерших монстров

		if len(self.enemies) >= 1:
			#print stats for hero and all enemies
			print ("Battle begins between\n{0}\nand".format(hero))
			for enemy in self.enemies:
				print(enemy)
			print()

			self.turnNum = 0
			# Бой идёт до тех пор пока герой не погибнет либо пока не погибнут все монстры
			while (not hero.isDead()) and (len(self.enemies)):
				self.turnNum += 1
				#orderedEntityList хранит список существ упорядоченных по DEX
				orderedEntityList = self.getOrder(hero, self.enemies)
				self.printTurnOrder(orderedEntityList)

				# Чем больше Dex тем раньше будет ходить существо
				for entity in orderedEntityList:
					if not entity.isDead():
						entity.doTurn(hero, self.enemies) #TODO!!! Сделать чтобы отмена работала типо делать пока не вернёт true.[через цикл] (Соответственно если false то функция вызывается еще раз)
				print()
				# Уберем умерших монстров если такие имеются
				self.removeDeadEnemies()

			if not hero.isDead():
				# Значит Герой победил
				for enemy in self.deadEnemies:
					enemy.giveExp(hero)
					enemy.giveLoot(hero)
				print ("You win!")
				#return True
			else:
				print ("You loose!")
				#return False
		else:
			raise Exception("Number of monster < 1")

	def printTurnOrder(self, orderedEntityList):
		print("Turn", self.turnNum, "Order:")
		for entity in orderedEntityList:
			print(" ",entity)
		print()

	def removeDeadEnemies(self):
		for enemy in self.enemies:
			if enemy.isDead():
				self.enemies.remove(enemy)
				self.deadEnemies.append(enemy)

	#Todo Note: с одинаковым dex герой ходит первым
	def getOrder(self, hero, enemies):
		entityList = [hero] + enemies
		return sorted(entityList, key=lambda entity: entity.stats.dex(),reverse=True)