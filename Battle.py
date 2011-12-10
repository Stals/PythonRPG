from utils import getChoice as utils
## Отвечает за бой между героем и монстрами
class Battle:#TODO! Изменить вывод боя (Нужно больше переносов строк, может где табуляция)
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

			# Бой идёт до тех пор пока victory не будет изменена внутри playerTurn или enemiesTurn
			while self.victory == None:
				print (hero) # чтобы игрок мог видеть свои hp при выборе действия

				#TODOlater Добавить очерёдность ходов
				if self.playerTurn(hero):
					self.enemiesTurn(hero)
				else:
					# Игрок выбрал отмену
					continue
				print()
			
			if self.victory == True:
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

	# return False - Если выбрана отмена
	# Иначе - return True
	def playerTurn(self, hero):
		# getBattleChoice возвращает только те варианты которые осуществимы
		# - например use Potion появляется  тольео если есть хотябы один potion
		choice = hero.getBattleChoice()
		#TODO! переписать используя это (Нужно вынести в отдельную функцию как-то так как монстр делает тоже самое): http://stackoverflow.com/questions/8141165/how-to-dynamically-select-a-method-call-in-python
		#TODO! Возможно как-то проверять is entity is self.hero тогда передавать в simpleAttack enemy, а иначе hero
		if choice[0] == 'A': #Attack #TODO заменить на функцию так как тоже самое вызывается и для enemy (тогда перенести проверку на убийство моба дальше)
			if len(self.enemies) > 1:
				choosedEnemy = utils.getChoice("Choose your target:", self.enemies, cancel=True)
				if choosedEnemy == 0:
					# Выбрана отмена
					return False

			else: # Если один противник - его бьёт автоматически
				choosedEnemy = self.enemies[0]
			hero.simpleAttack(choosedEnemy)
			# проверка на то не умер ли моб , если умер - то его запихиваем в deadEmenies чтобы потом получить с них нагруду (Loot) если игрок выйграет
			#TODO! перенести дальше так как spell тоже может убить
			if choosedEnemy.isDead():
				self.enemies.remove(choosedEnemy)
				self.deadEnemies.append(choosedEnemy)
		if choice[0] == 'U': #Use Potion
			choosedPotion = utils.getChoice("What potion to use?", hero.potionsPocket.items(), cancel=True)
			if not choosedPotion:
				# Выбрали отмену
				return False
			else:
				hero.use(choosedPotion)

		# Если монстров не осталось - игрок выиграл
		if len(self.enemies) == 0:
			self.victory = True

		#Если небыла выбрана отмена, значит игрок ударил противника либо убил его
		return True

	# Ходит каждый из монстров
	def enemiesTurn(self, hero):
		for enemy in self.enemies:
			choice = enemy.getBattleChoice()
			if choice[0] == 'A': #Attack
				enemy.simpleAttack(hero)

		# проверка на выйгрыш мобов
		if hero.isDead():
			self.victory = False


		# TODO! переписать enemies так как очерендность может выглядеть так если у монстра 1 dex больше чем у героя :
		# ход монстра 1
		# ход игрока
		# ход моснстра 2

		#   def getOrder(self,hero,enemyList): #TODO Определить последовательность хода в зависимости от Dex
		#      Потом в основной функции цели предлагается ударить того кого нету... ой ну хз
		#      pass