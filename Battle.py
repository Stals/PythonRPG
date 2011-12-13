from utils import getChoice as utils
from utils import printList
## Отвечает за бой между героем и монстрами
class Battle:#TODO!!!!! Изменить вывод боя (Нужно больше переносов строк, может где табуляция)
## Принемает героя и монстра или список монстров как противника
	def __init__(self, hero, enemies):
		self.enemies = [] # Список живых монтров
		self.enemies.extend (enemies)
		self.deadEnemies = [] # Список умерших монстров
		self.victory = None # Флаг выигрыша игрока

		if len(self.enemies) >= 1:
			#print stats for hero and all enemies
			print ("Battle begins between\n{0}\nand".format(hero))
			for enemy in self.enemies:
				print(enemy)
			print()

			# Бой идёт до тех пор пока герой не погибнет либо пока не погибнут все монстры
			while (not hero.isDead()) and (len(self.enemies)):
				#Entity list хранит героя и живых монстров
				entityList = [hero,]
				entityList.extend(self.enemies)
				#orderedEntityList хранит список существ упорядоченных по DEX
				orderedEntityList = self.getOrder(entityList)

				print("Turn Order:")
				printList.printList(orderedEntityList)

				# Чем больше Dex тем раньше будет ходить существо
				for entity in orderedEntityList:
					if not entity.isDead():
						entity.doTurn(entityList)
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


	def removeDeadEnemies(self):
		for enemy in self.enemies:
			if enemy.isDead():
				self.enemies.remove(enemy)
				self.deadEnemies.append(enemy)

	#Todo Note: с одинаковым dex герой ходит первым
	def getOrder(self,entityList): #TODO Определить последовательность хода в зависимости от Dex
		return sorted(entityList, key=lambda entity: entity.stats.dex(),reverse=True)